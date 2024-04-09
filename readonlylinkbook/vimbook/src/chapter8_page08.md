Repetição de Comandos
=====================

Para repetir a última edição saia do modo de Inserção e pressione ponto (.):

Para inserir um texto que deve ser repetido várias vezes:

1.  Posicione o cursor no local desejado;

2.  Digite o número de repetições;

3.  Entre em modo de inserção;

4.  Digite o texto;

5.  Saia do modo de inserção (tecle Esc).

Por exemplo, se você quiser inserir oitenta traços numa linha, em vez de
digitar um por um, você pode digitar o comando:
```
80i-<Esc>
```
Veja, passo a passo, o que aconteceu:

Antes de entrar em modo de inserção usamos um quantificador
```
`80`
```
depois iniciamos o modo de inserção
```
i
```
depois digitamos o caractere a ser repetido
```
-
```
e por fim saímos do modo de inserção
```
<Esc>
```
Se desejássemos digitar 10 linhas com o texto
```
isto é um teste
```
deveríamos então fazer assim:
```
<Esc> .. para ter certeza que ainda estamos no modo normal
10 ..... quantificador antes
i ...... entrar no modo de inserção
isto é um teste <Enter>
<Esc> .. voltar ao modo normal
```
