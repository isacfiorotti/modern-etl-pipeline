from pyspark.sql import SparkSession
from tools.log import log
import yaml


@log
def get_spark_session(app_name: str, config_overrides: dict = {}) -> SparkSession:
    builder = SparkSession.builder \
        .appName(app_name) \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    if config_overrides:
        for key, value in config_overrides.items():
            builder = builder.config(key, value)
            
    spark = builder.getOrCreate()
    return spark