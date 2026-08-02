---
title: Dicas da lista vi-br
---

Fonte: Grupo vi-br do Yahoo, mensagem 853. O Yahoo Grupos foi encerrado em
dezembro de 2020 e as mensagens não foram preservadas; resta apenas uma
[cópia arquivada da página do grupo](https://web.archive.org/web/20010522154801/http://groups.yahoo.com/group/vi-br).

Problema: Essa deve ser uma pergunta comum. Suponha o seguinte conteúdo
de arquivo:
```
... // várias linhas
texto1000texto    // linha i
texto1000texto    // linha i+1
texto1000texto    // linha i+2
texto1000texto    // linha i+3
texto1000texto    // linha i+4
... // várias linhas
```
Gostaria de um comando que mudasse para
```
... // várias linhas
texto1001texto    // linha i
texto1002texto    // linha i+1
texto1003texto    // linha i+2
texto1004texto    // linha i+3
texto1005texto    // linha i+4
... // várias linhas
```
Ou seja, somasse 1 a cada um dos números entre os textos especificando
como range as linhas i,i+4
```
:10,20! awk 'BEGIN{i=1}{if (match($0, /[0-9]+/)) print substr($0,1,RSTART-1) (substr($0,RSTART,RLENGTH) + i++) substr($0,RSTART+RLENGTH)}'
```
Mas muitos sistemas não tem awk, e logo a melhor solução
mesmo é usar o Vim:
```
:let i=1 | 10,20 g/texto\d\+texto/s/\d\+/\=submatch(0)+i/ | let i=i+1
```
Observação: 10,20 é o intervalo, ou seja, da linha 10 até a linha 20
```
:help /
:help :s
:help pattern
```
O plugin
[Visincr](https://www.vim.org/scripts/script.php?script_id=670) 
Possibilita incrementos em modo visual de diversas formas, um vídeo
demonstrativos pode ser visto [neste link](https://vimeo.com/4457161).
