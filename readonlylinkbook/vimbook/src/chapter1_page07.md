Modos de operação
-----------------

A tabela abaixo mostra uma referência rápida para os modos de operação
do Vim, a seguir mais detalhes sobre cada um dos modos.

|Modo|Descrição|Atalho|
|----|---------|------|
|Normal| Para deletar, copiar, formatar, etc | `<esc>` |
|Inserção| Prioritariamente, digitação de texto| i, a, I, A, o, O |
|Visual| Seleção de blocos verticais e linhas inteiras |V, v, Ctrl-v|
|Comando| Uma verdadeira linguagem de programação | `<esc>`: |

Em oposição à esmagadora maioria dos editores o Vim é um editor que
trabalha com “modos de operação (modo de inserção, modo normal, modo
visual e etc)”, o que a princípio dificulta a vida do iniciante, mas
abre um universo de possibilidades, pois ao trabalhar com modos
distintos uma tecla de atalho pode ter vários significados,
exemplificando: Em modo normal pressionar `dd` apaga a
linha atual, já em modo de inserção ele irá se comportar como se você
estivesse usando qualquer outro editor, ou seja, irá inserir duas vezes
a letra `d`. Em modo normal pressionar a tecla
`v` inicia uma seleção visual (use as setas de direção).
Para sair do modo visual `<Esc>`. Como um dos princípios do vim é
agilidade pode-se usar ao invés de setas (em modo normal) as letras
`h,l,k,j` como se fossem setas:
```
    k
h       l
    j
```

Imagine as letras acima como teclas de direção, a letra `k`
é uma seta acima a letra `j` é uma seta abaixo e assim por
diante.
