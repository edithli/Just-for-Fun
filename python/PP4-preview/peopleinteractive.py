import shelve

fieldnames = ['name', 'age', 'pay', 'job']
maxfield = max(len(f) for f in fieldnames)


def lookup():
    db = shelve.open('class-shelve')
    while True:
        key = input('\nkey? => ')
        if not key:
            break
        try:
            record = db[key]
        except:
            print('no such key %s' % key)
        else:
            for field in fieldnames:
                print(field.ljust(maxfield), getattr(record, field))

def update():
    from person import Person
    db = shelve.open('class-shelve')
    while True:
        key = input('\nkey? =>')
        if not key:
            break
        if key in db:
            record = db[key]
        else:
            record = Person(name='?', age='?')
        for field in fieldnames:
            curval = getattr(record, field)
            newtext = input('\t[%s]=%s\n\tnew?=>' % (field, curval))
            if newtext:
                setattr(record, field, eval(newtext))
        db[key] = record
    db.close()
                
