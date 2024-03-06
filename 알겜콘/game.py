
 #lst / 체력, 공격력, 방어력, 마나, 돈, 경험치, maxHp, maxMp ,무기1, 무기2, 무기3, 방어구1, 방어구2, 방어구3, maxExp, level
#monster / 체력 공격력 돈 경험치
import time as t
import random

#스킬리스트
sk1 = ["힘껏치기","두번때리기","회복"]
sk1_txt = '''1. 힘껏치기: 기존공격보다 더 많은 피해
2. 두번때리기: 몬스터 두번 공격
3. 회복: 체력회복'''

sk2 = ["힘껏치기","두번때리기","회복","기절시키기"] #마나사용캐릭터
sk2_txt = '''1. 힘껏치기: 기존공격보다 더 많은 피해
2. 두번때리기: 몬스터 두번 공격
3. 회복: 체력회복
4. 기절시키기: 공격 후 일정확률로 몬스터 2턴동안 기절'''

def player_data():
    f=open("player_data.txt")
    lst=[]
    file=f.readlines()
    for i in range(len(file)):
        lst.append(int(file[i].strip()))
    return lst

def text():
    f=open("player_data.txt",'w')
    for i in range(21):
        f.writelines('%d'%0)
        f.writelines("\n")
        
def save(lst):
    lst_save()
    f=open("player_data.txt",'w')
    for i in range(len(lst)):
        lst[i]=str(lst[i])
        f.writelines(lst[i])
        f.writelines("\n")
        lst[i]=int(lst[i])
    f.close()
    print("저장되었습니다")
    line()
    return

def lst_save():
    global lst
    lst[0]=hp
    lst[1]=power
    lst[2]=armor
    lst[3]=mp
    lst[4]=money
    lst[5]=exp
    lst[6]=maxHp
    lst[7]=maxMp
    lst[14]=maxExp
    lst[15]=level

def line():
    print("-"*70)

def lline():
    print("-"*20)
    
def start():
    global lst
    q=int(input("시작하시겠습니까?\n1.예, 2.아니요\n"))
    if q==1:
        q=int(input("1.새로시작 2.불러오기\n"))
        print("로딩중")
        t.sleep(1)
        line()
        print("[상명대에 좀비 바이러스가 퍼져 사람들이 좀비가 되기 시작했다..]\n")
        t.sleep(2)
        print("<뉴스 속보>\n\"숙주 좀비를 살생하면 바이러스가 종식될 수 있을 것이라는 \n연구결과가 나오고 있스ㅂ니..치...치지직\"\n")
        t.sleep(3)
        print("-송신 오류-\n")
        t.sleep(2)
        print("\"...\"\n")
        t.sleep(2)
        print("\"내가 숙주를 잡아서 상명대를 구하겠어!\"")
        line()
        t.sleep(1)
        return q
    else:
        print(";;")
        start()
    


def choose_character():
    lline()
    print("1.복학생\n\n 체력:20\n 공격력:5")
    lline()
    print("2.새내기 신입생\n\n 체력:40\n 공격력:3")
    lline()
    print("3.대학원생\n\n 체력:15\n 공격력:2\n 마나:100")
    lline()
    choose = int(input("캐릭터를 선택해주세요(번호 입력):"))
    line()
    if choose>=1 and choose<=3:
        return choose
    else:
        
        choose_character()
    return

def town():
    #상점 또는 사냥터 선택
    num = int(input("0.능력치\n1.상점\n2.사냥터\n3.휴식\n4.저장하기\n"))
    line()
    if num ==0:
        ability()
        town()
    elif num ==1:
        store()
    elif num==2:
        dungeon()
    elif num==3:
        heal()
    elif num==4:
        save(lst)
        town()
    else:
        town()

def ability():
    lst_save()
    print("-"*10)
    print("Level[%d]" %(lst[15]))
    print("Hp[%d]" %(lst[0]))
    print("Power[%d]" %(lst[1]))
    print("Armor[%d]" %(lst[2]))
    print("Mp[%d]" %(lst[3]))
    print("Money[%d]" %(lst[4]))
    print("Exp[%d/%d]" %(exp,maxExp))
    print("-"*10)
    
    
def heal():
    global hp
    global mp
    hp = maxHp
    mp = maxMp
    print("치유됐습니다.")
    line()
    town()

