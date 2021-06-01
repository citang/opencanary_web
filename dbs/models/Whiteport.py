#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship, backref
# import sys
# sys.path.append("..")
from dbs.initdb import Base, engine, DBSession


class Whiteport(Base):
    __tablename__ = 'Whiteport'
    dst_port = Column(Integer, nullable=False, primary_key=True)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
