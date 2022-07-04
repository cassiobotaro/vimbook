Junção de linhas com Vim
------------------------

Fonte: [dicas-l da unicamp](http://www.dicas-l.com.br/dicas-l/20081228.php)
Colaboração: Rubens Queiroz de Almeida

Recentemente precisei combinar, em um arquivo, duas linhas consecutivas.
O arquivo original continha linhas como:
```
Matrícula: 123456
Senha: yatVind7kned
Matrícula: 123456
Senha: invanBabnit3
```
E assim por diante. Eu precisava converter este arquivo para algo como:
```
Matrícula: 123456 - Senha: yatVind7kned
Matrícula: 123456 - Senha: invanBabnit3
```
Para isto, basta executar o comando:
```
:g/^Matrícula/s/\n/ - /
```
Explicando:
```
s/isto/aquilo/g .. substitui isto por aquilo
g ................ comando global
/................. inicia padrão de busca
^ ................ indica começo de linha
Matrícula ........ palavra a ser buscada
s ................ inicia substituição
/\n/ - / ......... troca quebra de linha `\n`, por `-`
```
