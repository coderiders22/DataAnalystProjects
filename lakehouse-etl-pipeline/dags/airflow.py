from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "lakehouse_pipeline",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="lakehouse_etl_pipeline",
    default_args=default_args,
    description="Lakehouse ETL Pipeline (Landing → Staging → Warehouse)",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["lakehouse", "spark", "etl"],
) as dag:


    # -----------------------------
    # DATE DIMENSION PIPELINE (SCD1)
    # -----------------------------

    date_landing = BashOperator(
        task_id="date_landing",
        bash_command="papermill /opt/airflow/src_notebooks/date_landing.ipynb /tmp/date_landing_out.ipynb"
    )

    date_staging = BashOperator(
        task_id="date_staging",
        bash_command="papermill /opt/airflow/src_notebooks/date_staging.ipynb /tmp/date_staging_out.ipynb"
    )

    date_warehouse = BashOperator(
        task_id="date_warehouse",
        bash_command="papermill /opt/airflow/src_notebooks/date_warehouse.ipynb /tmp/date_warehouse_out.ipynb"
    )


    # -----------------------------
    # CUSTOMER DIMENSION PIPELINE (SCD2)
    # -----------------------------

    customer_landing = BashOperator(
        task_id="customer_landing",
        bash_command="papermill /opt/airflow/src_notebooks/customer_landing.ipynb /tmp/customer_landing_out.ipynb"
    )

    customer_staging = BashOperator(
        task_id="customer_staging",
        bash_command="papermill /opt/airflow/src_notebooks/customer_staging.ipynb /tmp/customer_staging_out.ipynb"
    )

    customer_warehouse = BashOperator(
        task_id="customer_warehouse",
        bash_command="papermill /opt/airflow/src_notebooks/customer_warehouse.ipynb /tmp/customer_warehouse_out.ipynb"
    )


    # -----------------------------
    # PIPELINE ORDER
    # -----------------------------

    date_landing >> date_staging >> date_warehouse

    customer_landing >> customer_staging >> customer_warehouse