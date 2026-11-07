Definindo uma macro de nome `s` para ordenar e retirar linhas duplicadas
```vim
let @s=":sort u"
```
Para executar o registro `s` definido acima faça:
```text
@s
```
O Vim colocará no comando
```vim
:sort u
```
Bastando pressionar `<Enter>`. Observação: Este registro prévio pode
ficar no `vimrc` ou ser digitado em comando “:”
```vim
:5,20sort u
"da linha 5 até a linha 20 ordene e retire duplicados

:sort n
" ordene meu documento considerando números
" isto é útil pois se a primeira coluna contiver
" números a ordenação pode ficar errada caso não usemos
" o parâmetro ``n''
```
