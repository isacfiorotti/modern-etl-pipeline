from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator
import pendulum
import yaml
from ops.session import get_spark_session
from ops.extract import get_ticker_data, merge_ticker_data


@dag(
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC")
)
def run_ticker_data_pipeline():
    
    @task()
    def get_config():
        with open('/usr/local/airflow/config/config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        return {
            "ticker": config.get('default_ticker', 'SPY'),
            "app_name": config.get('app_name', 'modern_etl_pipeline'),
            "delta_path": config.get('delta_path', '/data/bronze/')
        }


    @task()
    def extract_and_load():
        spark = get_spark_session(app_name=APP_NAME)
        df = get_ticker_data(ticker=TICKER)
        merge_ticker_data(
            spark=spark,
            df=df,
            delta_path
        )
    @task()
    def transform():
        bo = BashOperator(bash_command=DBT_CMD)
