alice_candies=int(input("Nhập số kẹo của Alice:"))
bob_candies=int(input("Nhập số kẹo của Bob:"))
carol_candies=int(input("Nhập số kẹo của Carol:"))
if (alice_candies+bob_candies+carol_candies)%3==0:
    print("Kẹo được chia đêù")
else:
    print("Số kẹo dư:",(alice_candies+bob_candies+carol_candies)%3)
    
