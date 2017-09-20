import datetime


class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi{name}!
Thank you for purchase on {date}.
we hope you are excited about using it.

"""

    def add_user(self, name, amount,email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.year}/{today.month}/{today.day}'.format(
            today=today)
        detail['date'] = date_text
        if email is not None:
            detail["email"]=email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_message(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail['name']
                amount = detail['amount']
                date = detail['date']
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return[]


obj = MessageUser()
obj.add_user('justin', 323.23)
obj.add_user('shari', 97947.23)
obj.add_user('shAkKh', 092374.32)
obj.add_user('shail', 86743.32)
obj.add_user('shakya', 86836.32)
obj.get_details()
obj.make_message()

'''default_names = ['suman', 'hari', 'shyam', 'john', 'pawan', 'binita']

default_amount = [43, 213, 435, 434, 546, 443]

unf_message = """Hi{name}!


Thank you for purchase on {date}. 
we hope you are excited about using it.

"""


def make_messages(names, amount):
    messages = []

    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()

'''
