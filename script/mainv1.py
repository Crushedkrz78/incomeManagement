"""
Python Income Manager V1

Calculate income status using an Input Data File (CSV File) from an Excel File
"""
import csv



"""
For this file it's needed to make calculations with some specific columns.
1, 4, 5...
1 - Price
4 - Income or Spending or Movement (Movement do Nothing for now)
5 - Which account is the movement
"""

#This is for the starting Money (Total Money)
initial_state = 5737.82
initial_santander = 2841.46
initial_banamex = 2726.36
initial_cash = 170

with open("data/initial_data1.csv","r") as initial:
    csv_file = csv.reader(initial,delimiter=';')

    for row in csv_file:
        price = float(row[1].replace(',','.'))
        #print(float(price))
        type_of_transact = row[4]
        #print(type_of_transact)

        if(type_of_transact == "Gasto"):
            price = -1*(price)
        elif(type_of_transact == "Movimiento"):
            price = 0
            
        account = row[5]
        if(account == "Tarjeta Santander"):
            initial_santander += price
        elif(account == "Tarjeta Banamex"):
            initial_banamex += price
        else:
            initial_cash += price
        #initial_state = initial_state + price
    
    print("Resultado final: Santander: %s\n Banamex: %s\n Efectivo:%s" %(initial_santander,initial_banamex,initial_cash))
