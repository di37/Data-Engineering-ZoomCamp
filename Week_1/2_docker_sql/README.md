## Ingesting NY Taxi Data to Postgres

Pre-requisites:

- Git bash must be installed on the system.
- Must have docker and docker compose installed on the system.

1 - Open a new terminal window, and run `docker_run_pg.sh`

```bash
chmod +x docker_run_pg.sh
```

```bash
./docker_run_pg.sh
```

2 - Open another tab of the terminal and install pgcli client to access postgres from docker in the machine from the created docker container that is running.

```bash
pip install pgcli

pip3 install psycopg2

pip install sqlalchemy
```

2 - Enter the following command to access postgresql from docker.

```bash
pgcli -h localhost -p 6000 -u root -d ny_taxi
```

3 - In the same directory, create a new jupyter notebook - `upload-data.ipynb`.

4 - Download the parquet file consisting of tlc trip records and data dictionary - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page using following commands.

```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
```

```bash
wget https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv
```

```bash
wget https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
```

5 - Explore the dataset in `upload-data.ipynb`.

6 - In the notebook, generate schema and bring the dataset into Data Definition Language (DDL).

7 - In pgcli tab of the terminal, to list out tables:

```bash
\dt
```

8 - To check the schema of the dataset:

```bash
\d yellow_taxi_data
```

Press `q` to return to pgcli.

9 - Create postgresql engine connection and perform data ingestion to postgres. All details can be found in the notebook.

10 - In pgcli tab, check the number of rows in the table:

```bash
SELECT COUNT(1) FROM yellow_taxi_data
```

If it shows count of 1369769, then ingestion to postgres has been completed successfully. Lets perform another query.

```bash
SELECT MAX(tpep_pickup_datetime), MIN(tpep_pickup_datetime), MAX(total_amount) FROM yellow_taxi_data
```

## Connecting pgAdmin and Postgres

Note that there will be two containers running. The first container is the `docker_run_pg.sh` and the second container is the `docker_run_pgadmin.sh`. We will need to connect these containers.

This is achieved by creating network.

```bash
docker network create pg-network
```

1 - Now, run `docker_run_pgadmin.sh`.

```bash
chmod +x docker_run_pgadmin.sh
```

```bash
./docker_run_pgadmin.sh
```

2 - Open a web browser and navigate to http://localhost:8080/. Then login to the pg admin panel using the credentials mentioned in the `docker_run_pgadmin.sh` file.

3 - Once logged in, click Add New Server. In General section, name it as **Docker localhost**. In Connection section, under hostname/address, enter **pg-database**. In Port section, enter **5432** as it is the docker port # of postgresql. Enter same username and password as per the script in `docker_run_pg.sh` file.

4 - Lets make query to the postgresql database. On the left hand side, to show first 100 rows, Servers -> Docker localhost -> Databases -> ny_taxi -> Schemas -> public -> Tables -> yellow_taxi_data -> View/Edit Data -> First 100 Rows.

5 - Click on Tools -> Query Tool. Now we can run the required queries.

## Dockerizing the Ingestion Script

1 - Convert the `upload-data.ipynb` file into python script file:

```bash
jupyter nbconvert --to=script upload-data.ipynb
```

2 - Rename the script file to `ingest_data.py` and refactor the code.

3 - In pgAdmin, drop the table.

4 - Run the bash script, `run_ingest_data.sh` for re-inserting the data into postgres.

```bash
chmod +x run_ingest_data.sh
```

```bash
./run_ingest_data.sh
```

Note that we are ingesting the data from our local environment. We want to ingest the data from the docker container. Therefore, Docker file needs to be created.

5 - We will again delete the table for re-ingesting data into postgres. After creating Dockerfile, run the script - `docker_run_ingest.sh`.

```bash
chmod +x docker_run_ingest.sh
```

```bash
./docker_run_ingest.sh
```

Rather than having multiple bash scripts to run separate docker containers, we will use Docker Compose to run multiple docker containers. The docker compose file - `docker-compose.yaml` needs to be created.

## Running Postgres and pgAdmin with Docker-Compose

As we define multiple container specs in docker-compose.yaml, these containers automatically part of the same container. Therefore, no need of separately creating a network to create bridge between two containers.

- For persisting the credentials, create a new folder: `data_pgadmin`.
- Grant permission to the created folder otherwise it will throw Operation Not Permitted exception:

```bash
sudo chmod -R 777 ./data_pgadmin
```

- Run `docker-compose.yaml`:

```bash
docker-compose up
```

- Detach the file:

```bash
docker-compose up -d
```

- Stop running the docker:

```bash
docker-compose down
```
