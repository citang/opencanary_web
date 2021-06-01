#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        # Contains user found in previous auth
        self.render('index.html')

    def post(self):
    # Contains user found in previous auth
      self.render('index.html')