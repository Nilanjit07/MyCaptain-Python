r=float(input("Enter radius: "))
area=(22/7)*r*r
print(area)
dict={'py':"python",'txt':"text",'bin':"binary",'c':"C",'CPP':"C++",'java':"java"}
f_name=input("Input the Filename: ")
l=f_name.split('.')
if l[1] in dict.keys():
    print("The extention of the file is:",dict[l[1]])
