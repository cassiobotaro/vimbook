# Como contribuir

Primeiramente, muito obrigado pela disponibilidade em querer contribuir! 🫶

Estava lendo o repositório e teve uma nova ideia? Não entendeu alguma explicação, encontrou erros de grafia ou de código? Aqui você encontra um guia para você colaborar com a melhoria do material, independente do seu nível de conhecimento.

Entenda que não existem dúvidas simples demais e que toda contribuição é recebida com igual entusiasmo.

## Código de conduta

Trate todos igualmente com respeito e siga o nosso [código de conduta](CODE_OF_CONDUCT.md).

## Contribuições possíveis

Você pode ajudar o projeto das seguintes maneiras:

* Lendo o conteúdo e divulgando a seus conhecidos;
* Reportando erros de grafia encontrados no texto;
* Questionando explicações e solicitando uma melhoria no texto;
* Sugerindo melhorias do conteúdo;
* Adicionando novos materiais e tópicos.

## Sua primeira contribuição?

Caso queira apenas sugerir alguma modificação no conteúdo, vá em [issues](../../issues), certifique-se que alguém já não tenha feito a sugestão que você pretendia e tente descrever com maior riqueza de detalhes possíveis. Quando necessário adicione imagens (principalmente quando for um erro).

Uma outra maneira de contribuir, é editando você mesmo os arquivos através do github.

O caminho mais curto começa no próprio livro: abra a página onde está o erro em <https://vimbook.com.br/> e clique no ícone de lápis "Editar esta página", no canto superior direito do texto.

![Página do livro com o botão "Editar esta página" no canto superior direito](docs/imgs/editar-esta-pagina.png)

Ele leva direto ao arquivo certo, já aberto no editor do GitHub. Vale começar por aí em vez de procurar o arquivo na pasta [`docs/`](docs): os nomes não seguem a ordem de leitura, que fica no `nav` do arquivo `zensical.toml`. Então a página que você viu em terceiro lugar no livro dificilmente será a terceira da listagem.

A partir daí o próprio GitHub conduz o resto:

1. faça a alteração no editor e desça até o fim da página;
2. descreva em uma linha o que mudou — é isso que vira o título da sua proposta;
3. escolha enviar a mudança em uma nova *branch*, e não direto na `main`;
4. confira o resumo das alterações e confirme a criação do *pull request*.

Se você não tem permissão de escrita no repositório, não precisa preparar nada antes: o GitHub cria uma cópia dele na sua conta e abre o *pull request* a partir dela.

Assim que a pessoa responsável analisar sua contribuição, suas alterações serão mescladas ao conteúdo.

🤖 Automaticamente, em poucos minutos uma nova versão do site já estará disponível!


## Desenvolvendo localmente

Crie um ambiente virtual utilizando o comando:

```
python -m venv .venv
```

Ative o ambiente através do comando:

```
source .venv/bin/activate
```

ou [equivalente em seu sistema operacional](https://cassiobotaro.dev/do_zero_a_implantacao/projeto/#o-ambiente-virtual).

Em seguida instale as dependências necessárias

```
python -m pip install -r requirements.txt
```

e para executar localmente:

```
zensical serve
```

O site fica disponível em <http://localhost:8000> e recarrega automaticamente a cada alteração.

## Convenções utilizadas e dicas

* Não utilize emojis de forma textual `:emoji:`, copie do [emojipédia](https://emojipedia.org/pt) ao invés;
* Todo título de seção é iniciado com um emoji;
* Novos capítulos devem ser adicionados também no menu de navegação (`nav`) que se encontra no arquivo `zensical.toml`;
* Páginas cujo título não começa com um cabeçalho `#` precisam declarar o título no *front matter*, por exemplo:

```
---
title: Instalação do vim
---
```

### Tabelas de comandos

Listas de referência — comando de um lado, descrição do outro — vão em
tabelas, não em blocos de código. Blocos de código são reservados para
comandos que a pessoa vai de fato digitar, porque só eles fazem sentido
com o botão de copiar:

```
| Comando | Descrição |
|---------|-----------|
| `gg` | vai para o início do arquivo |
```

Dois detalhes que geram erro silencioso, porque o `zensical build`
aceita os dois casos sem reclamar:

* **Deixe uma linha em branco depois da tabela.** Sem ela, o parser
  continua lendo o parágrafo seguinte como linhas da tabela, e o texto
  aparece dentro dela, quebrado em uma célula por linha do arquivo.

* **Para exibir uma barra vertical dentro de uma célula, use
  `<code>&#124;</code>`.** O `\|` do GitHub não funciona aqui: o parser
  não é GFM e mostra a barra invertida na tela. Dentro de crases a
  entidade também não resolve, porque é escapada — só funciona com a
  tag `<code>` escrita à mão. Isso vale para comandos como `10|` (ir
  para a coluna 10); já o `\|` das expressões regulares do Vim, que é o
  operador de alternância, deve mesmo aparecer com a barra invertida.
