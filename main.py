from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from basepolygon_class import GoalPolygon
from models import SimpleDB

app = FastAPI()

app_db = SimpleDB()


class MpBase(BaseModel):
    osm_name: Optional[str]
    response_keys: Optional[list]


class DbCommiter(BaseModel):
    nested_request: dict


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def root():
    return {"message": "mp geodata app"}


@app.put("/site/{name}")
async def creat_from_place(name: str, data: MpBase):
    global app_db
    gp = GoalPolygon(data.osm_name)
    gp.name = name

    data_new = {
        app_db.root: {
            "site": {
                name: gp
            }
        }
    }

    app_db.update_data(data_new)
    ans = {
        'url': f'/site/{name}'
    }

    if data.response_keys:
        for k in data.response_keys:
            ans |= {
                k: getattr(gp, k)
            }
    return ans


@app.get("/site/{name}/{attr}")
async def get_site_attr(name, attr):
    global app_db
    gp = app_db.DB[app_db.root]["site"][name]
    return {attr: getattr(gp, attr)}


@app.put("/db/{name}")
async def db_commit(name: str, data: DbCommiter):
    global app_db

    data_new = {
        app_db.root: {
            name: data.nested_request
        }
    }

    app_db.update_data(data_new)
    return data_new