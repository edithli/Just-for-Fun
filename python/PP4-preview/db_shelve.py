from initdata import bob, sue
import shelve

def storeShelve():
    db = shelve.open('people-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db.close()

def loadShelve():
    db = shelve.open('people-shelve')
    for key in db:
        print(key, '=>', db[key])
    db.close()

def updateShelve():
    db = shelve.open('people-shelve')
    sue = db['sue']
    sue['pay'] *= 1.20
    db['sue'] = sue
    from initdata import tom
    db['tom'] = tom
    db.close()
