from flask import Flask, request, jsonify
from flask_cors import CORS
from model.user import user
from validation.validatior import *
from dotenv import load_dotenv
from model.movie import movie
import jwt
import os
import traceback
import logging

app = Flask(__name__)
CORS(app)

# Retrieve all movies


@app.route('/movies', methods=['GET'])
def getAllMovies():
    try:
        jsonMovies = movie.getAllMovies()
        output = {"Movies": jsonMovies}
        return jsonify(output), 200
    except Exception as err:
        traceback.print_exc()
        output = {"Message": "Internal Server Error"}
        return jsonify(output), 500

# Retrieve movies by movie ID


@app.route('/movies/byid/<int:movieid>', methods=['GET'])
def getMoviesByID(movieid):
    try:
        jsonMovies = movie.getMoviesByID(movieid)
        output = {"Movies": jsonMovies}
        return jsonify(output), 200
    except Exception as err:
        traceback.print_exc()
        output = {"Message": "Internal Server Error"}
        return jsonify(output), 500

# delete movie


@app.route('/movies/<int:movieid>', methods=['DELETE'])
@login_required
def deleteMovie(movieid):
    try:
        jsonMovieBody = request.json
        rows = movie.deleteMovie(movieid)
        msg = str(rows) + " row(s) deleted"
        output = {"Message": msg}
        return jsonify(output), 200
    except Exception as err:
        traceback.print_exc()
        output = {"Message": "Internal Server Error"}
        return jsonify(output), 500

# testing

load_dotenv()

logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
#this is to enable logging, the logs are stored in the record.log



@app.route('/', methods=['GET'])
def hello():
    return {'message': 'This is a response from the server 😀😃😄😁😆😅😂🤣'}, 200


@app.errorhandler(404)
def not_found(e):
    return {'error': 'Resource {} {} Not Found!'.format(request.method, request.url)}, 404

@app.route('/register', methods=['POST'])
def Insertuser():
    app.logger.info(request.json)
    #this will log the data inside the payload from the request in the JSON file
    try:
        jsonUserBody=request.json
        rows=user.Insertuser(jsonUserBody)
        msg=str(rows)+ " row(s) inserted"
        output= {"Message":msg}

        return jsonify(output), 201
    except Exception as err:
        traceback.print_exc()
        output={"Message":"Internal Server error"}
        return jsonify(output),500

@app.route('/users/login', methods=['POST'])
def loginUser():
    try:
        jsonUserBody=request.json
        token=user.login(jsonUserBody)
        msg={"JWT":token}
        return jsonify(msg), 200
    except Exception as err:
        traceback.print_exc()
        output={"Message":"Internal Server error"}
        return jsonify(output),500

@app.route("/add_movie", methods=["POST"])
@login_required
def AddOneMovie():
    app.logger.info(request.json)
    #this will log the data inside the payload from the request in the JSON file
    try:
        jsonMovieBody=request.json
        howmanyrows=movie.AddOneMovie(jsonMovieBody)
        info=str(howmanyrows)+" row(s) inserted"
        output={"Message": info}
        return jsonify(output), 201

    except Exception:
        traceback.print_exc()
        output={"Message": "Internal Server Error"}
        return jsonify(output), 500

@app.route("/update_movie/<int:id>", methods=["PUT"])
@login_required
def UpdateOneMovie(id):
    try:
        jsonMovieBody=request.json
        howmanyrows=movie.UpdateOneMovie(jsonMovieBody,id);
        info=str(howmanyrows)+ " row(s) updated"
        output={"Message": info}
        return jsonify(output), 200

    except Exception:
        traceback.print_exc()
        output={"Message": "Internal Server Error"}
        return jsonify(output), 500




if __name__ == "__main__":
    app.run(debug=True)
