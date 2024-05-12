
from dagster import asset, MetadataValue, MaterializeResult
from dagster_duckdb import DuckDBResource
from . import data_wrapper
from . import constants
import pandas as pd
import os
import sys

@asset(
    group_name="raw_files"
)
def nba_player_data_file(context):
    """
      The raw parquet files for the NBA player data dataset. Sourced from the open source NBA API.
    """
    
    phoenix_roster_list = ['Kevin Durant', 'Devin Booker', 'Bradley Beal', 'Yuta Watanabe', 'Eric Gordon', 'Bol Bol', \
                            'Grayson Allen', 'Drew Eubanks', 'Udoka Azubuike', 'Keita Bates-Diop', "Royce O'Neale", \
                            'Damion Lee', 'Saben Lee', 'Josh Okogie', 'Nassir Little', 'Théo Maledon', 'Jusuf Nurkić', \
                            'David Roddy', 'Thaddeus Young']
    
    # Establish dictionary of data wrapper class
    data_wrapper_class_list = {}

    # Player data url
    player_data_url = 'https://nba-stats-db.herokuapp.com/api/playerdata/name/{}'

    # Retrieve stats data for each player on the roster
    for player in phoenix_roster_list:

        PlayerData = data_wrapper.NBADataWrapper()
        PlayerData.set_api_url(player_data_url.format(player))
        PlayerData.get_data()
        PlayerData.hydrate()

        player_df = pd.DataFrame(PlayerData.data)

        player_df.to_csv(constants.NBA_PLAYER_DATA_RAW_FILE_DIRECTORY + player + '_stats.csv', index=False)

    return MaterializeResult(
    metadata={
        'Number of records': MetadataValue.int(len(player_df))
        }
    )

@asset(
    deps=["nba_player_data_file"],
    group_name="ingested"
)
def team_players_stats_duckdb_table(database: DuckDBResource):
    """
      The raw nba player datasets, loaded into a DuckDB table
    """

    player_stat_df_list = []

    dirpath = constants.NBA_PLAYER_DATA_RAW_FILE_DIRECTORY

    # Read in data
    directory = os.fsencode(dirpath)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        
        temp_df = pd.read_csv(dirpath + '/' + filename)

        player_stat_df_list.append(temp_df)

    appended_data_df = pd.concat(player_stat_df_list)

    with database.get_connection() as conn:
        #conn.execute(query)
        appended_data_df.to_csv(constants.NBA_PLAYER_DATA_AGGREGATED_FILE_DIRECTORY + 'suns_roster_player_data.csv', index=False)

        query = f"""
                CREATE TABLE team_players_stats 
                    AS SELECT * FROM read_csv_auto('{constants.NBA_PLAYER_DATA_AGGREGATED_FILE_DIRECTORY + 'suns_roster_player_data.csv'}');
        """
        # Create table
        conn.sql(query)

    # Write to duckdb table
    #duckdb.register('test_df_view', appended_data_df) #causes a known issue that will be fixed with next duckdb release https://github.com/duckdb/duckdb/pull/8738

    return MaterializeResult(
    metadata={
        'Number of records': MetadataValue.int(len(appended_data_df))
        }
    )
