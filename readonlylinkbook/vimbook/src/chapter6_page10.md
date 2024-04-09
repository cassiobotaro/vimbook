Filtrando arquivos com o vimgrep
--------------------------------------------

Por vezes sabemos que aquela anotação foi feita, mas no momento
esquecemos em qual arquivo está, no exemplo abaixo procuramos a palavra
dicas à partir da nossa pasta pessoal pela palavra ‘dicas’ em todos os
arquivos com extensão ‘txt’.
```
~/ ............ equivale a /home/user
:lvimgrep /dicas/gj ~/**/*.txt | ls
:vimgrep /dicas/gj **/*.txt | copen
:vimgrep dicas **/*.txt | copen
:h lvim ....... ajuda sobre o comando
```
