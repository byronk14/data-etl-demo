
import dagster
from dagster_duckdb import DuckDBResource
from data_wrapper import NBADataWrapper
from . import constants
import pandas as pd

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

        PlayerData = NBADataWrapper()
        PlayerData.set_api_url(player_data_url.format(player))
        PlayerData.get_data()
        PlayerData.hydrate()

        player_df = pd.DataFrame(PlayerData.data)

        player_df.to_csv(constants.NBA_PLAYER_DATA_RAW_FILE_DIRECTORY + player + '_stats.csv', index=False)
