import configparser
import os

con=configparser.ConfigParser()

def readconf(n):
    con.read('step.ini')
    step=con.get("config",n)
    step=int(step)
    return step

def writestep(num,n):
    con.read('step.ini')
    con.set("config",n,str(num))
    con.write(open('step.ini','w'))

