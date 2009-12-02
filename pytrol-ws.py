#!/usr/bin/python
#
# Eduardo S. Scarpellini, <scarpellini@gmail.com> - 20091201
#
import web
import pytrol

urls = (
	"/", "index",
	"/get_hosts", "get_avail_hosts"
)

app = web.application(urls, globals())

class index:
	def GET(self):
		return "Use: \n * get_hosts \n * exec_cmd (implementacao)"

class get_avail_hosts:
	def GET(self):
		render = web.template.render("templates/")

		hosts = sorted(pytrol.get_hosts())
		return render.hosts(hosts)


if __name__ == "__main__":
	app.run()
