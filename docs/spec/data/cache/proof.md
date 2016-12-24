# "CACHE PROOF"

A router (identified by their public key) can prove they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash (of content they have)
		32b nonce (as a challenge)
		32b result (hash of adding the nonce to the selected bytes)
		int position (place to grab bytes from)
		datestring (time they proved that nonce)
		32b sig (signature of the above)
```