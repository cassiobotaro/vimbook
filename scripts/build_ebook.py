#!/usr/bin/env python3
"""Gera o vimbook em EPUB e PDF a partir das páginas de docs/.

A ordem e os títulos vêm do `nav` do zensical.toml, a mesma fonte do
site. Cada página é lida pelo pandoc como AST (JSON) e ajustada aqui,
antes de todas virarem um documento só:

- cada seção do `nav` vira um capítulo (título de nível 1), aberto pela
  primeira página dela; as demais páginas viram seções de nível 2, com
  o título que o `nav` dá;
- os títulos internos de cada página descem de nível para caber abaixo
  disso;
- os ids de título ganham o caminho da página como prefixo, para não
  colidirem entre páginas, e os links `../capitulo_x/pagina.md` viram
  âncoras internas;
- `<code>...</code>` escrito em HTML vira código inline; sem isso o PDF
  perderia o trecho, porque o escritor typst do pandoc descarta HTML.

Notas de rodapé não precisam de tratamento: no AST elas já ficam presas
ao ponto do texto onde aparecem, então os `[^1]` de páginas diferentes
não colidem.

Antes dos capítulos entram a apresentação (o texto de docs/index.md) e a
lista de autores (AUTHORS); depois deles, o texto da GFDL (LICENSE),
que a licença exige em toda cópia distribuída.

Uso:
    python scripts/build_ebook.py                 # gera _book/vimbook.{epub,pdf}
    python scripts/build_ebook.py --versao v1.0   # carimba a versão na folha de rosto
    python scripts/build_ebook.py --formato epub  # só um dos formatos

Precisa do pandoc 3.8 ou mais novo e, para o PDF, do typst. A variável
PANDOC escolhe outro executável do pandoc.
"""

import argparse
import datetime
import json
import os
import posixpath
import re
import subprocess
import sys
import tomllib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
SAIDA = RAIZ / "_book"
PANDOC = os.environ.get("PANDOC", "pandoc")

TITULO = "Vimbook"
SUBTITULO = "O editor de texto Vim"
# O mesmo leitor para todas as páginas. CommonMark, e não o markdown do
# pandoc, porque divide as linhas de uma tabela antes de ler o código
# inline, como o site faz: no markdown do pandoc, um `` ` `` solto (o
# livro escreve `assim' em vários lugares) engole o resto da tabela.
# Desligados os recursos que o site não tem: `$` é o fim de linha do Vim,
# não fórmula; `~` e `^` não são subscrito e sobrescrito; `--` e aspas
# ficam como foram escritos.
FORMATO_ENTRADA = ("commonmark_x-tex_math_dollars-subscript-superscript"
                   "-smart")

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Cada capítulo (título de nível 1) começa numa página nova do PDF.
CABECALHO_TYPST = """\
#show heading.where(level: 1): it => { pagebreak(weak: true); it }
"""


# --- AST do pandoc --------------------------------------------------------

def texto(no) -> str:
    """O texto puro de um trecho do AST."""
    if isinstance(no, list):
        return "".join(texto(n) for n in no)
    if not isinstance(no, dict):
        return ""
    t, c = no.get("t"), no.get("c")
    if t == "Str":
        return c
    if t in ("Space", "SoftBreak", "LineBreak"):
        return " "
    if t == "Code":
        return c[1]
    return texto(c)


def normaliza(s: str) -> str:
    """Só letras e dígitos, em minúsculas, para comparar títulos."""
    return "".join(c for c in s.lower() if c.isalnum())


def inlines(s: str) -> list:
    """Uma string como lista de inlines do pandoc."""
    saida = []
    for i, palavra in enumerate(s.split()):
        if i:
            saida.append({"t": "Space"})
        saida.append({"t": "Str", "c": palavra})
    return saida


def titulo(nivel: int, ident: str, conteudo: list) -> dict:
    return {"t": "Header",
            "c": [nivel, [ident, ["unnumbered"], []], conteudo]}


def paragrafo(s: str) -> dict:
    return {"t": "Para", "c": inlines(s)}


