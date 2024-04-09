Instalação do Vim
-----------------

### Instalação no Windows

Há uma versão gráfica do Vim disponível para vários sistemas
operacionais, incluindo o Windows; esta versão pode ser encontrada no
[site oficial](http://www.vim.org/download.php).
Para instalá-lo basta baixar o instalador no link indicado e dispará-lo
com um duplo clique (este procedimento requer privilégios de
administrador).

### Instalação no GNU/Linux

A maioria das distribuições GNU/Linux traz o Vim em seus repositórios,
sendo que é bastante comum o Vim já vir incluído na instalação típica da
distribuição. A forma de instalação preferível depende da distribuição:

-   Já vir instalado por *default* – neste caso nada
    precisa ser feito.

-   Estar disponível no repositório, mas não instalado – em
    distribuições derivadas da Debian GNU/Linux[^1], a instalação do Vim
    através dos repositórios é usualmente executada digitando-se
    `apt-get install vim`[^2] em um *terminal*
    (este procedimento requer privilégios de administrador e,
    tipicamente, conexão com a internet).

    Algumas distribuições GNU/Linux dividem o programa Vim em vários
    pacotes. Pacotes adicionais como `gvim`, `vim-enhanced`,
    `vim-python`[^3], entre outros, representam diferentes versões do
    mesmo aplicativo. O `gvim` é a versão gráfica do Vim e o
    `vim-enhanced` é uma versão do vim compilada com um suporte interno
    ao Python[^4]. A alternativa para resolver esse problema é buscar na
    documentação da distribuição o que significa cada pacote.

-   Não estar disponível no repositório da distribuição – cenário
    *muito* improvável, mas nas sua ocorrência o Vim pode
    ser instalado através da compilação do código-fonte; basta seguir as
    instruções do [site oficial](http://www.vim.org/download.php).

    [^1]: Debian GNU/Linux - <http://www.debian.org/index.pt.html>

    [^2]: Recomenda-se também instalar a documentação em HTML do Vim: `apt-get install vim-doc`

    [^3]: Para ubuntu e Debian

    [^4]: O Python (<http://www.python.org>) é uma linguagem de programação orientada a objetos muito comum no meio profissional e acadêmico


