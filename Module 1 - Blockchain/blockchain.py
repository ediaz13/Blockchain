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


#Part 2 - Mining our Blockchain.
