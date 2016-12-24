# "CACHE RANK"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash of previous lookup rank hash
		rank info
		datestring (beginning rank date)
		datestring (expiry date)
		32b sig (signature of the above)
```