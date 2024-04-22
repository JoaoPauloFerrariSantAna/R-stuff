#!/bin/awk -f

BEGIN {
	print "Writing logs into \"/tmp/\"."
}

{
	passed_request = "/tmp/access.log"
	error_request = "/tmp/error.log"
}

{
	ip		= $1
	time	= gensub(/^\[/, "", "g", $4) # 'cause it starts with [
	method 	= gensub(/^"/, "", "g", $6)  # 'cause it starts with "
	page	= $7
	status	= $9
	bytes_returned = $10
} 

/200/ {
	printf("ip %s: requested %s for %s (%d bytes) at %s. Got %d\n", ip, method, page, bytes_returned, time, status) > passed_request
	ok_request++
}

/404/ {
	printf("ip %s tried to access file \"%s\" without permission (if file exist) at %s\n", ip, page, time) > error_request
	bad_request++
}

END {
	print "Total of good requests (OK):",ok_request
	print "Total of bad requests (ERROR):",bad_request
}
