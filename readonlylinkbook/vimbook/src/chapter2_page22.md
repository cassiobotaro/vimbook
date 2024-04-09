Substituindo tabulações por espaços
-----------------------------------

Se houver necessidade[^1] de trocar tabulações por espaços fazemos
assim:
```
:set tabstop=4 "tamanho da parada de tabulação
:set expandtab
:retab
```
Para fazer o contrário usamos algo como:
```
:%s/\s\{4,}/<pressiona-se ctrl-i>/g
```
onde
```
<Ctrl-i>...... insere uma tabulação
```
Explicando:
```
: ............ comando
% ............ em todo arquivo
s ............ substitua
/ ............ padrão de busca
\s ........... localiza espaço
\{4,} ........ quatro vezes
/ ............ inicio da substituição
<Ctrl-i> ..... pressione Ctrl-i para inserir <Tab>
/ ............ fim da substituição
g ............ global
```
[^1]: Em códigos Python por exemplo não se pode misturar espaços e tabulações
