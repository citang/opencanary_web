#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
  Author: pirogue 
  Purpose: 蜜罐主机状态表
  Site: http://pirogue.org 
  Created: 2018-10-30 20:34:58
"""

from sqlalchemy import Column, String, TIMESTAMP, UniqueConstraint
import sys

sys.path.append("..")
from dbs.initdb import Base, engine


class Host(Base):
    __tablename__ = 'Host'

    id = Column(String(50), primary_key=True)
    last_time = Column(TIMESTAMP, nullable=False)
    hostname = Column(String(50), nullable=False)
    ip = Column(String(50), nullable=False)
    status = Column(String(10), nullable=False)

    __table_args__ = (
        # 设置联合唯一索引
        UniqueConstraint('hostname', 'ip', name='uix_hostname_ip'),
        # 设置联合索引
        # Index('uix_hostname_ip', 'hostname', 'ip'),
    )


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


"""
CREATE TABLE `Host` (
	id VARCHAR(50) NOT NULL,
	last_time TIMESTAMP NOT NULL,
	hostname VARCHAR(50) NOT NULL,
	ip VARCHAR(50) NOT NULL,
	status VARCHAR(10) NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT uix_hostname_ip UNIQUE (hostname, ip)
)
"""
