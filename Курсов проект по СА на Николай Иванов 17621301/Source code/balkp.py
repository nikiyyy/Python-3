# изготвено от Николай Иванов №17621301
# Стъпки на алгоритъма
#1 извличане на данните от тесктов токумент
#2 оформяне на данните
#3 балансиране на лсита ако вече не е балансиран
#4 		избиране на елемент за работа
#5 			избирам дефалтен елемент
#6			сравнявам този дефалтен елемент със другите елементи от листа и избирам най-подходящия елемент
#7 		избирам кое е по-малко supply или demand и го изваждам от по-голямото
#8 		отстранявам еленти без ресурси
#9 пресмятам Zmin
#10 записвам данните в текстов документ

from datetime import datetime  #импортирам библиотека datetime

def fun(Filename): # главната фукция за рещаване на задача по метода на минималния елемент
######################Файлов OUTPUT
    # стздавам временни променливи Bdemand, Bsupply и lista за обработка на соровите данни от тесктовия дойумент
    Bdemand=[] 
    Bsupply=[]
    lista=[]
    with open(Filename, 'r') as file:# отварчм текстов документ чиито име местоположение е записано в променливата Filename под формата на string
        index_counter=0# боряч който следи на кой ред се намира filepointera
        for i in file.readlines():# визима 1 необработен ред от файла и го разделя на индивидуални елементи, който после вкарва в съответните листи
            if index_counter == 0:#ако file pointer е в позиция 0 то данните ще влязат в Bdemand
                Bdemand=i.split()
    
            elif index_counter == 1:#ако file pointer е в позиция 1 то данните ще влязат в Bsupply
                Bsupply=i.split()
    
            elif index_counter>1:#ако file pointer е в позиция по голяма от 1 то данните ще влязат в Bsupply
                lista.append(i.split())
            index_counter+=1
    # demand и supply са трайните листове които държат обработините данни от текстовия документ
    demand=[]
    supply=[]
    for i in Bdemand: # вкарвам уформените от demand
        demand.append(int(i))
    
    for i in Bsupply: # вкарвам уформените от supply
        supply.append(int(i))
    
    S1=[]# В S1,S2 и S3 се съхраняват редовете с транспортните цени
    S2=[]
    S3=[]
    unBalList=[]# unBalList съдържа обработините цени на странспорта
    for i in lista:# В този фор цикъл се обработват данните от листа и се вкарват ред по ред S1,S2 и S3, които после влизат в unBalList
        for j in i:
            if lista.index(i) == 0:
                S1.append([int(j),True])
            elif lista.index(i) == 1:
                S2.append([int(j),True])
            elif lista.index(i) == 2:
                S3.append([int(j),True])
    unBalList.append(S1)# вакарвам вече уформените данни в финалния лист
    unBalList.append(S2)
    unBalList.append(S3)
	# Тук преключва файловата чат от програмата
	
#######################Блансиране на листа ако вече не е балансиран
    if int(len(demand)) < int(len(supply) ): #ако в supply има повече елементи от demand, листа е не балансиран
        for i in unBalList:#добавям празен елемент с цел баланс
            i.append([0, True])
        
        demand.append(sum(supply)-sum(demand))
