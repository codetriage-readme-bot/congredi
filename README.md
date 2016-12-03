# Congredi
> a BASE representation-of-law-via-cryptography protocol

Congredi is a Twisted protocol for groups to representationally agree on things.

It behaves like gittorrent and gitchain, but with more onion-like proxying,
incentives to prove they stored a git object (i.e. filecoin), and ranking of which git objects
& trees they want to keep around.

* Requirements: Python Cryptography (Fernet & EC), Twisted
* Addons: Stem, Flask, PyJWT

Hopefully, with any luck, the files written here will be well-documented, unit
tested (lint + nose2?), & cohesive/decoupled.

I leave design of a perusing/issuing client to you. I tried angular with routes,
as well as traefik + nginx/flask. Others have made things with QT?

```
	.when('/', {
	.when('/auth', {
	.when('/settings', {
	.when('/search', {
	.when('/create', {
	.when('/edit', {
	.when('/points:id', {
	.otherwise({
		redirectTo: '/'
	});
```

**NOTE. Code partially from the regular [Congredi](//github.com/thetoxicarcade/congredi) repo**