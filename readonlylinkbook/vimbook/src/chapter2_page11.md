Escrevendo o texto
------------------

O Vim é um editor que possui diferentes modos de edição. Entre eles está
o modo de inserção, que é o modo onde escreve-se o texto naturalmente.

Para se entrar em modo de inserção, estando em modo normal, pode-se
pressionar qualquer uma das teclas abaixo:
```
i ..... entra no modo de inserção antes do caractere atual
I ..... entra no modo de inserção no começo da linha
a ..... entra no modo de inserção após o caractere atual
A ..... entra no modo de inserção no final da linha
o ..... entra no modo de inserção uma linha abaixo
O ..... entra em modo de inserção uma linha cima
<Esc> . sai do modo de inserção
```
Uma vez no modo de inserção todas as teclas são exatamente como nos
outros editores simples, caracteres que constituem o conteúdo do texto
sendo digitado. O que inclui as teclas de edição de caracteres.

Para salvar o conteúdo escrito, digite a tecla `<Esc>` para sair do modo
de inserção e digite o comando `:w` para gravar o conteúdo. Caso
queira sair do editor, digite o comando: `:q` caso tenha ocorrido
modificações no arquivo desde que ele foi salvo pela última vez haverá
uma mensagem informando que o documento foi modificado e não foi salvo,
nesse caso, digite o comando `:q!` para fechar o Vim **sem salvar**
as últimas modificações feitas. Caso queira salvar e
sair do arquivo, digite o comando `:wq`

Nesse ponto, conhece-se o vim de forma suficiente para editar qualquer
coisa nele. Daqui por diante o que existe são as formas de realizar a
edição do arquivo com maior naturalidade e produtividade.

O usuário iniciante do Vim pode cometer o erro de tentar decorar todos
os comandos que serão apresentados. **Não faça isso**.
Tentar decorar comando é exatamente o caminho contrário da naturalidade
exigida por um editor texto para aumentar a produtividade.

Ao contrário, sugere-se que leia-se todo o conteúdo. Identifique quais
são as atividades de maior recorrência no estilo individual de escrita e
busque como realizar tais funções com mais fluência nesse editor. A
prática levará ao uso fluente desse comandos principais, abrindo
espaço para os demais comandos.

Isso não impede que o usuário experimente cada comando conforme for
lendo. De fato, essa prática pode ajudar a selecionar as formas de
edição que lhe são mais simpáticas ao uso.