def level_up():
    global lst
    global exp
    global maxExp
    global level
    global hp
    global power
    if lst[5] >= lst[14]:
        lst[5] -= maxExp
         #레벨업 필요 경험치가 계속 늘어난다고 칠 시
        lst[14] += 1 #경험치늘어나는정도는임의로정함
        lst[15] += 1
        level = lst[15]
        exp=lst[5]
        maxExp=lst[14]
        print("레벨 업! - lv.%d\n" %(level))
    if level== 5 or level == 10 or level == 15:
        learn_sk()
        return
    if level%2==0:
        lst[0]+=1
        hp=lst[0]
        print("체력 1증가")
        lline()
    elif level%2==1:
        lst[1]+=1
        power+=1
        print("공격력 1증가")
        lline()

def fight():
    #전투 둘중 하나의 체력이 0 또는 도망가기
    global hp
    global money
    global lst
    global exp
    global mp
    global money
    power=lst[1]
    maxHp=lst[6]
    maxMp=lst[7]
    
    hp_m=monster[0]
    power_m=monster[1]
    if maxMp == 0: #마나여부에 따라 체력, 마나 잔여량 표시 다르게
        print("player HP:",hp,"/",maxHp)
        print("%s HP: %d / %d"%(monster[4],hp_m,monster[0]))
        lline()
    else:
        print("player HP:",hp,"/",maxHp,"MP:",mp,"/",maxMp)
        print("%s HP: %d / %d"%(monster[4],hp_m,monster[0]))
        lline()
    damage = power_m-armor
    if damage<0:
        damage=0
    while hp>0 and hp_m>0:
        act = int(input("1.공격 2.스킬 3.도망가기\n"))
        lline()
        if act ==1:
            hp_m -= power
            print("기본 공격:",-power)
        elif act == 2: #스킬
            if len(p_sk) != 0: #배운 스킬이 있음
                print("스킬:",p_sk)
                print("어떤 스킬을 사용하시겠습니까?")
                if maxMp == 0: #마나사용불가능캐릭터
                    sk = int(input("1, 2, 3 중 하나 입력\n> "))
                    lline()
                    while p_sk[sk-1] == 0:
                        sk = int(input("배우지 않은 스킬입니다. 다시 선택\n> "))
                    if sk == 1:
                        #공격스킬
                        hp_m -= round(power*1.5)
                        print('"',p_sk[sk-1],'!"','(',-power*1.5,')')
                    if sk == 2:
                        #두번공격
                        hp_m -= power*2
                        print('"',p_sk[sk-1],'!"','(',-power*2,')')
                    if sk == 3:
                        #회복
                        healHp = round(maxHp*0.3)
                        hp += healHp
                        if hp > maxHp:
                            hp = maxHp
                        print("체력을 회복했다!")
                else: #마나 사용 캐릭터
                    sk = int(input("1, 2, 3, 4 중 하나 입력\n> "))
                    lline()
                    while p_sk[sk-1] == 0:
                        sk = int(input("배우지 않은 스킬입니다. 다시 선택\n> "))
                    if sk == 1:
                        #공격스킬
                        hp_m -= power*2
                        mp -= 3
                        print('"',p_sk[sk-1],'!"','(',-power*2,')')
                    if sk == 2:
                        #두번공격
                        hp_m -= power*4
                        mp -= 5
                        print('"',p_sk[sk-1],'!"','(',-power*4,')')
                    if sk == 3:
                        #회복
                        healHp = round(maxHp*0.3)
                        healMp = round(maxMp*0.3)
                        hp += healHp
                        if hp > maxHp:
                            hp = maxHp
                        mp += healMp
                        if mp > maxMp:
                            mp = maxMp
                        print("체력과 마력을 회복했다!")
                    if sk == 4:
                        #공격 후 일정 확률로 기절시킴
                        hp_m -= round(power*1.5)
                        mp -= 5
                        r = random.randrange(1,7)
                        print(r)
                        if r >= 3: #몬스터기절
                            print("몬스터를 기절시켰다!")
                            continue
            else: #배운 스킬이 없음
                print("사용할 수 있는 스킬이 없습니다.")
                act = int(input("1.공격 2.도망가기\n"))
                while act != 1 and act != 2:
                        act = int(input("잘못된 선택입니다. 다시 선택\n>"))
                if act ==1:
                    hp_m -= power
                    print("monster Hp:",hp_m,"/",monster[0])
                elif act == 2:
                    run()
                    break
        elif act == 3:
            run()
            break
        else:
            print("잘못된 선택")
            lline()
            fight()
        if maxMp == 0: #마나여부에 따라 체력, 마나 잔여량 표시 다르게
            if hp_m<=0:
                lline()
                print("player HP:",hp,"/",maxHp)
                print("%s HP: 0 / %d\n"%(monster[4],monster[0]))
            else:
                print("%s 의 공격: -%d" %(monster[4],damage))
                hp -= damage
                lline()
                print("player HP:",hp,"/",maxHp)
                print("%s HP: %d / %d\n"%(monster[4],hp_m,monster[0]))
        else:
            if hp_m<=0:
                lline()
                print("player HP:",hp,"/",maxHp,"MP:",mp,"/",maxMp)
                print("%s HP: 0 / %d\n"%(monster[4],monster[0]))
            else:
                print("%s 의 공격: -%d" %(monster[4],damage))
                hp -= damage
                lline()
                print("player HP:",hp,"/",maxHp,"MP:",mp,"/",maxMp)
                print("%s HP: %d / %d\n"%(monster[4],hp_m,monster[0]))
    if hp<=0:
        money=0
        lst[4]=0
        print("사망")
        lst_save()
        town()
    elif hp_m<=0:
        #몬스터 처치 경험치 돈추가
        lst[4]+=monster[2]
        money +=monster[2]
        lst[5]+=monster[3]
        exp+=monster[3]
        print("좀비 처치성공(exp[%d], money[%d] 획득)" %(monster[3],monster[2]))
        lline()
        level_up()
        n=4
        lst_save()
        while (n!=1 and n!=2) and n!=0:
            line()
            n = int(input("0.능력치 1.마을로 돌아가기 2.다음 던전으로 나아가기\n"))
            line()
            if n==1:
                town()
            elif n==2:
                nextdungeon()
            elif n==0:
                ability()
                n=4
    return

