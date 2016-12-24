Congredi deals with a hash-value structure and a directed graph structure,
with both redis and neo4j.

Blobs will probably be zlib compressed ndiffs, even if I want them to be
unified diffs.


```
structures & query language (i.e. PUBLISH CACHE HAS <object>)
CACHE
COMPUTATION
HISTORY
IDENTITY
CONTENT
SETTING
```

```
users -> agg -> polls/votes/trees -> commits -> chunks

"directed graph":{
	"user":{
		"trusts":"users",
		"follows":"repos"
	"repo":"commits"
```
