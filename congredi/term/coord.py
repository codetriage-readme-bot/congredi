#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Coordinated port opening for testing.
"""
from os import path
import socket


def expand(pathname):
    return path.expanduser(pathname)


class fileCoord():

    @staticmethod
    def read(pathname="~/ort"):
        if not path.isfile(expand(pathname)):
            fileCoord.write(socket.gethostname(), 8800, pathname)
        with open(expand(pathname), 'r') as a:
            stuff = a.read()
            return stuff.strip('\n').split(":")

    @staticmethod
    def write(host, port, pathname="~/ort"):
        with open(expand(pathname), 'w+') as a:
            a.write(host + ":" + str(port))
