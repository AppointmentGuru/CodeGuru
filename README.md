# ICD10Guru

## Running locally:

**Dependencies:**

* Postgres

**docker-compose.yml**

```
version: "3"
services:
  db:
    restart: on-failure:10
    image: postgres:9.5
    volumes:
      - "icd10-postgres-db-volume:/var/lib/postgresql/data"
  web:
    restart: on-failure:10
    image: appointmentguru/icd10guru
    command: sh /code/run.sh
    depends_on:
      - db
    ports:
      - "8000:8000"

volumes:
  icd10-postgres-db-volume:
```

Then: `docker-compose up -d`

API is available at [localhost:8000](http://localhost:8000)


### Commands:

When installing from fresh, you'll probably want to run these:

```
# load code database
docker-compose run --rm web python manage.py loaddata /code/api/fixtures/initial_data.json
```
(this can take some time as there's about 44000 codes in there)
