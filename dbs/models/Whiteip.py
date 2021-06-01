#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String
from dbs.initdb import Base, engine


class Whiteip(Base):
    __tablename__ = 'Whiteip'
    src_host = Column(String(50), nullable=False, primary_key=True)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


"""
CREATE TABLE `Whiteip` (
	src_host VARCHAR(50) NOT NULL,
	PRIMARY KEY (src_host)
)

mysql> select * from Whiteip;
+----------------+
| src_host       |
+----------------+
| 172.18.222.170 |
+----------------+
1 row in set (0.01 sec)

"""
