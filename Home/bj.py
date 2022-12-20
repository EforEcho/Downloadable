from itertools import count
import random
import msvcrt

def make_shoe():
    shoe = []
    for decks in range(6):
        for types in "shcd":
                shoe.append(f"2{types}")
                shoe.append(f"3{types}")
                shoe.append(f"4{types}")
                shoe.append(f"5{types}")
                shoe.append(f"6{types}")
                shoe.append(f"7{types}")
                shoe.append(f"8{types}")
                shoe.append(f"9{types}")
                shoe.append(f"J{types}")
                shoe.append(f"Q{types}")
                shoe.append(f"K{types}")
                shoe.append(f"A{types}")

    random.shuffle(shoe)

    return shoe

def deal(shoe, pointeure, croupier, pointeure_count) -> list:
    for i in range(len(pointeure)):
        pointeure[i].append(shoe[0])
        shoe = shoe[1:]
        pointeure[i].append(shoe[0])
        shoe = shoe[1:]

    croupier.append(shoe[0])
    shoe = shoe[1:]
    croupier.append(shoe[0])
    shoe = shoe[1:]

    for idx, hand in enumerate(pointeure):
        for card in hand:
            num = card[0] 

            try:
                pointeure_count[idx] += int(num)
            
            except:
                if (num == 'J') or (num == 'Q') or (num == 'K'):
                    pointeure_count[idx] += 10 

    return shoe, pointeure, croupier, pointeure_count

def player_count():
    pointeure = []
    B = False
    while not B:
        count = input("Player Count:\t")
        try: 
            count = int(count)
            B = True
        except:
            print("Enter Integer")

    for i in range(count):
        pointeure.append([])

    return pointeure

def main():
    croupier = []

    pointeure = player_count()

    pointeure_count = [0 for i in range(len(pointeure))]

    shoe = make_shoe()

    shoe, pointeure, croupier, pointeure_count = deal(shoe, pointeure, croupier, pointeure_count)

    active = [i for i in range(len(pointeure))]


    print("Pointeure:")
    for i in pointeure: print(i)
    print(f"\nCroupier:\n{croupier}\n")

    print(active)

    while True:
        active_remove = []
        for i in active:
            print(active)
            print(f"p{i} -> {pointeure[i]}")
            act = input(f"p{i} turn:\t").lower()

            if act == "hit" or act == "carte":
                pointeure[i].append(shoe[0])
                shoe = shoe[1:]
                print(f"p{i} -> {pointeure[i]}")
                num = pointeure[i][-1][0]
                print(num)
                try:
                    pointeure_count[i] += int(num)
            
                except:
                    if (num == 'J') or (num == 'Q') or (num == 'K'):
                        pointeure_count[i] += 10 
                if pointeure_count[i] > 21:
                    active_remove.append(i)
                    pointeure_count[i] = 0

            elif act == "stand" or act == "reste":
                active_remove.append(i)

            else:
                print(
                "\n----------------Actions----------------\n"
                "hit, carte    -> Take another card \n"
                "stand, reste  -> Take no more cards \n"
                "double        ->\n"
                "---------------------------------------\n")
        for i in active_remove:
            active.remove(i)
    
    for idx, i in pointeure:
        pass

        

    pass

if __name__ == "__main__":
    main()