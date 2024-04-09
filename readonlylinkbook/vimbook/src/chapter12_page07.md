Complementação com “tab” 
------------------------
```
"Word completion
"Complementação de palavras

set dictionary+=/usr/dict/words
set complete=.,w,k

"------ complementação de palavras ----
"usa o tab em modo de inserção para completar palavras

function! InsertTabWrapper(direction)
   let col = col(``.'') - 1
   if !col || getline(``.'')[col - 1] !~ '\k'
      return ``>''
   elseif ``d'' == a:direction
      return ``>''
   else
      return ``>''
   endif
endfunction

inoremap <tab> <c-r>=InsertTabWrapper (``d'')<cr>
inoremap <s-tab> <c-r>=InsertTabWrapper (``d'')<cr>
```
