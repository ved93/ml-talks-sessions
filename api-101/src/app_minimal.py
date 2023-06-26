
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

import random


app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return JSONResponse({"status": 1})

@app.get("/get_random_number")
async def generate_random_number():
    return JSONResponse(random.randint(1, 100))

 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1122)
 
# uvicorn app:app --host 0.0.0.0 --port 1122
