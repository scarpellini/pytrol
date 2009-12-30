#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Eduardo S. Scarpellini, <scarpellini@gmail.com>
#
#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing,
#   software distributed under the License is distributed on an
#   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied.  See the License for the
#   specific language governing permissions and limitations
#   under the License.

import web
import pytrol

templates_dir = "templates/"

urls = (
	"/(?:html/)?(?:index(?:\.html?)?)?", "index",
	"/html/cmd_exec_form(?:\.html?)?", "cmd_exec",
	"/html/cmd_exec(?:\.html?)?", "cmd_exec",
)


app = web.application(urls, globals())


class index:
	def GET(self):
		"Redirects to index.html"

		return web.seeother('/static/index.html')


class cmd_exec:
	def GET(self):
		"""Renders the HTML Form.
		Take a look at /templates/ and /static/ directories"""

		render = web.template.render(templates_dir)

		hosts = sorted(pytrol.get_hosts())
		return render.cmd_exec_form(hosts)

	def POST(self):
		"""Process Form POST and renders the result.
		Take a look at /templates/ and /static/ directories"""

		render = web.template.render(templates_dir)

		input = web.input(hostname=[])

		if not input.cmd:
			return web.seeother('/static/error.html')

		if not input.hostname:
			return web.seeother('/static/error.html')

		exec_returns = pytrol.cmd_exec(";".join(input.hostname), input.cmd)

		return render.cmd_exec_return(input.cmd, exec_returns)

# Uncomment the line bellow if you intend to use apache + mod_fastcgi.
# Also, see an example of configuration in examples/apache.conf
#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

if __name__ == "__main__":
	app.run()
