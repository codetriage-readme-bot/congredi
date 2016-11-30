# -*- coding: utf-8 -*-
#https://cryptography.io/en/latest/fernet/
import os, sys, datetime, logging, time, io, pycurl, socket
from stem.control import Controller
from stem.util import term
from stem import process, Signal
#from urllib.request import urlopen
def print_bootstrap_lines(line):
    print(line)
def prox():
    tor_process = process.launch_tor_with_config(
        config = {
            'SocksPort': '8800',
            'ControlPort':'8801',
            'DataDirectory':'/temp/torserv'
        },
          init_msg_handler = print_bootstrap_lines
        )
    return tor_process
def start_rendesvous():
    with Controller.from_port(port = 8801) as controller:
        controller.authenticate()
        if not os.path.exists(key_path):
            service = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
            print("Started a new hidden service with the address of %s.onion" % service.service_id)
            with open(key_path, 'w') as key_file:
                key_file.write('%s:%s' % (service.private_key_type, service.private_key))
        else:
            with open(key_path) as key_file:
                key_type, key_content = key_file.read().split(':', 1)
            service = controller.create_ephemeral_hidden_service({80: 5000}, key_type = key_type, key_content = key_content, await_publication = True)
            print("Resumed %s.onion" % service.service_id)
        raw_input('press any key to shut the service down...')
        controller.remove_ephemeral_hidden_service(service.service_id)
tor_process = prox()
start_rendesvous()
tor_process.kill()
