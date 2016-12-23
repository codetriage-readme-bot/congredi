# Extending / Scaling / UI-ing

Congredi has no workable client. To make one, you might try:

* Traefik with docker-swarm serving docker containers
* nginx-served angular app (jwt, openpgp)


# Angular UI designs
> Think Hoodiecrow/mailvelope/whiteout-io/mailpile

```
# .when('/settings' etc
/#/self/settings
/#/node/admin
/#/search
/#/edit
/#/vote

/api/search?offset=0?limit=0
/api/auth/jwt
/api/docs/new
/api/docs/:id/edit
/api/vote/new
/api/vote/:id/cast
/api/orgs/new
/api/orgs/:id/
```

## Edits to Angular UI js

1. run `gulp clean`
2. make edits to `/js/`
    * if you change a library call, change its `.test.js`
    * if you change a controller or otherwise, change its `view`
3. run `gulp` (should run tests as well)
