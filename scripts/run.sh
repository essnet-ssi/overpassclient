sudo docker build -t overpassclient -f docker/Dockerfile . && sudo docker run -ti  -v "/home/pbeyens/git/overpassclient/storage:/opt/hbits/overpassclient/storage" --rm overpassclient bash
