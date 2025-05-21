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