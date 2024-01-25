from fastapi import FastAPI, Depends, Request
from fastapi.responses import Response

persons = FastAPI()


def credentials(request):
    dct = request.cookies
    try:
        return dct['api_key']
    except KeyError:
        return None


data = [
    {"name": "Alik", "age": 28},
    {"name": "Frank", "age": 24},
    {"name": "Alice", "age": 19},
]


class Properties:
    # def __init__(self, x: int, y: int):
    #     self.x = x
    #     self.y = y
    def __call__(self, x: int, y: int):
        self.x = x
        self.y = y
        return self


@persons.get('/persons/')
async def get_persons(params: Properties = Depends(Properties())):
    print(Properties)
    return data[params.x: params.y]


@persons.get('/')
async def index(request: Request, response: Response):
    response.set_cookie(key="user", value="admin")
    response.set_cookie(key="api_key", value="abracadabra")
    return {"message": "Home Page"}

# @persons.get('/persons/')
# async def get_persons(request: Request):
#     key = credentials(request)
#     if key is None:
#         return {"message": "API key not validated"}
#     else:
#         return data
