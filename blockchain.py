#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 12:03:49 2018

@author: prabhpahul
"""

import datetime  #save date time for each block
import hashlib #for hashing
import json
from flask import Flask, jsonify #for web interface

#building a blockchain

"""
1.make several function then use
2.with a class to make it reuseable

"""

class Blockchain:
    def __init__(self):
        self.chain = []
#create genenis first block
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):      
        block = {
                 'index': len(self. chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash
                 }    #transaction or data
        self.chain.append(block)
        return block

