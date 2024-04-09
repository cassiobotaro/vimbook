Gravando comandos
-----------------

Imagine que você tem o seguinte trecho de código:
```c
stdio.h
fcntl.h
unistd.h
stdlib.h
```
e quer que ele fique assim:
```c
#include "stdio.h"
#include "fcntl.h"
#include "unistd.h"
#include "stdlib.h"
```
Não é possível simplesmente executar repetidas vezes um comando do Vim,
pois é preciso incluir texto tanto no começo quanto no fim da linha? É
necessário mais de um comando para isso. É aí que entram as macros.
Pode-se gravar até 26 macros, já que elas são guardadas nos registradores do
Vim, que são identificados pelas letras do alfabeto. Para começar a
gravar uma macro no registrador ‘a’, digitamos
```
qa
```
No modo Normal. Tudo o que for digitado a partir de então, será gravado
no registrador ‘a’ até que seja concluído com o comando `<Esc>q` novamente
(no modo Normal). Assim, soluciona-se o problema:
```
<Esc> ....... para garantir que estamos no modo normal
qa .......... inicia a gravação da macro `a'
I ........... entra no modo de inserção no começo da linha
#include " .. insere #include "
<Esc> ....... sai do modo de inserção
A" .......... insere o último caractere
<Esc> ....... sai do modo de inserção
j ........... desce uma linha
<Esc> ....... sai do modo de inserção
q ........... para a gravação da macro
```
Agora só é preciso posicionar o cursor na primeira letra de uma linha
como esta
```c
stdio.h
```
E executar a macro do registrador ‘a’ quantas vezes for necessário, usando
o comando `@a`. Para executar quatro vezes, digite:
```
4@a
```
Este comando executa quatro vezes o conteúdo do registrador ‘a’.

Caso tenha sido executada, a macro pode ser repetida com o comando
```
@@
```
