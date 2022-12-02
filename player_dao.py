from domain import *
def get_all():
    result=[]
    for f in [e.strip().split(';') for e in open('dane\\dane.csv',encoding='utf-8') if len(e.strip())>0]:
        p=Player(int(f[0]),f[1],f[2],float(f[3]),float(f[4]))
        result.append(p)
    return result