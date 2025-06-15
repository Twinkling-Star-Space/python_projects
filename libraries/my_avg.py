'''
import statistics

avg = statistics.mean([12,12])

print(avg)



#-----------------------------------------------

import sys

print("My name is ", sys.argv[1])

#----------------------------------------------


#to handle the prompt if input is not given 

import sys

try:
    print("My name is " , sys.argv[1])
except:
    print("very few prompts")


#-----------------------------------------------------

import sys

if len(sys.argv) < 2:
    print("to few argument")
elif len(sys.argv) > 2:
    print("to many arguments")
else:
    print("my name is ", sys.argv[1])



#-----------------------------------------------------------

import sys

if len(sys.argv) < 2:
    sys.exit("to few argument")
elif len(sys.argv) > 2:
    sys.exit("to many arguments")

print("my name is ", sys.argv[1])



#-----------------------------------------------------------

import sys
                                            #here is a bug
if len(sys.argv) < 2:
    sys.exit("to few argument")

for arg in sys.argv:
    print("my name is ",arg)

#------------------------------------------------------------

import sys

if len(sys.argv) < 2:
    sys.exit("to few argument")
# here i took slice of list from 
for arg in sys.argv[1:]:
    print("my name is ",arg)
'''
#----------------------------------------------------------------


