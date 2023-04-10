"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-cgpqvi8u9tun42u513ig-a.oregon-postgres.render.com",
    database="todo_betsol",
    user="todo_betsol_user",
    password="OuGS4HKCPCEXQuLt9Djhh7EhkGwr3KjI")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
