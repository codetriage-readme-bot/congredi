#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, yaml, multiprocessing, time
from api import app
from tor import prox
class api(multiprocessing.Process):
    def run(self):
        app.run(host="0.0.0.0",port=5000,debug=False)

class proxy(multiprocessing.Process):
    def run(self):
        prox()

if __name__=="__main__":
    config = {}
    if os.path.isfile('.congredi'):
        config = yaml.load(open('.congredi','r').read())
    elif os.path.isfile(os.path.expanduser('~/.congredi')):
        config = yaml.load(os.path.expanduser(open('~/.congredi','r').read()))
    else:
        config['MONGO_URI'] = '' # default mongo uri
    dork = api()
    dork.start()
    lone = proxy()
    lone.start()
    try:
        while True:
            time.sleep(1)
    except: pass
    finally:
        dork.terminate()
        lone.terminate()