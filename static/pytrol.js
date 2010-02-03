/*global document, RegExp*/

function selectUnselect(selected) {
	var hostname, i;
	selected = !selected;
	hostname = document.getElementsByName("hostname");
	for (i in hostname) {
		if (hostname.hasOwnProperty(i)) {
			hostname[i].checked = selected;
		}
	}
	hostname = i = null;
	return selected;
}

function selectRegex(pattern) {
	var r, hostname, i;
	function FakeRegExp() {
		this.test = function () {
			return false;
		};
	}
	if (pattern === "") {
		r = new FakeRegExp();
	} else {
		r = new RegExp(pattern, "i");
	}
	hostname = document.getElementsByName("hostname");
	for (i in hostname) {
		if (hostname.hasOwnProperty(i)) {
			hostname[i].checked = r.test(hostname[i].value);
		}
	}
	r = hostname = i = null;
}
