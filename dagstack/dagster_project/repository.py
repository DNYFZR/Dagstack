## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two
__doc__ = '''
What's happening here:

- Using with_resources : 
    - we've provided resources to the assets in the repository. 
    - In this example, that's the dbt_cli_resource resource.
- Using load_assets_from_package_module : 
    - we've imported all assets in the assets module into the repository. 
    - This approach allows any new assets we create to be automatically added to the repository.

-  The duckdb_io_manager contains an I/O manager that allows :
    - Upstream assets to load data into DuckDB. 
        - The duckdb_io_manager:
            - Uses DuckDBPandasTypeHandler to store DataFrames in our assets as CSVs 
            - Load them into DuckDB.
    - Downstream assets to read data from DuckDB
'''

import os
from dagster_dbt import dbt_cli_resource
from dagster import load_assets_from_package_module, repository, with_resources

from dagster_duckdb import build_duckdb_io_manager
from dagster_duckdb_pandas import DuckDBPandasTypeHandler

from dagster_project import assets
from dagster_project.assets import DBT_PROFILES, DBT_PROJECT_PATH

DB_PATH = "tutorial.duckdb"

@repository
def dbt_resource():
    duckdb_io_manager = build_duckdb_io_manager([DuckDBPandasTypeHandler()])
    return with_resources( 
        load_assets_from_package_module(assets), 
        {
            "dbt" : dbt_cli_resource.configured(
                { "project_dir" : DBT_PROJECT_PATH, "profiles_dir" : DBT_PROFILES, }),
            "io_manager" : duckdb_io_manager.configured(
                { "duckdb_path" : os.path.join(DBT_PROJECT_PATH, DB_PATH), }),
        })
