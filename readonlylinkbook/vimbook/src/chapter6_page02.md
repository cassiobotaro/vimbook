Buscas e Substituições
======================

Para fazer uma busca, certifique-se de que está em modo normal,
pressione “/” e digite a expressão a ser procurada.\

Para encontrar a primeira ocorrência de “foo” no texto:
```
/foo
```
Para repetir a busca basta pressionar a tecla `n` e para repetir a
busca em sentido oposto `N`.
```
/teste/+3
```
Posiciona o cursor três linhas após a ocorrência da palavra “teste”\
```
/\<casa\>
```
A busca acima localiza ‘casa’ mas não
‘casamento’. Em expressões regulares, `\<` e `\>` são
representadas por `\b`, que representa, por sua vez, borda de palavras.
Ou seja, `casa` e `casa!` seriam
localizado, visto que sinais de pontuação não fazem parte da palavra.
