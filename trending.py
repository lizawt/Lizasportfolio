import pandas as pd
from datetime import datetime 
import requests
import urllib 
from flask import request 
import json 
from requests.exceptions import ConnectionError 
import ast


def get_trending(): 
    qp = hashabledict(request.args)
    return {"data": _get_trending(qp)}

def _get_trending(qp): 

    media = qp.get("media") or "movie" 
    timewindow = qp.get("timewindow") or 'day'

    path="https://api.themoviedb.org/3/"
    find = "trending"
    parameter_dict = {'api_key': api} 
    
    get_url = path+find+'/'+media+'/'+timewindow+'?' 
    + urllib.parse.urlencode(parameter_dict) 

    try: 
        r = requests.get(get_url, timeout=1) 
    except ConnectionError as e:
        print(e)
        r = None 

    if (media=='tv'):

        if r:
            response_dict = json.loads(r.text)
            df = pd.json_normalize(response_dict['results'], sep="_")
        else:
            result = {}

        df.poster_path = img_url + df.poster_path
        df = df.sort_values('Popularity', ascending=False)

        df.profile_path = img_url + df.profile_path
        df = df[COLS]
        df = df.merge(df_p, on='id', how='left')
        df = df.sort_values('Popularity', ascending=False)

    result = df.head(10).to_dict(orient='records')
    return result
