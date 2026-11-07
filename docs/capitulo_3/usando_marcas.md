As marcas são um meio eficiente de se pular para um local no arquivo.
Para criar uma, estando em modo normal faz-se:

```text
ma
```

Onde ‘m’ indica a criação de uma marca e ‘a’ é
o nome da marca. Para pular para a marca ‘a’:

```text
`a
```

Para voltar ao ponto do último salto:

```text
''
```

Para deletar da linha atual até a marca ‘a’ (em modo normal):

```text
d'a
```

### Marcas Globais

Durante a edição de vários arquivos pode-se definir uma marca global com
o comando:

```text
mA
```

Onde ‘m’ cria a marca e ‘A’ (maiúsculo) define
uma marca ‘A’ acessível a qualquer momento com o comando:

```text
'A
```

Isto fará o Vim dar um salto até a marca ‘A’ mesmo que
esteja em outro arquivo, mesmo que você tenha acabado de fechá-lo. Para
abrir e editar vários arquivos do Vim fazemos:

| Comando | Descrição |
|---------|-----------|
| `vim *.txt` | abre todos os arquivos 'txt' |
| `:bn` | vai para o próximo da lista |
| `:bp` | volta para o arquivo anterior |
| `:ls` | lista todos os arquivos abertos |
| `:wn` | salva e vai para o próximo |
| `:wp` | salva e vai para o anterior |
