---
title: Complementação com "tab"
---

```
"Word completion
"Complementação de palavras

set dictionary+=/usr/dict/words
set complete=.,w,k

"------ complementação de palavras ----
"usa o tab em modo de inserção para completar palavras

function! InsertTabWrapper(direction)
   let col = col('.') - 1
   if !col || getline('.')[col - 1] !~ '\k'
      return "\<tab>"
   elseif "backward" == a:direction
      return "\<c-p>"
   else
      return "\<c-n>"
   endif
endfunction

inoremap <tab> <c-r>=InsertTabWrapper ("forward")<cr>
inoremap <s-tab> <c-r>=InsertTabWrapper ("backward")<cr>
```
