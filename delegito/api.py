#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response
from tokens import checker

gate = checker('password')


app = Flask('Delegito')
@app.errorhandler(404)
def not_found(error):
	print('route: error')
	return make_response("Read the Congredi documentation", 404)

@app.route('/',methods=['GET','POST'])
def jwt_index():
    if request.method == 'GET':
        return "Welcome to Congredi."
    elif request.method == 'POST':
        pgpkey = request.get_json()['pubkey']
        return gate.make(fingerprint)
"""
@app.route('/gis/',methods=['GET'])
def gis():
    pass
@app.route('/gis/loc/<loc>/',methods=['GET'])
def jwt_starter(loc):
    pass
@app.route('/sync/',methods=['GET'])
def jwt_starter():
    pass
@app.route('/pgp/',methods=['GET'])
def jwt_starter():
    pass
@app.route('/jwt/',methods=['GET'])
def jwt_starter():
    pass
@app.route('/data/<hash>',methods=['GET','POST','DELETE'])
@app.route('/index/<hash>',methods=['GET','POST'])
@app.route('/gis/<l>/<b>/<r>/<t>',methods=['GET','POST'])
@app.route('/search',methods=['GET','POST'])
@app.route('/<hash>/vote',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
"""