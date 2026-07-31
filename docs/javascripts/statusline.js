/* ==========================================================================
   A statusline do livro.

   Mostra o que o Vim mostra no rodapé da janela: o modo, o arquivo aberto, a
   posição no livro e a régua de rolagem. O modo não é enfeite — ele muda de
   verdade quando você seleciona texto, que é o conceito mais difícil do editor
   para quem está começando.

   A barra é filha do <body>, e não do container que a navegação instantânea
   substitui, então ela sobrevive à troca de página; só o conteúdo é reescrito.
   ========================================================================== */

const TOTAL_CAPITULOS = 15

/*
 * O caminho do arquivo de origem, deduzido da URL. Não usa a raiz do site
 * porque ela muda entre o servidor local e o GitHub Pages; a estrutura de
 * capítulos, não.
 */
function arquivoAtual() {
  const partes = location.pathname.split("/").filter(Boolean)
  const capitulo = partes.findIndex((p) => /^capitulo_\d+$/.test(p))

  if (capitulo >= 0) {
    const resto = partes.slice(capitulo + 1)
    return resto.length
      ? `${partes[capitulo]}/${resto[resto.length - 1]}.md`
      : `${partes[capitulo]}/index.md`
  }
  if (partes[partes.length - 1] === "referencias") return "referencias/index.md"
  return "vimbook"
}

function capituloAtual() {
  const achado = location.pathname.match(/capitulo_(\d+)/)
  return achado ? Number(achado[1]) : null
}

/* --------------------------------------------------------------------------
   A barra
   -------------------------------------------------------------------------- */

const barra = document.createElement("div")
barra.className = "vimbook-status"
barra.innerHTML =
  '<span class="vimbook-status__modo" data-modo="normal">-- NORMAL --</span>' +
  '<span class="vimbook-status__arquivo"><span></span></span>' +
  '<span class="vimbook-status__dir">' +
  "<span></span><span class=\"vimbook-status__pos\"></span></span>"

const chipModo = barra.querySelector(".vimbook-status__modo")
const campoArquivo = barra.querySelector(".vimbook-status__arquivo span")
const campoLivro = barra.querySelector(".vimbook-status__dir span")
const campoPos = barra.querySelector(".vimbook-status__pos")

document.body.appendChild(barra)

/* Reserva o espaço que a barra ocupa, para ela não cobrir o fim do texto. */
function reservaEspaco() {
  document.documentElement.style.setProperty(
    "--vimbook-status-altura",
    `${barra.offsetHeight}px`,
  )
}

/* --------------------------------------------------------------------------
   A régua: Topo / Fim / Tudo / porcentagem, como no editor
   -------------------------------------------------------------------------- */

function atualizaRegua() {
  const doc = document.documentElement
  const rolavel = doc.scrollHeight - window.innerHeight

  if (rolavel <= 2) campoPos.textContent = "Tudo"
  else if (window.scrollY <= 1) campoPos.textContent = "Topo"
  else if (window.scrollY >= rolavel - 1) campoPos.textContent = "Fim"
  else campoPos.textContent = `${Math.round((window.scrollY / rolavel) * 100)}%`
}

/* --------------------------------------------------------------------------
   NORMAL <-> VISUAL, pela seleção real dentro do texto
   -------------------------------------------------------------------------- */

function defineModo(nome, rotulo) {
  chipModo.dataset.modo = nome
  chipModo.textContent = rotulo
}

document.addEventListener("selectionchange", () => {
  const artigo = document.querySelector(".md-content__inner")
  const selecao = document.getSelection()

  if (!artigo || !selecao || selecao.isCollapsed || !artigo.contains(selecao.anchorNode)) {
    defineModo("normal", "-- NORMAL --")
    atualizaRegua()
    return
  }

  const texto = selecao.toString()
  const linhas = texto.split("\n").filter((l) => l.trim()).length
  defineModo("visual", "-- VISUAL --")
  campoPos.textContent = linhas > 1 ? `${linhas} linhas` : `${texto.length} car.`
})

/* --------------------------------------------------------------------------
   A coluna de tis: o que está além da última linha do arquivo.

   Só aparece quando o texto acaba antes do fim da tela — que é o
   comportamento do editor, e o caso da maioria das páginas deste livro.
   -------------------------------------------------------------------------- */

const ALTURA_TIL = 17.28 // 0.72rem x 1.5, o mesmo par do CSS

function desenhaTis() {
  const antiga = document.querySelector(".vimbook-tils")
  if (antiga) antiga.remove()

  const artigo = document.querySelector(".md-content__inner")
  if (!artigo || window.matchMedia("(max-width: 76.1875em)").matches) return

  /* O limite é o rodapé, não a borda da tela: o espaço vazio de uma página
     curta fica entre o fim do texto e os links de anterior/próxima. */
  const rodape = document.querySelector(".md-footer")
  const fimDoTexto = artigo.getBoundingClientRect().bottom
  const limite = rodape
    ? rodape.getBoundingClientRect().top
    : window.innerHeight - barra.offsetHeight

  const sobra = limite - fimDoTexto
  if (sobra < ALTURA_TIL) return

  const coluna = document.createElement("div")
  coluna.className = "vimbook-tils"
  coluna.setAttribute("aria-hidden", "true")
  coluna.style.top = `${artigo.offsetHeight}px`
  for (let i = 0; i < Math.floor(sobra / ALTURA_TIL); i++) {
    const til = document.createElement("span")
    til.textContent = "~"
    coluna.appendChild(til)
  }
  artigo.appendChild(coluna)
}

/* --------------------------------------------------------------------------
   Ligações
   -------------------------------------------------------------------------- */

function atualizaPagina() {
  campoArquivo.textContent = arquivoAtual()
  const n = capituloAtual()
  campoLivro.textContent = n ? `[${n}/${TOTAL_CAPITULOS}]` : ""
  defineModo("normal", "-- NORMAL --")
  reservaEspaco()
  atualizaRegua()
  desenhaTis()
}

window.addEventListener("scroll", atualizaRegua, { passive: true })
window.addEventListener("resize", () => {
  reservaEspaco()
  atualizaRegua()
  desenhaTis()
})

if (window.document$) {
  window.document$.subscribe(atualizaPagina)
} else {
  document.addEventListener("DOMContentLoaded", atualizaPagina)
}
