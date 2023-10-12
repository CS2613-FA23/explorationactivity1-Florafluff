import pandas as pd

def ADDC(df, listIn, name):
    newdf = pd.DataFrame(listIn, columns=[name])
    return pd.concat([df, newdf], axis=1)

def ADDR(df, listIn):
    newdf = pd.DataFrame([listIn], columns=list(df.columns))
    return pd.concat([df, newdf], ignore_index=True)

def REMC(df, name):
    try:
        return df.drop(name, axis=1)
    except KeyError:
        print("Invalid Column Name")
        return df

def REMR(df, row):
    try:
        df = df.drop(int(row))
        df = df.reset_index()
        return REMC(df, "index")
    except KeyError:
        print("Invalid Row Number")
        return df

name = input("Enter your spreadsheet's file name: ")
try:
    df = pd.read_csv(name)
except FileNotFoundError:
    print("Invalid file name")
    exit()
print(df.to_string())
done = False
columnName = ""
newList = []
temp = 0
print("\nCommand list:\n"
          + "ADDC: adds a column to the spreadsheet.\n"
          + "ADDR: adds a row to the spreadsheet.\n"
          + "REMC: removes a column from the spreadsheet\n"
          + "REMR: removes a row from the spreadsheet\n"
          + "DONE: finalizes all operations.")
while(done==False):
    command = input("Input command: ")
    if(command=="ADDC"):
        columnName = input("Enter the name of the column: ")
        for i in range(df.shape[0]):
            temp = input("Enter value for row " + str(i) + ": ")
            newList.append(temp)
        df = ADDC(df, newList, columnName)
        newList = []
    elif(command=="ADDR"):
        for i in range(df.shape[1]):
            temp = input("Enter value for column " + str(i) + ": ")
            newList.append(temp)
        df = ADDR(df, newList)
    elif(command=="REMC"):
        columnName = input("Enter the name of the column to delete: ")
        df = REMC(df, columnName)
    elif(command=="REMR"):
        columnName = input("Enter the row number to delete: ")
        df = REMR(df, columnName)
    elif(command=="DONE"):
        done = True
    else:
        print("Invalid command")
    
    if(done!=True):
        print(df.to_string())

print("Output spreadsheet to csv or excel? ")
output = input("\"CSV\" for csv file\n\"EXCEL\" for excel file\n")
fileName = input("Input name for new file (don't include file extension): ")


valid = False
while(valid == False):
    if(output == "CSV"):
        try:
            f = open(fileName + ".csv", "x")
            valid = True
        except FileExistsError:
            fileName = input("File name already exists, enter a new one: ")
    elif(output == "EXCEL"):
        try:
            f = open(fileName + ".xlsx", "x")
            valid = True
        except FileExistsError:
            fileName = input("File name already exists, enter a new one: ")
    else:
        output = input("Please input a correct output type: ")
    
if(output == "CSV"):
    df.to_csv(fileName + ".csv")
elif(output == "EXCEL"):
    df.to_excel(fileName + ".xlsx")

f.close()