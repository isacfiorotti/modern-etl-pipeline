import yfinance as yf
import yaml
from pyspark.sql import SparkSession
import pandas as pd
from pathlib import Path
from delta.tables import DeltaTable
from session import get_spark_session
from tools.log import log


@log
def get_ticker_data(ticker) -> None:
    print(f"The ticker selected is: {ticker}")
    return None

@log
def merge_ticker_data(spark: SparkSession, df: pd.DataFrame, delta_path: str):
    if not Path(delta_path).exists():
        print("Delta table not found. Performing initial full write.")
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .partitionBy("Year", "Month") \
            .save(delta_path)
        return

    delta_table = DeltaTable.forPath(spark, delta_path)

    merge_condition = (
        "target.Date = updates.Date AND target.Ticker = updates.Ticker"
    )

    delta_table.alias("target") \
        .merge(
            source=df.alias("updates"),
            condition=merge_condition
        ) \
        .whenMatchedUpdateAll() \
        .whenNotMatchedInsertAll() \
        .execute()
    return None    

@log
def main() -> None:
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    
    for ticker in config.get('tickers'):
        spark = get_spark_session(app_name='yf')
        df = get_ticker_data(ticker)
        merge_ticker_data(
            spark=spark,
            df=df,
            delta_path=config.get('')
        )