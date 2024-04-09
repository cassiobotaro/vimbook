Set
---

Os comandos *set*, responsáveis por atribuir valores à
variáveis, podem ser colocados no `.vimrc`:
```
set nu
```
ou digitados como comandos:
```
:set nu
```
```
set number ............... "mostra numeração de linhas
set nu ................... "simplificação de `number'
set showmode ............. "mostra o modo em que estamos
set showcmd .............. "mostra no status os comandos inseridos
set tabstop=4 ............ "tamanho das tabulações
set ts=4 ................. "simplificação de `tabstop'
set shiftwidth=4 ......... "quantidade de espaços de uma
                       tabulação
set sw=4 ................. "simplificação de `shiftwidth'
syntax on ................ "habilita cores
syn on ................... "simplificação de `syntax'
colorscheme tema ......... "esquema de cores `syntax highlight'
autochdir ................ "configura o diretório de trabalho
set hls .................. "destaca com cores os termos procurados
set incsearch ............ "habilita a busca incremental
set ai ................... "auto identação
set aw ................... "salva automaticamente ao trocar de
                       `buffer'
set ignorecase ........... "ignora maiúsculas e minúsculas nas
                       buscas
set ic ................... "simplificação de ignorecase
set smartcase ............ "numa busca em maiúsculo habilita
                       `case'
set scs .................. "sinônimo de `smartcase'
set backup ............... "habilita a criação de arquivos de
                       backup
set bk ................... "simplificação de `backup'
set backupext=.backup .... "especifica a extensão do arquivo de
                       backup
set bex=.backup .......... "simplificação de backupext
set backupdir=~/.backup,./ "diretório(s) para arquivos de backup
set bdir ................. "simplificação de `backupdir'
set nobackup ............. "evita a criação de arquivos de backup
ste nobk ................. "simplificação de `nobackup'
set cursorline ........... "abreviação de cursor line (destaca
                       linha  atual)
set cul .................. "simplificação de `cursorline'
set ttyfast .............. "melhora o redraw de janelas.
set columns=88 ........... "deixa a janela com 88 colunas.
set mousemodel=popup ..... "exibe o conteúdo de folders e
                       sugestões spell
set viminfo=%,'50,\"100,/100,:100,n "armazena opções (buffers)
```
Se ao iniciar o vim obtivermos mensagens de erros e houver dúvida se o
erro é no vim ou em sua configuração, pode-se inicia-lo sem que o mesmo
carregue o arquivo `.vimrc`.
```
:vim -u NONE
```