def learn_sk():
    global p_sk
    global maxMp
    global lst
    print("스킬을 배울 수 있습니다.")
    lline()
    print("어떤 스킬을 배우시겠습니까?\n")
    
    if maxMp == 0: #마나사용불가능태릭터
        print(sk1)
        print("\n")
        print(sk1_txt)
        print("\n")
        n = int(input("(1, 2, 3 중 1가지 선택)\n> "))
        while n != 1 and n != 2 and n != 3:
            n = int(input("잘못된 선택입니다. 다시 선택\n>"))
        p_sk = [0, 0, 0]
        p_sk[n-1] = sk1[n-1]
        print(sk1[n-1],"을/를 배웠다!")
        line()
        for i in range(16,20):
            if p_sk[i-16]!=0:
                lst[i]=1

    else:         #마나사용가능캐릭터
        print(sk2)
        print("\n")
        print(sk2_txt)
        print("\n")
        n = int(input("(1, 2, 3, 4 중 1가지 선택)\n> "))
        while n != 1 and n != 2 and n != 3 and n != 4:
            n = int(input("잘못된 선택입니다. 다시 선택\n>"))
        p_sk = [0, 0, 0, 0]
        p_sk[n-1] = sk2[n-1]
        print(sk2[n-1],"을/를 배웠다!")
        line()
        for i in range(16,20):
            if p_sk[i-16]!=0:
                lst[i]=1
    return

def run():
    print("도망쳤습니다")
    line()
    town()
    lst_save()
    return

#던전들 세팅
def dungeon():
    #몇번째 사냥터인지 선택
    which_dungeon = int(input("[1.상명대 입구 2.자하관 3.공학관 4.밀레니엄관 5.사범대학(최종보스)]\n\n※난이도는 1번이 가장 쉽고 번호가 올라갈수록 더 어려운 던전입니다.\n"))
    line()
    if which_dungeon == 1:
        dungeon1_1()
    elif which_dungeon == 2:
        dungeon2_1()
    elif which_dungeon == 3:
        dungeon3_1()
    elif which_dungeon == 4:
        dungeon4_1()
    elif which_dungeon == 5:
        dungeon5_1()
    return

