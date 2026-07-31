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
   Ligações

   Não há coluna de tis nas páginas de conteúdo. A margem entre o texto e o
   menu lateral é ocupada pela barra de rolagem da navegação, e qualquer tom
   discreto o bastante para não competir com o texto ficava perto de 1,2:1 —
   invisível. A coluna sobrevive só na capa, onde há espaço e fundo próprios.
   -------------------------------------------------------------------------- */

function atualizaPagina() {
  campoArquivo.textContent = arquivoAtual()
  const n = capituloAtual()
  campoLivro.textContent = n ? `[${n}/${TOTAL_CAPITULOS}]` : ""
  defineModo("normal", "-- NORMAL --")
  reservaEspaco()
  atualizaRegua()
}

window.addEventListener("scroll", atualizaRegua, { passive: true })
window.addEventListener("resize", () => {
  reservaEspaco()
  atualizaRegua()
})

if (window.document$) {
  window.document$.subscribe(atualizaPagina)
} else {
  document.addEventListener("DOMContentLoaded", atualizaPagina)
}
