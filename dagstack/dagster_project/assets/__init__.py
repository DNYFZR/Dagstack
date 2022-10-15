## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two
import pandas as pd, plotly.express as px
from dagster_dbt import load_assets_from_dbt_project
from dagster import AssetIn, MetadataValue, asset, file_relative_path

__doc__ = '''
load_assets_from_dbt_project :
  This function loads dbt models into Dagster as assets, creating one Dagster asset for each model.

  When invoked, this function:
    - Compiles your dbt project,
    - Parses the metadata provided by dbt, and
    - Generates a set of software-defined assets reflecting the models in the project. These assets share the same underlying op, which will invoke dbt to run the models represented by the loaded assets.
  
  Arguments:

    - project_dir : which is the path to the dbt project
    - profiles_dir : which is the path to the dbt project's connection profiles
    - key_prefix : which is a prefix to apply to all models in the dbt project

@asset : 
  - key_prefix :
    - When the assets are materialized, Dagster will store them in DuckDB 
    - In the schema defined by the last value in key_prefix.
  
  - group_name : 
    - When Dagster loads the dbt models as assets, the assets will be placed in an asset group 
    - Based on the name of the folder (staging) containing the models. 

Dagster output
  - customers is supplied as an argument to ins, 
  - defining it as an upstream asset dependency of the order_count_chart asset
  - Used AssetIn to explicitly define an upstream dependency
  - The chart is saved as order_count_chart.html in CWD
  - The chart is automatically opened in the browser upon successful materialization
'''

# Project Config
PROJECT_NAME = "jaffle_shop"
DBT_PROJECT_PATH = file_relative_path(__file__, f"../../{PROJECT_NAME}")
DBT_PROFILES = file_relative_path(__file__, f"../../{PROJECT_NAME}/config")

# Data Config
CUSTOMERS_RAW = "https://docs.dagster.io/assets/customers.csv"
ORDERS_RAW = "https://docs.dagster.io/assets/orders.csv"

# Asset Config
@asset(key_prefix=[PROJECT_NAME], group_name="staging")
def customers_raw() -> pd.DataFrame:
    return pd.read_csv(CUSTOMERS_RAW)

@asset(key_prefix=[PROJECT_NAME], group_name="staging")
def orders_raw() -> pd.DataFrame:
    return pd.read_csv(ORDERS_RAW)

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, 
    profiles_dir=DBT_PROFILES,
    key_prefix=[PROJECT_NAME], )


# Create Dagster Asset
@asset(ins={"customers": AssetIn(key_prefix=[PROJECT_NAME])}, group_name="staging", )
def order_count_plot(context, customers: pd.DataFrame):
  fig = px.histogram(customers, x = 'number_of_orders')
  fig.update_layout(bargap = 0.25)

  chart_path = file_relative_path(__file__, "OrderCount.html")
  fig.write_html(chart_path, auto_open=True)

  context.add_output_metadata({"plot_url": MetadataValue.url(f"file://{chart_path}")})
  