import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "suman33.sb@gmail.com"
password = "@#3147547314@#"
username = from_email
to_list = ['suman33.ab@gmail.com']


class BloodDonors:
    user_details = []
    messages = []
    base_message = """Dear Donors  there is Request for ,
                    Blood group:{blood_group}
                    patient: {patient}
                    Address of Hospital:{address}
                    Contact:{contact}
                    Thank you for being a part of saving life !!!
                """

    def add_user(self, patient, address, blood_group, contact, email=None):
        patient = patient[0].upper() + patient[1:].lower()
        address = address[0].upper() + address[1:].lower()
        detail = {
            "patient": patient,
            "blood_group": blood_group,
            "address": address,
            "contact": contact,
        }
        today = datetime.date.today()
        date_text = '{today.year}/{today.month}/{today.day}'.format(
            today=today)
        detail['date'] = date_text
        if email is not None:  # if email != None
            detail['email'] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_message(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                patient = detail['patient']
                blood_group = detail['blood_group']
                date = detail['date']
                address = detail['address']
                contact = detail['contact']
                message = self.base_message
                new_msg = message.format(
                    patient=patient,
                    blood_group=blood_group,
                    address=address,
                    contact=contact,
                    date=date
                )
                self.messages.append(new_msg)
            return self.messages
        return[]


obj = BloodDonors()
obj.add_user('justin', 'Thapathali', "AB+", "9843610435")
obj.add_user('shari', 'Kathmandu', "O+", "984361068")
obj.add_user('shAkKh', 'Nepal', "AB-", "79734007034")
obj.get_details()
obj.make_message()
'''
obj.add_user('shail', "A-")
obj.add_user('shakya', "AB+")
obj.get_details()
obj.make_message()
'''
