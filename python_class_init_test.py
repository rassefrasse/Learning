class Intern:
    num_of_interns = 0
    pay_increase = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.mail = firstname + '.' + lastname + "@company.com"
        self.pay = pay

        Intern.num_of_interns += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    def pay_raise(self):
        return int(self.pay * self.pay_increase)
    
    @classmethod
    def change_pay(cls, amount):
        return cls.pay_increase == amount

print(Intern.num_of_interns)
intern1 = Intern('Rasmus', 'Ekblom', 30000)
intern2 = Intern('Poon', 'Chan', 35000)

Intern.pay_increase = 1.06

print(intern1.mail, intern2.mail)
print(Intern.pay_increase)
print(intern2.pay_increase)
print(intern2.fullname())
print(intern2.pay_raise())
print(Intern.num_of_interns)



