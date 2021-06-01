#!/usr/bin/env python
# coding:utf-8


from datetime import datetime
from sqlalchemy import Column, String, Integer, TIMESTAMP
from dbs.initdb import Base, engine


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(32), nullable=False)
    create_time = Column(TIMESTAMP, default=datetime.now)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


'''
    CREATE TABLE `User` (
	id INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(32) NOT NULL,
	create_time TIMESTAMP NULL,
	PRIMARY KEY (id)
    )
INSERT INTO `User` (username, password, create_time) VALUES (%(username)s, %(password)s, %(create_time)s)
{'username': 'admin', 'password': '21232f297a57a5a743894a0e4a801fc3', 'create_time': datetime.datetime(2018, 8, 7, 16, 52, 44, 676617)}
'''
