## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two

from dagster_dbt import load_assets_from_dbt_project
from dagster import file_relative_path

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

'''

PROJECT_NAME = "jaffle_shop"
DBT_PROJECT_PATH = file_relative_path(__file__, f"../../{PROJECT_NAME}")
DBT_PROFILES = file_relative_path(__file__, f"../../{PROJECT_NAME}/config")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, 
    profiles_dir=DBT_PROFILES,
    key_prefix=[PROJECT_NAME], )
