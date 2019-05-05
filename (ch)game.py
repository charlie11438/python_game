import time
import random

hp=50
intell=0
health=0
stragy=0

class event:
    def initial():
        print('歡迎來到此遊戲!')
        time.sleep(2)
        print('這個遊戲是關於pyhon與資料分析基礎')
        time.sleep(2)
        print('這個遊戲有三種不同的問題類型')
        time.sleep(2)
        print('智慧是關於python的基礎語法')
        time.sleep(2)
        print('健康是關於pandas的基礎')
        time.sleep(2)
        print('而策略則是有關matplotlib')
        time.sleep(2)
        print('選擇正確的選項可以得5分')
        time.sleep(2)
        print('但如果選錯了...生命值將會減少5分')
        time.sleep(2)
        print('你準備好了嗎?那就開始吧!')
        time.sleep(2)


    def show():
        print('生命值:',hp)
        print('智慧:',intell)
        print('健康:',health)
        print('策略:',stragy)

    def inte0():
        global hp
        global intell
        global health
        global stragy
        print('智慧事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生想寫出一程式')
        time.sleep(2)
        print('儲存輸入的數值然後排序')
        time.sleep(2)
        print('在python,你應該使用哪個選項')
        time.sleep(2)
        print('如果列表叫做number?')
        time.sleep(2)
        print('1:number.sort()')
        time.sleep(2)
        print('2:number.pop()')
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            intell=intell+5
            time.sleep(2)
            print('智慧+5')
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            hp=hp-5
            time.sleep(2)
            print('生命值-5')
            event.show()
            time.sleep(2)

    def inte1():
        global hp
        global intell
        global health
        global stragy
        print('智慧事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一學生想印出星星圖形')
        time.sleep(2)
        print('有五行')
        time.sleep(2)
        print('從1顆星到5顆星')
        time.sleep(2)
        print('哪個選項是正確的??')
        time.sleep(2)
        print('1:\nfor i in range(1,5):\nprint(''*''*i)')
        time.sleep(2)
        print('2:\nfor i in range(1,6):\nprint(''*''*i)')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='2':
            print('正確!')
            time.sleep(2)
            print('智慧+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def inte2():
        global hp
        global intell
        global health
        global stragy
        print('智慧事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一學生想寫出一個程式')
        time.sleep(2)
        print('如果使用者輸入一數字')
        time.sleep(2)
        print('程式將會判斷數字是否大於0')
        time.sleep(2)
        print('哪個選項是正確的??')
        time.sleep(2)
        print('1:\nnumber=eval(input())\nif number>0:\nprint(''bigger than 0'')\nelse:\nprint(''not bigger than 0'')')
        time.sleep(2)
        print('1:\nnumber=eval(input())\nif(number>0)\n{print(''bigger than 0'')}\nelse\n{print(''not bigger than 0'')}')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('智慧+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def inte3():
        global hp
        global intell
        global health
        global stragy
        print('智慧事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一學生想寫出一個程式')
        time.sleep(2)
        print('如果使用者輸入一些數字')
        time.sleep(2)
        print('程式會計算出這些數字的和')
        time.sleep(2)
        print('如使用者輸入-1,將會停止輸入')
        time.sleep(2)
        print('如果使用迴圈來進行判斷是否停止輸入')
        time.sleep(2)
        print('哪個選項是正確的?')
        time.sleep(2)
        print('1:while n != -1:')
        time.sleep(2)
        print('2:while n <= -1:')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('智慧+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)


    def inte4():
        global hp
        global intell
        global health
        global stragy
        print('智慧事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生想寫出一個程式判斷數字是否為質數')
        time.sleep(2)
        print('但如果使用者輸入非整數')
        time.sleep(2)
        print('程式將會報錯並關閉')
        time.sleep(2)
        print('如果學生想使程式不會報錯然後關閉')
        time.sleep(2)
        print('他應該要選擇哪個選項?')
        time.sleep(2)
        print('1:try:...except IOError:...')
        time.sleep(2)
        print('2:try:...except ValueError:...')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        if ans=='2':
            print('正確!')
            time.sleep(2)
            print('智慧+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def inte5():
        global hp
        global intell
        global health
        global stragy
        print('智慧事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一學生想寫出一個程式')
        time.sleep(2)
        print('來顯示出月曆')
        time.sleep(2)
        print('但程式報出沒有這個方法')
        time.sleep(2)
        print('他需要怎麼做?')
        time.sleep(2)
        print('1:導入模組')
        time.sleep(2)
        print('2:重新啟動IDE')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('智慧+5')
            intell=intell+5
            time.sleep(2)
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea0():
        global hp
        global intell
        global health
        global stragy
        print('健康事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一學生想寫出一個程式')
        time.sleep(2)
        print('想讀取一個csv檔並儲存成dataframe')
        time.sleep(2)
        print('哪個選項是正確的?')
        time.sleep(2)
        print('1:import pandas as pd\npd.read_xls(''data.csv'')')
        time.sleep(2)
        print('2:import pandas as pd\npd.read_csv(''data.csv'')')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='2':
            print('正確')
            time.sleep(2)
            print('健康+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea1():
        global hp
        global intell
        global health
        global stragy
        print('健康事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個資料工程師在預處理資料')
        time.sleep(2)
        print('他找出資料中有些缺失值')
        time.sleep(2)
        print('如果他想填補缺失值')
        time.sleep(2)
        print('他應該使用哪個方法?')
        time.sleep(2)
        print('1:data.fillna(0)')
        time.sleep(2)
        print('2:data.dropna(inplace=True)')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確')
            time.sleep(2)
            print('健康+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea2():
        global hp
        global intell
        global health
        global stragy
        print('健康事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個資料分析師在分析資料')
        time.sleep(2)
        print('此資料有100行和20列')
        time.sleep(2)
        print('現在他想切片: 50:100 行,第3列')
        time.sleep(2)
        print('哪個選項是正確的?')
        time.sleep(2)
        print('1:data.iloc[49:100,3]')
        time.sleep(2)
        print('2:data.loc[49:100,3]')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確')
            time.sleep(2)
            print('健康+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea3():
        global hp
        global intell
        global health
        global stragy
        print('健康事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生正在練習解讀敘述性統計的值')
        time.sleep(2)
        print('他正在處理資料')
        time.sleep(2)
        print('如果他想列出大部分敘述性統計的值')
        time.sleep(2)
        print('他應該使用哪個方法?')
        time.sleep(2)
        print('1:data.mean()')
        time.sleep(2)
        print('2:data.describe()')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='2':
            print('正確')
            time.sleep(2)
            print('健康+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea4():
        global hp
        global intell
        global health
        global stragy
        print('健康事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個資料分析師想新增一個dataframe')
        time.sleep(2)
        print('顯示出每年的平均價格')
        time.sleep(2)
        print('這個資料有三個欄位:')
        time.sleep(2)
        print('year,price和month')
        time.sleep(2)
        print('他應該使用哪個選項?')
        time.sleep(2)
        print('1:pd.pivot_table(data,index=year,columns=month,values=price,aggfunc=np.mean')
        time.sleep(2)
        print('2:data.groupby(by=''year'')')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('健康+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def hea5():
        global hp
        global intell
        global health
        global stragy
        print('健康事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生想處理資料')
        time.sleep(2)
        print('他發現此資料有許多重複的值')
        time.sleep(2)
        print('如果他想清理這份資料')
        time.sleep(2)
        print('他應該使用哪個方法?')
        time.sleep(2)
        print('1:data.dropna()')
        time.sleep(2)
        print('2:data.drop_duplicate()')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='2':
            print('正確')
            time.sleep(2)
            print('健康+5')
            time.sleep(2)
            health=health+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)


    def stra0():
        global hp
        global intell
        global health
        global stragy
        print('策略事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生想做資料視覺化')
        time.sleep(2)
        print('他想繪出長條圖')
        time.sleep(2)
        print('哪個選項是正確的?')
        time.sleep(2)
        print('1:plt.bar()')
        time.sleep(2)
        print('2:plt.plot()')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('策略+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra1():
        global hp
        global intell
        global health
        global stragy
        print('策略事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生正在練習資料視覺化')
        time.sleep(2)
        print('他想繪出資料的變化')
        time.sleep(2)
        print('他應該使用哪個方法?')
        time.sleep(2)
        print('1:plt.pie()')
        time.sleep(2)
        print('2:plt.boxplot()')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='2':
            print('正確!')
            time.sleep(2)
            print('策略+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra2():
        global hp
        global intell
        global health
        global stragy
        print('策略事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個資料分析師想繪出圓餅圖')
        time.sleep(2)
        print('他有一份有三個欄位的資料:')
        time.sleep(2)
        print('Big,medium and small size')
        time.sleep(2)
        print('他應該選擇哪個方法?')
        time.sleep(2)
        print('1:plt.pie(data.iloc[0,:],labels=[''Big'',''medium'',''small''],autopct=''%1.2f%%)')
        time.sleep(2)
        print('2:plt.plot(data[''Big''],marker=''o'')')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('策略+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra3():
        global hp
        global intell
        global health
        global stragy
        print('策略事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個學生正在做資料視覺化')
        time.sleep(2)
        print('他想新增一個1500x1400的畫布')
        time.sleep(2)
        print('他應該選擇哪個選項?')
        time.sleep(2)
        print('1:plt.figure(figsize=(15,14))')
        time.sleep(2)
        print('2:z1.add_subplots(2,1,1)')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('策略+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra4():
        global hp
        global intell
        global health
        global stragy
        print('策略事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個資料分析師正在繪出一個圖形')
        time.sleep(2)
        print('他想要在圖形上加上標題')
        time.sleep(2)
        print('他應該選擇哪個選項?')
        time.sleep(2)
        print('1:plt.title()')
        time.sleep(2)
        print('2:plt.xticks()')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('策略+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
            time.sleep(2)
            hp=hp-5
            event.show()
            time.sleep(2)

    def stra5():
        global hp
        global intell
        global health
        global stragy
        print('策略事件發生!')
        time.sleep(2)
        print('事件:')
        time.sleep(2)
        print('一個資料分析師在繪製圖表')
        time.sleep(2)
        print('這是一個長條圖,顯示出2001~2018的資料')
        time.sleep(2)
        print('如果他想在x軸增加刻度,顯示出年分')
        time.sleep(2)
        print('有一個列表儲存年分:yeararr')
        time.sleep(2)
        print('他應該使用哪個選項?')
        time.sleep(2)
        print('1:plt.xticks(range(17),yeararr,rotation=45)')
        time.sleep(2)
        print('2:plt.xlabel(''yeararr'')')
        time.sleep(2)
        ans=input('請輸入選項:')
        time.sleep(5)
        print()
        if ans=='1':
            print('正確!')
            time.sleep(2)
            print('策略+5')
            time.sleep(2)
            stragy=stragy+5
            event.show()
            time.sleep(2)
        else:
            print('錯誤!')
            time.sleep(2)
            print('生命值-5')
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
    print('遊戲結束!')
    time.sleep(2)
    print('最後成績:')
    time.sleep(2)
    event.show()

