# SimpleRESTAPI
This is a simple REST API written in Python for testing API-Gateways like Tyk or Kong.

## Installation
This REST-API uses Flask and a SQLITE Database, to install the dependencies use the following pip command.:
````
 pip install flask flask-jsonpify flask-sqlalchemy flask-restful
````

## Usage
To Start the REST-API use the following Command:
````
python simpleRESTAPI.py
````
The API can be found at 127.0.0.1 on Port 5002. The following Requests are supported:
`GET /heroes` --> Show all heroes 
`GET /hero/<hero-id>`--> Show hero with id
`PUT /hero/add` --> Add a new hero with these POST parameters: `hero_id, hero_name, hero_enemy, hero_cityId`
`DELETE /hero/delete` --> delete a hero with a `hero_id` POST parameter
`PATCH /hero/change`--> change values of hero with these POST parameters: `hero_id, hero_name, hero_enemy, hero_cityId`

`GET /cities` --> Show all cities 
`PUT /city/add` --> Add a new city with these POST parameters: `city_id, city_name`
`DELETE /city/delete` --> delete a city with a `city_id` POST parameter


## the structure of the database
The database consists of two tables, the heroes table and the cities table. Those tables consist of the following columns and entries:
````
sqlite> select * from heroes;
id          name        enemy       cityId
----------  ----------  ----------  ----------
1           Daredevil   Kingpin     1
2           Spider-Man  Green Gobl  1

sqlite> select * from cities;
id          name
----------  ----------
1           New York
2           Gotham
````