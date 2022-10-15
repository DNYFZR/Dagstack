## Refer to Using dbt with Dagster, part two for info about this file:
## https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-two

import os, assets
from dagster_dbt import dbt_cli_resource
from dagster import load_assets_from_package_module, repository, with_resources

from dagster_project.assets import DBT_PROFILES, DBT_PROJECT_PATH

__doc__ = '''
What's happening here:

- Using with_resources : 
    - we've provided resources to the assets in the repository. 
    - In this example, that's the dbt_cli_resource resource.
- Using load_assets_from_package_module : 
    - we've imported all assets in the assets module into the repository. 
    - This approach allows any new assets we create to be automatically added to the repository.
'''

@repository
def dbt_resource():
    return with_resources( 
        load_assets_from_package_module(assets), 
        {"dbt" : dbt_cli_resource(
                { "project_dir" : DBT_PROJECT_PATH, "profiles_dir" : DBT_PROFILES, }) 
            })
