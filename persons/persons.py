from fastapi import FastAPI, Depends

persons = FastAPI()


async def properties(x: int, y: int):
    return {"from": x, "to": y}


data = [
    {"name": "Alik", "age": 28},
    {"name": "Frank", "age": 24},
    {"name": "Alice", "age": 19},
]


@persons.get('/persons/')
async def get_persons(params: dict = Depends(properties)):
    return data[params['from']:params['to']]
