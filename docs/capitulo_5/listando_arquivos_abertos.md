
Suponha que você abriu vários arquivos txt assim:
```bash
vim *.txt
```
Para listar os arquivos abertos, faça:
```vim
:buffers
```
Usando o comando acima o Vim exibirá a lista de todos os arquivos
abertos, após exibir a lista você pode escolher um dos arquivos da
lista, algo como:
```vim
:buf 3
```
Para editar arquivos em sequência faça as alterações no arquivo atual e
acesse o próximo assim:
```vim
:wn
```
O comando acima diz -> 'w gravar' -> 'n próximo'
