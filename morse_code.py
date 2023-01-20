# initialise dict
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '': ""}


class Solution:

    def run(self, morseToEnglish: bool, textToTranslate: str) -> str:
        """method converts morse code to english text and english text to morse code.
        Args:
        morseToEnglish - boolean, true if the given input text is in morse and false if it is in english
        textToTranslate - a string containing the text we wish to translate

        Returns:
        translatedText - string denoting morse code or english text"""

        translatedText = ""

        if not morseToEnglish:
            for letter in textToTranslate.upper():
                if letter == " ":
                    translatedText += "  "
                else:
                    translatedText += MORSE_CODE_DICT[letter] + " "

        else:
            word_list = textToTranslate.split("   ")
            EngWords = []

            for word in word_list:
                letter_list = word.split(" ")

                new_word = ""
                for letter in letter_list:
                    if letter != " ":
                        Engletter = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)]
                        new_word += Engletter

                EngWords.append(new_word.lower())
            translatedText = " ".join(EngWords)

        return translatedText

test = Solution()

print(test.run(True, "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   "))