import sys
input = sys.argv[2]
info= open("student.txt")
dict= {}
for i in info:
    student,school=i.split(":")
    dict[student]= school
for i in input.split(","):
    try:
        assert i in dict.keys()
        print("Name: "+ i+ " University: "+dict[i])
    except:
        print("No record of "+i +" was found")
    

