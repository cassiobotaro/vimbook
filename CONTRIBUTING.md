Transcrição de capítulos
========================

* Clone o repositório

`git clone https://github.com/cassiobotaro/vimbook.git`

* Crie seu feature-branch

`git checkout -b capitulo-x`

* Atribua a issue correspondente ao capítulo escolhido a seu usuário.

[Issues](https://github.com/cassiobotaro/vimbook/issues)

* Crie um diretório para o capítulo na raiz do projeto no formato `capitulo_n` (exemplo `capitulo_15`).

* Adicione o capítulo ao sumário.

[SUMMARY](SUMMARY.md)

* Envie PR do capítulo.

Os [capítulos](https://github.com/cassiobotaro/vimbook/tree/master/chapters) originais se encontram em formato markdown, com alguns problemas de formatação pois foram diretamente gerados à partir do .tex.

*Por favor remova as tags span encontradas.*

Para auxiliar a transcrição, a última versão pdf gerada à partir do .tex está disponível para [download](https://github.com/cassiobotaro/vimbook/blob/master/vimbook-livro-original/vimbook-31-08-2009.pdf).

Padrões de formatação
=====================

Highlights
----------
Sempre que usar a syntax de _highlight_ (``) em uma parte do texto, evite o uso de _aspas_ desnecessárias, ex:
```diff
- "`texto`".
+ `texto`
```

Notas de rodapé
---------------
As notas de rodapé devem ser preenchidas por página, ou seja, sempre que houver uma nota de rodapé, essa deverá estar na mesma página onde
sua referência foi feita.

A numeração das notas de rodapé são por página e não por capitulo.

Links
-----
Links internos do livro devem ser descritos com o título do capitulo e não o número do capítulo ou número da página, ex:
```diff
- veja o capítulo [3](capitulo_3/movendo-se_no_documento.md)
+ veja o capítulo [Movendo-se no documento](capitulo_3/movendo-se_no_documento.md)
```
Além disso devem ser relativos:
```diff
- veja o capítulo [Movendo-se no documento](capitulo_3/movendo-se_no_documento.md)
+ veja o capítulo [Movendo-se no documento](../capitulo_3/movendo-se_no_documento.md)
```
Para testar se o link está correto, utilize os comandos `<c-w>f` ou `gf` do Vim.

Representação de Setas
----------------------
No caso de comandos/atalhos que utilizem as setas do teclado, a representação deverá ser baseada nas setas UTF-8:
```
⬆⬇⬅➡
```
Por exemplo **Ctrl-⬆**, **Alt-➡**, etc.

Blocos de highlight
-------------------
Utilizar blocos com highlight para destaque da sintaxe.
```diff
-         for i in range(10)
+ ```python
+ for i in range(10)
+ ```

```

Outros
======

É muito bem vindo correções de ortografia, erros de digitação e outras coisas.

Quando aceito o PR, uma nova versão do livro é gerada automaticamente.


Dicas
-----

* Substituir padrão *LaTex* de itálico (`{\em Texto}`) pelo padrão markdown (`*Texto*`)
```vim
:%s/{\\em \([^}]*\)}/*\1*/g
```
* Substituir o padrão *LaTex* de título (`\section{Título}`) pelo título normal (`Título`)
```vim
:%s/\\section{\([^}]*\)}/\1/g
```
* Substituir o padrão *LaTeX* de subtítulo (`\subsection{SubTítulo}`) pelo padrão markdown (`### SubTítulo`)
```vim
:%s/\\subsection{\([^}]*\)}/### \1/g
```
* Substituir o padrão *LaTeX* de link (`\href{link}{texto}`) pelo padrão markdown (`[texto](link)`)
```vim
:%s/\\href{\([^}]*\)}{\([^}]*\)}/[\2](\1)/g
```
* Substituir o padrão *LaText* de fonte diferenciada (`{\tt texto}`) pelo padrão markdown de highlighting (``texto``)
```vim
:%s/{\\tt \([^}]*\)}/`\1`/g
```
