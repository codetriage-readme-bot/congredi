#### PUBLISH - privledged set
`PUBLISH IDENTITY USER <key><previousfingerprint><sigbyprevious>`
Differences:
2. Fail if we don't have the key, publish operations are privledged,
	Ask for permission before using them!
2.5. Check if a trust-path exists from this node's users to that key. ErrBack.

