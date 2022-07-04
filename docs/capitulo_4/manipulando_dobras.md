Manipulando dobras
-------------------

Os principais comandos relativos ao uso de dobras são:
```
zo ................ abre a dobra
zO ................ abre a dobra, recursivamente
za ................ abre/fecha (alterna) a dobra
zA ................ abre/fecha (alterna) a dobra, recursivamente
zR ................ abre todas as dobras do arquivo atual
zM ................ fecha todas as dobras do arquivo atual
zc ................ fecha uma dobra
zC ................ fecha a dobra abaixo do cursor, recursivamente
zfap .............. cria uma dobra para o parágrafo 'ap' atual
zf/casa ........... cria uma dobra até a palavra casa
zf'a .............. cria uma dobra até a marca 'a'
zd ................ apaga a dobra (não o seu conteúdo)
zj ................ move para o início da próxima dobra
zk ................ move para o final da dobra anterior
[z ................ move o cursor para início da dobra aberta
]z ................ move o cursor para o fim da dobra aberta
zi ................ desabilita ou habilita as dobras
zm, zr ............ diminui/aumenta nível da dobra 'fdl'
:set fdl=0 ........ nível da dobra 0 (foldlevel)
:set foldcolumn=4 . mostra uma coluna ao lado da numeração
```
Para abrir e fechar as dobras usando a barra de espaços coloque o trecho
abaixo no seu arquivo de configuração do Vim (`.vimrc`) - veja o
[Como editar preferências no Vim](../capitulo_12/como_editar_preferencias_no_vim.md).
```
nnoremap <space> @=((foldclosed(line(".")) < 0) ?
				  \ 'zc' : 'zo')<CR>
```
A barra, `\`, nesse comando representa o particionamento do comando em
mais de uma linha.

Para abrir e fechar as dobras utilizando o clique do mouse no gvim,
basta acrescentar na configuração do seu `.vimrc`:
```
set foldcolumn=2
```
o que adiciona uma coluna ao lado da coluna de enumeração das linhas.