def percorre(no, visita):
    """Aplica `visita` a cada dicionário do AST, de baixo para cima."""
    if isinstance(no, list):
        for item in no:
            percorre(item, visita)
    elif isinstance(no, dict):
        percorre(no.get("c"), visita)
        visita(no)


def junta_code_html(no) -> None:
    """Troca `<code>`, inlines, `</code>` (HTML cru) por um Code."""
    if not isinstance(no, list):
        return
    i = 0
    while i < len(no):
        item = no[i]
        if (isinstance(item, dict) and item.get("t") == "RawInline"
                and item["c"][0] == "html" and item["c"][1] == "<code>"):
            for j in range(i + 1, len(no)):
                fim = no[j]
                if (isinstance(fim, dict) and fim.get("t") == "RawInline"
                        and fim["c"][1] == "</code>"):
                    no[i:j + 1] = [{"t": "Code",
                                    "c": [["", [], []], texto(no[i + 1:j])]}]
                    break
        i += 1


def junta_code_html_em(no: dict) -> None:
    """`junta_code_html` em cada lista de inlines filha de `no`."""
    if isinstance(no.get("c"), list):
        junta_code_html(no["c"])
        for filho in no["c"]:
            junta_code_html(filho)


def ler_pagina(caminho: Path) -> dict:
    fonte = caminho.read_text(encoding="utf-8")
    proc = subprocess.run(
        [PANDOC, "--from", FORMATO_ENTRADA, "--to", "json"],
        input=admonicoes(fonte), capture_output=True, text=True,
        encoding="utf-8")
    if proc.returncode != 0:
        sys.exit(f"pandoc falhou em {caminho}:\n{proc.stderr}")
    return json.loads(proc.stdout)


def admonicoes(fonte: str) -> str:
    """`!!! note` do zensical como citação, que todo leitor destaca."""
    def troca(m):
        linhas = m.group(2).rstrip("\n").split("\n")
        return "".join(f">{linha[4:] and ' ' + linha[4:]}\n"
                       for linha in linhas) + "\n"
    return re.sub(r'^!!! (\w+).*\n((?:(?: {4}.*)?\n)+)', troca, fonte,
                  flags=re.M)


# --- Páginas do livro -----------------------------------------------------

def id_da_pagina(caminho: str) -> str:
    """`capitulo_12/mapeamentos.md` -> `capitulo_12-mapeamentos`."""
    return caminho.removesuffix(".md").replace("/", "-")


def paginas_do_nav() -> list[tuple[str, str, bool]]:
    """(caminho, título, abre capítulo?) na ordem do `nav`, sem a capa."""
    config = tomllib.loads((RAIZ / "zensical.toml").read_text("utf-8"))
    paginas = []
    for entrada in config["project"]["nav"][1:]:
        (capitulo, valor), = entrada.items()
        itens = valor if isinstance(valor, list) else [valor]
        for i, item in enumerate(itens):
            if isinstance(item, str):
                caminho, nome = item, capitulo
            else:
                (nome, caminho), = item.items()
            paginas.append((caminho, capitulo if i == 0 else nome, i == 0))
    return paginas


def ajusta_pagina(caminho: str, nome: str, abre: bool,
                  ast: dict, avisos: list) -> list:
    """Os blocos da página, prontos para entrar no documento único."""
    pid = id_da_pagina(caminho)
    pasta = posixpath.dirname(caminho)
    blocos = ast["blocks"]
    nivel_pagina = 1 if abre else 2

    # O primeiro título da página, se repete o nome dela, é o título.
    if (blocos and blocos[0]["t"] == "Header"
            and normaliza(texto(blocos[0]["c"][2])) == normaliza(nome)):
        conteudo = blocos.pop(0)["c"][2]
    else:
        conteudo = inlines(nome)

    niveis = [b["c"][0] for b in blocos if b["t"] == "Header"]
    desloca = max(0, nivel_pagina + 1 - min(niveis)) if niveis else 0

    def visita(no):
        t = no.get("t")
        if t == "Header":
            no["c"][0] = min(6, no["c"][0] + desloca)
            attr = no["c"][1]
            attr[0] = f"{pid}--{attr[0]}" if attr[0] else ""
        elif t == "Link":
            alvo = no["c"][2]
            alvo[0] = link_interno(alvo[0], pasta, pid, caminho, avisos)
        elif t == "Image":
            alvo = no["c"][2]
            if "://" not in alvo[0]:
                alvo[0] = str(DOCS / pasta / alvo[0])
        elif t in ("RawBlock", "RawInline") and no["c"][0] == "html":
            avisos.append(f"{caminho}: HTML ignorado: {no['c'][1]!r}")

    percorre(blocos, junta_code_html_em)
    percorre(blocos, visita)
    return [titulo(nivel_pagina, pid, conteudo), *blocos]


