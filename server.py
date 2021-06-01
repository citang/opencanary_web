#!/usr/bin/env python
# coding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from util.task import check_scheduler

from application import settings
from url import url
from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

if __name__ == '__main__':
    check_scheduler()
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=url, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('Server is running on http://127.0.0.1:%s/' % options.port)
    tornado.ioloop.IOLoop.instance().start()

