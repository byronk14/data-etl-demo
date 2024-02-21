import duckdb
import pandas as pd
from data_wrapper import NBADataWrapper




if __name__ == "__main__":

    # players on Phoenix Suns roster
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

        player_df.to_csv('/Users/byronkim/Documents/projects/data-etl-demo/data/players/' + player + '_stats.csv', index=False)



