# "CACHE SEEN"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash of previous lookup hash
		datestring last seen
		datestring (beginning storage date)
		datestring (expiry date)
		32b sig (signature of the above)
```