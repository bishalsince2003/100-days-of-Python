print("Welcome to the split bill calculator")
bill=float(input("What was the total bill? Rs."))
tip=int(input("How much tip would you like to give? 10% ,12% or 15% \n"))
person=int(input("how many people to split the bill? "))
# final_bill=round((int(bill)+int(tip))/int(person) , 2)
# print(f"Bill per head is :Rs.{final_bill}")

final_bill=round((bill/ person)* (1+tip/100),2)
print(f"Final bill for each person is {final_bill}")



