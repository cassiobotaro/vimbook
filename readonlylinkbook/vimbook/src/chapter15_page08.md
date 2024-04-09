O Plugin *Project*
------------------

O plugin project acessível através deste
[link](http://www.vim.org/scripts/script.php?script_id=69)
cria toda uma estrutura de gerenciamento de projetos.
Para programadores é uma funcionalidade extremamente necessária.
Costuma-se trabalhar com vários arquivos da mesma família ("extensão"),
e ao clicar em um dos arquivos do projeto o mesmo é aberto instantaneamente.

```
:Project ......... abre uma janela lateral para o projeto
\C ............... inicia a criação de um projeto (recursivamente)
\c ............... inicia a criação de um projeto na pasta local
```

Após digitar o atalho de criação do projeto aparecerá uma janela
para designar um nome para o mesmo, em seguida digita-se o caminho para
o diretório do projeto, após isto digita-se `.` (ponto) como parâmetro,
cria-se um filtro como `*.py`.
Para criar uma entrada (acesso ao plugin) no menu do Gvim colocamos
a seguinte linha no `vimrc`.

```
amenu &Projetos.togle <Plug>ToggleProject<cr>
```

Pode-se definir um projeto manualmente assim:

```
nome=~/docs/ CD=. filter="*.txt" {

}
```

Ao recarregar o Vim pode-se abrir o *Plugin* `:Projetc` e
pressionar o atalho `\r` para que o mesmo gere um índice dos arquivos
contidos no caminho indicado.