def link_interno(url: str, pasta: str, pid: str, caminho: str,
                 avisos: list) -> str:
    if re.match(r"^[a-z]+:", url):
        return url
    arquivo, _, ancora = url.partition("#")
    if not arquivo:
        return f"#{pid}--{ancora}"
    if not arquivo.endswith(".md"):
        return url
    destino = posixpath.normpath(posixpath.join(pasta, arquivo))
    if not (DOCS / destino).exists():
        avisos.append(f"{caminho}: link para página inexistente: {url}")
        return url
    alvo = id_da_pagina(destino)
    return f"#{alvo}--{ancora}" if ancora else f"#{alvo}"


# --- Partes fora do nav ---------------------------------------------------

def apresentacao() -> list:
    """docs/index.md sem a capa em HTML, o título do site e os links de
    download, que não fazem sentido dentro do próprio livro."""
    ast = ler_pagina(DOCS / "index.md")
    blocos, pulando = [], False
    for b in ast["blocks"]:
        if b["t"] == "Header":
            if b["c"][1][0] == "o-editor-de-texto-vim":
                continue
            pulando = b["c"][1][0] == "baixe-o-livro"
        # A capa em HTML vem como uma sequência de RawBlock e Plain soltos.
        if not pulando and b["t"] not in ("RawBlock", "Plain"):
            blocos.append(b)
    for b in blocos:
        if b["t"] == "Header":
            b["c"][0] = 2
            b["c"][1][0] = f"apresentacao--{b['c'][1][0]}"
    return [titulo(1, "apresentacao", inlines("Apresentação")), *blocos,
            paragrafo("O texto completo da licença está no fim do livro, "
                      "em “GNU Free Documentation License”.")]


def autores() -> list:
    """AUTHORS como uma lista de nomes por fase do livro, sem e-mails."""
    blocos = [titulo(1, "autores", inlines("Autores"))]
    linhas = (RAIZ / "AUTHORS").read_text(encoding="utf-8").splitlines()
    nomes = []
    for i, linha in enumerate(linhas):
        if re.fullmatch(r"-+", linha.strip()):
            continue
        if (linha.strip() and i + 1 < len(linhas)
                and re.fullmatch(r"-+", linhas[i + 1].strip())):
            if nomes:
                blocos.append(lista(nomes))
                nomes = []
            blocos.append(titulo(2, "", inlines(linha.strip())))
        elif linha.strip():
            nomes.append(re.sub(r"\s*<[^>]*>", "", linha).strip())
    if nomes:
        blocos.append(lista(nomes))
    return blocos


def lista(itens: list[str]) -> dict:
    return {"t": "BulletList",
            "c": [[{"t": "Plain", "c": inlines(item)}] for item in itens]}


def licenca() -> list:
    """LICENSE (texto puro) como apêndice, sem mudar uma palavra.

    Linhas com recuo são a lista de exigências da seção 4 (`    * A. ...`)
    ou os modelos de aviso do adendo, que ficam como bloco de código."""
    linhas = (RAIZ / "LICENSE").read_text(encoding="utf-8").splitlines()
    blocos = [titulo(1, "licenca", inlines(linhas[0].strip()))]
    itens, codigo = [], []

    def fecha():
        if itens:
            blocos.append(lista(itens[:]))
            itens.clear()
        if codigo:
            blocos.append({"t": "CodeBlock",
                           "c": [["", [], []], "\n".join(codigo)]})
            codigo.clear()

    for linha in linhas[1:]:
        if linha.startswith("    * "):
            itens.append(linha[6:])
            continue
        if linha.startswith("    "):
            codigo.append(linha[4:])
            continue
        fecha()
        if not linha.strip():
            continue
        if re.fullmatch(r"\d+\. [A-Z ,]+|ADDENDUM: .*", linha.strip()):
            blocos.append(titulo(2, "", inlines(linha.strip())))
        else:
            blocos.append(paragrafo(linha))
    fecha()
    return blocos