#######################избиране на елемент за работа
    while sum(supply)+sum(demand) != 0: #този цикъл се повтаря докато ресурсите в supply и demand не се изразходят
        chosen_element=[]# Този лист запазва стойноста на избрания елемент
        chosen_element_demand=0#запазвам demand стойноста отговаряща за избрания елемент
        chosen_element_supply_index=0#запазвам индейса на supply отговарящ за избрания елемент
        chosen_element_demand_index=0#запазвам индейса на demand отговарящ за избрания елемент
        
        exitflag=False # ако този флаг е True значе вече имаме избран елемент,този флаг се ресетва всяка иерация на цикъла
        for i in unBalList: # С този двумерен фор цикъл се избира валиден дефалтен елемент за работа
            if exitflag == True:# ако имаме избран елемент излизаме от цикъла
                break
            first_index=unBalList.index(i) #брои първия индекс за еленент
            for j in i:
                second_index=i.index(j) #брои врория индекс за еленент
                if j[1]==True: # ако елемента е валиден/свободен ибва избран за дефалтен работен елемент, независимо дъли е оптимален
                    exitflag = True #флага става True и следващата иерация на цикъла излизаме от него
                    chosen_element=unBalList[first_index][second_index]
                    chosen_element_demand=demand[second_index]
                    chosen_element_supply_index=first_index
                    chosen_element_demand_index=second_index
                    break
        
        for i in unBalList: # В този двумерен цикъл се избира оптималния елемент за работа ако вече не е избран от предходната съпка
            first_index=unBalList.index(i) #брои първия индекс за еленент
            for j in i:
                second_index=i.index(j) #брои врория индекс за еленент
                if j[1] == True and j[0] <=chosen_element[0]: #ако елемента е свободен/валиден и стойноста на транспорта е по малка от тази на вече избрания елемент влизам продължавам напред
                    if j[0] == chosen_element[0]: # ако елементите имат еднакви транспортни стойности се избира този със по-големия demand
                        if demand[second_index] > chosen_element_demand:
                            chosen_element=chosen_element=unBalList[first_index][second_index]
                            chosen_element_demand=demand[second_index]
                            chosen_element_supply_index=first_index
                            chosen_element_demand_index=second_index
                        continue # пропускам тази итерация на цикъла
                    chosen_element=chosen_element=unBalList[first_index][second_index]
                    chosen_element_demand=demand[second_index]
                    chosen_element_supply_index=first_index
                    chosen_element_demand_index=second_index
                        
        # Избирам коя е по голямата стойност измежду supply и demand ,и от нея изваждам по-малката
        if supply[chosen_element_supply_index] <= demand[chosen_element_demand_index]: # ако supply е по малка ще я извадя от demand и ще я зануля
            demand[chosen_element_demand_index]-=supply[chosen_element_supply_index] # изваждам
            unBalList[chosen_element_supply_index][chosen_element_demand_index][1]=supply[chosen_element_supply_index] # замествам индекатора за свободност на клетката с количеството ресурси което ще се транспортира
            supply[chosen_element_supply_index]=0 #занулявам
            
            for i in unBalList: #прави елементите, чийто ресурси са изчерпани, невалидни
                first_index=unBalList.index(i) #брои първия индекс за еленент
                for j in i:
                    second_index=i.index(j) #брои второя индекс за еленент
                    if j[1] == True and first_index==chosen_element_supply_index: #проверка по елемент
                        j[1]=False
            
        elif supply[chosen_element_supply_index] > demand[chosen_element_demand_index]: # ако demand е по малка ще я извадя от supply и ще я зануля
            supply[chosen_element_supply_index]-=demand[chosen_element_demand_index] # изваждам
            unBalList[chosen_element_supply_index][chosen_element_demand_index][1]=demand[chosen_element_demand_index] # замествам индекатора за свободност на клетката с количеството ресурси което ще се транспортира
            demand[chosen_element_demand_index]=0 #занулявам
            
            for i in unBalList: #прави елементите, чийто ресурси са изчерпани, невалидни
                first_index=unBalList.index(i) #брои първия индекс за еленент
                for j in i:
                    second_index=i.index(j) #брои второя индекс за еленент
                    if j[1] == True and second_index==chosen_element_demand_index: #проверка по елемент
                        j[1]=False
                        
        #for i in unBalList : #изкарва таблицата на конзола с цел дебъгване , само трябва да се откоментира кода
        #    print(i,end='')
        #    print("       "+str(supply[unBalList.index(i)]))
        #print(demand)
        
        if sum(demand) + sum(supply)  == 0: #ако ресурсите са изчерпани и програмата е на прослената си итерация ще се пресметне цената 'Z'
            Z=0 # минималната цена
            for i in unBalList: # иерира през всички елементи на лста
                for j in i:
                    if j[1] !=False and j[1] !=0: # ако в летката има ресурси, към Z ще се добави сбора на цената на транспорта и ресурса
                        Z+=(j[1]*j[0])
            #print(Z) #изкарва минималната цена на конзола с цел дебъгване , само трябва да се откоментира кода
######################Файлов INPUT
            with open("minicost - "+str(datetime.now().strftime("%H-%M-%S"))+".txt", 'w') as file: #създавам фал със автоматично генериращо име (сегашно време)
                file.write(str(Z)) # записвам минималната цена в файла
                for i in unBalList:
                    file.write("\n") # записвам нов ред
                    for j in i:
                        if(j[1]==False): # записвам цните на транспорта и ресурсите в файл
                            file.write(" ("+str(j[0])+" 0)")
                        else:
                            file.write(" ("+str(j[0])+" "+str(j[1])+")")


