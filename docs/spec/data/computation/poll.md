# "COMPUTATION POLL"

An org can compute a poll (public vote) together, and publish their findings
in a poll object. Computation fields are byzantian problems, so consensus
needs reaching. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
32b hash of original poll spec :
	32b lookup hash of bellow :
		32b hash (of polls we do have)
		list:
			user's latest poll on this
		result object
		datestring (date)
		32b sig (signature of the above)
		32b threshsig
```