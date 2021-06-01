#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers.base import BaseHandler
from service.hostservice import hostonline


# @jwtauth
class HelloHandler(BaseHandler):
    def get(self):
        print(hostonline())
        # self.write(str(hostonline()))
        self.write("ok")

        # Contains user found in previous auth
        # if self.request.headers.get('Authorization'):
        #     self.write('ok')
