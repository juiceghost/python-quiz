
#def translate():
#    string = input("Enter some text: ")
#    new_string = string.replace('a', '4').replace('b', '8').replace('e', '3').replace(
#        'l', '1').replace('o', '0').replace('s', '5').replace('t', '7')
#    print(new_string)

def translate():
    replacements = ( ('a','4'), ('b','8'), ('e','3'), ('l','1'),
                 ('o','0'), ('t','7') )
    string = input("Enter some text: ")
    
    for old, new in replacements:
        string = string.replace(old, new)

    print(string)


"""
def menu():
    print("\n==================== Personlighetstest======================")
    print("Vilken barbapapa-figur är du?? 2 snabba frågor.\n")


def main():
    # För varje key i dictionary questions
    for key, value in questions.items():
        # Skriv ut key
        print(f"{key}")
        # För varje value. Skriv ut index
        for indx, answer in enumerate(value):
            print(f'{indx + 1}: {answer}')
        # Aktivera funktionen scoring
        scoring()


def scoring():
    while True:
        answer = input(">>> ")
        # Om answer är numeriskt och int under 7
        if answer.isnumeric() and int(answer) <= 7:
            # Lägg till svaret i listan score
            score.append(int(answer))
            break
        else:
            call_error()


def call_error():
    print("Felaktigt val. Försök igen")


score = []


questions = {
    "Du slö-zappar framför tvn. Vilket program fastar du i:\n": [
        "Djur och natur",
        "En bra konsert",
        "Boktipset",
        "Konstmagasinet",
        "Skönhet",
        "Vetenskapens värld",
        "Sporten"],
    "Det finns många färger men vilken är din favorit:\n": ["Gul", "Grön", "Orange", "Svart", "Lila", "Blå", "Röd"],
}

barbs = [
    'Barbazoo -(Barbazoo) älskar och skyddar natur och djur. Han är väldigt bra på naturvetenskap. Han kan allt om flora och fauna, klimat och föroreningar.Barbazoo misstror många av Barbabrights experiment på genetik. Han har ofta rätt i att vara försiktig...',
    'Barbalala -(Barbalala) älskar musik. Hon kan spela alla sorters instrument. Hon är också intresserad av botanik och ekologi som sin bror Barbazoo. Barbalala har ett drömskt och fridfullt temperament. Hon blir nästan aldrig arg: hon är en bra sport.',
    'Barbabok -(Barbalib) is an intellectual and an activist. She is always immersed in books and knows a lot. She loves to play the teacher. She doesn’t have an easy personality. She often fights with Barbabravo because she also wants to be the leader.',
    'Barbaskön -(Barbaeau) är hårig och han är en konstnär. Han är sällan skild från sin skissbok. Rita, måla, skulptera, modellera, Barbaeau kan allt. I greppet av kreativa plågor kan han ibland vara väldigt känslig',
    'Barbafin -(Barbabelle) är väldigt vacker. Hon gillar smycken, klänningar och parfymer. Hon lägger mycket tid på att sminka sig. Hon är rädd för små håriga djur som larver eller spindlar. Hon svimmar när hon ser en! Barbouille tycker att det är riktigt irriterande.',
    'Barbaflink -(Barbabright) är en stor vetenskapsman. Varken kemi, astrofysik eller genetik är en hemlighet för honom. Störande drycker, galna maskiner... dessa fantastiska uppfinningar är ibland användbara men de orsakar ofta katastrofer!',
    'Barbastark -(Barbabravo) är en idrottsman.Han är väldigt stark och gillar att vinna. han gillar också att leda och älskar att äta. Med sin Sherlock Holmes outfit (hatt och förstoringsglas) och med hjälp av sin trogna Lolita spelar han detektiv.Barbabravo är lite för nöjd med sig själv, men han är en bra karl.'
]

menu()
main()
# Summan av svaren dividerat med antal frågor
mid = (sum(score)) / len(questions)
# Skriv ut det element som motsvarar det tal variabeln mid har ex. print(barbs[1])
print(f'Du är {barbs[round(mid) - 1]}')
int """
