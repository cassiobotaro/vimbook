---
title: Ajustando parágrafos em modo normal
---

O comando `gqap` ajusta o parágrafo atual em modo normal. Usando a
opção *:set joinspaces* o vim colocará dois espaços após
o ponto final ao se ajustar os parágrafos; com *:set nojoinspaces*,
que é o padrão, ele coloca apenas um.

geralmente usamos `^I` para representar uma tabulação `<Tab>`, e `$`
para indicar o fim de linha. Mas é possível customizar essas opções.
sintaxe:
```

set listchars=key:string,key:string

 - eol:{char}
 Define o caracter a ser posto depois do fim da linha

 - tab:{char1}{char2}
 O tab é mostrado pelo primeiro caracter {char1} e
 seguido por {char2}

 - trail:{char}
 Esse caracter representa os espaços em branco no
 fim da linha

 - extends:{char}
 Esse caracter é mostrado na última coluna quando a
 linha continua além da borda direita da tela
 Esta opção funciona com a opção nowrap habilitada

 - precedes:{char}
 Esse caracter é mostrado na primeira coluna quando
 há conteúdo antes do início visível da linha
 Esta opção funciona com a opção nowrap habilitada

"exemplo 1:
"set listchars=tab:>-,trail:.,eol:#,extends:@

"exemplo 2:
"set listchars=tab:>-

"exemplo 3:
set nowrap    "Essa opção desabilita a quebra de linha
"set listchars=extends:+,precedes:<
```
