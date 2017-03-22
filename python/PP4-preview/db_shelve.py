from initdata import bob, sue
import shelve
from person import Person, Manager

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

def makeDBwithClass():
    bob = Person('Bob Smith', 42, 30000, 'Software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)
    db = shelve.open('class-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()

def dumpDBclass():
    db = shelve.open('class-shelve')
    for key in db:
        print(key, "=>", db[key].name, db[key].pay)
    db.close()

def updateDBclass():
    db = shelve.open('class-shelve')
    sue = db['sue']
    sue.raiseSalary(.05)
    db['sue'] = sue
    tom = db['tom']
    tom.raiseSalary(.10)
    db['tom'] = tom
    db.close()
