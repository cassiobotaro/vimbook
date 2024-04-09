Edite vários arquivos de uma só vez
-----------------------------------

O Vim pode abrir vários arquivos que contenham um determinado padrão. Um
exemplo seria abrir dezenas de arquivos HTML e trocar a ocorrência
`bgcolor="ffffff"` Para `bgcolor="eeeeee"` Usaríamos a seguinte
sequência de comandos:
```
vim *.html  .................................... abre os arquivos
:bufdo :%s/bgcolor=`ffffff'/bgcolor=`eeeeee'/g   substituição
:wall       .................................... salva todos
:qa[ll]     .................................... fecha todos
```

Ainda com relação à edição de vários arquivos poderíamos abrir alguns
arquivos txt e mudar de um para o outro assim:

```
:wn
```

O ‘w’ significa gravar e o ‘n’ significa
*next*, ou seja, gravaríamos o que foi modificado no
arquivo atual e mudaríamos para o próximo.

Veja também [Movendo-se no documento](../capitulo_3/movendo-se_no_documento.md).
