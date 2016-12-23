* twisted nodes
* redis nodes / api key to hosted redis
* neo4j nodes / api key to hosted neo4j

docker run -it -d -p 4400:4400 --name="actions" --restart="always" -v $(pwd):/root ericoflondon/congredi
docker --verbose build --tag ide .
python main/amp.py
python -m congredi
python -m congredi peer
