# -*- coding: utf-8 -*-
# File Name: ics_crawler.py
# Author: Lawrence Fernandes
# This Python script uses the Shodan REST API to search for ICS related devices.

import shodan
import sys
import os

# Configuration
SHODAN_API_KEY = "Insert your Shodan key here!"
api = shodan.Shodan(SHODAN_API_KEY)
      
print '\nWelcome to ICS_Crawler!\n'

op = True
while op:
  os.system('clear')
  print ("""
  ********* Menu *********
  1. Info
  2. Search
  3. Quit
  """)
  #op = int(input('Choose one option:'))
  op = raw_input("Choose one option:") 
  if op == "1":
      print """\nICS_Crawler is a Python script developed for
      Industrial Control Systems (ICS) Penetration Tests.
      It uses the Shodan REST Python API to search for ICS related devices.\n"""
      os.system("pause")
    
  elif op =="2":
        try:
          query1 = api.search('siemens S7+simatic')
          query2 = api.search('SCADA')
          
          for result in query1['matches']:
                print 'Query: siemens S7+simatic'
                print 'Results found: %s' % query1['total']
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''

          for result in query2['matches']:
                print 'Query: SCADA'
                print 'Results found: %s' % query2['total']
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
                
        except shodan.APIError, e:
                print 'Error: %s' % e
        os.system("pause")
  else:
    print("\n Not Valid Choice! Please, try again.")
    os.system("pause")
