import duckdb
import pandas as pd
import os
import sys





if __name__ == "__main__":
    
    player_stat_df_list = []

    dirpath = sys.argv[1]

    # Establish connection to duckdb 
    con = duckdb.connect(database=sys.argv[2])

    # Read in data
    directory = os.fsencode(dirpath)
    
    for file in os.listdir(directory):
        print(file)
        filename = os.fsdecode(file)
        
        temp_df = pd.read_csv(dirpath + '/' + filename)

        player_stat_df_list.append(temp_df)

    appended_data_df = pd.concat(player_stat_df_list)

    print(appended_data_df.head())

    appended_data_df.to_csv('data/aggregated/suns_roster_player_data.csv', index=False)


    # Create table
    con.sql(f"CREATE TABLE team_players_stats AS SELECT * FROM read_csv_auto({dataFilePath});".format(dataFilePath=sys.argv[3]))

    # Write to duckdb table
    #duckdb.register('test_df_view', appended_data_df) #causes a known issue that will be fixed with next duckdb release https://github.com/duckdb/duckdb/pull/8738

    print('Data written to new table!')


