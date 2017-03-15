import pickle, glob

# store records in different files so that updating only access one file at a time

def storeRecords():
    # store into files entry by entry
    from initdata import db
    for (key,rec) in db.items():
        recfile = open(key+".pkl", 'wb')
        pickle.dump(rec, recfile)
        recfile.close()

def loadRecords():
    recfilenames = glob.glob("*.pkl")
    for filename in recfilenames:
        recfile = open(filename, 'rb')
        rec = pickle.load(recfile)
        print(filename, "=>", rec)
