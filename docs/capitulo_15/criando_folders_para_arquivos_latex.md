Criando *folders* para arquivos LaTeX
-------------------------------------
```
set foldmarker=\\begin,\\end
set foldmethod=marker
```

Adicionar marcadores (*labels*) às seções de um documento *LaTeX*
```
:.s/^\(\\section\)\({.*}\)/\1\2\r\\label\2

: ........... comando
/ ........... inicia padrão de busca
^ ........... começo de linha
\(palavra\) . agrupa um trecho
\(\\section\) agrupa `\section'
\\ .......... torna \ literal
{ ........... chave literal
.* .......... qualquer caractere em qualquer quantidade
} ........... chave literal
/ ........... finaliza parão de busca
\1 .......... repeter o grupo 1 \(\\section\)
\2 .......... repete o grupo 2 \({.*\}\)
\r .......... insere quebra de linha
\\ .......... insere uma barra invertida
\2 .......... repete o nome da seção
```
