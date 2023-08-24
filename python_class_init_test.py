class Intern:
    num_of_interns = 0
    pay_increase = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.mail = firstname + '.' + lastname + "@company.com"


        Intern.num_of_interns += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    def pay_raise(self):
        return int(self.pay * self.pay_increase)
    
    @classmethod
    def change_pay(cls, amount):
        return cls.pay_increase == amount
    

class Marketing_Intern(Intern):
    pay_increase = 1.15
    def __init__(self, firstname, lastname, pay, speciality):
        super().__init__(firstname, lastname, pay)
        self.speciality = speciality

class Manager(Intern):
    def __init__(self, firstname, lastname, pay, manage=None):
        super().__init__(firstname, lastname, pay)
        if manage == None:
            self.manage = []
        else: 
            self.manage = manage

    def add_intern(self, intern):
        if intern not in self.manage:
            self.manage.append(intern)

    def remove_intern(self, intern):
        if intern in self.manage:
            self.manage.remove(intern)

    def show_interns(self):
        for intern in self.manage:
            print("-->", intern.fullname())




print(Intern.num_of_interns)

intern1 = Intern('Rasmus', 'Ekblom', 30000)
intern2 = Marketing_Intern('Poon', 'Chan', 35000, "Advertisement")

employee = Manager("Lotta", "På_Bråckmackagatan", 80000, [intern2])

employee.show_interns()

print(intern2.mail)
print(intern2.speciality)




