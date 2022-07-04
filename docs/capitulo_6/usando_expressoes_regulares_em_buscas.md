Usando “Expressões Regulares” em buscas
----------------------------------------------------------
```
/ ........... inicia uma busca (modo normal)
\%x69 ....... código da letra `i'
/\%x69 ...... localiza a letra `i' - hexadecimal 069
\d .......... localiza números
[3-8] ....... localiza números de 3 até 8
^ ........... começo de linha
$ ........... final de linha
\+ .......... um ou mais
/^\d\+$ ..... localiza somente dígitos
/\r$ ........ localiza linhas terminadas com ^M
/^\s*$ ...... localiza linhas vazias ou contendo apenas espaços
/^\t\+ ...... localiza linhas que iniciam com tabs
\s .......... localiza espaços
/\s\+$ ...... localiza espaços no final da linha
```
### Evitando escapes ao usar Expressões regulares

O Vim possui um modo chamado “*very magic*” para uso em
expressões regulares que evita o uso excessivo de escapes, alternativas
etc. Usando apenas uma opção: veja `:h /\v`.

Em um trecho com dígitos + texto + dígitos no qual se deseja manter só
as letras.
```
12345aaa678
12345bbb678
12345aac678
```
Sem a opção “*very magic*” faríamos:
```
:%s/\d\{5\}\(\D\+\)\d\{3\}/\1/
```
Já com a opção “*very magic*” `\v` usa-se bem menos
escapes:
```
:%s/\v\d{5}(\D+)\d{3}/\1/

" explicação do comando acima
: ......... comando
% ......... em todo arquivo
s ......... substitua
/ ......... inicia padrão de busca
\v ........ use very magic mode
\d ........ dígitos
{5} ....... 5 vezes
( ........ inicia um grupo
\D ........ seguido de não dígitos
)  ........ fecha um grupo
+ ......... uma ou mais vezes
\d ........ novamente dígitos
{3} ....... três vezes
/ ......... inicio da substituição
\1 ........ referencia o grupo 1
```
Analisando o exemplo anterior, a linha de raciocínio foi a de “manter o
texto entre os dígitos”, o que pode ser traduzido, em uma outra forma de
raciocínio, como “remover os dígitos”.
```
:%s/\d//g

" explicação do comando acima
% ......... em todo arquivo
s ......... substitua
/ ......... inicia padrão de busca
\d ........ ao encontrar um dígito
/ ......... subtituir por
vazio ..... exato, substituir por vazio
/g ........ a expressão se torna gulosa
```
Por guloso - `/g` - se entende que ele pode e deve tentar achar mais de
uma ocorrência do padrão de busca na mesma linha. Caso não seja gulosa,
a expressão irá apenas casar com a primeira ocorrência em cada linha.

#### Classes *POSIX* para uso em Expressões Regulares

Ao fazermos substituições em textos poderemos nos deparar com erros,
pois [a-z] não inclui caracteres acentuados, as classes
*POSIX* são a solução para este problema, pois adequam o
sistema ao idioma local, esta é a mágica implementada por estas classes.
```
[:lower:] ...... letras minúsculas incluindo acentos
[:upper:] ...... letras maiúsculas incluindo acentos
[:punct:] ...... ponto, virgula, colchete, etc
```
Para usar estas classes fazemos:
```
:%s/[[:lower:]]/\U&/g

Explicando o comando acima:
: ....... modo de comando
% ....... em todo o arquivo atual
s ....... substitua
/ ....... inicia o padrão a ser buscado
[ ....... inicia um grupo
[: ...... inicia uma classe POSIX
lower ... letras minúsculas
:] ...... termina a classe POSIX
] ....... termina o grupo
/ ....... inicia substituição
\U ...... para maiúsculo
& ....... correponde ao que foi buscado
```
Nem todas as classes *POSIX* conseguem pegar caracteres
acentuados, portanto deve-se habilitar o destaque colorido para buscas
usando:
```
:set hlsearch .... destaque colorido para buscas
:set incsearch ... busca incremental
```
Dessa forma podemos testar nossas buscas antes de fazer uma
substituição.

Para aprender mais sobre Expressões Regulares leia:

-   [Guia sobre Espressões Regulares](http://guia-er.sourceforge.net)

-   :help regex

-   :help pattern

Uma forma rápida para encontrar a próxima ocorrência de uma palavra sob
o cursor é teclar `*`. Para encontrar uma ocorrência anterior da
palavra sob o cursor, existe o `#` (em ambos os casos o cursor deve
estar posicionado sobre a palavra que deseja procurar). As duas opções
citadas localizam apenas se a palavra corresponder totalmente ao padrão
sob o cursor, pode-se bucar por trechos de palavras que façam parte de
palavras maiores usando-se `g*`. Pode-se ainda exibir “dentro do
contexto” todas as ocorrências de uma palavra sob o cursor usando-se o
seguinte atalho em modo normal:
```
[ Shift-i
```
