"""project 1 - Generate random name combinations. used pylint for format and got 10/10"""
import random

def main():
    """Choose random first and last name from the two tuples"""
    print("Welcome to the Random Name Genorator.\n")
    print("A Name Will be picked for you:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
                "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
                'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
                'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
                'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
                'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
                'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
                'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
                '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
                'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
                'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
                "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
                'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
                'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
                "Winston 'Jazz Hands'", 'Worms')

    middle = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
                'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
                'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
                'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
                'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
                'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
                'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
                'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
                'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
                'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
                'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
                'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
                'Woolysocks')
    
    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
                'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
                'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
                'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
                'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
                'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
                'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
                'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
                'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
                'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
                'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
                'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
                'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
                'Woolysocks')
    while True:
        first_name = random.choice(first)
        middle_name = random.choice(middle)
        last_name = random.choice(last)

        print("\n\n")
        # Trick Idle by using "fatal error" detting to print name in red.
        print(f"{first_name} \"{middle_name}\" {last_name}")
        print("\n\n")

        try_again = input("Try Again? (Press Enter to continue else n to Exit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
    