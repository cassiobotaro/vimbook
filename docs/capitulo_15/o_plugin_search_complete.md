---
title: O Plugin SearchComplete
---

Para que o vim complete opções de busca com a tecla `<tab>`, digita-se uma
palavra parcialmente e o plugin atua, exibindo palavras que tem
o mesmo início, por exemplo:

```
/merca<tab>
/mercado
/mercantil
/mercadológico
```

Cada vez que se pressiona a tecla `<tab>` o cursor saltará para
a próxima ocorrência daquele fragmento de palavra.
Pode-se obter o plugin *SearchComplete* no seguinte
[link](https://www.vim.org/scripts/script.php?script_id=474),
e para instalá-lo basta copiá-lo para a pasta apropriada:

| Comando | Descrição |
|---------|-----------|
| `~/vimfiles/plugin` | no windows |
| `~/.vim/plugin` | no Gnu/Linux |

Há outro plugin similar chamado `CmdlineComplete` disponível
[neste link](https://www.vim.org/scripts/script.php?script_id=2222).
