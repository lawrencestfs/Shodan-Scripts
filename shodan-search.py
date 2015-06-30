# -*- coding: utf-8 -*-
#Author: Lawrence Fernandes
#This Python script uses the Shodan REST API to search for devices and saves the results in a file

import shodan
import sys

# Configuration: setting up the API
SHODAN_API_KEY = "Insert your Shodan key here!"
api = shodan.Shodan(SHODAN_API_KEY)

# Gather our code in a main() function
def main():

    # Input validation
    if len(sys.argv) == 1:
            print 'Usage: %s <search query>' % sys.argv[0]
            sys.exit(1)
    
    try:
            # Perform the search
            query = ' '.join(sys.argv[1:])
            search = api.search(query)
    
            # Loop through the matches and print each IP and data
            cont = 1
            for result in search['matches']:
                    print 'Result number %s' % cont
                    cont += 1
                    print 'IP: %s' % result['ip_str']
                    print result['data']
                    print '' 
            print 'Results found: %s' % search['total']     
    
            try:
                    filename = sys.argv[1]
            except:
                    print 'Error! You must provide a parameter: File name'
                    sys.exit(1) 
            
            # Saving the results in a file
            try:
                    file = open(filename, 'w+')
                    cont = 1
                    for result in search['matches']:
                            file.write('\nResult number %s' % cont);
                            file.write('\nIP: %s\n' % result['ip_str']);
                            file.write(result['data']);
                            file.write('\n');
                            cont += 1
                    file.close()
    
            except IOError:
                    print 'Error! Could not open', filename
                    sys.exit(1)
    
    except Exception, e:
            print 'Error: %s' % e
            sys.exit(1)
            
# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
