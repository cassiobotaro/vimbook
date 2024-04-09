Desfazendo
----------

Se você cometer um erro, não se preocupe! Use o comando `u`:
```
u ............ desfazer
U ............ desfaz mudanças na última linha editada
Ctrl-r  ...... refazer
```
### Undo tree

Um novo recurso muito interessante que foi adicionado ao Vim a partir da
versão 7 é a chamada árvore do desfazer. Se você desfaz alguma coisa e
faz uma alteração, um novo `branch` (galho) ou derivação de
alteração é criado. Basicamente, os `branches` nos permitem
acessar quaisquer alterações ocorridas no arquivo.

#### Um exemplo didático

Siga estes passos (para cada passo `<Esc>`, ou seja, saia do modo de
inserção)

Passo 1

:   - digite na linha 1 o seguinte texto
```
# controle de fluxo <Esc>
```
Passo 2

:   - digite na linha 2 o seguinte texto
```
# um laço for <Esc>
```
Passo 3

:   - Nas linhas 3 e 4 digite...
```
for i in range(10):
    print i  <Esc>
```
Passo 4

:   - pressione `u` duas vezes (você voltará ao passo 1)

Passo 5

:   - Na linha 2 digite
```
# operador ternário <Esc>
```
Passo 6

:   - na linha 3 digite
```
var = (1 if teste == 0 else 2)  <Esc>
```
Obs: A necessidade do `Esc` é para demarcar as ações, pois o
Vim considera cada inserção uma ação. Agora usando o atalho de desfazer
tradicional “u” e de refazer `Ctrl-r` observe que não é mais
possível acessar todas as alterações efetuadas. Em resumo, se você fizer
uma nova alteração após um desfazer (alteração derivada) o comando
refazer não mais vai ser possível para aquele momento.

Agora volte até a alteração 1 e use seguidas vezes:

```
g+
```

e/ou

```
g-
```
Dessa forma você acessará todas as alterações ocorridas no texto.

### Máquina do tempo

O Vim possui muitas formas para desfazer e refazer, e uma das mais
interessantes é a máquina do tempo! A máquina do tempo é extremamente
útil quando no meio de um texto se percebe que boa parte do que foi
adicionado é inútil e que nos ultimos 10 minutos não há nada que se
possa aproveitar. Utilizando a máquina do tempo é possível eliminar os
últimos 10 minutos de texto inútil do seu documento facilmente,
utilizando:
```
:earlier 10m
```
Com esse comando o documento ficará exatamente como ele estava 10
minutos atrás! Caso após a exclusão perceba-se que foi excluído um
minuto a mais, é possível utilizar o mesmo padrão novamente para avançar
no tempo:
```
:later 60s
```
Note que dessa vez foi utilizado `later` ao invés de
`earlier`, e passando segundos como argumento para viajar
no tempo. Portanto o comando acima avança 60 segundos no tempo.

Para uma melhor visão de quanto se deve voltar, pode ser usado o
comando:
```
:undolist
```
O comando acima mostra a lista com as informações sobre Desfazer e
Refazer. E com essas informações pode-se voltar no tempo seguindo cada
modificação:
```
:undo 3
```
Esse comando fará o documento regredir 3 modificações.
