# Projeto de Data Warehouse

## Definição:

**Datawarehouse**: Um Data Warehouse é um tipo de arquitetura de banco de dados orientado
por assunto, seu principal objetivo é integrar e consolidar as informações
de fontes internas e externas heterogêneas, filtrando, limpando disponibilizando essas
informações para apoio a decisões de uma empresa.

## Visão Geral:

Este projeto foi parte do curso *"Data Engineering Nanodegree"* da Udacity e consiste da 
criação de uma ETL para montar um Data Warehouse hospedado no AWS Redshift. \
(Obs: O projeto não contempla a exploração dos dados armazenados.)

O _case_ consiste em uma startup que possui um app de streaming de músicas que cresceu e
deseja migrar seus dados e processos para a cloud.

Os dados residem em um bucket S3 de acesso restrito aos alunos do curso, em um diretório
de logs em formato JSON a respeito da atividade dos usuários no aplicativo, bem como um
diretório com metadados em JSON a respeito das músicas no app.

## Dataset das músicas:

É um subconjunto de dados reais da [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/).
Os arquivos estão em JSON e contem metadados sobre a música e artista de cada canção,
Estes arquivos estão particionados tomando como base as três primeiras letras da ID de cada faixa.

Exemplo:

```
{"num_songs": 1, "artist_id": "ARJBB14A8I177YE299", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Motorhead", "song_id": "SOUA1DEAIU4R126F1P", "title": "Brotherhood of Man", "duration": 320.92036, "year": 2010}
```

## Dataset do Log:

É um arquivo JSON gerado a partir daqui: [event simulator](https://github.com/Interana/eventsim) ;
Baseado no dataset de músicas, simula os logs do aplicativo. 
Estes arquivos são particionados por ano e mês.

## Esquema dos dados:

Utilizei a estrutura básica de um modelo de dados dimensional, chamado _"Star Schema"_,
Portanto, o esquema é composto por definição de uma grande entidade central chamada de **fato**
(_"fact tables"_) e um conjunto de entidades menores denominadas **dimensões**.

Os relacionamentos entre a entidade fato e as dimensões são simples ligações entre duas 
entidades em um relacionamento de um para muitos no sentido da dimensão para o fato.


### Fatos:
Definição de fato: Um fato é uma coleção de ítens, composta de dados de medidas e de contexto.
É utilizado para analisar o processo de negócio de uma empresa, reflete a evolução dos
negócios de uma organização.

Cada fato pode representar um ítem, transação ou evento de negócio, tem por característica
básica ser representado por valores numéricos e ser implementado nas chamadas _tabelas de fatos_.

#### Tabela de fatos:

songplays - dados de registros associados a uma música tocada. Suas colunas são:

    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimensões: 

Definição: As dimensões descrevem e classificam os elementos que participam de um fato,
determinando o contexto de um assunto de negócios.

Uma tabela de dimensões pode responder a perguntas como: 
1. O quê ?
2. Quem ?
3. Quando ?
4. Onde ?

#### Tabelas de dimensões: 

##### users

    user_id, first_name, last_name, gender, level
##### songs

    song_id, title, artist_id, year, duration

##### artists

    artist_id, name, location, lattitude, longitude

##### time

    start_time, hour, day, week, month, year, weekday

### Setup: 
1.- Configurar o arquivo dwh.cfg

2.- Executar o comando `python create_tables.py` em um terminal

3.- Executar o comando  `python etl.py` em um terminal

