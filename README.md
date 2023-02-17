# Shelly status saver
Requests data from Shelly 3EM and stores status in sql database.

## Environment Variables
`SQL_URL` - the URL for database, e.g. `mysql+pymysql://user:password@host:3306/database`

## Run
### With python
#### MySQL
```sh
export SQL_URL=mysql+pymysql://user:password@host:3306/database
python -m main
```

#### PostgreSQL
```sh
export SQL_URL=postgresql+psycopg2://user:password@host:5432/database
python -m main
```

### With Docker Container
#### MySQL
```sh
docker run \
    --name shelly-status-saver \
    -e "SQL_URL=mysql+pymysql://user:password@host:3306/database" \
    ghcr.io/maexled/shelly-status-saver:master
```
#### PostgreSQL
```sh
docker run \
    --name shelly-status-saver \
    -e "SQL_URL=postgresql+psycopg2://user:password@host:5432/database" \
    ghcr.io/maexled/shelly-status-saver:master
```