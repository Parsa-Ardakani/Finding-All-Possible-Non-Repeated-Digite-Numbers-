#---------------------------Libraries------------------------------
import numpy as np
import time

#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#|||||||||----------------------------Variables-------------------------------|||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴

#---------------------------Global Variables-----------------------
numbers = [] #out input numbers would be inside of this list(array)



#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#||||||||---------------------------Functions--------------------------------||||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴


#------------------Function to receive numbers from user---------------------------------

def Number_Input():
    global numbers # To be able to use list(array)

    i = 0 # this variable will be used to count
    while True:
        # this loop countinues as long as the user enter a number
        
        input_number = input("Please Enter the number " + str(i) + ": ") # Receive number
        print(input_number)
        numbers.append(input_number) #Store number in the list(array)

        

        # check that if the number is an integer and if it is not receive it again
        while True:
            #https://www.w3schools.com/python/python_try_except.asp
            try:
                # check it is eighter integer or empty string  or neighter of them
                if numbers[i] == '':
                    pass
                else:
                    numbers[i] = int(numbers[i])
            except:
                print("!The input is not integer!")
                numbers[i] = input("Please try again: ") # Receive the number, again
            else:
                #if it is an integer break the loop
                break


        # if the input is empety, break the loop
        if numbers[i] == '':
            numbers.pop()# Remove the last index which is empty string
            break
        # add 1 to i     
        i = i+1


#═════════════════════════════════════════════════════════════════════════════════════════

#--------------------------Function to Remove Repeated Numbers----------------------------

def Remover():
    # TWO WAYS TO REMOVE REPEATED NUMBERS
    global numbers# To be able to use list(array)
    
    #-->First way
    """
    i = 0 #count
    # Removing Repeated Numbers
    while i < len(numbers)-1:
        print(len(numbers))
        i_Help = i+1 #Count
        while i_Help < len(numbers):
            # Check if the value of an index is repeated
            if numbers[i] == numbers[i_Help]:
                # Remove if it is
                del numbers[i_Help]

            i_Help += 1

        i += 1
    """

    #-->Second Way
    numbers = list(dict.fromkeys(numbers))

    #Sort the List(array): it would be helpful
    numbers.sort()
    

#═════════════════════════════════════════════════════════════════════════════════════════

#----------------------------Calculate all possibilities----------------------------------

def Calculation():
    global numbers 
    print("Numbers ---> " + str(numbers))
    calculator = [] # Store digits of each number everytime
    store = [numbers[len(numbers)-1]] # use to store new numbers
    Final = [] # Use it to store new numbers of each process, then store them in "store" and store final numbers
    turn = 1 # count the number of turns
    posibility = 1 # the number of possible numbers
    num = 0 # stores numbers

    # iteration variables
    i = 0
    nth = 0
    i_help = 0

    # Calculation
    while turn < len(numbers):

        # adding new digit of "numbers" to each number in store
        i = len(store)
        while i>0:
            store[i-1] *= 10 # multiply each number by 10
            store[i-1] += numbers[(len(numbers)-1)-turn] # add new digit
            print("Store ---> " + str(store))
            i -= 1
        

        # Calculate possilbe number
        # it helps us to know how many number do we have to calculate them
        # code below does factorial ---> math form: turn!
        i=1
        while i <= turn:
            posibility *= i #multipy posibility by i and add it to possibility
            i += 1
        
        
        # Find, write, and store all possible numbers
        while posibility > 0:

            # Store each digit of first number of "store" in "calculator"
            i = turn
            num = store[0] # make num equal with first number of store
            calculator.clear() # empties the calculator if there is any element
            while i >= 0:
                """" First, we divide the "num" by 10^i
                it gives us a float number. First digit is befor Radix Point
                and others are after. for instans, 235 --> 2.35. By using "int()" we remove all numbers that are after
                Radix Point. Now we have one digit of the number, so we store it in
                calculator."""
                calculator.append(int(num / pow(10, i)))
                print("i ---> " + str(i))  
                """ Now we have to remove the digit we stored. Simply we multiply the 
                digit by 10^i and remove it from num."""
                num = num - calculator[-1]*pow(10, i)
                i -= 1
                if i == 0:
                    """when i is equals to 0 it means all digites are
                    removed and only index = 0 is remaining which is the first
                    digit. we just add 'num' to the 'calculator'"""
                    calculator.append(num)
                    break
            print("cal ---> " + str(calculator))    
            
            
            
            # Find all possible numbers            
            i = 0
            i_help = len(calculator) - 1 # we decreas the "i_help" by 1 becuase index of list(array) starts from 0 not 1
            while True:
                num = 0 
                # this loop is used to store digits order in calculator as a number in "num"
                for nth in range(len(calculator)):
                    num += calculator[nth] * pow(10, (len(calculator)-1)-nth)
                
                # add "num" to "Final" list(array)
                if calculator[0] != 0:
                    Final.append(num)
                
                # change the place of the new digit. it starts from last index to the first
                calculator[i_help], calculator[i_help-1] = calculator[i_help-1], calculator[i_help] 
                
                    
                i += 1
                i_help -= 1
                # break if it is finished
                if i_help < 0:
                    i_help = 0
                    break
                    
            # dcreased "posibility" by 1 to do all this processes with the other numbers
            posibility -= 1
            # remove the number we finished the calculation with
            store.pop(0)
            print("Store.pop ---> " + str(store))
    
        turn += 1
        posibility = 1 # Note: it has to be one not 0
        store = Final.copy() # Store new numbers in "store"
        Final.clear() # empties the "Final"
        
        
    Final = store.copy() # Store All possible numbers in "Final"
    store.clear()
    print(Final)


        



#┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬
#||||||||--------------------------Main Loop--------------------------------|||||||||
#┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴



while 1:
    # Call functions
    Number_Input()
    Remover()
    Calculation()

    #empties "numbers"
    numbers.clear() 
