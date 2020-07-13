
while True:
    print("\n \n")
    #input (amount of penny)
    given_change = int(input("Enter amount of coins: " ))
    print("\n \n")
    # print(given_change)
    pro = given_change

    #quarter
    if given_change >= 25:
        global quarter_remainder
        quarter_remainder = given_change % 25
        quarter_sort = pro - quarter_remainder
        quarter = quarter_sort // 25
        given_change = quarter_remainder
        pro = quarter_remainder
        print("Quarter:", quarter, "\n ") 
    else:
        print("Quarter: 0 \n")

    #dime
    if  given_change >= 10 :
        global dime_remainder
        dime_remainder = given_change % 10
        dime_sort = pro - dime_remainder
        dime = dime_sort // 10
        given_change = dime_remainder
        pro = dime_remainder
        print("Dime:", dime, "\n ") 
    else:
        print("Dime: 0 \n")

    #nickle
    if given_change >= 5 :
        global nickle_remainder
        nickle_remainder = given_change % 5
        nickle_sort = pro - nickle_remainder
        nickle = nickle_sort // 5
        given_change = nickle_remainder
        pro = nickle_remainder
        print("Nickle:", nickle, "\n ")
    else:
        print("Nickle: 0 \n")
        
    #penny
    if given_change >= 1 and given_change < 5:
        penny_remainder = given_change % 1
        penny_sort = pro - penny_remainder
        penny = penny_sort // 1
        given_change = penny_remainder
        pro = penny_remainder
        print("Penny:", penny) 
    else:
        print("Penny: 0")