def nextdungeon():
    if place==11:
        dungeon1_2()
    elif place==12:
        dungeon1_3()
    elif place==13:
        dungeon1_4()
    elif place==14:
        dungeon1_5()
    elif place==15:
        print("상명대 입구 클리어")
        town()
    elif place==21:
        dungeon2_2()
    elif place==22:
        dungeon2_3()
    elif place==23:
        dungeon2_4()
    elif place==24:
        dungeon2_5()
    elif place==25:
        print("자하관 클리어")
        town()
    elif place==31:
        dungeon3_2()
    elif place==32:
        dungeon3_3()
    elif place==33:
        dungeon3_4()
    elif place==34:
        dungeon3_5()
    elif place==35:
        print("공학관 클리어")
        town()
    elif place==41:
        dungeon4_2()
    elif place==42:
        dungeon4_3()
    elif place==43:
        dungeon4_4()
    elif place==44:
        dungeon4_5()
    elif place==45:
        print("밀레니엄관 클리어")
        town()
    elif place==51:
        dungeon5_2()
    elif place==52:
        dungeon5_3()
    elif place==53:
        dungeon5_4()
    elif place==54:
        dungeon5_5()
    elif place==55:
        line()
        print("[숙주를 잡고 상명대를 지키는대 성공했다!]\n")
        t.sleep(1)
        print("\'내가 상명대의 영웅이 된거야..!\'\n")
        t.sleep(1)
        print("-End-")
        line()
        town()
        
        
        

def dungeon1_1():
    #첫번째 사냥터 몬스터 체력 및 공격력 세팅
    global monster
    global place
    print("[상명대 입구 1-1]")
    line()
    monster=[10,2,1,1,'버스정류장 학생좀비']
    place = 11 #장소를 11로 지정(다음 던전으로 넘어갈때 사용)
    fight()
    return
def dungeon1_2():
    global monster
    global place
    print("[상명대 입구 1-2]")
    line()
    monster=[11,2,2,2,'경사로 올라가는 학생좀비']
    place=12
    fight()
    return
def dungeon1_3():
    global monster
    global place
    print("[상명대 입구 1-3]")
    line()
    monster=[12,2,3,3,'7016 기다리는 학생좀비']
    place=13
    fight()
def dungeon1_4():
    global monster
    global place
    print("[상명대 입구 1-4]")
    line()
    monster=[15,3,4,4,'가방 휘두르는 학생좀비']
    place=14
    fight()
    return
def dungeon1_5():
    global monster
    global place
    print("[상명대 입구 1-5]")
    line()
    monster=[20,5,8,8,'차 운전하는 교수좀비']
    place=15
    Boss()
    fight()
    return

def dungeon2_1():
    #첫번째 사냥터 몬스터 체력 및 공격력 세팅
    global monster
    global place
    print("[자하관 2-1]")
    line()
    monster=[22,4,9,9,'역사콘텐츠전공 학생좀비']
    place = 21 #장소를 11로 지정(다음 던전으로 넘어갈때 사용)
    fight()
    return
def dungeon2_2():
    global monster
    global place
    print("[자하관 2-2]")
    line()
    monster=[25,5,10,10,'행정학부 학생좀비']
    place=22
    fight()
    return
def dungeon2_3():
    global monster
    global place
    print("[자하관 2-3]")
    line()
    monster=[28,5,11,11,'가족복지학과 학생좀비']
    place=23
    fight()
def dungeon2_4():
    global monster
    global place
    print("[자하관 2-4]")
    line()
    monster=[30,6,12,12,'국가안보학과 학생좀비']
    place=24
    fight()
    return
def dungeon2_5():
    global monster
    global place
    print("[자하관 2-5]")
    line()
    monster=[35,7,20,20,'자하관 교수좀비']
    place=25
    Boss()
    fight()
    return

def dungeon3_1():
    #첫번째 사냥터 몬스터 체력 및 공격력 세팅
    global monster
    global place
    print("[공학관 3-1]")
    line()
    monster=[40,6,21,21,'전기공학전공 학생좀비']
    place = 31 #장소를 11로 지정(다음 던전으로 넘어갈때 사용)
    fight()
    return
def dungeon3_2():
    global monster
    global place
    print("[공학관 3-2]")
    line()
    monster=[60,5,22,22,'게임전공 학생좀비']
    place=32
    fight()
    return
