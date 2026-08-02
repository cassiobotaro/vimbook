Por vezes sabemos que aquela anotação foi feita, mas no momento
esquecemos em qual arquivo está, no exemplo abaixo procuramos a palavra
dicas a partir da nossa pasta pessoal pela palavra ‘dicas’ em todos os
arquivos com extensão ‘txt’.
O `~/` equivale a `/home/user`.
```
:lvimgrep /dicas/gj ~/**/*.txt | lopen
:vimgrep /dicas/gj **/*.txt | copen
:vimgrep dicas **/*.txt | copen
```
Use `:h lvim` para a ajuda sobre o comando.
