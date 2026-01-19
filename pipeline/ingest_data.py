#!/usr/bin/env python
# coding: utf-8

# # New York Taxi Dataset

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

def run():

    pg_user ='root'
    pg_pass ='root'
    pg_host ='localhost'
    pg_port=5432
    pg_db='ny_taxi'

    year=2021
    month=1

    chunksize = 100000
    target_table = 'yellow_taxi_data'

    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    # Connect to the SQL database
    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

    # Define the url of the data
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url=f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'
    url 

    df_iter =pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True, 
        chunksize=100000,
    )

    # Complete ingestion loop
    first = True

    for df_chunk in tqdm(df_iter):

        if first:
            df_chunk.head(0).to_sql(
                name=target_table,
                con=engine,
                if_exists="replace"
                )
            first = False
            print("Table created")

        # Insert chunk
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append"
        )

        print("Inserted:", len(df_chunk))


if __name__ == '__main__':
    run()
