Log do Subversion
-----------------

A variável de ambiente *\$SVN\_EDITOR* pode ser usada para
se especificar o caminho para o editor de texto de sua preferência, a
fim de usá-lo na hora de dar um *commit* usando o
*subversion*.
```bash
export SVN_EDITOR=/usr/bin/vim
svn commit
```
Será aberto uma sessão no Vim, que depois de salva, será usada para LOG
do commit.
