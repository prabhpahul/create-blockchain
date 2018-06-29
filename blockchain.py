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
     
    def get_previous_block(self):  # get last block
        return self.chain[-1]
    def proof_of_work(self, previous_proof):  #check the proof of work
        new_proof = 1                      #trial and error approach
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
                
        return new_proof   
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    #check the validity of the block
    def is_chain_valid(self,chain):
        block_index = 1
        previous_block = chain[0]
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False 
            previous_block = block
            block_index +=1
        return True   
        
app = Flask(__name__)
blockchain =  Blockchain()
#mining a block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof,previous_hash)
    response = {
                'message':'Congratulations',
                'index':block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']
                }
    return jsonify(response),200    

#getting the full block chain

@app.route('/get_chain',methods=['GET'])
def get_chain():
    response = {'chain':blockchain.chain,
                'length':len(blockchain.chain)}
    return jsonify(response),200    

#running the result
app.run(host='0.0.0.0',port = 5000)
          

