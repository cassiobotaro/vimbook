Comandos relativos à verificação ortográfica
--------------------------------------------

### Encontrando palavras desconhecidas

Muito embora o verificador ortográfico cheque imediatamente cada palavra
digitada, sinalizando-a ao usuário caso não a reconheça, às vezes é mais
apropriado realizar a verificação ortográfica do documento por inteiro.
O Vim dispõe de comandos específicos para busca e movimentação em
palavras grafadas incorretamente (desconhecidas) no escopo do documento,
dentre eles:
```
]s ..... vai para a próxima palavra desconhecida
[s ..... como o ]s, mas procura no sentido oposto
```
Ambos os comandos aceitam um prefixo numérico, que indica a quantidade
de movimentações (buscas). Por exemplo, o comando 3]s vai
para a *terceira* palavra desconhecida a partir da posição
atual.

### Tratamento de palavras desconhecidas

Há basicamente duas operações possíveis no tratamento de uma palavra
apontada pelo verificador ortográfico do Vim como desconhecida:

1.  **corrigi-la** – identificando o erro com ou sem o
    auxílio das sugestões do Vim.

2.  **cadastrá-la no dicionário** – ensinando o Vim a
    reconhecer sua grafia.

Assume-se nos comandos descritos nas seções a seguir que o cursor do
editor encontra-se sobre a palavra marcada como desconhecida.

#### Correção de palavras grafadas incorretamente

É possível que na maioria das vezes o usuário perceba qual foi o erro
cometido na grafia, de forma que o próprio possa corrigi-la sem auxílio
externo. No entanto, algumas vezes o erro não é evidente, e sugestões
fornecidas pelo Vim podem ser bastante convenientes. Para listar as
sugestões para a palavra em questão executa-se:
```
z= ..... solicita sugestões ao verificador ortográfico
```
Se alguma das sugestões é válida – as mais prováveis estão nas primeiras
posições – então basta digitar seu prefixo numérico e pressionar
`<Enter>`. Se nenhuma sugestão for adequada, basta simplesmente
pressionar `<Enter>` e ignorar a correção.

#### Cadastramento de novas palavras no dicionário

Por mais completo que um dicionário seja, eventualmente palavras,
especialmente as de menor abrangência, terão que ser cadastradas a fim
de aprimorar a exatidão da verificação ortográfica. A manutenção do
dicionário dá-se pelo cadastramento e retirada de palavras:
```
zg ..... adiciona a palavra no dicionário
zw ..... retira a palavra no dicionário, marcando-a como
         `desconhecida'
```
