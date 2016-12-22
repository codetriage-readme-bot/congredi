#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing, time
from ..crypto.token import app
from .tor import prox
class api(multiprocessing.Process):
	def run(self):
		app.run(host="0.0.0.0", port=5000, debug=False)
class proxy(multiprocessing.Process):
	def run(self):
		prox()

if __name__=="__main__":
	dork = api()
	dork.start()
	lone = proxy()
	lone.start()
	try:
		while True:
			time.sleep(1)
	finally:
		dork.terminate()
		lone.terminate()
