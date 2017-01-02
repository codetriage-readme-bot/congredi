#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Stem tor controls (could publish .onions in address table instead of ip as feature)
"""
import os
from stem.control import Controller
from stem import process
# small rendesvous pieces (see MainLoop)


def print_bootstrap_lines(line): # test
    print(line)


def prox(): # test
    tor_process = process.launch_tor_with_config(
        config={
            'SocksPort': '8800',
            'ControlPort': '8801',
            'DataDirectory': '/temp/torserv'
        },
        init_msg_handler=print_bootstrap_lines
    )
    return tor_process


def start_rendesvous(key_path): # test
    with Controller.from_port(port=8801) as controller:
        controller.authenticate()
        if not os.path.exists(key_path):
            service = controller.create_ephemeral_hidden_service(
                {80: 5000}, await_publication=True)
            print("Started a new hidden service with the address of %s.onion" %
                  service.service_id)
            with open(key_path, 'w') as key_file:
                key_file.write('%s:%s' %
                               (service.private_key_type, service.private_key))
        else:
            with open(key_path) as key_file:
                key_type, key_content = key_file.read().split(':', 1)
            service = controller.create_ephemeral_hidden_service(
                {80: 5000}, key_type=key_type, key_content=key_content, await_publication=True)
            print("Resumed %s.onion" % service.service_id)
        return service.service_id


def stop_rendesvous(service, tor_process): # test
    with Controller.from_port(port=8801) as controller:
        controller.authenticate()
        controller.remove_ephemeral_hidden_service(service.service_id)
        tor_process.kill()
