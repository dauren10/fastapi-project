from fastapi import FastAPI
import requests
import http3
import psycopg2
import redis
import pymongo
import strawberry
import typing
from strawberry.asgi import GraphQL
from pymongo import MongoClient
from bson.objectid import ObjectId
from celery import Celery
from .tasks import add
client = http3.AsyncClient()
app = FastAPI()



@app.get("/")
async def read_main():
    result = add.delay(4,4)
    return {"msg": "Hello World"}


