marks = int(input ("enter your marks"))
if marks >= 90 and marks <= 100:
    print ("outstanding")
elif marks >= 80 and marks <= 89:
    print ("very good")
elif marks >= 70 and marks <= 79:
    print ("good") 
elif marks >= 60 and marks <= 69:  
    print ("fair")
elif marks >= 50 and marks <= 59:
    print ("average")
elif marks >= 40 and marks <= 49:
    print ("below average")
else:
    print ("fail")