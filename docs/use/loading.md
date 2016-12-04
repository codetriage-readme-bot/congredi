# Congredi - scaling clusters

We recommend using Traefik with a docker-swarm (on whatever provider you're using,
with docker-machine). This needs to serve up the static app, run a flask api,
and communicate with the protocol instances.

```
OnionBalance (tor nodes)
Traefik (scaling)
    nginx (angular)
    flask (jwt)
        redis (read only)
        twisted (p2p)
            redis (read/write)
```