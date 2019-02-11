# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class BookModel(Base):
    __tablename__ = 'bookmodel'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    url = Column(String(128), unique=True)
    image_url = Column(String(128), unique=True)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, url=None, image_url=None, date=None):
        self.title = title
        self.body = body
        self.url = url
        self.image_url = image_url
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)


class StudyModel(Base):
    __tablename__ = "studymodel"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, primary_key=True)
    user_id = Column(String(128), unique=True)
    study_time = Column(String(128), unique=True)

    def __init__(self, book_id=None, user_id=None, study_time=None):
        self.book_id = book_id
        self.user_id = user_id
        self.study_time = study_time

    def __repr__(self):
        return '<UserID %r>' % (self.user_id)
