## Commands Overview

Congredi, whether via the HTTP api, terminal client, or AMP peers,
issues atomic statements to other peers using a specific syntax
for each one. It uses the following:

* GET
* SET
* SEEK
* SEARCH



## GET & SET
Both `get` and `set` have a `permissions` boolean. When permisions is set to
`True`, we check that the author is in our trust model, and perform the same
command on our peers with `permissions` set to `False`.

They return the lifetime of the object.

0. Check signature of message
1. When permissions are set, check web-of-trust to that key

1. Check that we have the hash
2. When publishing a CHAIN, if we don't have previous
    queue a job to get it or delete it
2. Return results + peers where we got it + lifetime of data


### Recursions
0. Check their auth
1. Check what we have - return as iter
2. Ask peers - store & return to user
    * divide work between peers
    * work to the null-hash at the front of the tree
    * prove the content lines up end-to-end

## SEEK
Seek operates on a direction (`Forward` or `Backward`), an index (`current` or
the 32 bit hash), and a `count` integer. 

This returns a dictionary of objects and the users/routers who have them.

If permissions are set, it'll begin trying to obtain those hashes.

## SEARCH
Search relies on having the entire object.
`order` `offset` `count` `term`

This returns the larger resolved byte context, the object, and the
revision we searched from (say, 'defghj', which could be 6 commits ahead
of another server you search on).

1. If we have it, search it.
2. Else, use recursions to divvy work
3. return results
