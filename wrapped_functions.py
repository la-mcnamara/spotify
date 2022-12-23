import pandas as pd
import os

def read_spotify_json_data(path):
    """Read JSON data from Spotify download

    Args:
        path (str): file path where downloaded data is stored

    Returns:
        json_df_dict (dict): dictionary with file names as keys and dataframes as values
    """

    dir_list = os.listdir(path)
    print(f"Files found in path: {dir_list}")

    # identify json files out of downloaded files
    json_list = [f for f in dir_list if f[-5:] == '.json']

    # create dictionary to store data
    json_df_dict = {}

    # read JSON file as series or dataframe
    for json in json_list:
        filename = json[:-5].lower()
        pathfile = f"{path}/{json}"

        try:
            json_df_dict[filename] = pd.read_json(pathfile)

        except ValueError:
            json_df_dict[filename] = pd.read_json(pathfile, typ='series')

    return json_df_dict
