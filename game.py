import time
import random

hp=50
intell=0
health=0
stragy=0

class event:
    def initial():
        print('welcome to this game!')
        time.sleep(2)
        print('This game is about python and data analysis')
        time.sleep(2)
        print('This game has three type question')
        time.sleep(2)
        print('intelligence is about basic python syntax')
        time.sleep(2)
        print('health is about pandas')
        time.sleep(2)
        print('strategy is about matplotlib')
        time.sleep(2)
        print('choose the right option can get 5 point')
        time.sleep(2)
        print('but if wrong...hp will decrease 5')
        time.sleep(2)
        print('Are you ready?Let''s start!')
        time.sleep(2)


    def show():
        print('hp:',hp)
        print('intelligence:',intell)
        print('health:',health)
        print('strategy:',stragy)

    def inte0():
        global hp
        global intell
        global health
        global stragy
        print('intelligence event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('The student wants to write a function')
        time.sleep(2)
        print('to save the number input and sorted')
        time.sleep(2)
        print('In python,which option  should you write')
        time.sleep(2)
        print('If list named number?')
        time.sleep(2)
        print('1:number.sort()')
        time.sleep(2)
        print('2:number.pop()')
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right!')
            time.sleep(2)
            intell=intell+5
            time.sleep(2)
            print('intelligence+5')
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            hp=hp-5
            time.sleep(2)
            print('hp-5')
            event.show()
            time.sleep(2)

    def inte1():
        global hp
        global intell
        global health
        global stragy
        print('intelligence event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to print star graph')
        time.sleep(2)
        print('With 5 rows')
        time.sleep(2)
        print('starts with 1 star and ends with 5 stars')
        time.sleep(2)
        print('which option is right?')
        time.sleep(2)
        print('1:\nfor i in range(1,5):\nprint(''*''*i)')
        time.sleep(2)
        print('2:\nfor i in range(1,6):\nprint(''*''*i)')
        time.sleep(2)
        print('which option is right?')
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='2':
            print('Right!')
            time.sleep(2)
            print('intelligence+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def inte2():
        global hp
        global intell
        global health
        global stragy
        print('intelligence event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to write a program')
        time.sleep(2)
        print('If user input a number')
        time.sleep(2)
        print('Program will detect this number is bigger than 0 or not')
        time.sleep(2)
        print('which option is right?')
        time.sleep(2)
        print('1:\nnumber=eval(input())\nif number>0:\nprint(''bigger than 0'')\nelse:\nprint(''not bigger than 0'')')
        time.sleep(2)
        print('1:\nnumber=eval(input())\nif(number>0)\n{print(''bigger than 0'')}\nelse\n{print(''not bigger than 0'')}')
        time.sleep(2)
        print('which option is right?')
        ans=input('please input option:')
        time.sleep(5)
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('intelligence+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def inte3():
        global hp
        global intell
        global health
        global stragy
        print('intelligence event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to write a program')
        time.sleep(2)
        print('If user input some numbers')
        time.sleep(2)
        print('Program will compute sum of numbers')
        time.sleep(2)
        print('input will end with inputting -1')
        time.sleep(2)
        print('If we use while loop to determine input is end or not')
        time.sleep(2)
        print('which option is right?')
        time.sleep(2)
        print('1:while n != -1:')
        time.sleep(2)
        print('2:while n <= -1:')
        time.sleep(2)
        print('which option is right?')
        ans=input('please input option:')
        time.sleep(5)
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('intelligence+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)


    def inte4():
        global hp
        global intell
        global health
        global stragy
        print('intelligence event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to write a program to determine input is prime or not')
        time.sleep(2)
        print('but once user input number that is not integer')
        time.sleep(2)
        print('The program will close with reporting error')
        time.sleep(2)
        print('If the student wants to write code that prevent closing program suddenly')
        time.sleep(2)
        print('Which option should him write?')
        time.sleep(2)
        print('1:try:...except IOError:...')
        time.sleep(2)
        print('2:try:...except ValueError:...')
        time.sleep(2)
        print('which option is right?')
        ans=input('please input option:')
        time.sleep(5)
        if ans=='2':
            print('Right!')
            time.sleep(2)
            print('intelligence+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def inte5():
        global hp
        global intell
        global health
        global stragy
        print('intelligence event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to write a program')
        time.sleep(2)
        print('To show the calender')
        time.sleep(2)
        print('But there shows the error that has no method to use')
        time.sleep(2)
        print('What should him do?')
        time.sleep(2)
        print('1:import modules')
        time.sleep(2)
        print('2:restart the IDE')
        time.sleep(2)
        print('which option is right?')
        ans=input('please input option:')
        time.sleep(5)
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('intelligence+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea0():
        global hp
        global intell
        global health
        global stragy
        print('health event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to write a program')
        time.sleep(2)
        print('To read a csv file named data as dataframe')
        time.sleep(2)
        print('Which option is Right?')
        time.sleep(2)
        print('1:import pandas as pd\npd.read_xls(''data.csv'')')
        time.sleep(2)
        print('2:import pandas as pd\npd.read_csv(''data.csv'')')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='2':
            print('Right')
            time.sleep(2)
            print('health+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea1():
        global hp
        global intell
        global health
        global stragy
        print('health event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A data engineer is preprocessing the data')
        time.sleep(2)
        print('He found that has some null values in data')
        time.sleep(2)
        print('If he want to fill null values')
        time.sleep(2)
        print('Which method will he use?')
        time.sleep(2)
        print('1:data.fillna(0)')
        time.sleep(2)
        print('2:data.dropna(inplace=True)')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right')
            time.sleep(2)
            print('health+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea2():
        global hp
        global intell
        global health
        global stragy
        print('health event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A data anaylst is analysing the data')
        time.sleep(2)
        print('The data has 100 rows and 4 columns')
        time.sleep(2)
        print('Now she wants to slice the data that is 50:100 rows and columns is 3')
        time.sleep(2)
        print('Which option is right?')
        time.sleep(2)
        print('1:data.iloc[49:100,3]')
        time.sleep(2)
        print('2:data.loc[49:100,3]')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right')
            time.sleep(2)
            print('health+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea3():
        global hp
        global intell
        global health
        global stragy
        print('health event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student is exercising to explain the describe statistics')
        time.sleep(2)
        print('He is processing a data')
        time.sleep(2)
        print('If he wants the program shows all the describe statistics values')
        time.sleep(2)
        print('Which method should him use?')
        time.sleep(2)
        print('1:data.mean()')
        time.sleep(2)
        print('2:data.describe()')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='2':
            print('Right')
            time.sleep(2)
            print('health+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea4():
        global hp
        global intell
        global health
        global stragy
        print('health event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A data anaylst wants to create a dataframe')
        time.sleep(2)
        print('That shows every year''s average price')
        time.sleep(2)
        print('This data has three columns:')
        time.sleep(2)
        print('year,price and month')
        time.sleep(2)
        print('Which option should him use?')
        time.sleep(2)
        print('1:pd.pivot_table(data,index=year,columns=month,values=price,aggfunc=np.mean')
        time.sleep(2)
        print('2:data.groupby(by=''year'')')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right')
            time.sleep(2)
            print('health+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea5():
        global hp
        global intell
        global health
        global stragy
        print('health event occured!')
        time.sleep(2)
        print('Event:')
        time.sleep(2)
        print('A student wants to processing a data')
        time.sleep(2)
        print('He finds that data has a lot repeating values')
        time.sleep(2)
        print('If he wants to clear the data')
        time.sleep(2)
        print('Which method should him use?')
        time.sleep(2)
        print('1:data.dropna()')
        time.sleep(2)
        print('2:data.drop_duplicate()')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='2':
            print('Right')
            time.sleep(2)
            print('health+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)


    def stra0():
        global hp
        global intell
        global health
        global stragy
        print('strategy event occured!')
        time.sleep(2)
        print('event:')
        time.sleep(2)
        print('A man wants to do data visualization')
        time.sleep(2)
        print('To draw the bar graph')
        time.sleep(2)
        print('Which option is right?')
        time.sleep(2)
        print('1:plt.bar()')
        time.sleep(2)
        print('2:plt.plot()')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('strategy+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra1():
        global hp
        global intell
        global health
        global stragy
        print('strategy event occured!')
        time.sleep(2)
        print('event:')
        time.sleep(2)
        print('A student is exercising data visulization')
        time.sleep(2)
        print('He wants to draw the graph that shows the change of data')
        time.sleep(2)
        print('Which method should him use?')
        time.sleep(2)
        print('1:plt.pie()')
        time.sleep(2)
        print('2:plt.boxplot()')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='2':
            print('Right!')
            time.sleep(2)
            print('strategy+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra2():
        global hp
        global intell
        global health
        global stragy
        print('strategy event occured!')
        time.sleep(2)
        print('event:')
        time.sleep(2)
        print('A data anaylst wants to draw a pie chart that shows the percentage of values')
        time.sleep(2)
        print('She has the data that has three columns:')
        time.sleep(2)
        print('Big,medium and small size')
        time.sleep(2)
        print('Which option should be right?')
        time.sleep(2)
        print('1:plt.pie(data.iloc[0,:],labels=[''Big'',''medium'',''small''],autopct=''%1.2f%%)')
        time.sleep(2)
        print('2:plt.plot(data[''Big''],marker=''o'')')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('strategy+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra3():
        global hp
        global intell
        global health
        global stragy
        print('strategy event occured!')
        time.sleep(2)
        print('event:')
        time.sleep(2)
        print('A student is doing data visualization')
        time.sleep(2)
        print('He wants to create a graph that is 1500x1400')
        time.sleep(2)
        print('Which option should him write?')
        time.sleep(2)
        print('1:plt.figure(figsize=(15,14))')
        time.sleep(2)
        print('2:z1.add_subplots(2,1,1)')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('strategy+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra4():
        global hp
        global intell
        global health
        global stragy
        print('strategy event occured!')
        time.sleep(2)
        print('event:')
        time.sleep(2)
        print('A data analyst is creating a graph')
        time.sleep(2)
        print('He creates a graph and wants to add a title')
        time.sleep(2)
        print('Which option ahould him use?')
        time.sleep(2)
        print('1:plt.title()')
        time.sleep(2)
        print('2:plt.xticks()')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('strategy+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra5():
        global hp
        global intell
        global health
        global stragy
        print('strategy event occured!')
        time.sleep(2)
        print('event:')
        time.sleep(2)
        print('A data anaylst is creating a graph')
        time.sleep(2)
        print('It is a bar graph that shows 2001~2018''s data')
        time.sleep(2)
        print('If she wants to set the axis x to show the year')
        time.sleep(2)
        print('There is an array store year label that names yeararr')
        time.sleep(2)
        print('Which option should she write?')
        time.sleep(2)
        print('1:plt.xticks(range(17),yeararr,rotation=45)')
        time.sleep(2)
        print('2:plt.xlabel(''yeararr'')')
        time.sleep(2)
        ans=input('please input option:')
        time.sleep(5)
        print()
        if ans=='1':
            print('Right!')
            time.sleep(2)
            print('strategy+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('Wrong!')
            time.sleep(2)
            print('hp-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)


count1=0
count2=0
count3=0

event.initial()

while (count1<5 or count2<5 or count3<5):
    x=random.randint(1,3)
    if hp==0:
        break
    if x==1:
        if count1==0:
            event.inte0()
            count1=count1+1
        elif count1==1:
            event.inte1()
            count1=count1+1
        elif count1==2:
            event.inte2()
            count1=count1+1
        elif count1==3:
            event.inte3()
            count1=count1+1
        elif count1==4:
            event.inte4()
            count1=count1+1
        elif count1==5:
            event.inte5()
            count1=count1+1
        else:
            pass
    elif x==2:
        if count2==0:
            event.hea0()
            count2=count2+1
        elif count2==1:
            event.hea1()
            count2=count2+1
        elif count2==2:
            event.hea2()
            count2=count2+1
        elif count2==3:
            event.hea3()
            count2=count2+1
        elif count2==4:
            event.hea4()
            count2=count2+1
        elif count2==5:
            event.hea5()
            count2=count2+1
        else:
            pass
    elif x==3:
        if count3==0:
            event.stra0()
            count3=count3+1
        elif count3==1:
            event.stra1()
            count3=count3+1
        elif count3==2:
            event.stra2()
            count3=count3+1
        elif count3==3:
            event.stra3()
            count3=count3+1
        elif count3==4:
            event.stra4()
            count3=count3+1
        elif count3==5:
            event.stra5()
            count3=count3+1
        else:
            pass

else:
    print()
    print('game over')
    time.sleep(2)
    print('Final grade:')
    time.sleep(2)
    event.show()

