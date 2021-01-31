# Mocule 1 - Create Blockchain
"""
Created on Sun Jan 31 12:15:55 2021
pip install Flask==0.12.2
@author: diaze
"""
import datetime
import hashlib
import json
from Flask import Flask, jsonify

#Part 1 - Building a Blockchain.

class Blockchain:
         
    def __init__(self):
        self.chain =[]
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain) + 1,
                 'timestamp' : str(datetime.datetime.now()), 
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block

#Part 2 - Mining our Blockchain.
