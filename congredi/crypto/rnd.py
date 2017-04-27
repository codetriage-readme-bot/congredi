#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Random Generator (currently PyCryptoDome.Random)
"""
from __future__ import absolute_import
from Crypto import Random

rng = Random.new().read
