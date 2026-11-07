---
title: Não digite duas vezes
---

-   O Vim complementa com ‘tab’. Veja mais no capítulo [complementação com "tab"](../capitulo_12/complementacao_com_tab.md)

-   Use macros. Detalhes no capítulo [gravando comandos](../capitulo_8/gravando_comandos.md).

-   Use abreviações. Coloque abreviações como abaixo em seu `~/.vimrc`.
    Veja mais no capítulo [abreviações](../capitulo_12/abreviacoes.md).

-   As abreviações fazem o mesmo que autocorreção e autotexto em
    outros editores
```vim
iab tambem também
iab linux GNU/Linux
```
No modo de inserção você pode usar:

| Comando | Descrição |
|---------|-----------|
| `Ctrl-Y` | copia caractere a caractere a linha acima |
| `Ctrl-E` | copia caractere a caractere a linha abaixo |
| `Ctrl-X Ctrl-L` | completa linhas inteiras |

Para um trecho muito copiado coloque o seu conteúdo em um registrador:

| Comando | Descrição |
|---------|-----------|
| `"ayy` | copia a linha atual para o registrador `a' |
| `"ap` | cola o registrador `a' |

Crie abreviações para erros comuns no seu arquivo de configuração
(`~/.vimrc`):

```vim
iabbrev teh the
syntax keyword WordError teh
```
As linhas acima criam uma abreviação para erro de digitação da palavra
‘the’ e destacam textos que você abrir que contenham este erro.
