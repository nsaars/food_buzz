1. Run docker network create -d bridge --subnet 192.168.0.0/24 --gateway {{ip of your pc}} dockernet
2. Run docker-compose up --build
3. Connect to http://{{ip of your pc}}:8000
