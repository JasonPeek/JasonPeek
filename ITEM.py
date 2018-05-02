def leather_wallet (wallet_owner, material, color, pockets, quality):
    wallet = {
        'Wallet Owner':wallet_owner,
        'Material':material,
        'Color':color,
        'Pockets':pockets,
        'Quality':quality
        }
    return wallet

my_wallet = leather_wallet ('Jason', 'Leather', 'Brown', '7', 'Good')

friends_wallet = leather_wallet ('Ryan', 'Leather', 'Red', '13','Horrible')

def display_wallet(wallet):
    for key, value in wallet.items():
        print(key + ": " + value)
    print("\n")

display_wallet(my_wallet)
display_wallet(friends_wallet)

plastic = 14.00
metal = 100.00
leather = 22.00

walletlist = []
your1_wallet = str(input("What color is your wallet?: "))
if your1_wallet == "red" or your1_wallet == "black" or your1_wallet == "brown":
    print("Coolio")
else:
    print("NASTY")

your2_wallet = str(input("What material is your wallet?: "))
if your2_wallet == "leather" or your2_wallet == "plastic" or your2_wallet == "metal":
    print("Ignant")
else:
    print("NASTY")

your3_wallet = int(input("How many pockets does your pocket have?: "))
if your3_wallet >= 5:
    print("SUPER")
else:
    "ok"

your4_wallet = str(input("What is the quality of your wallet?: "))
if your4_wallet == "good":
    print("FANTASTIC")
elif your4_wallet == "decent":
    print("Cool")
else:
    print("NASTY")
walletlist.append(your1_wallet)
walletlist.append(your2_wallet)
walletlist.append(your3_wallet)
walletlist.append(your4_wallet)


def your_wallet(your1_wallet, your2_wallet, your3_wallet, your4_wallet):
    wallet2 = {
        'Material':your1_wallet,
        'Color':your2_wallet,
        'Pockets':your3_wallet,
        'Quality':your4_wallet,
        }
    return wallet2

x = your_wallet(your1_wallet, your2_wallet, your3_wallet, your4_wallet)

print(x) 
 