def dungeon3_3():
    global monster
    global place
    print("[공학관 3-3]")
    line()
    monster=[25,15,23,23,'지능IOT융합전공 학생좀비']
    place=33
    fight()
def dungeon3_4():
    global monster
    global place
    print("[공학관 3-4]")
    line()
    monster=[50,9,24,24,'컴퓨터과학전공 학생좀비']
    place=34
    fight()
    return
def dungeon3_5():
    global monster
    global place
    print("[공학관 3-5]")
    line()
    monster=[70,10,30,30,'공학관 교수좀비']
    place=35
    Boss()
    fight()
    return

def dungeon4_1():
    #첫번째 사냥터 몬스터 체력 및 공격력 세팅
    global monster
    global place
    print("[밀레니엄관 4-1]")
    line()
    monster=[72,8,31,31,'경제금융학부 학생좀비']
    place = 41 #장소를 11로 지정(다음 던전으로 넘어갈때 사용)
    fight()
    return
def dungeon4_2():
    global monster
    global place
    print("[밀레니엄관 4-2]")
    line()
    monster=[80,10,32,32,'글로벌경영학과 학생좀비']
    place=42
    fight()
    return
def dungeon4_3():
    global monster
    global place
    print("[밀레니엄관 4-3]")
    line()
    monster=[87,11,33,33,'경영학부 학생좀비']
    place=43
    fight()
def dungeon4_4():
    global monster
    global place
    print("[밀레니엄관 4-4]")
    line()
    monster=[95,12,34,34,'융합경영학과 학생좀비']
    place=44
    fight()
    return
def dungeon4_5():
    global monster
    global place
    print("[밀레니엄관 4-5]")
    line()
    monster=[110,14,50,50,'밀레니엄관 교수좀비']
    place=45
    Boss()
    fight()
    return

def dungeon5_1():
    #첫번째 사냥터 몬스터 체력 및 공격력 세팅
    global monster
    global place
    print("[사범대학관 5-1]")
    line()
    monster=[60,25,40,40,'교육학과 학생좀비']
    place = 51 #장소를 11로 지정(다음 던전으로 넘어갈때 사용)
    fight()
    return
def dungeon5_2():
    global monster
    global place
    print("[사범대학관 5-2]")
    line()
    monster=[150,10,42,42,'국어교육과 학생좀비']
    place=52
    fight()
    return
def dungeon5_3():
    global monster
    global place
    print("[사범대학관 5-3]")
    line()
    monster=[138,17,44,44,'영어교육과 학생좀비']
    place=53
    fight()
def dungeon5_4():
    global monster
    global place
    print("[사범대학관 5-4]")
    line()
    monster=[170,20,50,50,'수학교육과 학생좀비']
    place=54
    fight()
    return
def dungeon5_5():
    global monster
    global place
    print("[사범대학관 5-5]")
    line()
    monster=[200,35,100,100,'사범대학관 교수좀비(숙주)']
    place=55
    Boss()
    fight()
    return

def Boss():
    print("="*30)
    print("%17s" %("[보스 출현!!]"))
    print("="*30)


