total_bill = input("What is your total bill? ")
#ignore the $ sign if user inputs
total_bill= total_bill.replace("$","")
#convert users bill to float 
total_bill=float(total_bill)
print(total_bill)


#list of possible tips calculation
tip_1= 0.15*total_bill
tip_2= 0.18*total_bill
tip_3= 0.20*total_bill



#list out all tips
print("Here's a recommendation of amounts that you can tip")

#converts results of calculation to 2 d.p
print(f"1. ${tip_1:.2f}")
print(f"2. ${tip_2:.2f}")
print(f"3. ${tip_3:.2f}")
