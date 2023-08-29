# sentiment_analysis

Este código foi elaborado para a ativade nas áreas de experiência do usuário, programação e matemática. O propósito do código reside na análise de sentimento de duas frases distintas: uma de conotação negativa e outra de conotação positiva. Além disso, o código também engloba a identificação de palavras negativas, tanto em seu uso isolado quanto quando inseridas em contextos que as envolvem.

A presente documentação tem por objetivo explicar as escolhas feitas durante o desenvolvimento, bem como as especificações adotadas no código, contendo também a apresentação dos resultados obtidos.

## Como rodar o projeto

Este código foi desenvolvido em Python, fazendo uso de bibliotecas selecionadas. Antes de executar o projeto, é importante que o Python esteja devidamente instalado em sua máquina. Adicionalmente, há uma lista de bibliotecas cuja presença também se faz necessária:

```python
    pip install unidecode # Biblioteca para representação em ASCII
    pip install spacy # Biblioteca para funções de PLN
    python -m spacy download pt_core_news_sm # Pacote do idioma português do spacy
    pip install python-dotenv # Biblioteca para utilizar variaveis de ambiente
    pip install twilio # Biblioteca para envio de SMS
```

Uma vez satisfeitas as etapas prévias, a simples realização do código exige a execução de um comando no terminal:

```python
    python sentences.py
```

## Justificativa

Este projeto foi criado com foco primordial no uso mais frequente pelos usuários do aplicativo de busca por voz. Ele visa manter os usuários informados sobre as notícias atuais, apresentando a funcionalidade adicional de oferecer uma prévia da conotação dessas notícias - se ela é positiva ou negativa. Essa avaliação é realizada por meio da criação de uma lista de palavras negativas, considerando tanto o contexto isolado dessas palavras quanto sua coexistência em uma estrutura maior. Subsequentemente, é calculada a similaridade cosseno entre as frases, que já foram previamente definidas e tratadas, com as palavras negativas identificadas. Caso haja uma alta similaridade, o sistema pode emitir um dos quatro alertas distintos para o usuário, através de mensagens de texto (SMS):

  - Quando ambas as frases são classificadas como negativas
  - Quando somente a primeira frase é classificada como negativa.
  - Quando somente a segunda frase é classificada como negativa.
  - Quando nenhuma das frases é classificada como negativa.

Vale ressaltar que os três primeiros tipos de alerta são acompanhados pela própria frase no corpo da mensagem de texto.

A preferência pelo uso do SMS como canal de recebimento de alertas encontra justificativa no cenário atual, no qual passamos a maior parte do nosso dia interagindo constantemente com nossos dispositivos móveis. Dessa forma, a escolha desse meio se mostra altamente conveniente, uma vez que nos permite receber e visualizar as mensagens de alerta de maneira mais ágil. Isso, por sua vez, reduz significativamente a probabilidade de deixarmos passar desapercebidos tais alertas, evitando a perda de um tempo de extrema importância para reagir prontamente a campanhas ou estratégias de vendas direcionadas à IBM.

## Escolha das frases

A frase de teor positivo foi extraída do [site](https://www.ibm.com/blogs/ibm-comunica/ibm-lanca-capacidades-para-watson/) destacado durante a aula, conforme demonstrado nos slides. A frase em questão é a seguinte:

"Os novos recursos de IA de hoje são mais um exemplo de como os avanços de ponta da IA provenientes de IBM Research nos ajudam a fornecer inovações em linguagem, automação e construção de confiança no IBM Watson que estão fazendo a diferença para empresas de todos os tamanhos e em todos os setores"

Por outro lado, a sentença de cunho negativo foi gerada por meio de um prompt utilizado no GPT, solicitando a criação de uma notícia desfavorável acerca da IBM. Nesse contexto, também foi requerido que fossem indicadas as palavras negativas, tanto considerando-as de maneira isolada como avaliando o contexto em que poderiam estar inseridas. A frase gerada é a seguinte:

"A reputação da IBM sofre um golpe à medida que alegações de práticas obscuras de privacidade, coleta não autorizada de dados e falta de transparência vêm à tona, levantando sérias preocupações sobre a ética corporativa e a confiança dos clientes na empresa."

A lista de palavras negativas definida foi a seguinte:

['reputacao','sofre', 'golpe', 'alegacoes', 'obscuras','privacidade', 'falta','transparencia', 'preocupacoes', 'questionavel', 'nao','autorizada','dados', 'confianca', 'etica', 'clientes']

## Resultados obtidos

Os resultados conquistados serão apresentados por meio de um vídeo de demonstração, acompanhado por duas fotos que capturam os resultados obtidos com a execução do código.

O vídeo de demonstração do projeto pode ser acessado pelo link a seguir:
[Demonstração Sentiment Analysis](https://youtu.be/l7DOjElSZIg)

Quanto as fotos, elas exibem os resultados do projeto, que coincidem com o conteúdo demonstrado no vídeo:

<img width="543" alt="Capturar" src="https://github.com/brun0meira/sentiment_analysis/assets/99202553/bd9006a6-79c5-4bdb-a2c2-16b78225a01b">

![Screenshot_2023](https://github.com/brun0meira/sentiment_analysis/assets/99202553/0f1c6884-12ff-41e6-b3d8-d8f93d6c3f39)

