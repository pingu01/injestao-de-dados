# Injestão de dados
Nessa atividade, a ideia é fazer a injestão de dados de uma API pública que mostra informações de destilarias de whisky.

# Subindo MiniIO e Clickhouse no com Docker

Entre na pasta `/src/data_pipeline`, e execute o comando
```bash
docker compose up -d
```
Vale lembrar que o Clickhouse também tem senha, que é determinada no arquivo users.xml

# Executando

Primeiro, crie um arquivo `.env` na pasta em que vocẽ está:
```
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=8123
CLICKHOUSE_PASSWORD=senhabizarra_21421 
```

Execute o arquivo `app.py`, ele vai subir uma API que vai salvar os dados raw.
Abra o DBeaver e se conecte no clickhouse para ver os dados working.

A senha é a variável `CLICKHOUSE_PASSWORD` do `.env`

Depois de se conectar, com o `app.py` rodando, é necessário executar o arquivo `/scripts/fetch_data.py`. Esse arquivo pega uma informação aleatória de uma API externa, e envia para um endpoint da nossa API, que salva o dado recebido como RAW. 

Depois de executar, vai dar pra ver o dado salvo na tabela 'working_data'

Para fazer uma view desses dados, execute esse script SQL no DBeaver.

```
CREATE VIEW IF NOT EXISTS working_data_view AS
SELECT
    toDateTime(JSONExtractInt(dado_linha, 'date')) AS date_unix,
    JSONExtractString(dado_linha, 'dados') AS dados,
    toDateTime(JSONExtractInt(dado_linha, 'data_ingestao') / 1000) AS data_ingestao_datetime
FROM
    working_data;
```

