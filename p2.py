def dislplayArguments(argument1, *argument2, **argument3):
    print(argument1) 
    for arg in argument2: 
        print(arg) 
    for arg in argument3.items(): 
        print(arg) 
  
arg1 = "Welcome"
arg3 = "Golang"
dislplayArguments(arg1, "to", arg3, agr4 = 4,arg5 ="Golang !") 
                   