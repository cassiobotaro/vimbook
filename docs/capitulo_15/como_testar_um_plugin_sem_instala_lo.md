---
title: Como testar um plugin sem instalá-lo?
---

```vim
:source <path>/<plugin>
```
Caso o plugin atenda as necessidades, pode-se instalá-lo. Este
procedimento também funciona para temas de cor!


No GNU/Linux
```text
~/.vim/plugin/
```
No Windows
```text
~/vimfiles/plugin/
```
Obs.: Caso ainda não exista o diretório, ele pode ser criado pelo próprio usuário

Exemplo no GNU/Linux
```text
+ /home/usuario/
            |
            |
            + .vim
              |
              |
              + plugin
```
Obs.: Alguns plugins dependem da versão do Vim; para saber qual
a que está atualmente instalada:
```vim
:ve[rsion]
```
