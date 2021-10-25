import json
def edit_quiz(data):
    print("Avaliable quizes for edit:")
    l = data['quiz'].keys()
    for i in l:
        print(i)
    a = input(":")
    print("Avaliable questions for edit:")
    ss = data['quiz'][a].keys()
    for j in ss:
        print(j)
    sss = input(":")
    print(data['quiz'][a][sss]['Q'])
    print('A', data['quiz'][a][sss]['A'], '\n', 'B', data['quiz'][a][sss]['B'], '\n', 'C',
          data['quiz'][a][sss]['C'], '\n', 'D', data['quiz'][a][sss]['D'], '\n')

    print("Q to edit question A to edit option A, B to edit to option B and so on:")
    ssss = input(":")
    re = input("matter you want to replace:")
    data['quiz'][a][sss][ssss] = re
    print("sucesssfully replaced")
    print("\n\n<------------------------------------------------------->\n\n")
def view_topics(data):
    l = data['quiz'].keys()
    for i in l:
        print(i)
    a = input('select a quiz above:')
    aa=data['quiz'][a].keys()
    for i in aa:
        print(data['quiz'][a][i]['t'])
    print("\n\n<------------------------------------------------------->\n\n")
def edit_topics(data):
    l=data['quiz'].keys()
    for i in l:
        print(i)
    a=input('select a quiz above:')
    aa=data['quiz'][a].keys()
    for j in aa:
        print(j)
    aaa=input('select a question above:')
    s=input("entre the topic which used to be placed :")
    data['quiz'][a][aaa]['t']= s
    print("\n\n<------------------------------------------------------->\n\n")
def crete_quiz(data):
    a = input("Enter the quiz name:")
    b = int(input("chosse no of questions"))
    k = {}
    for i in range(1, b + 1):
        t = {}
        que = input("enetr the question:")
        qd = input("enter the question discription:")
        ql = input("enter the level(E,M,H):")
        top = input("entre the topic:")
        A = input("enter the option A:")
        B = input("enter the option B:")
        C = input("enter the option C:")
        D = input("enter the option D:")
        ans = input("set the correct option:")
        t['Q'] = que
        t['qd'] = qd
        t['ql'] = ql
        t['t'] = top
        t['A'] = A
        t['B'] = B
        t['C'] = C
        t['D'] = D
        t['ans'] = ans
        k[i] = t
    data['quiz'][a] = k
    print("\n\n<------------------------------------------------------->\n\n")
def admin_menu():

    while True:
        print('Main menu\n1)View Quizzes\n2)Create Quiz\n3)Edit Quiz\n4)Delete Quiz\n6)View Topics\n7)Edit Topics\n9)exit')
        choice=int(input(":"))
        if choice==1:
            print("Avaliable quizes:")
            l=data['quiz'].keys()
            for i in l:
                print(i)
        elif choice==2:
            crete_quiz(data)
        elif choice == 9:
            end(data)

        elif choice == 3:
            edit_quiz(data)
        elif choice == 4:
            print("Avaliable quizes:")
            l = data['quiz'].keys()
            for i in l:
                print(i)
            a=input("enetre the quiz to delete:")
            del data['quiz'][a]
        elif choice == 6:
            view_topics(data)
        elif choice ==7:
            edit_topics(data)
        print("\n\n<------------------------------------------------------->\n\n")


def perform_quiz(data,key,username):
    if key in data['quiz'].keys():
        count=0
        res={}
        questions=data['quiz'][key].keys()
        for i in questions:
            print('Q:',data['quiz'][key][i]['Q'])

            print('question discription:',data['quiz'][key][i]['qd'])
            print('question level:',data['quiz'][key][i]['ql'])
            print('question topic:',data['quiz'][key][i]['t'])
            print('A',data['quiz'][key][i]['A'],'\n','B',data['quiz'][key][i]['B'],'\n','C',data['quiz'][key][i]['C'],'\n','D',data['quiz'][key][i]['D'],'\n')
            ans=input("your answer:")
            res[i]=ans
            if data['quiz'][key][i]['ans']== ans:
                if data['quiz'][key][i]['ql'] == 'E':
                    count+=5
                elif data['quiz'][key][i]['ql'] == 'M':
                    count += 10
                else:
                    count +=15
        print('Name:',data['user_details'][username]['name'])
        for j in questions:
            print(data['quiz'][key][j]['Q'])
            print('ANS:',data['quiz'][key][j]['ans'])
        print('total score=',count)
        print("\n\n<------------------------------------------------------->\n\n")
def test_menu(data,username):
    while True:
        print('Main menu\n1)Take Quiz\n2)exit')
        a=int(input(':'))
        if a==1:
            l=data['quiz'].keys()
            print('<----available quiz---->\n')
            for i in  l:
                print(i)
            c=input("please enter the quiz name:")
            perform_quiz(data,c,username)
        elif a==2:
            end(data)
        else:
            print("no proper input.")
        print("\n\n<------------------------------------------------------->\n\n")
def end(data):
    #data={"user_details": {"sujith@123": {"name": "sujithkumar", "password": "1234"}, "s@123": {"name": "sushma", "password": "1234"}}, "quiz": {"title":{1: {'Q': "who is the pm of india?", "A": "modi", "B": "bodi", "C": "Kedi", "D": "dd", "ans":  "A"}}}}
    with open('result.json', 'w') as fp:
        json.dump(data, fp)
    exit()

def creat_user(data):
    name=input('enter your name:')
    username=input('enter the username:')
    setpass=input('set password:')
    tem = {}
    tem['name']=name
    tem['password']=setpass
    data['user_details'][username]=tem
    print("\n\n<------------------------------------------------------->\n\n")

if __name__ == '__main__':

    f=open('result.json')
    data =json.load(f)

    admin_user='admin'
    admin_password ='1234'
    print('<*-*-*-*-*-*-*-*-*-*-*-*-WELCOME-*-*-*-*-*-*-*-*-*-*-*-*>\n Login:\n\n1)Admin\n2)Student\n')
    user_choice=int(input(":"))


    if user_choice == 1:
        login=input('User name:')
        password=input('Password :')

        if login == admin_user and password == admin_password:
            admin_menu()
        else:
            print("entered deatils are wrong")
    elif user_choice ==2:
        while True :
            print('1)login\n2)register\n3)exit\n')
            a=int(input(':'))
            if a==1:
                username=input('enter user name:')
                password=input('enter password :')
                if username in data['user_details'].keys():
                    if password==data['user_details'][username]['password']:
                        test_menu(data,username)
                    else:
                        print("incorrect password")
                else:
                    print("User name not found")
            elif a==2:
                creat_user(data)
            elif a==3:
                end(data)
            else:
                print('please select a proper input.')

    else:
        print('Please select proper Account')

