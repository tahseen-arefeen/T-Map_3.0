from os import *
from pandas import DataFrame
from requests import request
from random import *
import logging

def API_to_JSON (url):
    """enter credentials into MBTA and retrieve API data

    Args:
        url (str): url for desired data

    Returns:
        df: formatted dataframe of API data
    """
    try:
        # retrieves and formats API data to json
        bearer_token = environ.get('a2d93c719b8349d0905b19cc9e250e02')
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        response = request("GET", url, headers=headers).json()

        df = DataFrame(response['data'])
        return df
    
    except Exception:
        #insert logging
        print()
        print(f"{url} is offline")
        print("check connection")
        print()

def FindTrainValue (tf, sf, attr, train_id):
    """_summary_

    Args:
        tf (_type_): _description_
        sf (_type_): _description_
        attr (_type_): _description_
        train_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    tf_index = int((tf[tf["id"]==train_id].index.values))
    
    if attr == "stop":
        relationships = tf.iloc[tf_index,3]
        stop = relationships.get("stop")
    
        data = stop.get("data")
        stop_id = data.get("id")
    
        stop_index = int((sf[sf["id"]==stop_id].index.values))
        attributes = sf.iloc[stop_index,0]

        platform_name = attributes.get('name')
    
        return platform_name, stop_id
    
    elif attr in ['direction_id', 'current_status', 'latitude', 'longitude']:
        attributes = tf.iloc[tf_index,0]
        
        value = attributes.get(attr)
        
        return value
    
    else:
        #logging
        print("invalid attr")

def FindStationValue (sf, attr, station_id):
    
    sf_index = int((sf[sf["id"]==station_id].index.values))
    
    if attr in ["longitude", "latitude"]:
        attributes = sf.iloc[sf_index,0]
        
        value = attributes.get(attr)
        
        return value
    
    else:
        #logging
        print("invalid attr")

#Test

sf = API_to_JSON("https://api-v3.mbta.com/stops")
tf = API_to_JSON("https://api-v3.mbta.com/vehicles")