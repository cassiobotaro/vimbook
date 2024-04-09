Mapeamentos
-----------

Mapeamentos permitem criar atalhos de teclas para quase tudo. Tudo
depende da criatividade do usuário e do quanto conhece o Vim, com eles
podemos controlar ações com quaisquer teclas, mas antes temos que saber
que para criar mapeamentos, precisamos conhecer a maneira de representar
as teclas e combinações. Alguns exemplos:
```
tecla ....... tecla mapeada

<c-x> ....... Ctrl-x
<left> ...... seta para a esquerda
<right> ..... seta para a direita
<c-m-a> ..... Ctrl-Alt-a
<cr> ........ Enter
<Esc> ....... Escape
<leader> .... normalmente \
<bar> ....... | pipe
<cword> ..... palavra sob o cursor
<cfile> ..... arquivo sob o cursor
<cfile> ..... arquivo sob o cursor sem extensão
<sfile> ..... conteúdo do arquivo sob o cursor
<left> ...... salta um caractere para esquerda
<up> ........ equivale clicar em `seta acima'
<m-f4> ...... a tecla alt (m) mais a tecla f4
<c-f> ....... Ctrl-f
<bs> ........ backspace
<space> ..... espaço
<tab> ....... tab
```
No Vim podemos mapear uma tecla para o modo normal, realizando
determinada operação e a mesma tecla pode desempenhar outra função
qualquer em modo de inserção ou comando, veja:
```VimL
" mostra o nome do arquivo com o caminho
map <F2> :echo expand("%:p")
" insere um texto qualquer
imap <F2> Nome de uma pessoa
```
A única diferença nos mapeamentos acima é que o mapeamento para modo de
inserção começa com `i`, assim como para o modo “comando” `:` começa
com `c` no caso `cmap`. O comando `:echo` pode ser abreviado
assim: `:ec`.

### Recarregando o arquivo de configuração

Cada alteração no arquivo de configuração do Vim só terá efeito na
próxima vez que você abrir o Vim a menos que você coloque isto dentro do
mesmo
```VimL
" recarregar o vimrc
" Source the .vimrc or _vimrc file, depending on system
if &term == "win32" || "pcterm" || has("gui_win32")
   map ,v :e $HOME/_vimrc<CR>
   nmap <F12> :<C-u>source ~/_vimrc <BAR> echo "Vimrc recarregado!"<CR>
else
   map ,v :e $HOME/.vimrc<CR>
   nmap <F12> :<C-u>source ~/.vimrc <BAR> echo "Vimrc recarregado!"<CR>
