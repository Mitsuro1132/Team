class Bank:
    credit_person = None
    __bankname = 'PrivatBank'

    def __init__(self, name, email, count_dollar):
        self.name = name
        self.email = email
        self.count_dollar = count_dollar
        self.customer_credit = 0
        self.customer_goods = []

    @classmethod
    def get_bank_name(cls):
        print(cls.__bankname)

    @staticmethod
    def course_dollar():
        count = 42
        print(f'count dollar now {count}')

    def product(self, name_product, price):
        if self.count_dollar >= price:
            self.customer_goods.append(name_product)
            self.count_dollar -= price
            print('Buy product')
        else:
            print("Dont have money :(")

    def give_credit(self, credit_dollar):
        self.count_dollar += credit_dollar
        self.customer_credit += credit_dollar

    @property
    def Name(self):
        return self.name

    @Name.setter
    def Name(self, new_name):
        self.name = new_name

    @property
    def Email(self):
        return self.email

    @Email.setter
    def Email(self, new_email):
        self.email = new_email

    def check_credit(self):
        if self.customer_credit > 10000:
            print('ALOOOOOO!')
        else:
            print('ok')



sasha = Bank('Sasha', 'perlinka@gmail.com', 1000)
sasha.get_bank_name()
sasha.course_dollar()
sasha.product('Apple',200)
sasha.give_credit(11000)
sasha.check_credit()

print(sasha.Name,sasha.Email)

print(sasha.count_dollar)