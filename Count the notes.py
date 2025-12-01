amount=int(input("Please Enter Amountfor Withdraw:"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("note of 100 rupee",note_1)
print("note of 50 rupee",note_2)
print("note of 10 rupee",note_3)