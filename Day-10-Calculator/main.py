#
#
# def add(n1, n2):
#     return n1 + n2
# def sub(n1, n2):
#     return n1 - n2
# def mul(n1, n2):
#     return n1 * n2
# def div(n1, n2):
#     return n1 / n2
#
# def calculator():
#     import art
#     print(art.logo)
#     n1=float(input("Whats the first number?  "))
#     further_calc(n1)
# def further_calc(n1):
#     print("+\n-\n*\n/")
#     operation=input("Pick an operation:  ")
#     n2=float(input("Whats the next number? "))
#
#
#     result=""
#     if operation=="+":
#         result=float(add(n1,n2))
#     elif operation=="-":
#         result=float(sub(n1,n2))
#     elif operation=="*":
#         result=float(mul(n1,n2))
#     elif operation=="/":
#         result=float(div(n1,n2))
#     else:
#         print("Invalid operator")
#
#     print(f"{n1} {operation} {n2} = {result}")
#     decision=input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start new calculation. ").lower()
#     if decision=="n":
#         print("\n"*50)
#         calculator()
#     elif decision=="y":
#         n1=result
#         further_calc(n1)
#
#
# calculator()
#

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
def calculation():
    import art
    print(art.logo)
    n1=float(input("whats the number ? "))
    should_proceed=True

    while should_proceed==True:
        for key in operations:
            print(key)
        operation=input("Pick an operation:  ")
        n2=float(input("whats the number ? "))

        perform=operations[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {perform} ")

        decision=input(f"Type 'Y' to continue calculating with {perform}, or type 'N' to start new calculation. ").lower()

        if decision=="y":
            n1=perform
        elif decision=="n":
            should_proceed=False
            print("\n"*100)
            calculation()

calculation()


