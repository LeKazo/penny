
#here bc its funny
def main():
    coin = int(input("whats the amount of pennies that you have? or want to just say you have:\n"))
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

#coin values!
    while coin > 0:
        if coin >= 100:
            coin -= 100
            dollars += 1
            print(coin)
        elif coin >= 25:
            coin -=25
            quarters += 1
            print(coin)
        elif coin >= 10:
            coin-=10
            dimes += 1
            print(coin)
        elif coin >= 5:
            coin-=5
            nickels+=1
            print(coin)
        else:
            pennies += coin
            coin=0
#prints the amount of coins converted from pennies to other currency
    print(f"""dollars: {dollars}
    quarters: {quarters}
    dimes: {dimes}
    nickels: {nickels}
    pennies: {pennies}""")

    main()
main()
