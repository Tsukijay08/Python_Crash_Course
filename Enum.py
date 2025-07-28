#from enum import Enum
#subjects = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
#print(subjects.ENGLISH)
#print(subjects.MATHS)
#print(subjects.SCIENCE)
#print(subjects.SANSKRIT)

#from enum import Enum

#class subjects(Enum):
# ENGLISH = "E"
#   MATHS = "M"
 #  GEOGRAPHY = "G"
 #  SANSKRIT = "S"
   
#obj = subjects.SANSKRIT
#print(type(obj))
#print(obj.name)
#print(obj.value)

from enum import Enum

class subjects(Enum):
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"

for sub in subjects:
   print (sub.name, sub.value)