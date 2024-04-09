O dicionário de termos
----------------------

A qualidade da verificação ortográfica do Vim está diretamente ligada à
completude e corretude do dicionário da linguagem em questão.
Dicionários pouco completos são inconvenientes à medida que acusam falso
positivos em demasia; pior, dicionários contendo palavras grafadas
incorretamente, além de acusarem falso positivos, induzem o usuário ao
erro ao sugerirem grafias erradas.

É razoavelmente comum o Vim já vir instalado com dicionários de relativa
qualidade para algumas linguagens (ao menos inglês, habitualmente).
Entretanto, ainda é raro para a maioria das instalações do Vim trazer
por *default* um dicionário realmente completo e atualizado
da língua portuguesa. A próxima seção sintetiza, pois, os passos para a
instalação de um excelente—e disponível livremente—dicionário de
palavras para a língua portuguesa.

### Dicionário português segundo o acordo ortográfico

A equipe do projeto BrOffice.org e seus colaboradores
mantêm e disponibilizam livremente um grandioso dicionário de palavras
da língua portuguesa. Além do expressivo número de termos, o dicionário
contempla as mudanças ortográficas definidas pelo *Acordo
Ortográfico* que entraram em vigor no
início de 2009.

A instalação envolve três passos, são eles:

1.  obtenção do dicionário através do site BrOffice.org;

2.  conversão para o formato interno de dicionário do Vim; e

3.  instalação dos arquivos resultantes.

#### Obtenção do dicionário

O dicionário pode ser obtido no [site do libreoffice](https://pt-br.libreoffice.org/projetos/vero#baixarvero).
O arquivo baixado encontra-se compactado no formato oxt,
bastando portanto descompactá-lo com qualquer utilitário compatível com
este formato, por exemplo, o comando unzip.

#### Conversão do dicionário

Após a descompactação, os arquivos `pt_BR.aff` e `pt_BR.dic`, extraídos
no diretório corrente[^1], serão usados para a criação dos dicionários
no formato interno do Vim[^2]. A conversão propriamente dita é feita
pelo próprio Vim através do comando mkspell:

1.  Carrega-se o Vim a partir do diretório onde foram extraídos
    `pt_BR.aff` e `pt_BR.dic`

2.  O comando mkspell é então executado como:
```
:mkspell pt pt_BR
```
O Vim então gera um arquivo de dicionário da forma
`pt.<codificação>.spl`, onde `<codificação>` é a codificação de
caracteres do sistema, normalmente `utf-8` ou `latin1`; caso queira-se
um dicionário em uma codificação diferente da padrão será preciso
ajustar a variável encoding antes da invocação do comando
mkspell:
```
:set encoding=<codificação>
:mkspell pt pt_BR
```
#### Instalação do(s) dicionário(s) gerado(s)

Finalmente, o dicionário gerado—ou os dicionários, dependendo do uso ou
não de codificações diferentes—deve ser copiado para o subdiretório
spell/ dentro de qualquer caminho (diretório) que o Vim
“enxergue”. A lista de caminhos lidos pelo Vim encontra-se na variável
runtimepath, que pode ser inspecionada através de:
```
:set runtimepath
```
É suficiente então copiar o dicionário `pt.<codificação>.spl` para o
subdiretório spell/ em qualquer um dos caminhos listados
através do comando mostrado.

[^1]: Eventualmente, dependendo da versão do pacote de correção ortográfica, os arquivos de dicionário podem ser extraídos no subdiretório dictionaries ou outro qualquer.

[^2]: O formato interno de dicionário do Vim assegura melhor desempenho, em termos de agilidade e consumo de memória, quando a verificação ortográfica do editor encontra-se em operação.
