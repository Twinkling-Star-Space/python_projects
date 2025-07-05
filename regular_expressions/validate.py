
email = input("Email:").strip()

if '@' in email and "." in email:
    print("valid")
else:
    print("invalid")


#-------------------------------------

email = input("Enter your email: ")

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("invalid")

#--------------------------------------
email = input("Enter your email: ")

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")



#-------------------------------------------------------------

import re

email = input("Enter your email: ")

if re.search(r"^.+@.+\.edu$", email):
    print("valid")

else:
    print("invalid")


#-----------------------------------------------------------------

import re

email = input("Enter your email: ")

if re.search(r"^[^@]+@[^@]+\.edu$", email, re.IGNORECASE):
    print("valid")

else:
    print("invalid")


#------------------------------------------------------------------------



