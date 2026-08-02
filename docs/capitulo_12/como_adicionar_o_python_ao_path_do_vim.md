---
title: Como adicionar o Python ao path do Vim?
---

Coloque o seguinte
[script](http://vim.wikia.com/wiki/Automatically_add_Python_paths_to_Vim_path)
em:

-   `~/.vim/after/ftplugin/python.vim` (em sistemas Unix)
-   `$HOME/vimfiles/after/ftplugin/python.vim` (no Windows)

```VimL
python3 << EOF
import os
import sys
import vim
for p in sys.path:
    # Add each directory in sys.path, if it exists.
    if os.path.isdir(p):
        # Command 'set' needs backslash before each space.
        vim.command(r"set path+=%s" % (p.replace(" ", r"\ ")))
EOF
```
Isto lhe permite usar *gf* ou *Ctrl-w Ctrl-F*
para abrir um arquivo sob o cursor