def store():
    global armor
    global lst
    global money
    global power
    
    while 1:
        print("[money: %d]"%(money))
        n = int(input("1.무기 구입 2.방어구 구입 3.나가기\n"))
        line()
        if n==1:
            print("[무기 리스트]")
            lline()
            print("1.낡은 검\n\n 공격력:+3\n 가격:100")
            lline()
            print("2.평범한 검\n\n 공격력:+10\n 가격:500")
            lline()
            print("3.전설의 검\n\n 공격력:+20\n 가격:1000")
            lline()
            a = int(input("어떤 검을 구입하시겠습니까?(번호 입력):"))
            line()
            if a==1:
                if lst[8]==0:
                    if money>=100:
                        power+=5
                        money-=100
                        lst[8]=1
                        print("낡은 검을 구매하였습니다.(공격력+3)")
                        print("[money: %d]"%(money))
                        line()
                    else:
                        print("돈이 부족합니다.")
                        line()
                else:
                    print("이미 구매된 상품입니다.")
                    line()
            elif a==2:
                if lst[9]==0:
                    if money>=500:
                        power+=10
                        money-=500
                        lst[9]=1
                        print("평범한 검을 구매하였습니다.(공격력+10)")
                        print("[money: %d]"%(money))
                        line()
                    else:
                        print("돈이 부족합니다.")
                        line()
                else:
                    print("이미 구매된 상품입니다.")
                    line()
            elif a==3:
                if lst[10]==0:
                    if money>=1000:
                        power+=20
                        money-=1000
                        lst[10]=1
                        print("전설의 검을 구매하였습니다.(공격력+20)")
                        print("[money: %d]"%(money))
                        line()
                    else:
                        print("돈이 부족합니다.")
                        line()
                else:
                    print("이미 구매된 상품입니다.")
                    line()
                
        elif n==2:
            print("[방어구 리스트]")
            lline()
            print("1.낡은 방어구\n\n 방어력:+1\n 가격:50")
            lline()
            print("2.평범한 방어구\n\n 방어력:+3\n 가격:200")
            lline()
            print("3.전설의 방어구\n\n 방어력:+5\n 가격:500")
            lline()
            a = int(input("어떤 방어구를 구입하시겠습니까?(번호 입력):"))
            line()
            if a==1:
                if lst[11]==0:
                    if money>=50:
                        armor+=1
                        money-=50
                        lst[11]=1
                        print("낡은 방어구를 구매하였습니다.(방어력+1)")
                        print("[money: %d]"%(money))
                        line()
                    else:
                        print("돈이 부족합니다.")
                        line()
                else:
                    print("이미 구매된 상품입니다.")
                    line()
            if a==2:
                if lst[12]==0:
                    if money>=200:
                        armor+=3
                        money-=200
                        lst[12]=1
                        print("평범한 방어구를 구매하였습니다.(방어력+3)")
                        print("[money: %d]"%(money))
                        line()
                    else:
                        print("돈이 부족합니다.")
                        line()
                else:
                    print("이미 구매된 상품입니다.")
                    line()
            if a==3:
                if lst[13]==0:
                    if money>=500:
                        armor+=5
                        money-=500
                        lst[13]=1
                        print("전설의 방어구를 구매하였습니다.(방어력+5)")
                        print("[money: %d]"%(money))
                        line()
                    else:
                        print("돈이 부족합니다.")
                        line()
                else:
                    print("이미 구매된 상품입니다.")
                    line()
        elif n==3:
            print("돈도 없으면서 여길 들어와?")
            line()
            break
        
    town()
            
    return

def main():
    #플레이어 데이터 불러오고 기본 스텟 세팅
    global lst
    global hp
    global maxHp
    global power
    global armor
    global mp
    global money
    global exp
    global maxMp
    global level
    global maxExp
    global p_sk
    lst = player_data()
    #시작 후 캐릭 고르기
    q=start()
    if q==1:
        text()
        print("[캐릭터 리스트]")
        for i in range(len(lst)):
            lst[i]=0
        character = choose_character()
        if character ==1:
            lst[0] = 20
            lst[6] = 20
            lst[1] = 5
        elif character == 2:
            lst[0] = 40
            lst[6] = 40
            lst[1] = 3
        elif character == 3:
            lst[0]= 15
            lst[6] = 15
            lst[1]= 2
            lst[3]=20
            lst[7]=20
        lst[14]=1
        lst[15]=1
    hp=lst[0]
    power=lst[1]
    armor=lst[2]
    mp=lst[3]
    money=lst[4]
    exp=lst[5]
    maxHp=lst[6]
    maxMp=lst[7]
    maxExp=lst[14]
    level=lst[15]
    p_sk=[lst[16],lst[17],lst[18],lst[19]]
    if maxMp==0:
        for i in range(4):
            if p_sk[i]==1:
                p_sk[i]=sk1[i]
    else:
        for i in range(4):
            if p_sk[i]==1:
                p_sk[i]=sk2[i]
    if q == 1 and character == 3: #대학원생캐릭터 스킬배우고시작
        learn_sk()
        #게임진행(마을)
    town()


main()
    

#추가해야할 내용
#스킬 사용(skill()에서 스킬이 있는지 확인 하고 스킬이 있으면 사용할 수 있도록 구현)
#상점이용(무기 또는 방어구 구매(무기와 방어구로 능력치 상승)) 
#캐릭터별 스탯 설명(시작전에 캐릭고를때)
#돈과 경험치(레벨업에 따른 능력치 상승)
#던전 추가(난이도 조절)

#불러오기 기능을 위한 저장(이건 내가 할거)



#print(lst)
