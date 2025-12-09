months = {"1":"january","2":"february","3":"march","4":"april","5":"may","6":"june",
          "7":"july","8":"august","9":"september","10":"october","11":"november","12":"december",
          "january":"january", "february":"february", "march":"march",
         "april":"april", "may":"may", "june":"june",
          "july":"july", "august":"august", "september":"september",
         "october":"october", "november":"november", "december":"december"}

while True:
    user = input("Enter your birth month: ").lower().strip()
    if user in months:
        user=months[user]
    elif user not in months:
        print("Not a valid month!")
        continue
    while True:
        user2 = int(input("Enter your birth date (1-31): "))

        if user2 < 1 or user2 > 31:
            print('Please enter a date between 1 and 31!')
            continue
        break

    if (user == 'march' and user2 >= 21) or (user == 'april' and user2 <= 19):
            zodiac = "Aries"
    elif (user == 'april' and user2 >= 20) or (user == 'may' and user2 <= 20):
            zodiac = "Taurus"
    elif (user == 'may' and user2 >= 21) or (user == 'june' and user2 <= 20):
            zodiac = "Gemini"
    elif (user == 'june' and user2 >= 21) or (user == 'july' and user2 <= 22):
            zodiac = "Cancer"
    elif (user == 'july' and user2 >= 23) or (user == 'august' and user2 <= 22):
            zodiac = "Leo"
    elif (user == 'august' and user2 >= 23) or (user == 'september' and user2 <= 22):
            zodiac = "Virgo"
    elif (user == 'september' and user2 >= 23) or (user == 'october' and user2 <= 22):
            zodiac = "Libra"
    elif (user == 'october' and user2 >= 23) or (user == 'november' and user2 <= 21):
            zodiac = "Scorpio"
    elif (user == 'november' and user2 >= 22) or (user == 'december' and user2 <= 21):
            zodiac = "Sagittarius"
    elif (user == 'december' and user2 >= 22) or (user == 'january' and user2 <= 19):
            zodiac = "Capricorn"
    elif (user == 'january' and user2 >= 20) or (user == 'february' and user2 <= 18):
            zodiac = "Aquarius"
    elif (user == 'february' and user2 >= 19) or (user == 'march' and user2 <= 20):
            zodiac = "Pisces"
    traits = {
        "Aries": "Courageous, determined, confident",
        "Taurus": "Reliable, patient, practical",
        "Gemini": "Adaptable, curious, outgoing",
        "Cancer": "Loyal, empathetic, protective",
        "Leo": "Generous, warm-hearted, creative",
        "Virgo": "Analytical, kind, hardworking",
        "Libra": "Diplomatic, graceful, social",
        "Scorpio": "Passionate, resourceful, brave",
        "Sagittarius": "Optimistic, adventurous, honest",
        "Capricorn": "Disciplined, responsible, ambitious",
        "Aquarius": "Independent, inventive, humanitarian",
        "Pisces": "Compassionate, artistic, intuitive"
        }
    print(f"Your zodiac sign is {zodiac}!")
    print(f"Traits: {traits[zodiac]}")

    end = input('Do you want to continue? (yes/no): ').lower().strip()
    if end == "yes":
        continue
    elif end == "no":
        print('Bye!')
        break
