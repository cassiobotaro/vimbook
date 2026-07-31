/* ==========================================================================
   Ler o livro com as teclas de movimento do Vim.

     h  [    página anterior      j   desce uma linha
     l  ]    próxima página       k   sobe uma linha

   n/p (e ./,) já vinham do tema e continuam valendo. Ctrl+J e Ctrl+K também
   são dele — nada com Ctrl/Cmd chega até aqui.
   ========================================================================== */

const DIRECOES = {
  h: "prev",
  "[": "prev",
  l: "next",
  "]": "next",
}

const ROLAGEM = {
  j: 1,
  k: -1,
}

/*
 * O link do rodapé é um <a> de verdade, que o roteador do tema intercepta;
 * clicar nele preserva a navegação instantânea. O <link rel> do <head> é o
 * reserva para quando o rodapé está oculto por `hide: [footer]`.
 */
function alvo(direcao) {
  return (
    document.querySelector(`.md-footer__link--${direcao}`) ||
    document.querySelector(`link[rel=${direcao}]`)
  )
}

/* Uma linha de texto, medida no elemento real para acompanhar o zoom e a
   fonte que o leitor escolheu. */
function alturaDaLinha() {
  const conteudo = document.querySelector(".md-content__inner")
  if (!conteudo) return 24

  const estilo = getComputedStyle(conteudo)
  const linha = parseFloat(estilo.lineHeight)
  if (Number.isFinite(linha)) return linha

  const fonte = parseFloat(estilo.fontSize)
  return Number.isFinite(fonte) ? fonte * 1.6 : 24
}

/*
 * keyboard$ traz de graça as guardas do tema: não dispara com a busca aberta,
 * dentro de campos de texto, nem no meio de uma composição de acentos.
 */
if (window.keyboard$) {
  window.keyboard$.subscribe((tecla) => {
    if (tecla.mode !== "global" || tecla.meta) return

    const direcao = DIRECOES[tecla.type]
    if (direcao) {
      const destino = alvo(direcao)
      if (!destino) return

      tecla.claim()
      if (destino.tagName === "A") destino.click()
      else location.assign(destino.href)
      return
    }

    /* Sem animação: o Vim não anima, e segurar a tecla precisa deslizar
       contínuo em vez de enfileirar transições. */
    const sentido = ROLAGEM[tecla.type]
    if (sentido) {
      tecla.claim()
      window.scrollBy(0, sentido * alturaDaLinha())
    }
  })
}

/*
 * A dica só aparece se este script rodou — anunciada pelo template, seria
 * mentira com o JS desligado. E reaparece a cada troca de página, porque a
 * navegação instantânea substitui o rodapé inteiro.
 */
function anunciaAtalhos() {
  const navegacao = document.querySelector(".md-footer__inner")
  if (!navegacao || navegacao.parentElement.querySelector(".vimbook-atalhos")) {
    return
  }

  const dica = document.createElement("p")
  dica.className = "vimbook-atalhos"
  dica.append(
    tecla("h"),
    tecla("l"),
    " virar a página · ",
    tecla("j"),
    tecla("k"),
    " rolar",
  )
  navegacao.after(dica)
}

function tecla(nome) {
  const kbd = document.createElement("kbd")
  kbd.textContent = nome
  return kbd
}

if (window.document$) {
  window.document$.subscribe(anunciaAtalhos)
} else {
  document.addEventListener("DOMContentLoaded", anunciaAtalhos)
}
