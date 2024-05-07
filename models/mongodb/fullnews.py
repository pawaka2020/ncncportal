# models/mongodb/fullnews.py

from .db import db

class FullNews:
    # Constructor and field definition
    def __init__(self, name):
        self.name = name