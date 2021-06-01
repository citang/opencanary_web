#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')  # 这个地方可以写域名
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.set_header("Server", "Apache-Coyote/1.1")

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('index.html')
        elif status_code == 500:
            self.render('index.html')
        else:
            self.write('error:' + str(status_code))
