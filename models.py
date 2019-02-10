# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class UserModel(Base):
    __tablename__ = 'usermodel'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    admin_id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, user_id=None, name=None, admin_id=None, date=None):
        self.user_id = user_id
        self.name = name
        self.admin_id = admin_id
        self.date = date

    def __repr__(self):
        return '<name %r>' % (self.name)