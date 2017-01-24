#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tor proxy design
possibly usable for testing framework (start multiple processes with different ports...)
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import multiprocessing
import time
from ..auth.token import app
from .tor import prox


class api(multiprocessing.Process):

    def run(self):  # test
        app.run(host="0.0.0.0", port=5000)  # , debug=False)


class proxy(multiprocessing.Process):

    def run(self):  # test
        prox()

if __name__ == "__main__":  # test
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
# congredi/extra/daemon.py                    23     11    52%   18, 24, 27-36
