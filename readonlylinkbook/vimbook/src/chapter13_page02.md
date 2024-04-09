Problemas com codificação de caracteres
---------------------------------------

Atualmente uso o Ubuntu em casa e ele já usa utf-8. Ao restaurar meu
“backup” do Wiki no Kurumin os caracteres ficaram meio estranhos, daí
fiz:
```
# baixei o pacote [recode]
apt-get install recode
```
para recodificar caracteres de `utf-8` para `iso` faça:
```
recode -d u8..l1 arquivo
```
