Editando comandos longos no Linux
---------------------------------

É comum no ambiente GNU/Linux a necessidade de digitar comandos longos
no terminal, para facilitar esta tarefa pode-se seguir estes passos:

1.  Definir o Vim como editor padrão do sistema editando o arquivo
    `.bashrc`[^1]:
    ```bash
    #configura o vim como editor padrão
    export EDITOR=vim
    export VISUAL=vim
    ```

2.  No terminal usar a combinação de teclas `Ctrl-x-e`.
    Esta combinação de teclas abre o editor padrão do sistema onde se
    deve digitar o comando longo, ao sair do editor o terminal executa o
    comando editado.

[^1]: Arquivo de configuração do bash
