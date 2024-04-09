Folders
=======

*Folders* são como dobras nas quais o Vim esconde partes do
texto, algo assim:
```
+-- 10 linhas ---------------------------
```
Deste ponto em diante chamaremos os *folders* descritos no
manual do Vim como dobras! Quando tiver que manipular grandes
quantidades de texto tente usar dobras, isto permite uma visualização
completa do texto. Um modo de entender rapidamente como funcionam as
dobras no Vim seria criando uma “dobra” para as próximas 10 (dez) linhas
com o comando abaixo:
```
zf10j
```
Você pode ainda criar uma seleção visual
```
Shift-v ............ seleção por linha
j .................. desce linha
zf ................. cria o folder
zo ................. abre o folder
```
