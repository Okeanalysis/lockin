print("Welcome to the tip calculator")
bill= float(input("what is the bill: "))
tip=int(input("how much tip will you like to give? 10, 12, 15: "))
people= int(input("how many people are we spliting the bill among: "))
tip_percent= 1+(tip/100)
totalbill= bill+tip_percent
totalbillp= totalbill/people
totalamount= round(totalbillp, 2)

print("Each person pays", totalamount)