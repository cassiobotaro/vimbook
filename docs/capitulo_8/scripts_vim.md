*Scripts* Vim
--------------------------

Usando um *script* para modificar um nome em vários
arquivos: Crie um arquivo chamado subst.vim contendo os
comandos de substituição e o comando de salvamento :wq.
```
%s/bgcolor="eeeeee"/bgcolor="ffffff"/g
wq
```
Para executar um *script*, digite o comando
```
:source nome_do_script.vim
```
O comando :source também pode ser abreviado com
:so bem como ser usado para testar um esquema de cor:
```
:so tema.vim
```
