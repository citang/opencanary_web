#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dbs.initdb import DBSession
from dbs.models.Host import Host
from sqlalchemy import desc
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.dialects.mysql import insert


class HostOp:

    def __init__(self):
        self.session = DBSession

    def insert_data(self, id, last_time, hostname, ip, status):
        insert_stmt = insert(Host). \
            values(id=id, last_time=last_time, hostname=hostname, ip=ip, status=status)

        on_conflict_stmt = insert_stmt.on_duplicate_key_update(
            last_time=last_time, status=status)
        try:
            self.session.execute(on_conflict_stmt)
            self.session.commit()
            return True
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def select_data(self):
        """查询在线主机"""
        try:
            host_online = self.session.query(Host).filter(
                Host.status == "online").order_by(desc(Host.last_time)).all()
            return host_online
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def select_allhost(self):
        """查询在线主机"""
        try:
            all_host = self.session.query(Host).order_by(desc(Host.last_time)).all()
            return all_host
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
