Viminfo
---------

Se o Vim for fechado e iniciado novamente, normalmente perderá uma
porção considerável de informações. A diretiva viminfo pode
ser usada para memorizar estas informações.

-   Histórico da linha de comando

-   Histórico de buscas

-   Histórico de entradas *input-line history*

-   Conteúdo de registradores não vazios

-   Marcas de vários arquivos

-   Último padrão de busca/substituição

-   A lista de *buffers*

-   Variáveis globais

Deve-se colocar no arquivo de configuração algo como:

    set viminfo=%,'50,\"100,/100,:100,n

Algumas opões da diretiva viminfo:

!

:   Quando incluído salva e restaura variáveis globais (variáveis com
    letra maiúscula) e que não contém letras em minúsculo como
    MANTENHAISTO.

"

:   Número máximo de linhas salvas para cada registrador.

%

:   Quando incluído salva e restaura a lista de *buffers*.
    Caso o Vim seja iniciado com um nome como argumento, a lista de
    *buffers* não é restaurada. *Buffers* sem
    nome e *buffers* de ajuda não são armazenados no
    viminfo.

’

:   Número máximo de arquivos recém editados.

/

:   Máximo de itens do histórico de buscas.

:

:   Máximo de itens do histórico da linha de comando

\<

:   Número máximo de linhas salvas por cada registrador, se zero os
    registradores não serão salvos. Quando não incluído, todas as linhas são
    salvas.

Para ver mais opções sobre o arquivo ‘viminfo’ leia
‘:h viminfo’. Pode-se também usar um arquivo de “Sessão”. A
diferença é que ‘viminfo’ não depende do local de trabalho
(escopo). Quando o arquivo ‘viminfo’ existe e não está
vazio, as informações novas são combinadas com as existentes. A opção
‘viminfo’ é uma string contendo informações sobre o que
deve ser armazenado, e contém limites de o quanto vai ser armazenado
para cada item.
