Como adicionar o Python ao **path** do Vim?
-------------------------------------------

Coloque o seguinte
[script](http://vim.wikia.com/wiki/Automatically_add_Python_paths_to_Vim_path)
em:
```
 * ~/.vim/after/ftplugin/python.vim    (on Unix systems)
 %* $HOME/vimfiles/after/ftplugin/python.vim    (on Windows systems)

 python << EOF
 import os
 import sys
 import vim
 for p in sys.path:
     # Add each directory in sys.path, if it exists.
     if os.path.isdir(p):
         # Command `set' needs backslash before each space.
         vim.command(r``s'' % (p.replace(`` '', r`` '')))
 EOF
```
Isto lhe permite usar *gf* ou *Ctrl-w Ctrl-F*
para abrir um arquivo sob o cursor
