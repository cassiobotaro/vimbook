Salvamento automático para o Wiki 
----------------------------------

Procure por uma seção *autowrite* no manual do Potwiki
```
:help potwiki
```
O valor que está em zero deverá ficar em 1
```
call s:default(`autowrite',0)
```
Como eu mantenho o meu Wiki oculto “.wiki” criei um “link” para a pasta
de textos
```
ln -s ~/.wiki /home/sergio/docs/textos/wiki
```
Vez por outra entro na pasta `~/docs/textos/wiki` e crio um pacote
tar.gz e mando para “web” como forma de manter um “backup”.
