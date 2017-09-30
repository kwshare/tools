# coding:utf-8

from pymongo import MongoClient

client = MongoClient('127.0.0.1', username='root', password='cisco123',
                     authMechanism='SCRAM-SHA-1')


db=client['hello']

col=db['col']
mydic={'name':'Benny','age':22,'job':'DE'}

print col.find_one()