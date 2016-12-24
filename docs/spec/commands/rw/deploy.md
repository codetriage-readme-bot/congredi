#### DEPLOY - unprivledged set
`DEPLOY IDENTITY USER <key><previousfingerprint><sigbyprevious>`
1. Check validity of sig against given key.
2. Request previous key if we don't have it.
3. Add previous key, new key, and query proof to DB, expire (lim)
4. Return certification that it'll be in there, barring space considerations.

