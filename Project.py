#importing libraries
import pandas as pd
#========================================================================================


#reading related files
df=pd.read_csv("Final.csv")
#========================================================================================
df_columns=df.columns.tolist()

#print(df_columns)
#print("=======================================")
train_dict={}

for index,i in enumerate (df[df_columns[0]].tolist()):
    train_dict.update({i:[df[df_columns[1]][index],df[df_columns[2]][index],df[df_columns[3]][index],df[df_columns[4]][index],df[df_columns[5]][index]]})
#print(train_dict)

#Defining important functions
def choice_admin():
    global action_admin
    action_admin = eval(input('''
    ---------------------------------------
    |For Train Details:   \tPress 1|
    |For News and Offers:  \tPress 2|
    |To Edit News and Offers :\tPress 3|
    ---------------------------------------
    '''))
    print("---------------------------------")
    return action_admin
#--------------------------------
def dataframe_list(index):
    arr=[]
    #print(index,"+")
    for i in train_dict:
        arr.append(train_dict[i][index])

    return arr
        

def update_data():
    updated_dict={}
    col=df_columns
    #print(col)
    updated_dict.update({col[0]:train_dict.keys()})
    col.pop(0)
    #print(col)
    for i,key in enumerate(col):
        updated_dict.update({key:dataframe_list(i)})
    dataframe=pd.DataFrame(updated_dict)
    print("=======================================")
    print(dataframe)
    
    dataframe.to_csv("User_Profile.csv",index=False)


def edit_train_details():
    destination=input("Enter the Destination you want to change details :")
    if destination in train_dict.keys():
        Departure=input("Write new departure time :")
        Arrival=input("Write new arrival time :")
        train_dict[destination][1]=Departure
        train_dict[destination][2]=Arrival
        train_dict.update
        update_data()


def choice():
    global action
    action = eval(input('''
    ---------------------------------------
    |To book a ticket:   \tPress 1|
    |For Train Details:  \tPress 2|
    |For News and Offers:\tPress 3|
    ---------------------------------------
    '''))
    print("---------------------------------")
    return action
#----------------------------------------------------------------
def booking():
        print("\n\nWelcome! To Ticket Booking System\n")
        restart = ('Y')
        while restart != ('N','NO','n','no'):
                        restart = ('N')
                        people = int(input("\nEnter no. of Ticket you want : "))
                        name_l = []
                        age_l = []
                        sex_l = []
                        destination=input("Write your destination :")
                        if destination in train_dict.keys():
                            print("Details of the train are given below.")
                            #print(df_columns)
                            print(destination,":",train_dict[destination])
                        else:
                            print("Na kaka")
                        for p in range(people):
                                name = str(input("\nName : "))
                                name_l.append(name)
                                age  = int(input("\nAge  : "))
                                age_l.append(age)
                                sex  = str(input("\nMale or Female : "))
                                sex_l.append(sex)

                        restart = str(input("\nOops! Forget someone. Want to book again? : "))
                        if restart in ('y','YES','yes','Yes'):
                                restart = ('Y')
                        else :
                                x = 0
                                print("\nTotal Ticket : ",people)
                                print("========================")
                                for p in range(1,people+1):
                                        print("Ticket : ",p)
                                        print("Name : ", name_l[x])
                                        print("Age  : ", age_l[x])
                                        print("Sex : ",sex_l[x])
                                        print("Destination: ",destination)
                                        print("========================")
                                        x += 1
                                
                                break

#-----------------------------------------------------------------
def train_details():
    print(df.to_string())
    
#-----------------------------------------------------------------
def news():
    print(pd.read_csv("Final.csv", usecols=[0,1,5]).to_string())
#============================================================================================




person = eval(input('''
----------------------------------------
|Are you a normal passenger?:\tPress 1|
|Are you a railway personnel?:\tPress 2|
----------------------------------------
'''))
if person == 1:
    choice()
    if action == 1:
        booking()
    elif action == 2:
        train_details()
    elif action == 3:
        news()

elif person == 2:
    choice_admin()
    if action_admin == 1:
        train_details()
        update_data()
    elif action_admin == 2:
        news()
    elif action_admin == 3:
        edit_news()
        update_data()