endif
```
Agora basta pressionar `<F12>` em modo normal e as alterações passam a
valer instantaneamente, e para chamar o `vimrc` basta usar.
```
,v
```
Os mapeamentos abaixo são úteis para quem escreve códigos HTML, permitem
inserir caracteres reservados do HTML usando uma barra invertida para
proteger os mesmos, o Vim substituirá os “barra alguma coisa” pelo
caractere correspondente.
```VimL
inoremap \&amp; &amp;amp;
inoremap \&lt; &amp;lt;
inoremap \&gt; &amp;gt;
inoremap \. &amp;middot;
```
O termo **inoremap** significa: em modo de inserção não
remapear, ou seja ele mapeia o atalho e não permite que o mesmo seja
remapeado, e o mapeamento só funciona em modo de inserção, isso
significa que um atalho pode ser mapeado para diferentes modos de
operação.\

Veja este outro mapeamento:
```VimL
map <F11> <Esc>:set nu!<cr>
```
Permite habilitar ou desabilitar números de linha do arquivo corrente. A
exclamação ao final torna o comando booleano, ou seja, se a numeração
estiver ativa será desabilitada, caso contrário será ativada. O `<cr>`
ao final representa um *Enter*.

### Limpando o “registrador” de buscas

A cada busca, se a opção ‘*hls*’[^1] estiver habilitada o Vim
faz um destaque colorido, para desabilitar esta opção pode-se criar um
mapeamento qualquer, no caso abaixo usando a combinação de teclas
`<S-F11>`.
```VimL
nno <S-F11> <Esc>:let @/=""<CR>
```
É um mapeamento para o modo normal que faz com que a combinação de
teclas `Shift-F11` limpe o “registrador” de buscas

### Destacar palavra sob o cursor
```VimL
nmap <s-f> :let @/=">"<CR>
```
O atalho acima `s-f` corresponde a `Shift-f`.

### Contar ocorrências de uma palavra
```VimL
" contagem de ocorrências de uma palavra (case insensitive)
" busca somente ocorrências exatas
nmap <F4> <esc>mz:%s/\c\<\(<c-r>=expand("<cword>")<cr>\)\>//gn<cr>`z
" busca parcial, ou seja acha palavra como parte de outra
nmap <s-F4> <esc>mz:%s/\c\(<c-r>=expand("<cword>")<cr>\)//gn<cr>`z
```
### Remover linhas em branco duplicadas
```VimL
map ,d <Esc>:%s/\(^\n\{2,}\)/\r/g<cr>
```
No mapeamento acima estamos associando o atalho:
```
,d
```
… à ação desejada, fazer com que linhas em branco sucessivas sejam
substituídas por uma só linha em branco, vejamos como funciona:
```
map ......... mapear
,d .......... atalho que quermos
<Esc> ....... se estive em modo de inserção sai
: ........... em modo de comando
% ........... em todo o arquivo
s ........... substitua
\n .......... quebra de linha
{2,} ........ duas ou mais vezes
\r .......... trocado por \r Enter
g ........... globalmente
<cr> ........ confirmação do comando
```
As barras invertidas podem não ser usadas se o seu Vim estiver com a
opção **magic** habilitada
```
:set magic
```
Por acaso este é um padrão portanto tente usar assim pra ver se funciona
```
map ,d :%s/\n{2,}/\r/g<cr>
```
### Mapeamento para Calcular Expressões

Os mapeamentos abaixo exibem o resultado das quatro operações básicas
(soma, subtração, multiplicação e divisão). O primeiro para o modo
normal no qual posiciona-se o cursor no primeiro caractere da expressão
tipo `5\9` e em seguida pressiona-se
“*Shift-F1*”, o segundo para o modo **insert** em
que, após digitada a expressão pressiona-se o mesmo atalho.
```VimL
" calculadora
map <s-f1> <esc>0"myEA=<c-r>=<c-r>m<enter><esc>
imap <s-f1> <space><esc>"myBEa=<c-r>=<c-r>m<enter><del>
```
Para efetuar cálculos com maior precisão e também resolver problemas
como potências raízes, logaritmos pode-se mapear comandos externos, como
a biblioteca matemática da linguagem de programação Python.
[Neste link](http://vim.wikia.com/wiki/Scientific_calculator)
há um manual que ensina a realizar este procedimento, ou acesse o
capítulo [Uma calculadora diferente](../capitulo_2/uma_calculadora_diferente.md).

### Mapeamentos globais

Podemos fazer mapeamentos globais ou que funcionam em apenas um modo:
```
map  - funciona em qualquer modo
nmap - apenas no modo Normal
imap - apenas no modo de Inserção
```
Mover linhas com *Ctrl-⬇* ou
*Ctrl-⬆*
```VimL
" tem que estar em modo normal!
nmap <C-Down> ddp
nmap <C-Up> ddkP
```
Salvando com uma tecla de função:
```VimL
" salva com F9
nmap <F9> :w<cr>
" F10 - sai do Vim
nmap <F10> <Esc>:q<cr>
```
### Convertendo as iniciais de um documento para maiúsculas
```VimL
" MinusculasMaiusculas: converte a primeira letra de cada
" frase para MAIÚSCULAS
nmap ,mm :%s/\C\([.!?][])"']*\($\|[ ]\)\_s*\)\(\l\)/\1\U\3/g<CR>
" Caso queira confirmação coloque uma letra ``c'' no final da
" linha acima:
" (...) \3/gc<CR>
```

[^1]: hls é uma abreviação de hightlight search