# --- Montagem e saída -----------------------------------------------------

def monta(avisos: list) -> dict:
    api = None
    blocos = apresentacao() + autores()
    for caminho, nome, abre in paginas_do_nav():
        ast = ler_pagina(DOCS / caminho)
        api = api or ast["pandoc-api-version"]
        blocos += ajusta_pagina(caminho, nome, abre, ast, avisos)
    blocos += licenca()
    return {"pandoc-api-version": api, "meta": {}, "blocks": blocos}


def data_por_extenso(dia: datetime.date) -> str:
    return f"{dia.day} de {MESES[dia.month - 1]} de {dia.year}"


def metadados(versao: str | None) -> list[str]:
    hoje = data_por_extenso(datetime.date.today())
    data = f"Versão {versao} · {hoje}" if versao else hoje
    return ["--metadata", f"title={TITULO}",
            "--metadata", f"subtitle={SUBTITULO}",
            "--metadata", f"date={data}",
            "--metadata", "lang=pt-BR"]


def pandoc(fonte: Path, destino: Path, extras: list[str]) -> None:
    comando = [PANDOC, str(fonte), "--from", "json",
               "--output", str(destino), "--toc", "--toc-depth=2", *extras]
    proc = subprocess.run(comando, capture_output=True, text=True,
                          encoding="utf-8")
    if proc.stderr.strip():
        print(proc.stderr.strip(), file=sys.stderr)
    if proc.returncode != 0:
        sys.exit(f"pandoc falhou ao gerar {destino.name}")
    print(f"gerado {destino.relative_to(RAIZ)}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--versao", help="versão impressa na folha de rosto")
    ap.add_argument("--formato", choices=["epub", "pdf", "todos"],
                    default="todos")
    args = ap.parse_args()

    avisos: list[str] = []
    livro = monta(avisos)
    for aviso in avisos:
        print(f"aviso: {aviso}", file=sys.stderr)

    SAIDA.mkdir(exist_ok=True)
    fonte = SAIDA / "vimbook.json"
    fonte.write_text(json.dumps(livro, ensure_ascii=False), encoding="utf-8")
    meta = metadados(args.versao)

    if args.formato in ("epub", "todos"):
        # A data da folha de rosto é por extenso, e o pandoc deixaria o
        # dc:date do EPUB vazio por não conseguir lê-la; este arquivo dá
        # a ele a data no formato ISO.
        dc = SAIDA / "epub-metadata.xml"
        dc.write_text(f"<dc:date>{datetime.date.today().isoformat()}"
                      "</dc:date>\n", encoding="utf-8")
        # Para leitores e-ink: código destacado com negrito e itálico,
        # sem cores.
        pandoc(fonte, SAIDA / "vimbook.epub", [
            *meta, "--split-level=1",
            "--syntax-highlighting=monochrome",
            "--epub-cover-image", str(DOCS / "imgs" / "cover.jpg"),
            "--epub-metadata", str(dc),
        ])
    if args.formato in ("pdf", "todos"):
        cabecalho = SAIDA / "cabecalho.typ"
        cabecalho.write_text(CABECALHO_TYPST, encoding="utf-8")
        pandoc(fonte, SAIDA / "vimbook.pdf", [
            *meta, "--pdf-engine=typst",
            "--include-in-header", str(cabecalho),
            "--variable", "papersize:a4",
            # As imagens têm caminho absoluto; a raiz do typst precisa
            # contê-las.
            f"--pdf-engine-opt=--root={RAIZ}",
        ])


if __name__ == "__main__":
    main()
