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
