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


def aggregate_music(streaming_df, grouping):
    """Aggregate music history by grouping variable

    Args:
        streaming_df: dataframe with streaming data
        grouping: grouping variable (artistName, trackName)

    Returns:
        agg_df: dataframe aggregated
    """

    agg_df = streaming_df.groupby(grouping) \
                         .agg({grouping: 'count', 'msPlayed': 'sum'})  \
                         .rename(columns={grouping: 'count_played'})    \
                         .reset_index()

    agg_df['min_played'] = agg_df['msPlayed'] / 60000
    agg_df = agg_df.drop(columns=['msPlayed'])

    return agg_df


def map_track_to_artist(streaming_df):
    """Create mapping of track to artist using tracks in music history

    Args:
        streaming_df: dataframe with streaming data

    Returns:
        track_artist_dict: dictionary mapping tracks to artists
    """

    unique_tracks = streaming_df[['trackName', 'artistName']].drop_duplicates()

    tracklist = unique_tracks['trackName'].to_list()
    artistlist = unique_tracks['artistName'].to_list()

    track_artist_dict = dict(zip(tracklist, artistlist))

    return track_artist_dict
