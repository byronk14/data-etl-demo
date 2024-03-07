# Orchestrated Data ETL Pipeline

This demo encompasses all three operations of a typical ETL workflow. Since I enjoy watching the NBA, I decided to use free basketball data API. 

First the raw data is retrieved from the API [nba-stats-db.herokuapp.com] via a series a python scripts. The raw data is saved to a csv file. Then this data is written to a table within a local duckdb instance. dbt is used to calculalte aggregated metrics and loaded to multiple views.

# Prerequisites

1. Python 
2. Duckdb 
3. dbt 
4. git
