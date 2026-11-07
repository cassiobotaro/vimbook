---
title: Substituindo tabulações por espaços
---

Se houver necessidade[^1] de trocar tabulações por espaços fazemos
assim:
```vim
:set tabstop=4 "tamanho da parada de tabulação
:set expandtab
:retab
```
Para fazer o contrário, digite `:%s/\s\{4,}/`, pressione `Ctrl-I` para
inserir uma tabulação e complete com `/g`.
Explicando:

| Comando | Descrição |
|---------|-----------|
| `:` | comando |
| `%` | em todo arquivo |
| `s` | substitua |
| `/` | padrão de busca |
| `\s` | localiza espaço |
| `\{4,}` | quatro ou mais vezes |
| `/` | início da substituição |
| `Ctrl-I` | insere uma tabulação (`<Tab>`) |
| `/` | fim da substituição |
| `g` | global |

[^1]: Em códigos Python por exemplo não se pode misturar espaços e tabulações
