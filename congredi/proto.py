#!/usr/bin/env python
# -*- coding: utf-8 -*-

class interlocutor():
    def __init__(self,config):
        self.ec = config
    # client
    def reach():
    # server
    def greet():
        
# some sort of handshake would be needed (EC + fernet?) with an incentive to behave
def hello_send(): # send cleartext signed Time & Session key
    #Hello peer, my session EC is 'A', and my time is 'T', signed 'a'
def hello_get(): # check sig, send encrypted challenge nounce/time, & Session key
    #Hello, compute 'N' at my time 't', my session key is 'S', let's use 'T' signed 's'
def earn_query(): #compute nounce, send result + query, both signed
    #(encrypted T) - 'N'*'T' = 'S', Query = 'abc', sig = 'Q'
def run_result(): #check result, run query, transfer data
    #(encrypted T) - result, certification
def thank_server(): #thank the server for behaving
    #(encrypted T) - thank you, I rank you better. 'sig'
def welcome_client(): #welcome client to search again, for behaving
    #(encrypted T) - you're welcome, I rank you better for ranking me better "sig" 'sig'
