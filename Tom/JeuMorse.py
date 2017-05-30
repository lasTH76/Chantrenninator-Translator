import random

def morse():
        Morse = {'A': '.-', 'B': '-...', 'C':'-.-.', 'D': '-..',
                 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..',
                
                '0': '-----', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..',
                '9': '----.',
                 
                 '?': '..--..', '!': '-.-.--', '.': '.-.-.-',
                 ';': '-.-.-.', ':': '---...', ',': '--..--',
                 "'": '.----.', '-': '-....-', '(': '-.--.',
                 ')': '-.--.-', '"': '.-..-.'
                }

        answer = "."
        result = 0

        prenom = input("Please put your name here -->	    ")
        print("You'll have to translate a random letter, number or ponctuation mark into Morse code")
        number = int(input("Now select the number of characters you want to translate -->	    "))
        print("It's time to start!")
        print("")

        for loop in range(number):
                letter = random.randint(33,90)
                while (letter > 34 and letter < 39) or (letter > 41 and letter < 44) or (letter > 46 and letter < 48) or (letter > 59 and letter < 63) or (letter > 63 and letter < 65):
                        letter = random.randint(33,90)
                goodanswer = Morse[chr(letter).upper()]
                Try = 3
                
                print(chr(letter))
                
                while answer != goodanswer and Try > 0:
                        answer = input()
                        if answer != goodanswer:
                                Try += -1
                                print(Try, "attempt left.")
                if answer == goodanswer:
                        result += 1
                        print("Good answer")
                        print("")
                if Try == 0 and answer != goodanswer:
                        print("The answer was", goodanswer, ".")
                        print("")

        print(prenom, "has", result, "over", number, ".")

if __name__ == '__main__':
        morse()
