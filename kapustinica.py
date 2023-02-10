n = int(input())
text = input()
newText = ""
pocetT = 0
pocetV = 0
first = True
vIsWaiting = 0
for i in text:
    if first:
        if i == "T":
            newText += "VT"
        elif i == "V":
            vIsWaiting += 1
            newText += "V"
        first = False
        continue
    if i == "T":
        if vIsWaiting == 0:
            newText += "VT"
        else:
            vIsWaiting -= 1
            newText += "T"
    elif i == "V":
        newText += "V"
        vIsWaiting += 1

print(newText+"T"*vIsWaiting)
print("David je divny")
