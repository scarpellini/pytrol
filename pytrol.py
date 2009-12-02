#!/usr/bin/python
#
# Eduardo S. Scarpellini, <scarpellini@gmail.com> - 20091201
#
import certmaster.certmaster
import func.overlord.client as fc

def cmd_exec(clients, cmd):
	"""Remote command execution using FUNC (https://fedorahosted.org/func/).
	Returns a hash like {hostname: (exit-code, stdout, stderr)}."""

	client = fc.Client(clients)
	return client.command.run(cmd)


def get_hosts():
	"""Get available hosts which you can run remotely commands.
	Returns a array with hostnames."""

	cm = certmaster.certmaster.CertMaster()
	return cm.get_signed_certs("*")
