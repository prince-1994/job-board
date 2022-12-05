import configparser
import os

from fastapi import FastAPI
import psycopg2
from app.usecases import UserUsecases
from app.repositories import UserRepository

env_file = os.environ.get('env_file')
config = configparser.ConfigParser()
config.read(env_file)
connection = psycopg2.connect(user=config["DB"]["user"],
                                  password=config["DB"]["password"],
                                  host=config["DB"]["host"],
                                  port=config["DB"]["port"],
                                  database=config["DB"]["database"])

app = FastAPI()
user_repo = UserRepository(conn=connection)
user_usecases = UserUsecases(user_repo=user_repo)

@app.post("/users")
def create_new_user(email: str):
    user_repo.create(email=email)

@app.get("/users")
def get_users():
    user_repo.get_all()
    