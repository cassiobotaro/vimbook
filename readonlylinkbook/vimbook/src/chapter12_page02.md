Ajustando parágrafos em modo normal
-----------------------------------

O comando `gqap` ajusta o parágrafo atual em modo normal. Usando a
opção *:set nojoinspaces* o vim colocará dois espaços após
o ponto final ao se ajustar os parágrafos.

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
 Esse caracter representa os espaços em branco.

 - extends:{char}
 Esse caracter representa o início do fim da linha
 sem quebrá-la
 Está opção funciona com a opção nowrap habilitada

"exemplo 1:
"set listchars=tab:>-,trail:.,eol:#,extends:@

"exemplo 2:
"set listchars=tab:>-

"exemplo 3:
"set listchars=tab:>-

"exemplo 4:
set nowrap    "Essa opção desabilita a quebra de linha
"set listchars=extends:+
```
