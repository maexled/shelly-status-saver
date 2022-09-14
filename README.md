# Shelly status saver
Requests data from Shelly 3EM and stores status in sql database.

## Environment Variables
`SQL_URL` - the URL for database, e.g. `mysql+pymysql://user:password@host:3306/database`

## Run
### With python
```sh
export SQL_URL=mysql+pymysql://user:password@host:3306/database
python -m main
```

### With Docker Container
```sh
docker run \
    --name mystrom-python \
    -e "SQL_URL=mysql+pymysql://user:password@host:3306/database" \
    ghcr.io/maexled/mystrom-python:master
```
