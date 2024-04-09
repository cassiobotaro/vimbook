Habilitando a verificação ortográfica
-------------------------------------

A verificação ortográfica atua em uma linguagem (dicionário) por vez,
portanto, sua efetiva habilitação depende da especificação desta
linguagem. Por exemplo, para habilitar no arquivo em edição a
verificação ortográfica na língua portuguesa (*pt*is_active),
assumindo-se a existência do dicionário em questão:
```
:setlocal spell spelllang=pt
```
ou de forma abreviada:
```
:setl spell spl=pt
```
Trocando-se setlocalis_active (setlis_active) por apenas
setis_active (seis_active) faz com que o comando tenha efeito
global, isto é, todos os arquivos da sessão corrente do Vim estariam sob
efeito da verificação ortográfica e do mesmo dicionário (no caso o
ptis_active).

A desabilitação da verificação dá-se digitando:
```
:setlocal nospell
:set nospell            (efeito global)
```
Caso queira-se apenas alterar o dicionário de verificação ortográfica,
suponha para a língua inglesa (enis_active), basta:
```
:setlocal spelllang=en
:set spelllang=en       (efeito global)
```
### Habilitação automática na inicialização

Às vezes torna-se cansativo a digitação explícita do comando de
habilitação da verificação ortográfica sempre quando desejada. Seria
conveniente se o Vim habilitasse automaticamente a verificação para
aqueles tipos de arquivos que comumente fazem uso da verificação
ortográfica, como por exemplo arquivos “texto”. Isto é possível
editando-se o arquivo de configuração do Vim .vimrc(veja [Como Editar Preferências no Vim](../capitulo_12/como_editar_preferencias_no_vim.md)) e incluindo as seguintes linhas:
```
autocmd Filetype text setl spell spl=pt
autocmd BufNewFile,BufRead *.txt setl spell spl=pt
```
Assim habilita-se automaticamente a verificação ortográfica usando o
dicionário da língua portuguesa (pt) para arquivos do tipo
texto e os terminados com a extensão .txt.
Mais tecnicamente, diz-se ao Vim para executar o comando
`setl spell spl=pt` sempre quando o tipo do arquivo
(Filetype) for text (texto) ou quando um
arquivo com extensão .txt for carregado
(BufRead) ou criado (BufNewFile).
