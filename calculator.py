
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK )
print( Back.GREEN )
what = input( "Ce facem?(+, -): " )
print( Back.CYAN )

a = float(input("Prima cifra: "))
b = float(input("A doua cifra: "))
print( Back.YELLOW )

if what == "+":
    c = a +b 
    print("Rezultat: " + str(c))
elif what == "-":
    c = a - b
    print("Rezultat: " + str(c))
else:
    print("Ai ales operatie gresita!")

input()
exit