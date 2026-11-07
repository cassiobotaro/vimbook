---
title: O Plugin SearchComplete
---

Para que o Vim complete opções de busca com a tecla `<tab>`, digita-se uma
palavra parcialmente e o plugin atua, exibindo palavras que têm
o mesmo início, por exemplo:

```text
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
| `~/vimfiles/plugin` | no Windows |
| `~/.vim/plugin` | no GNU/Linux |

Há outro plugin similar chamado `CmdlineComplete` disponível
[neste link](https://www.vim.org/scripts/script.php?script_id=2222).
