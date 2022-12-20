from os import system
from msvcrt import getch

def kasse(a: str, b: str) -> None:
    try:
        a = float(a); b = float(b)
    except ValueError as e:
        print(e)
        return 0
    if b >= a: print(f"Rückgeld:\t{b - a}")
    else: print("Zu wenig Geld")

def main():
    while True:
        kasse(input("Preis:\t"), input("Geld:\t"))
        getch()
        system("cls")

if __name__ == "__main__":  main()   