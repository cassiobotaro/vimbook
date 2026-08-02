---
title: Alternando entre buffers de arquivo
---

Ao abrir um documento qualquer no Vim o mesmo fica em um buffer. Caso
seja decidido que outro arquivo seja aberto na mesma janela, o documento
inicial irá desaparecer da janela atual cedendo lugar ao mais novo, mas
permanecerá ativo no buffer para futuras modificações.

Para saber quantos documentos estão abertos no momento utiliza-se o
comando *:ls* ou *:buffers*. Esses comandos
listam todos os arquivos que estão referenciados no buffer com suas
respectivas “chaves” de referencia.

Para trocar a visualização do Buffer atual pode-se usar:

| Comando | Descrição |
|---------|-----------|
| `:buffer #` | Altera para o buffer alternativo (o editado anteriormente) |
| `:b2` | Altera para o buffer cuja chave é 2 |

Para os que preferem atalhos para alternar entre os buffers, é possível
utilizar ‘Ctrl-6’ que tem o mesmo funcionamento do comando `:b#`
