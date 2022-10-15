-- Refer to Using dbt with Dagster, part one for info about this file:
-- https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster/part-one

SELECT 
    id as customer_id
    first_name,
    last_name
FROM {{ source('jaffle_shop', 'customers_raw') }}