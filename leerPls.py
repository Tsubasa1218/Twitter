#!/usr/bin/env python
'''
Integrantes: 
	Juan David Suaza Cruz
'''
import json
from pprint import pprint

with open('twittertimeline.txt') as data_file:    
    data = json.load(data_file)

for elements in data:
	print "Nombre usuario: \n\t" + elements['user']['name']
	print "Ubicacion: \n\t" + elements['user']['location']
	print "Fecha: \n\t" + elements['created_at']
	print "Tweet: \n\t" + elements['text']
	print "\n\n"
	
