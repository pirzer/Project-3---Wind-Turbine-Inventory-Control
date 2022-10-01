# Light program version of WindTurbines Inventory.
from datetime import datetime


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'


the_date = datetime.now().date()
print(" ")
print(f'{bcolors.YELLOW} ✇ Second Hand Windturbines. Inventory Tool ✇ ')
print(the_date)
print("==============================================")


class Windturbine:
    def __init__(self):
        self._name = ''
        self._mfg = ''
        self._model = ''
        self._country = ''
        self._year = 0        
        self._npower = 0   

    def addTurbine(self):
        try:
            self._uname = input('Agent-Name: ')
            self._mfg = input('Enter Windturbine Manufacturer: ')
            self._model = input('Enter Windturbine Model: ')
            self._country = input('Enter Country Location: ')
            self._year = int(input('Enter Windturbine year: '))
            self._npower = int(input('Enter Nominal Power [kW]: '))
            return True
        except ValueError:
            print(f'{bcolors.YELLOW}Enter year & power,and filled the form')
            return False

    def __str__(self):
        return '\t'.join(str(x) for x in [self._uname, self._mfg, self._model, self._country, self._year, self._npower])


class Inventory:
    def __init__(self):
        self.turbines = []

    def addTurbine(self):
        turbine = Windturbine()
        if turbine.addTurbine() is True:
            self.turbines.append(turbine)
            print()
            print('Fantastic!!! 😎, The Windturbine was added ✇')

    def viewInventory(self):
        print('\t'.join(['', 'Agt', 'Mfg', 'Model', 'Ctry', 'Year', 'Power']))
        for idx, turbine in enumerate(self.turbines):
            print(idx + 1, end='\t')
            print(turbine)


inventory = Inventory()
while True:

    print(' ✔ Add Windturbine to Inventory          [1]')
    print(' ✔ Delete Windturnine from Inventory     [2]')
    print(' ✔ List all Windturbines                 [3]')
    print(' ✔ Update Windturbine in Inventory       [4]')
    print(' ✔ Export Current Inventory              [5]')
    print(' ✔ Exit                                  [6]')
    print("==============================================")
    userInput=input('Select 1-6: ') 
    if userInput=="1": 
        #Add a Windturbines
        inventory.addTurbine()
    elif userInput=='2':
        #Remove a Windturbine
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
        item = int(input('Enter # of Windturbine to be deleted: '))
        if item - 1  > len(inventory.turbines):
            print('Wrong number provided')
        else:
            inventory.turbines.remove(inventory.turbines[item - 1])
            print ()
            print('Windturbine deleted')
    elif userInput == '3':
        #list of the Windturbines recorded
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
    elif userInput == '4':
        #Edit Windturbine recorded 
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        inventory.viewInventory()
        item = int(input('Select # of Windturbine to be updated: '))
        if item - 1  > len(inventory.turbines):
            print('Wrong number provided')
        else:
            windturbine = Windturbine()
            if windturbine.addTurbine() == True :
                inventory.turbines.remove(inventory.turbines[item - 1])
                inventory.turbines.insert(item - 1, windturbine)
                print ()
                print('Great 😊, Windturbine was updated')
    elif userInput == '5':
        #Create a file txt to export it 
        if len(inventory.turbines) < 1:
            print('WindTurbine(s) not found!!!')
            continue
        f = open('windturbine_inventory.txt', 'w')
        f.write('\t'.join(['Agt', 'Mfg', 'Model', 'Ctry', 'Year', 'Power']))
        f.write('\n')
        for turbile in inventory.turbines:
            f.write('%s\n' %turbile)
        f.close()
        print('Cool!! 😎 info exported to the file')
    elif userInput == '6':
        #exit the loop
        print('Talk to Soon 😉')
        break
    else:
        #Wrong user input
        print('Invalid Input. Please try again.')
