class Bank:
    credit_person = None
    __bankname = 'PrivatBank'
    customer_credit = 0
    customer_goods = []

    def __init__(self,name,email,count_dollar):
        self.name = name
        self.email = email
        self.count_dollar = count_dollar

    @classmethod
    def get_bank_name(cls):
        print(cls.__bankname)

    @staticmethod
    def course_dollar():
        count = 42
        print(f'count dollar now {count}')

    def product(self,name_product,price):
        if self.count_dollar > price:
            self.customer_goods.append(name_product)
            self.count_dollar -= price
            print('Buy product')
        else:
            print("Dont have money :(")

    def give_credit(self,credit_dollar):
        self.count_dollar += credit_dollar
        self.customer_credit += credit_dollar

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self,new_name):
        self.name = new_name

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self,new_email):
        self.email = new_email

    def check_credit(self):
        if self.customer_credit > 10000:
            print('ALOOOOOO!')
        else:
            print('ok')