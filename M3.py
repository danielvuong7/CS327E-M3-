from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import pymysql

import datetime
import random

def test1():
  # Test 1: "Hello World" program
  print("Hello World")
  print()

test1()
    
def test2():  
  # Test 2: Beautiful Soup
  html = urlopen("http://www.pythonscraping.com/pages/page3.html")
  bsObj = BeautifulSoup(html, "html.parser")
    
  imgs = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
  for image in imgs:
    print (image["src"])
  print()

test2()

def test3():
  # Test 3: PyMySQL
  conn = pymysql.connect(host='127.0.0.1', port=3306, user='moosenugget', passwd='mamba04d', db='mysql')
  cur = conn.cursor()

  print("Test 3")
  cur.execute("USE bank")
  cur.execute("SELECT * FROM employee WHERE title = 'Head Teller';")
  print(cur.fetchall())
  cur.close()
  conn.close()
  print()

test3()
