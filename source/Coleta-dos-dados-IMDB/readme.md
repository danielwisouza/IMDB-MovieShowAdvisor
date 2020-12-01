O banco de dados de filmes da Internet, [imdb.com], é um site dedicado a coletar dados de filmes fornecidos por estúdios e fãs. Ele afirma ser o maior banco de dados de filmes da web e é administrado pela Amazon. Mais informações sobre a imdb.com podem ser encontradas online, incluindo informações sobre o processo de coleta de dados.

O IMDB disponibiliza seus dados brutos. Infelizmente, os dados são divididos em muitos arquivos de texto e o formato de cada arquivo é ligeiramente diferente. Para criar um arquivo de dados contendo todas as informações desejadas, esses scripts ruby ​​extraem as informações relevantes e armazenam em um banco de dados. Por fim, esses dados são exportados para csv para facilitar a importação para pacotes de análise de dados.

Os seguintes arquivos de texto foram baixados e usados:

* business.list. Orçamento total
* genres.list. Gêneros aos quais um filme pertence (por exemplo, comédia e ação)
* movies.list. Lista mestre de todos os títulos de filmes com ano de produção.
* mpaa-ratings-reason.list. Classificações MPAA.
* ratings.list. Avaliações de fãs do IMDB.
* running-times.list. Duração do filme em minutos.

Os filmes foram selecionados para inclusão se tivessem uma duração conhecida e tivessem sido avaliados por pelo menos um usuário do IMDB. A saída final contém os seguintes campos:

* título. Título do filme.
* ano. Ano de lançamento.
* despesas. Orçamento total (se conhecido) em dólares americanos
* comprimento. Duração em minutos.
* Avaliação. Avaliação média do usuário IMDB.
* votos. Número de usuários IMDB que avaliaram este filme.
* r1-10. Distribuição de votos para cada classificação, até o ponto médio do decil mais próximo: 0 = sem votos, 4,5 = 1-9 $% $ votos, 14,5 = 11-19 $% $ de votos, etc. Devido a erros de arredondamento, eles podem não somar a 100.
* mpaa. Classificação de MPAA.
* ação, animação, comédia, drama, documentário, romance, curta. Variáveis ​​binárias que representam se o filme foi classificado como pertencente a esse gênero
