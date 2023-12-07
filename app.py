from flask import Flask, jsonify, request, after_this_request
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route("/people")
def people():
    status_code=200
    try:
        r = requests.get('https://swapi.dev/api/people')
        if r.status_code == 200:
            print('Success!')
            people=json.loads(r.text)['results']
            return jsonify(people) ,status_code
        elif r.status_code == 404:
            print('Not Found.')
            status_code=404
            return jsonify({"error":"Not Found"}),status_code
    except Exception as e:
        status_code=500
        error={"error":e}
        return f"{e}",status_code


@app.route("/people/<name>")
def people_by_name(name=None):
    status_code=200
    try:
        r = requests.get(f'https://swapi.dev/api/people/?search={name}')
        if r.status_code == 200:
            print('Success!')
            person=json.loads(r.text)
            return jsonify(person),status_code
        elif r.status_code == 404:
            print('Not Found.')
            status_code=404
            return jsonify({"error":"Not Found"}),status_code
    except Exception as e:
        status_code=500
        error={"error":e}
        return f"{e}",status_code


@app.route("/movies")
def movies():
    status_code=200
    try:
        r =  requests.get('https://swapi.dev/api/films')
        if r.status_code == 200:
            print('Success!')
            movies=json.loads(r.text)['results']
            return jsonify(movies) ,status_code
        elif r.status_code == 404:
            print('Not Found.')
            status_code=404
            return jsonify({"error":"Not Found"}),status_code
    except Exception as e:
        status_code=500
        error={"error":e}
        return f"{e}",status_code


@app.route("/movies/<id>")
def movies_id(id=None):
    status_code=200
    try:
        r = requests.get(f'https://swapi.dev/api/films/{id}')
        if r.status_code == 200:
            print('Success!')
            movie=json.loads(r.text)
            actors=[]
            for character in movie['characters']:
                character_resp = requests.get(character)
                name=json.loads(character_resp.text)["name"]
                actors.append({"name":name})

            movie["actors"]=actors
            return jsonify(movie),status_code
        elif r.status_code == 404:
            print('Not Found.')
            status_code=404
            return jsonify({"error":"Not Found"}),status_code
    except Exception as e:
        status_code=500
        error={"error":e}
        return f"{e}",status_code
    

# when you run with py falskapp, set debug to False for production
if __name__ =='__main__':
   app.run(debug=False,host="0.0.0.0")




    