#!/usr/bin/python3

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom William', 'age': 33, 'pay': 100000, 'job': 'writing'}

db = dict(bob=bob, sue=sue, tom=tom)

if __name__ == '__main__':
    for key in db:
        print(key, "=>", db[key])
