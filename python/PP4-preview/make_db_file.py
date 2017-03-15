#!/usr/bin/python3

'''
write db into file using silly ways
re-typing examples
'''
dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeFile(db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name, RECSEP, repr(value), file = dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

    
def loadFile(dbfilename=dbfilename):
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        line = input()
        while line != ENDREC:
            name, value = line.split(RECSEP)
            rec[name] = eval(value)
            line = input()
        db[key] = rec
        key = input()
    return db
