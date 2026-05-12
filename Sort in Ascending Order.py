import numpy as np
data_type=[('name','s15'),('class','int'),('height','float')]

students_details=[('james',5,40.5),('nail',6,52.5),('paul',5,42.10),('pit'5,40.11)]

students=np.array(students_details,dtype=data_type)

print("Original array:")
print(students)
print("Short by height")
print(np.short(students,order='height'))