network packets (twisted/tornado)
p2p/dht libraries

```
PSC:
    relationmap, searching over shard, incentive to keep up-to-date, ranking
SHA: markdown compressed with gzip signed with ec
    - sig, ent, time, nonce
        - piece (hash+sig)
            - peer (signed hash, nonce?, date?)
    keep/delete votes ( O(1) nettrust)
VER
    bookmark-head (hash + sig + user)
    diffs (hash + sig + author)
    - subscribers who actually value that version (or children)
ENT
    - sig-denounces-last
    vers, subs, votes, groups
STV
    - sig-adds-all-known?
    person, versions, ranking, signature
AGR
    - aggregation-adds-all-group
    - group-membership-current
    STV aggregations
    membership lists


