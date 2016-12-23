## Design Problems

`PUBLISH, DEPLOY, SUBSCRIBE, MONITOR, PAST, CURRENT, FUTURE, SEARCH`

Congredi uses three classes of operations, unprivledged local,
privledged global, and privledged recursion.

Operations like `DEPLOY` and `MONITOR` need no permissions but
only ask about that local node, and don't have a guarentee of
persisting on it. If more important things need to be stored,
these ones will be removed first.

Operations like `PUBLISH` and `SUBSCRIBE`, however, use the
node's time and resources to ask around for things, and deploy
their results to multiple servers to get the word around.

Finally, operations like `PAST` `CURRENT` `FUTURE` and `SEARCH`
are dependant on having the full list of objects, and operate
by trying to split the work among other nodes.


Blobs will probably be zlib compressed ndiffs, even if I want them to be
unified diffs.

Example Operations:

MONITOR CACHE foobar HAS : <listobject>

DEPLOY CACHE foobar HAS <listobject>

