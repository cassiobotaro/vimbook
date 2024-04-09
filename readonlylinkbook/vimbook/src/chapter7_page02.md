Alternando entre Buffers de arquivo
===================================

Ao abrir um documento qualquer no Vim o mesmo fica em um buffer. Caso
seja decidido que outro arquivo seja aberto na mesma janela, o documento
inicial irá desaparecer da janela atual cedendo lugar ao mais novo, mas
permanecerá ativo no buffer para futuras modificações.

Para saber quantos documentos estão abertos no momento utiliza-se o
comando *:ls* ou *:buffers*. Esses comandos
listam todos os arquivos que estão referenciados no buffer com suas
respectivas “chaves” de referencia.

Para trocar a visualização do Buffer atual pode-se usar:
```
:buffer# ...... Altera para o buffer anterior
:b2 ........... Altera para o buffer cujo a chave é 2
```
Para os que preferem atalhos para alternar entre os buffers, é possível
utilizar ‘Ctrl-6’ que tem o mesmo funcionamento do comando `:b#`
