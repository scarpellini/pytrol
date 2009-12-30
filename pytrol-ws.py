#!/usr/bin/python
#
# Eduardo S. Scarpellini, <scarpellini@gmail.com> - 20091203
#
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
