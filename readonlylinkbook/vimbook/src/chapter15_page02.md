O plugin *Ctags*
----------------

*Ctags* em si é um programa externo que indexa arquivos de código fonte. Ele lê
o código fonte em busca de identificadores, declarações de função, variáveis,
e constrói seu índex de referências cruzadas. Mas vamos ao plugin,
mesmo por que não estamos no CtagsBook.

Primeiro precisamos ter o arquivos de tags. Para tal, usamos o comando:

```
ctags -R <arquivos>
```

Normalmente o parâmetro `<arquivos>` pode ser uma expressão regular
do tipo `*.[ch]` e afins. Depois de obter o arquivo de tags, você já pode
sair usando os atalhos do plugin para navegar pelo código fonte.
Com o cursor em cima de um identificador, usando o atalho `ctrl+]`
o cursor pula diretamente para a sua declaração. O atalho `ctrl+o`
volta o cursor para a posição inicial.

Quando navegando por um código fonte muito extenso com vários diretórios,
é possível mapear o caminho dos arquivos usando o caminho absoluto deles no seu
diretório de trabalho deste jeito:

```
find $(pwd) -regex ".*py$" | xargs ctags
```

Assim você pode copiar o arquivo de tags para todos os diretórios e mesmo
assim conseguir usar os atalhos do plugin para navegar no código fonte.

Pode-se obter o programa *Ctags* neste
[link](http://ctags.sourceforge.net/).
O plugin de *Ctags* para o Vim está neste
[link](http://vim.sourceforge.net/scripts/script.php?script_id=12),
e para instalá-lo basta copiá-lo para a pasta apropriada:

```
 ~/vimfiles/plugin .......... no windows
 ~/.vim/plugin .............. no Gnu/Linux
```
