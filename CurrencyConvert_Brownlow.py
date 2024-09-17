#This program will let the user convert the American Dollar to different currencies.

#function used to convert USD to Euros
def EuroConvert(USD): 

    euro = 0.91 #variable 
    euro = float(euro) #casts the variable euro to a float 
    print(f"1 USD is {euro} euros") 
    euros = euro * USD #calculates the USD to euros 
    print("Euro to USD: ", round(euros, 2)) #prints out to terminal and rounds the variable euros two places

#function used to convert usd to yen 
def YenCovert(usd):

    yen = 147.20
    yen = float(yen)
    print(f"1 USD is {yen} yens")
    yens = yen * usd
    print("Yen to USD: ", round(yens, 2))

#function used to convert usd to wons
def WonConvert(USD):

    won = 1368.21
    won = float(won)
    print(f"1 USD is {won} wons")
    wons = won * USD
    print("Won to USD: ", round(wons, 2))

#function used to convert usd to pounds
def PoundConvert(USD):

    pound  = 0.78
    pound = float(pound)
    print(f"1 USD is {pound} pounds")
    pounds = pound * USD
    print("Pounds to USD: ", round(pounds, 2))

#function used to convert usd to aussie dollars 
def AussieConvert(USD):

    Aussie = 1.52
    Aussie = float(Aussie)
    print(f"1 USD is {Aussie} AUDs")
    AUDs = Aussie * USD
    print("Aussie Dollars to USD: ", round(AUDs, 2))

#function used to convert usd to indian rupees
def IndianConvert(USD):

    Rupee = 83.94
    Rupee = float(Rupee)
    print(f"1 USD is {Rupee} rupees")
    Rupees = Rupee * USD
    print("Indian Rupees to USD: ", round(Rupees, 2))

#functon used to convert usd to pesos
def PesoConvert(USD):

    peso = 19.05
    peso = float(peso)
    print(f"1 USD to {peso} pesos")
    pesos = peso * USD
    print("Mexican Pesos to USD: ", round(pesos, 2))

#drivercode

#string menu to store the diffent currencies 
menu = "\n1.Euro\n2.Yen\n3.Won\n4.Pound\n5.Aussie Dollar\n6.Indian Rupees\n7.Mexican Peso\n8.Quit"
print(menu) #prints out the menu

#asks the user to choose a exchange rate 
user = input("Enter the Exchange Rate would you like to use?")
UsDollar = int(input("Enter the dollar amount: ")) #asks the use to enter the amount they wound like to convert 

#if elif statement used to loop thru the menu 
if user == "1":
    EuroConvert(UsDollar) #call needed fuction to execute 
     

elif user == "2":
    YenCovert(UsDollar)

elif user == "3":
    WonConvert(UsDollar)

elif user == "4":
    PoundConvert(UsDollar)

elif user == "5":
    AussieConvert(UsDollar)

elif user == "6":
    IndianConvert(UsDollar)

elif user == "7":
    PesoConvert(UsDollar)
else: user == "8"

