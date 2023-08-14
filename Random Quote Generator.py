import random
print("****** Random Quote Generator ******")

choice = input("Would you like a random quote (yes/no) > ")

quoteOptions = ["Failure is simply the opportunity to begin again, this time more intelligently.","Our greatest glory is not in never falling, but in rising every time we fall.","I never dreamed about success. I worked for it.","Don’t let yesterday take up too much of today.","Either you run the day or the day runs you.","Setting goals is the first step in turning the invisible into the visible."]
if choice == "no":
    print("Goodbye:)")
    exit()
else:
    randomChoice =random.choice(quoteOptions)
    print("Your random quote: ", randomChoice)

while True:
    repeat = input("Would you like another quote? (yes/no) > ")

    if repeat == "no":
        print("Goodbye :)")
        exit()
    else:
        randomChoice = random.choice(quoteOptions)
        print("Your random quote: ", randomChoice)
quoteOptions = ["Failure is simply the opportunity to begin again, this time more intelligently.",
                    "Our greatest glory is not in never falling, but in rising every time we fall.",
                    "I never dreamed about success. I worked for it.", "Don’t let yesterday take up too much of today.",
                    "Either you run the day or the day runs you.",
                    "Setting goals is the first step in turning the invisible into the visible.", "Anger is the ultimate destroyer of your own peace of mind.","Don't be afraid. Be focused. Be determined. Be hopeful. Be empowered.", "I think beauty comes from actually knowing who you are. That’s real beauty to me."]




