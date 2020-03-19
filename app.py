#!/usr/bin/python3
"""API para casos de corona virus."""
import json, os, datetime, sys, math, requests, argparse, time, requests, string, pickle, threading
from flask import Flask, request, render_template, send_file, make_response, current_app
from functools import update_wrapper
from flask_cors import CORS
from urllib.request import urlopen


# %% Flask app
app = Flask(__name__)
CORS(app)

from readPDFSSCOVID19Mx import PDFCOVIDtoList
from downloadPDFCOVID19Mx import downloadPDFCOVID19Mx
import csv

def get_covid_list():
    URL_COVID_MX = downloadPDFCOVID19Mx()
    return PDFCOVIDtoList(URL_COVID_MX)

print(get_covid_list)
"""
    Pickle example 
    with open(productsFile, 'wb') as fi:
        pickle.dump(dictProductos, fi)
    
    def getproducts():
    productsFile = "products.pk"
    with open(productsFile, 'rb') as fi:
        dictionary = pickle.load(fi)
    return dictionary
"""

def f(f_stop):
    """ Code for saving the pickles every given time"""

    if not f_stop.is_set():
        # call f() again in 60 seconds
        threading.Timer(21600, f, [f_stop]).start()

f_stop = threading.Event()
# start calling f now and every 60 sec thereafter
f(f_stop)


def getCasesByState(state = None):
    return {} 

def getCases(case = None):
    return {}

def getHistoricCases(date):
    """Date in format DD_MM_YY"""
    day, month, year =  date.split("_")
    return {}

@app.route('/casos', methods=['GET'])
def get_cases():
    id = request.args.get("id")
    if id:
        return getCases(id)
    else:
        return getCases()


@app.route('/casos_por_estado', methods=['GET'])
def get_cases_by_state():
    state = request.args.get("state")
    if state:
        return get_cases_by_state(state)
    else:
        return get_cases_by_state()

@app.route('/casos_por_fecha')
def get_historic_cases():
    date = request.args.get("date")
    return get_historic_cases(state)

help_string = """
API para obtener los casos de coronavirus en México.
Las siguentes urls son basicas
/casos_por_fecha (GET) Recibe como parametro la fecha en formato DD_MM_YY y regresa un json con la informacion de ese día
/casos_por_estado (GET) Recibe como parametro opcional el nombre del estado. regresa un json con la informacion de ese estado
/casos (GET) Recibe como parametro opcional el # de caso. regresa un json con la informacion de los casos

"""


@app.route('/')
def home():
    return help_string

if __name__ == '__main__':
    app.run()