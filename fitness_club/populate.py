from faker import Faker
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_club.settings')
fakegen = Faker()
import django
django.setup()
from manager.models import Member , Trainer , Admin , Fee

import  csv
import random

def populateMember(n=5):
    for i in  range(n):
        fname = fakegen.name()
        fusername = fakegen.name()
        femail = fakegen.email()
        fpassword = 'Aliraza123'
        fage = fakegen.ean8()[:2]
        fheight = fakegen.ean8()[:3]
        fweight = fakegen.ean8()[:4]

        mem  = Member.objects.get_or_create(name=fname , username=fusername , email=femail  , password=fpassword , age=fage ,height=fheight, weight=fweight)[0]
        populateFee(mem)

def populateTrainer(n=5):
    for i in  range(n):
        fname = fakegen.name()
        fusername = fakegen.name()
        femail = fakegen.email()
        fpassword = 'Aliraza123'

        Trainer.objects.get_or_create(name=fname , username=fusername , email=femail  , password=fpassword )[0]

# def populateAdmin(n=5):
#     for i in  range(n):
#         fusername = fakegen.name()
#         femail = fakegen.email()
#         fpassword = 'Aliraza123'

#         Admin.objects.get_or_create(username=fusername , email=femail  , password1=fpassword ,password2=fpassword   )[0]

def populateFee(mem):

    for i in  range(10):
        fmember = mem 
        famount = int(fakegen.ean8()[:4])
        fmonth = fakegen.month_name()

        # print(fmember , type(fmember))
        # print(famount, type(famount))
        # print(fmonth, type(fmonth))
        # print("___________________")
        # print()

        Fee.objects.get_or_create(member=fmember , amount=famount , month=fmonth)[0]



if __name__ == "__main__":

    print("populationg member script")
    populateMember(50)
    print("success populating member")

    # print("populationg trainer script")
    # populateTrainer(100)
    # print("success populating trainer")

    # print("populationg admin script")
    # populateAdmin(100)
    # print("success populating admin")
