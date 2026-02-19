# This program will replace common letters with letters from Old English

text = "   " + str(input("Type the string you wish to convert: "))
new_text = ""

print("\nConversion:\n")

for i in range(len(text)):

    # thorn ("th" at beginning of words)
    if text[i-1:i+2] == " Th":
        new_text += "Þ"
    elif text[i-1:i+2] == " th":
        new_text += "þ"

    # eth ("th" in middle and end of words)
    elif text[i:i+2] == "Th":
        new_text += "Ð"
    elif text[i:i+2] == "th":
        new_text += "ð"

    # wynn ("w")
    elif text[i] == "W":
        new_text += "Ƿ"
    elif text[i] == "w":
        new_text += "ƿ"

    # ash (short a)
    elif text[i] == "A" and (text[i+1:i+2].lower() not in "aeiouy" and text[i+2:i+3].lower() not in "aeiouy"):
        new_text += "Æ"
    elif text[i] == "a" and (text[i+1:i+2].lower() not in "aeiouy" and text[i+2:i+3].lower() not in "aeiouy"):
        new_text += "æ"

    # ethel ("long e")
    elif text[i:i+2] in "Ee Ea Ey".split() or text[i-1:i+1] == "Ie":
        new_text += "Œ"
    elif text[i:i+2] in "ee ea ey".split() or text[i:i+3:2] == "ee" or text[i-1:i+1] == "ie":
        new_text += "œ"

    # long s (first "s" in a row and not at end of words)
    elif text[i:i+1].lower() == "s" and text[i-1:i].lower() != "s" and text[i+1:i+2] != " " and text[i+1:i+2] != ".":
        new_text += "ſ"

    elif ((text[i].lower() == "h" and text[i-1].lower() == "t") or (text[i-1].lower() == "e" and (text[i].lower() == "e" or text[i].lower() == "a" or text[i].lower() == "y")) or
        (text[i-2].lower() == "e" and text[i].lower() == "e") or (text[i+1:i+2].lower() == "e" and text[i].lower() == "i")):
        pass

    else:
        new_text += text[i]

print(new_text)

input("\nPress Enter to terminate...")
