Registradores nomeados de 0 a 9
---------------------------

O registrador zero armazena o conteúdo da última cópia `yy`, à
partir do registrador 1 vão sendo armazenadas as deleções sucessivas de
modo que a mais recente deleção será armazenada no registrador 1 e os
registradores vão sendo incrementados em direção ao nono. Deleção menores
que uma linha não são armazenadas nestes registradores, caso em que o Vim
usa o registrador de pequenas deleções ou que se tenha especificado algum
outro registrador.
