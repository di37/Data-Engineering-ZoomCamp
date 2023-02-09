#!/usr/bin/env python
# coding: utf-8

import argparse
import os

from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = "output.parquet"

    os.system(f"wget {url} -O {parquet_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    engine.connect()

    trip_df = pd.read_parquet(parquet_name)
    trip_df.drop(columns=["airport_fee"], inplace=True)

    trip_df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")
    print(f"Loading data into {table_name}....")
    trip_df.to_sql(name=table_name, con=engine, if_exists="append")
    print(f"Data Loading completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Parquet data to Postgres")
    parser.add_argument("--user", type=str, default="user name for postgres")
    parser.add_argument("--password", type=str, default="password for postgres")
    parser.add_argument("--host", type=str, default="host for postgres")
    parser.add_argument("--port", type=str, default="port for postgres")
    parser.add_argument("--db", type=str, default="database name for postgres")
    parser.add_argument(
        "--table_name", type=str, default="name of the table where results will be written"
    )
    parser.add_argument("--url", type=str, default="url of the parquet file")

    args = parser.parse_args()

    main(args)


