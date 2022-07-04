Salvando Sessões de Trabalho
============================

Suponha a situação em que um usuário está trabalhando em um projeto no
qual vários arquivos são editados simultaneamente; quatro arquivos estão
abertos, algumas macros foram criadas e variáveis que não constam no
`vimrc` foram definidas. Em uma situação normal, se o Vim for fechado a
quase totalidade dessas informações se perde[^1]; para evitar isto uma
sessão pode ser criada, gerando-se um “retrato do estado atual”, e então
restaurada futuramente pelo usuário—na prática é como se o usuário não
tivesse saído do editor.

Uma sessão do Vim guarda, portanto, uma série de informações sobre a
edição corrente, de modo a permitir que o usuário possa restaurá-la
quando desejar. Sessões são bastante úteis, por exemplo, para se
alternar entre diferentes projetos, carregando-se rapidamente os
arquivos e definições relativas a cada projeto.

[^1]: Algumas informações, no entanto, são automaticamente armazenadas no arquivo viminfo; veja :h viminfo
