#students =["Abhinand", "Roopchand"]      #list
#students.sort(reverse=True)

#for i in students:
 #   print(i)

#students =("Abhinand", "Roopchand")      #tuple
#sorted_students = sorted(students, reverse=True)
#for i in sorted_students:
 #    print(i)


#list of tuples

students =[("Abhinand", "20"),("Roopchand", "25")]

age = lambda ages:ages[1]
students.sort(key=age,reverse=True)

for i in students:
    print(i)
