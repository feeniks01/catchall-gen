import random
import string
import namelist


email_count = int(input("How many emails would you like to generate? "))

#email gen
for i in range(email_count):
    randnumbers = random.randint(1,9999999)
    randnames = random.choice(namelist.Names)
    print(randnames + str(randnumbers) + '@yourDomainHere')
