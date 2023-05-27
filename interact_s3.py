import boto3
import pandas as pd

# Criar um cliente para interagir com a AWS S3
s3_client = boto3.client('s3')

# s3_client.download_file("datalake-paulos-igti-edc", "data/MICRODADOS_ENEM_2020.csv", "data/arquivo.csv")

# df = pd.read_csv("data/arquivo.csv", sep=";")
# print(df)

s3_client.upload_file("data/MICRODADOS_ENEM_2020.csv", "datalake-paulos-igti-edc", "raw-data/MICRODADOS_ENEM_2020.csv")