Editando saídas do Shell
------------------------

Muitas vezes, precisamos manipular saídas do shell antes de enviá-las
por e-mail, reportar ao chefe ou até mesmo salvá-las. Utilizando
```
vim -
ou
gvim -
```
a saída do Shell é redirecionada para o (G)Vim automaticamente, não
sendo necessário redirecioná-la para um arquivo temporário e, logo após,
abrí-lo para editá-lo e modificá-lo. Quem trabalha com sistemas de
controle de versão como svn pode visualizar as diferenças entre o código
que está sendo editado e o que está no repositório com sintaxe colorida
desta forma:
```
svn diff | view -
```
Outra situação em que se pode combinar o vim com saidas do shell é com o
comando `grep`. Usando-se a opção `-l` do grep listamos apenas os
arquivos que correspondem a um padrão.
```
grep -irl voyeg3r .
./src/img/.svn/entries
./src/Makefile
./src/vimbook.tex
```
Pode-se em seguida chamar o vim usando substituição de comandos, como o
comando `!!` corresponde ao último comando, e neste caso a saida
corresponde a uma lista de arquivos que contém o padrão a ser editado
faz-se:
```
vim ${!!}
```
