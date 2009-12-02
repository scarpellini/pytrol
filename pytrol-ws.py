#!/usr/bin/python
#
# Eduardo S. Scarpellini, <scarpellini@gmail.com> - 20091201
#
import web
import pytrol

templates_dir = "templates/"

urls = (
	"/", "index",
	"/html/cmd_exec_form(?:\.html?)?", "cmd_exec",
	"/html/cmd_exec(?:\.html?)?", "cmd_exec",
	"/rest/get_hosts", "get_avail_hosts"
)


app = web.application(urls, globals())


class index:
	def GET(self):
		return "Use: \n * get_hosts \n * exec_cmd (implementacao)"


class get_avail_hosts:
	def GET(self):
		return "\n".join(pytrol.get_hosts())


class cmd_exec:
	def GET(self):
		render = web.template.render(templates_dir)

		hosts = sorted(pytrol.get_hosts())
		return render.cmd_exec_form(hosts)

	def POST(self):
		render = web.template.render(templates_dir)

		input = web.input(hostname=[])

		exec_returns = pytrol.cmd_exec(";".join(input.hostname), input.cmd)

		return render.cmd_exec_return(exec_returns)


if __name__ == "__main__":
	app.run()
