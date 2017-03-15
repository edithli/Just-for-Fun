class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def raiseSalary(self, percent):
        self.pay *= (1 + percent)

    def lastName(self):
        return self.name.split()[-1]

    def __str__(self):
        string = '<%s => %s>:\n' % (self.__class__.__name__, self.name)
        for key, value in self.__dict__.items():
            string = string + key + '=>' + str(value) + '\n'
        return string[:-1]

if __name__ == '__main__':
    bob = Person('Bob Smith', 45, 3000, 'software')
    sue = Person('Sue Jones', 42, 4000, 'hardware')
    print(bob.lastName())
    sue.raiseSalary(.20)
    print(sue.pay)


class Manager(Person):
    def raiseSalary(self, percent, bonus=0.1):
        # self.pay *= (1 + percent + bonus)
        # to reduce code redundancy, we can augment the inherited method
        Person.raiseSalary(self, percent+bonus)
