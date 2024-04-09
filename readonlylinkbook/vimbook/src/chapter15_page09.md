O plugin pydiction
------------------

Plugin que completa códigos python assim:

```
import sys
sys.<tab>
```

O plugin contém dois arquivos:

- 1. `pydiction.py` deve ser colocado no `path`
- 2. `pydiction` deve ser colocado em um lugar de sua preferência

Deve-se adicionar algumas linhas do `.vimrc`.
No exemplo abaixo o dicionário é adicionado ao diretório `~/.vim/dict`

```VimL
if has("autocmd")
    autocmd FileType python set complete+=k/.vim/dict/pydiction isk+=.,(
endif " has("autocmd")
```

Pode-se obter o plugin  [neste link](http://www.vim.org/scripts/script.php?script_id=850).
