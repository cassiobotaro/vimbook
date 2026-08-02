---
title: Comparando arquivos com o vimdiff
---

O vim possui um modo para checagem de diferenças entre arquivos, é
bastante útil especialmente para programadores, para saber quais são as
diferenças entre dois arquivos faz-se:

| Comando | Descrição |
|---------|-----------|
| `vimdiff arquivo1.txt arquivo2.txt` | exibe as diferenças |
| `]c` | mostra a próxima diferença |
| `[c` | mostra a diferença anterior |
| `vim -d arquivo1.txt arquivo2.txt` | outro modo de abrir o vimdiff |

Para usuários do GNU/Linux é possível ainda checar diferenças
remotamente assim:
```
vimdiff projeto scp://usuario@estacao//caminho/projeto
```
O comando acima irá exibir lado a lado o arquivo local chamado
`projeto` e o arquivo remoto contido no computador de nome
`estacao` de mesmo nome.

