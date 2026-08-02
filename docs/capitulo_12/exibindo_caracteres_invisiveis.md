---
title: Exibindo caracteres invisíveis
---

```
:set list
```

Com essa opção habilitada, geralmente usamos `^I` para representar uma
tabulação `<Tab>`, e `$` para indicar o fim de linha. Mas é possível
customizar essas opções através de *listchars*, cuja sintaxe é:

```
set listchars=key:string,key:string
```

As chaves disponíveis são:

| Chave | Descrição |
|-------|-----------|
| `eol:{char}` | define o caracter a ser posto depois do fim da linha |
| `tab:{char1}{char2}` | o tab é mostrado pelo primeiro caracter `{char1}` e seguido por `{char2}` |
| `trail:{char}` | representa os espaços em branco no fim da linha |
| `extends:{char}` | é mostrado na última coluna quando a linha continua além da borda direita da tela; funciona com a opção *nowrap* habilitada |
| `precedes:{char}` | é mostrado na primeira coluna quando há conteúdo antes do início visível da linha; funciona com a opção *nowrap* habilitada |

Alguns exemplos de uso, para colocar no *vimrc* descomentando a linha
desejada:

```
"exemplo 1:
"set listchars=tab:>-,trail:.,eol:#,extends:@

"exemplo 2:
"set listchars=tab:>-

"exemplo 3:
set nowrap    "Essa opção desabilita a quebra de linha
"set listchars=extends:+,precedes:<
```
