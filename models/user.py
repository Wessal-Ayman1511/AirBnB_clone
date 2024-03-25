#!/usr/bin/python3
"""
Module user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user info
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
