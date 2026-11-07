---
title: Registradores somente leitura ":.%#"
---

Registradores somente leitura ": . % \#"
------------------------------------

| Comando | Descrição |
|---------|-----------|
| `":` | armazena o último comando |
| `".` | armazena uma cópia do último texto inserido |
| `"%` | contém o nome do arquivo corrente |
| `"#` | contém o nome do arquivo alternativo |

Uma forma prática de usar registradores em modo de inserção é usando:
`Ctrl-R`

| Comando | Descrição |
|---------|-----------|
| `Ctrl-R %` | insere o nome do arquivo atual |
| `Ctrl-R :` | insere o último comando digitado |
| `Ctrl-R /` | insere a última busca efetuada |
| `Ctrl-R a` | insere o registrador `a' |

Em modo de inserção pode-se repetir a última inserção de texto
simplesmente pressionando `Ctrl-A`.
