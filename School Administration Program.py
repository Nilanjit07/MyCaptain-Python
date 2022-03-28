import csv
def add_into_csv(info_list):
    with open('student_info.csv','a',newline='') as file:     
        w=csv.writer(file)
        if file.tell()==0:                                    
            w.writerow(['Name','Admission no','class','dob'])  
        w.writerow(info_list)
def takes_info():
    while True:
        info=input('Enter info in following format(Name, Admission_no, Class, DOB): ')
        info_list=info.split(' ')                           
        print('Info entered is- \nName: {} \nAdmission no: {} \nClass: {} \ndob:{}'.format(info_list[0],info_list[1],info_list[2],info_list[3]))       
        ch=input('Is the info correct[Y/N]: ')              
        if ch=='y':
            add_into_csv(info_list)                         
            print('Info added')
            break
        else:
            continue                                        
print('This is a School Administration program\n')
takes_info()
ch=input('More students are left to be added? [Y/N]: ')                       
if ch=='y':
    takes_info()
