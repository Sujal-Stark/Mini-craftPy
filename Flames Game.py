def getCount(name1 : str, name2 : str):
    name1 = name1.lower()
    name2 = name2.lower()
    for i in name1:
        for j in name2:
            if i == j:
                name1 = name1.replace(i, "", 1)
                name2 = name2.replace(j, "", 1)
                break
    return len(name1) + len(name2)

def getLetter(length : int):
    flames = "FLAMES"
    flameLength  = len(flames)
    while flameLength != 1:
        index = length - 1 if len(flames) >= length else (length % len(flames)) - 1
        if index == 0:
            flames = flames[1:]
            flameLength -= 1
        elif index == len(flames)-1:
            flames = flames[:-1]
            flameLength -= 1
        else:
            flames = flames[index+1:] + flames[:index]
            flameLength -= 1
    return flames

def getRelation(word1 : str, word2  : str):
    FREINDS,LOVE,ADDRESSABLE,MATES,ENEMY,SOULMATE = "Friends","Love","Affair","Marriage","Enemy","Siblings"
    length = getCount(word1, word2)
    letter = getLetter(length)
    if len(letter) == 1:
        if letter == "F":
            return FREINDS
        elif letter == "L":
            return LOVE
        elif letter == "A":
            return ADDRESSABLE
        elif letter == "M":
            return MATES
        elif letter == "E":
            return ENEMY
        elif letter == "S":
            return SOULMATE
        else:
            return "No relationship"
    else:
        return "No relationship"

name1 = input("Enter name 1:\t")
name2 = input("Enter name 2:\t")
print(f"The relationship between {name1} and {name2} is \t",getRelation(name1, name2))