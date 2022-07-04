
Listando arquivos abertos
-------------------------

Suponha que você abriu vários arquivos txt assim:
```
vim *.txt
```
Para listar os arquivos aberto faça:
```
:buffers
```
Usando o comando acima o Vim exibirá a lista de todos os arquivos
abertos, após exibir a lista você pode escolher um dos arquivos da
lista, algo como:
```
:buf 3
```
Para editar arquivos em sequência faça as alterações no arquivo atual e
acesso o próximo assim:
```
:wn
```
O comando acima diz -> 'w gravar' -> 'n próximo'
