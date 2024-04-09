Mantendo apenas um Gvim aberto
------------------------------

Essa dica destina-se apenas à versão do Vim que roda no ambiente
gráfico, ou seja, o Gvim, pois ela faz uso de alguns recursos que só
funcionam nesse ambiente. A meta é criar um comando que vai abrir os
arquivos indicados em abas novas sempre na janela já existente.

Para isso deve-se definir um **script** que esteja no seu
**path**[^1] do sistema (e que possa ser executado de alguma
forma por programas do tipo **launcher** no modo gráfico) que
vai ser utilizado sempre que quisermos abrir nossos arquivos dessa
maneira. Para efeito do exemplo, o nome do arquivo será
*tvim* (de **tabbed vim**), porém pode ser nomeado
com o nome que for conveniente.

A única necessidade para essa dica funcionar é a versão do Vim ter
suporte para o argumento *–serverlist*, o que deve ser
garantido nas versões presentes na época em que esse documento foi
escrito. Para fazer uma simples verificação se o comando está
disponível, deve ser digitado em um terminal:
```
vim --serverlist
gvim --serverlist
```
Se ambos os comandos acima resultaram em erro, o procedimento não poderá
ser implementado. Do contrário, deve-se utilizar o comando que teve um
retorno válido (*vim* ou *gvim*) para criar o
**script**. Supondo que foi o comando *gvim* que
não retornou um erro, criamos o **script** da seguinte forma:
```
#!/bin/bash
if [ $# -ne 1 ]
then
   echo "Sem arquivos para editar."
   exit
fi
gvim --servername $(gvim --serverlist | head -1) --remote-tab $1
```
Desse modo, se for digitado *tvim* sem qualquer argumento, é
exibida a mensagem de erro, do contrário, o arquivo é aberto na cópia
corrente do Gvim, em uma nova aba, por exemplo:
```
tvim .vimrc
```
Fonte: [Site do Eustáquio Rangel](http://eustaquiorangel.com/posts/477) 

[^1]: Diretórios nos quais o sistema busca pelos comandos
