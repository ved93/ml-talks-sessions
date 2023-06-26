import json

import numpy as np
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

# redis_client = redis.Redis("172.22.74.203", 6384)

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return JSONResponse({"status": 1})


import random
from datetime import datetime

 

@app.get("/kridaai/playerlist")
def query_data(query: str):
    short_player_list = player_list[:30]
    retreival_prompt = f"""
    Consider the following data about players in json format-
    '''
    {json.dumps(short_player_list)}
    '''
    Based on the above data, find players that match the following query -  
    
    '''
    {query}
    '''
    Your response should be in a similar json format with only entries for players who match the query. If not players are found, retun an empty json. The maximum number of     players you can return is 5.

    """
    messages = [{"role": "user", "content": f"{retreival_prompt}"}]
    res = chat_completion(messages)
    player_ls = json.loads(res["choices"][0]["message"]["content"])
    return JSONResponse(content={"player_info": player_ls})




@app.on_event("startup")
async def startup_event():
    # Load the model during startup
    global player_list

    # my_model = MyModel()
    # df_userteam_score = pd.read_parquet("/home/centos/wtrf/df_userteam_score.parquet")

    player_list = pickle.load(
        open("/Users/ved.prakash/Downloads/player_data.pkl", "rb")
    )

    # winning_zone_threshold = df_userteam_score.shape[0] * 0.62


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1122)

    # uvicorn src.app:app --reload --port 1345

    # uvicorn app:app --host 18.116.117.105 --port 1346
    # uvicorn app:app --reload  --host 172.22.74.203 --port 1345

# uvicorn app:app --host 0.0.0.0 --port 1346
