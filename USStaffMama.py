#!/usr/bin/python3

class color:
    yellow = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    end  = '\033[0m'

import sys
import re
import requests
import subprocess
import json
import argparse, textwrap
import os
import urllib
import string
import configparser
from bs4 import BeautifulSoup

""" Setup Argument Parameters """
parser = argparse.ArgumentParser(description='[INFO] Example: python3 USStaffMana.py -c telsa -e telsa.com -n 0', formatter_class=argparse.RawTextHelpFormatter)
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-c', '--company', help='Company Name', required=True)
requiredNamed.add_argument('-e', '--email', help='Company Email Domain', required=True)
requiredNamed.add_argument('-n', '--naming', help= textwrap.dedent('''\
    User Name Format: 
    \t[0] Auto (Hunter.io) 
    \t[1] FirstLast
    \t[2] FirstMiddleLast
    \t[3] FLast
    \t[4] FirstL
    \t[5] First.Last
    \t[6] Last.First'''), required=True)
args = parser.parse_args()

""" API-KEY """
config = configparser.RawConfigParser()
config.read("USStaffMama.cfg")
api_key = config.get('API_KEYS', 'hunter_api')

def error():
    print("[ERROR] Something went wrong!")
    sys.exit()

def banner():
    print
    print("   __  ____________ __        __________  ___                       ")
    print("  / / / / ___/ ___// /_____ _/ __/ __/  |/  /___ _____ ___  ____ _  ")
    print(" / / / /\__ \\\\__ \/ __/ __ `/ /_/ /_/ /|_/ / __ `/ __ `__ \/ __ `/  ")
    print("/ /_/ /___/ /__/ / /_/ /_/ / __/ __/ /  / / /_/ / / / / / / /_/ /   ")
    print("\____//____/____/\__/\__,_/_/ /_/ /_/  /_/\__,_/_/ /_/ /_/\__,_/    ")
    print("                                                 [bigb0ss]          ")
    print                                                                  
    print

# US Staff Search
def search(company, email, prefix):
    csv = []

    url = "https://bearsofficialsstore.com/company/%s" % company
    
    r = requests.get(url)

    if r.status_code != 200:
        print("[ERROR] 404 Error! The company name needs to be verified. Go to https://bearsofficialsstore.com/ and find the EXACT company name (e.g., t-mobile != t_mobile)")
        sys.exit()
    
    content = (r.text)
    contentSoup = BeautifulSoup(content, 'html.parser')

    # Finding the last page
    for i in contentSoup.find_all('a'):
        page = i.get('href')
    match = re.search('page([0-9]*)', page)

    if match == None:
        lastPage = 1
    else:
        lastPage = match.group()[4:]
        lastPage = int(lastPage)
        print("[INFO] Total Pages: %s" % lastPage) 

    for page in range(1, lastPage):
               
        url = "https://bearsofficialsstore.com/company/%s/page%s" % (company, page)
        print("[INFO] Fetching usernames: %s" % url)
        
        r = requests.get(url)
        content = (r.text)
        contentSoup = BeautifulSoup(content, 'html.parser')

        for j in contentSoup.find_all("img"):
            if 'id="imgCompanyLogo"' in str(j):
                # The Logo img tag is alt="" which breaks forloop
                continue
            else:
                raw = j.get('alt').lower().split()

                firstName = raw[0]
                lastName = raw[1:]

                name = firstName + " " + lastName[0]

                fname = ""
                mname = ""
                lname = ""

                if len(lastName) == 1:
                    fname = firstName
                    mname = '?'
                    lname = lastName[0]
                elif len(lastName) == 2:
                    fname = firstName
                    mname = lastName[0]
                    lname = lastName[1]
                elif len(lastName) >= 3:
                    fname = firstName
                    lname = lastName[0]
                else:
                    fname = firstName
                    lname = '?'

                fname = re.sub('[^A-Za-z]+', '', fname)
                mname = re.sub('[^A-Za-z]+', '', mname)
                lname = re.sub('[^A-Za-z]+', '', lname)

                #print(fname, mname, lname)

                if len(fname) == 0 or len(lname) == 0:
                    continue

                # Username Scheme Generator
                # [0] Auto (hunter.io) 
                # [1] FirstLast
                if prefix == "1" or prefix == 'firstlast':
                    user = '{}{}'.format(fname, lname)
            
                # [2] FirstMiddleLast 
                if prefix == "2" or prefix == 'fistmlast':
                    if len(mname) == 0:
                        user = '{}{}{}'.format(fname, mname, lname)
                    else:
                        user = '{}{}{}'.format(fname, mname[0], lname)
                
                # [3] FLast 
                if prefix == "3" or prefix == 'flast':
                    user = '{}{}'.format(fname[0], lname)
                
                # [4] FirstL  
                if prefix == "4" or prefix == 'firstl':
                    user = '{}{}'.format(fname, lname[0])
                
                # [5] First.Last 
                if prefix == "5" or prefix == 'first.last':
                    user = '{}.{}'.format(fname, lname)
                
                # [6] Last.First
                if prefix == "6" or prefix == 'lastfirst':
                    user = '{}.{}'.format(lname, fname)

                if prefix == 'fmlast':
                    if len(mname) == 0:
                        user = '{}{}{}'.format(fname[0], mname, lname)
                    else:
                        user = '{}{}{}'.format(fname[0], mname[0], lname)
                    
                # CSV
                csv.append('"%s","%s","%s","%s"' % (fname, lname, name, user + "@" + email))
                f = open('{}.csv'.format(company), 'w')
                f.writelines('\n'.join(csv))
                f.close()

if __name__ == '__main__':
    banner()

    company = args.company
    company = company.lower()
    
    email = args.email
    email = email.lower()
    if "." not in email:
        print(color.red + "[ERROR] Incorrect Email Format." + color.end)
        sys.exit()

    prefix = args.naming
    prefix = prefix.lower()

    if prefix == "0":
        # Hunter.io
        print("[INFO] Hunter.io search...")
        url_hunter = "https://api.hunter.io/v2/domain-search?domain=%s&api_key=%s" % (email, api_key)
        r = requests.get(url_hunter)

        if r.status_code != 200:
            print("[ERROR] Something is wrong accessing Hunter.io")
            sys.exit()

        content = json.loads(r.text)
        prefix = content['data']['pattern']
        print("[INFO] %s" % prefix)
        if prefix:
            prefix = prefix.replace("{","").replace("}", "")
            if prefix == "firstlast" or prefix == "firstmlast" or prefix == "flast" or prefix == "firstl" or prefix =="first" or prefix == "first.last" or prefix == "fmlast" or prefix == "lastfirst":
                print("[INFO] Found %s Naming Scheme" % prefix)
            else:
                print(color.red + "[ERROR] Auto-search Failed. Select the user name format from the option." + color.end)
                sys.exit()
        else:
            print(color.red + "[ERROR] Auto-search Failed. Select the user name format from the option." + color.end)
            sys.exit()

    # Scraping
    search(company, email, prefix)

    print("[INFO] US Staff Scrapping Done!")