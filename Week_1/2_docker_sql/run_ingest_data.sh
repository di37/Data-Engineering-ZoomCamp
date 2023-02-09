URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet" 

python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=6000 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}
