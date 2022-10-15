<h2 align="center"><b> 🥞 Dagstack 🥞 </b></h2>

<br>

In this project we will build an analytics pipeline using Dagster, dbt, DuckDB, Pandas & Plotly.

Raw data will be fetched with Pandas, processed using dbt, stored with DuckDB, all orchestrated by Dagster, the output will be generated with Plotly.

Dagster Guide : [Dagster, dbt & DuckDB tutorial](https://docs.dagster.io/integrations/dbt/using-dbt-with-dagster)


<h3 align="center"><b> 🧱 Project Set-up </b></h3>

<br>

---

This repo has been developed in the following environment :

````yaml
Environment:
  - Python: 3.10.8
  - setuptools: 63.2.0
  - pip: 22.2.2

Dependencies:
  dbt: 
    - dbt-core: 1.3.0
    - dbt-duckdb: 1.2.2
  dagster: 
    - dagster: 1.0.13
    - dagit: 1.0.13
    - dagster-dbt: 0.16.13
    - dagster-duckdb: 0.16.13
    - dagster-duckdb-pandas: 0.16.13
  pandas: 1.5.0
  plotly: 5.10.0
````

To clone the template project from Dagster :

````cmd
dagster project from-example --name dbt_dagster --example tutorial_dbt_dagster 
````

---
---
