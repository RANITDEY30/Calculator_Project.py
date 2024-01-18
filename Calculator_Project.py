def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dictionary={
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": divide
}
def calculator():
    number1 = int(input("Enter First Number:"))
    for symbol in operations_dictionary:
      print(symbol)

    continue_flag= True
    while continue_flag:
        op_symbol = input("Pick An Operation:")
        number2 = int(input("Enter Next Number:"))
        calculator_function=operations_dictionary[op_symbol]
        output =calculator_function(number1,number2)
      print(f"{number1} {op_symbol} {number2}= {output}")
    should_continue = input(f"Enter y to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit"). lower()
if should_continue=='y':
   number1=output
elif should_continue == 'n':
    continue_flag= False
    calculator()

else:
       continue_flag = False
       print("Bye")
calculator()