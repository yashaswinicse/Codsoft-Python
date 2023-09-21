#PASSWORD GENERATOR#

import random
import string

#using string methods for lowercase,uppercase amd digits
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = "!@#$&*%-_"
gen_pass = lower+upper+symbol+num
length = int(input("Enter the password length:\n"))
print("Your passsord is:","".join(random.sample(gen_pass,length)))



