def word_to_morse(word):
    """Convertie un mot en morse"""

    code = { "a" : ".-",
             "b" : "-...",
             "c" : "-.-.",
             "d" : "-..",
             "e" : ".",
             "f" : "..-.",
             "g" : "--.",
             "h" : "....",
             "i" : "..",
             "j" : ".---",
             "k" : "-.-",
             "l" : ".-..",
             "m" : "--",
             "n" : "-.",
             "o" : "---",
             "p" : ".--.",
             "q" : "--.-",
             "r" : ".-.",
             "s" : "...",
             "t" : "-",
             "u" : "..-",
             "v" : "...-",
             "w" : ".--",
             "x" : "-..-",
             "y" : "-.--",
             "z" : "--..",
             "1" : ".----",
             "2" : "..---",
             "3" : "...--",
             "4" : "....-",
             "5" : ".....",
             "6" : "-....",
             "7" : "--...",
             "8" : "---..",
             "9" : "----.",
             "0" : "-----"
        }

    morse_word = []
    for char in word:
        morse_word.append(code[char.lower()])

    return " ".join(morse_word)



def string_to_morse(string):
    """Convertie une phrase en morse"""

    string = string.split(" ")
    morse_string = []
    
    for word in string:
        morse_string.append(word_to_morse(word))
        
    return " ".join(morse_string)
    
