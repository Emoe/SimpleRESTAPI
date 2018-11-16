from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///heroes.db')
app = Flask(__name__)
api = Api(app)

class getAllHeroes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from heroes")
        result = {'Heroes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class getHero(Resource):
    def get(self, hero_id):
        conn = db_connect.connect()
        query = conn.execute("select * from heroes where  id=%d "  %int(hero_id))
        result = {'Hero': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class addHero(Resource):
    def put(self):
        conn = db_connect.connect()
        hero_id = request.form['hero_id']
        hero_name = request.form['hero_name']
        hero_enemy = request.form['hero_enemy']
        hero_cityId = request.form['hero_cityId']
        query = conn.execute("insert into heroes (id, name, enemy, cityId)  values (%d, '%s', '%s', %d)"  %(int(hero_id),str(hero_name),str(hero_enemy),int(hero_cityId)))
        return {'result': 1}

class changeHero(Resource):
    def patch(self):
        conn = db_connect.connect()
        hero_id = request.form['hero_id']
        hero_name = request.form['hero_name']
        hero_enemy = request.form['hero_enemy']
        hero_cityId = request.form['hero_cityId']
        query = conn.execute("update heroes set id=%d, name='%s', enemy='%s', cityId=%d where id=%d"  %(int(hero_id),str(hero_name),str(hero_enemy),int(hero_cityId),int(hero_id)))
        return {'result': 1}

class deleteHero(Resource):
    def delete(self):
        conn = db_connect.connect()
        heroe_id = request.form['hero_id']
        query = conn.execute("delete from heroes where id=%d" %int(heroe_id))
        return {'result': 1}

class getCities(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from cities")
        result = {'Cities': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class addCity(Resource):
    def put(self):
        conn = db_connect.connect()
        city_id = request.form['city_id']
        city_name = request.form['city_name']
        query = conn.execute("insert into cities (id, name)  values (%d, '%s')"  %(int(city_id),str(city_name)))
        return {'result': 1}


class deleteCity(Resource):
    def delete(self):
        conn = db_connect.connect()
        heroe_id = request.form['city_id']
        query = conn.execute("delete from cities where id=%d" %int(city_id))
        return {'result': 1}

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(getAllHeroes, '/heroes')
api.add_resource(getHero,'/hero/<hero_id>')
api.add_resource(addHero, '/hero/add',methods=['PUT'])
api.add_resource(changeHero, '/hero/change',methods=['PATCH'])
api.add_resource(deleteHero, '/hero/delete',methods=['DELETE','POST'])

api.add_resource(getCities, '/cities')
api.add_resource(addCity, '/city/add',methods=['PUT'])
api.add_resource(deleteCity, '/city/delete',methods=['DELETE','POST'])

if __name__ == '__main__':
     app.run(port='5002')