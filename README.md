# Orchestrated Data ETL Pipeline

This demo encompasses all three operations of a typical ETL workflow. Since I enjoy watching the NBA, I decided to use free basketball data API. 

First the raw data is retrieved from the API [nba-stats-db.herokuapp.com](nba-stats-db.herokuapp.com) via a series a python scripts. Then the raw data is saved to a csv file. Following the csv files, this data is written to a table within a local duckdb instance. Finally, dbt is used to calculate aggregated metrics and load to multiple views.

# Prerequisites

**1.** Python \
**2.** Duckdb \
**3.** dbt \
**4.** Git



Clone the git repository and use the main branch.
```bash
git clone https://github.com/byronk14/data-etl-demo.git

cd data-etl-demo

# Set path to duckdb database (.db) file. Replace <file path>.
export DBT_ENV_SECRET_PATH=<file path>
```


## Duckdb

Duckdb is a convenient and extensible database system that can be integrated into ETL pipelines. It provides fast data analytics capabilities, efficient storage, and an user-friendly SQL interface without having to deploy and manage a separate database server.

To install DuckDB usingg Homebrew:
```
brew install duckdb
```

You can launch DuckDB by either executing `duckdb` as a CLI command or connect to a local instance using your favorite database UI tool.

## Extracting Raw Data

Run the following python script. This script calls a public API to retrieve nba data (currently player data for the Phoenix Suns). Then the extracted data is written to a table in a local duckdb instance.

```bash
python3 data_ingestion.py <file path to /data/players> <file path to duckdb .db file> <file path to /data/aggegated>
```

## Running dbt 

dbt is an etl tool that simplifies complex data pipelines and makes it easier to manage, document, and deploy data transformations.

Once the raw API data is written to the raw data table. The following dbt commands are run from terminal for further data processing.

```
dbt deps
dbt snapshot
dbt run --select sde_dbt_tutorial
dbt test
dbt docs generate
dbt docs serve
```