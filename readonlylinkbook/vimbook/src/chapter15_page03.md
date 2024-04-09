O plugin EasyGrep
-----------------

Usuários de sistemas *Unix Like*[^1], já conhecem o poder do comando `grep`,
usando este comando procuramos palavras dentro de arquivos.
Este plugin simplifica esta tarefa, além de permitir a utilização da
versão do `grep` nativa do Vim `vimgrep`, assim usuários do Windows
também podem usar este recurso. Um comando `grep` funciona mais ou menos assim:

```
grep [opções] "padrão" /caminho
```

Mas no caso do plugin *EasyGrep* fica assim:

```
:Grep foo  ........ procura pela palavra 'foo'
:GrepOptions ...... exibe as opções de uso do plugin
```

O plugin pode ser obtido no seguinte
[link](http://www.vim.org/scripts/script.php?script_id=2438#0.9).
Já sua instalação é simples, basta copiar o arquivo obtido no link acima
para a pasta:

```
~/.vim/plugin .......... no caso do linux
~/vimfiles/plugin ...... no caso do windows
```

Um vídeo de exemplo (na verdade uma animação gif) pode ser visto
[aqui](http://downloads.veryspeedy.net/vim/EasyGrep.gif).


[^1]: Sistemas da família Unix tipo o GNU/Linux
