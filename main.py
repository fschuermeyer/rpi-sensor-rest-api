from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from tinydb import TinyDB

app = FastAPI(title="Weather Sensor API",version="1",contact={"name":"Felix Schürmeyer"})

data = TinyDB('./sensor.json')

@app.get("/", tags=['Overview'])
async def current_Data():
    current = {}

    for key in data.tables():
        current[key] = list(data.table(key).all())[-1]

    return current

@app.get("/sensor", tags=['Details'])
async def list_Sensors():
    return data.tables()

@app.get("/sensor/{sensor}", tags=['Details'])
async def read_Sensor(sensor: str):
    if sensor in data.tables():
        return data.table(sensor).all()

    return JSONResponse(content={"message": "Unfortunately no data could be found for the requested sensor, to get a selection of possible sensors call the route /sensor"}, status_code=404)
