How to run:
1. Run docker network create -d bridge --subnet 192.168.0.0/24 --gateway {{ip of your pc}} dockernet
2. Run docker-compose up --build
3. Connect to http://{{ip of your pc}}:8000

How to fill db:
1. Run docker exec -it food_buzz_web_1 python manage.py shell
2. Insert into the console code from fill_database.py
