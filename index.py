class bank:
    credit_person = None
    __bankname = 'PrivatBank'
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
