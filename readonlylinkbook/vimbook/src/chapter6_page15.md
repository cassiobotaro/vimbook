Obtendo informações do arquivo
------------------------------
```
ga ............. mostra o código do caractere em decimal hexa e octal
^g ............. mostra o caminho e o nome do arquivo
g^g ............ mostra estatísticas detalhadas do arquivo
```
Obs: O código do caractere pode ser usado para substituições,
especialmente em se tratando de caracteres de controle como tabulações
`^I` ou final de linha DOS/Windows `\%x0d`. Você pode apagar os
caracteres de final de linha Dos/Windows usando uma simples
substituição, veja mais adiante:
```
:%s/\%x0d//g
```
Uma forma mais prática de substituir o terminador de linha DOS para o
terminador de linha Unix:
```
:set ff=unix
:w
```
Na seção [Como editar preferências no Vim](../capitulo_12/como_editar_preferencias_no_vim.md) há um código para
a barra de status que faz com que a mesma exiba o código do caractere
sob o cursor na seção [Função para barra de status](../capitulo_12/funcoes.md). O caractere de
final de linha do Windows/DOS pode ser inserido com a seguinte
combinação de teclas:
```
i ............ entra em modo de inserção
<INSERT> ..... entra em modo de inserção
Ctrl-v Ctrl-m  insere o simbolo ^M (terminador de linha DOS)
```
