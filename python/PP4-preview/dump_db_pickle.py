import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, "=>", db[key])
dbfile.close()
