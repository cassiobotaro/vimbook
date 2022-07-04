Use marcas
----------

veja a seção [Usando marcas](../capitulo_3/usando_marcas.md).
```
ma ..... em modo normal cria uma marca `a'
'a ..... move o cursor até a marca `a'
d'a .... deleta até a marca `a'
y'a .... copia até a marca `a'

gg ... vai para a linha 1 do arquivo
G .... vai para a última linha do arquivo
0 .... vai para o início da linha
$ .... vai para o fim da linha
fx ... pula até a próxima ocorrência de ``x''
dfx .. deleta até a próxima ocorrência de ``x''
g, ... avança na lista de alterações
g; ... retrocede na lista de alterações
p .... cola o que foi deletado/copiado abaixo
P .... cola o que foi deletado/copiado acima
H .... posiciona o cursor no primeiro caractere da tela
M .... posiciona o cursor no meio da tela
L .... posiciona o cursor na última linha da tela

* ........ localiza a palavra sob o cursor
% ........ localiza fechamentos de chaves, parênteses etc.
g* ....... localiza palavra parcialmente

'.  apostrofo + ponto retorna ao último local editado
'' retorna ao local do ultimo salto
```

Suponha que você está procurando a palavra ‘argc’:

```
/argc
```

Digita ‘n’ para buscar a próxima ocorrência

```
n
```

Um jeito mais fácil seria:

```
"coloque a linha abaixo no seu vimrc
:set hlsearch
```

Agora use asterisco para destacar todas as ocorrências do padrão
desejado e use a letra ‘n’ para pular entre ocorrências, caso deseje
seguir o caminho inverso use ‘N’.
