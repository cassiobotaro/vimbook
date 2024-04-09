Efetivação das alterações no `vimrc` 
------------------------------------

As alterações no *vimrc* só serão efetivadas na próxima vez
que o Vim for aberto, a não ser que o recarregamento do arquivo de
configuração seja instruído explicitamente:
```
:source ~/vimrc ....... se estiver no GNU/Linux
:source ~/_vimrc ...... caso use o Windows
:so arquivo ........... `so' é uma abreviação de `source'
```
