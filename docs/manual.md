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


#### DEPLOY - unprivledged set
`DEPLOY IDENTITY USER <key><previousfingerprint><sigbyprevious>`
1. Check validity of sig against given key.
2. Request previous key if we don't have it.
3. Add previous key, new key, and query proof to DB, expire (lim)
4. Return certification that it'll be in there, barring space considerations.

#### PUBLISH - privledged set
`PUBLISH IDENTITY USER <key><previousfingerprint><sigbyprevious>`
Differences:
2. Fail if we don't have the key, publish operations are privledged,
	Ask for permission before using them!
2.5. Check if a trust-path exists from this node's users to that key. ErrBack.

#### MONITOR - unprivledged get
`MONITOR CACHE <hash> WANTS`

1. Check that we know about the hash
2. Return results
3. include where we got it from so they can do their research

#### SUBSCRIBE - privledged get
1. Check what we know about it
2. Check what peers know about it
3. Return results, and where we got it from
4. Update their rendesvous peers if they want to know more

#### PAST
1. Check the user permissions
2. Check all the info we have, send this to peers to help them
3. Try to get to a null-beginning hash of the tree
4. Prove that the content lines up end to end
5. Return the content

#### FUTURE
Same as above

#### CURRENT
1. Check the info we have
2. Check where we got it from
3. Check our peers
4. Return our results

#### SEARCH
`SEARCH <> ORDER <> OFFSET <> COUNT <> TERM <>`
1. if we have the full diff, search it
2. if we don't, request PAST/FUTURE queries
3. return ranked results

Blobs will probably be zlib compressed ndiffs, even if I want them to be
unified diffs.

Example Operations:

MONITOR CACHE foobar HAS : <listobject>

DEPLOY CACHE foobar HAS <listobject>

