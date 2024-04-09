Evitando arquivos de backup no disco 
------------------------------------

Nota-se em algumas situações que existem alguns arquivos com o mesmo
nome dos arquivos que foram editados, porém com um til (\~) no final.
Esses arquivos são **backups** que o Vim gera antes de
sobrescrever os arquivos, e podem desde ocupar espaço significativo no
disco rígido até representar falha de segurança, como por exemplo
arquivos *.php\~* que não são interpretados pelo servidor web
e expõem o código-fonte.

Para que os **backups** sejam feitos enquanto os arquivos
estejam sendo escritos, porém não mantidos após terminar a escrita,
utiliza-se no `.vimrc`:
```
set nobackup
set writebackup
```
Fonte: [Site do Eustáquio
Rangel](http://eustaquiorangel.com/posts/520).

