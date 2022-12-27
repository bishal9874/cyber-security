#ceaser Ciper

txt=input("Enter the text Which you want to extract: ")
sval=int(input("enter the text Shifting value: "))


def encription(text,shiftVal):
    ciper=''
    for char in text:
        if char=='':
            ciper=ciper+char
        elif char.isupper():
            ciper=ciper+chr((ord(char)+shiftVal-65)%26+65)
        else:
            ciper=ciper+chr((ord(char)+shiftVal-97)%26+97)
    return ciper
def decription(encriptedText,shiftingVal):
    ceaser=''
    for ch in encriptedText:
        if ch=='':
            ceaser=ceaser+ch
        elif ch.isupper():
            ceaser=ceaser+chr((ord(ch)-shiftingVal+65)%26+65)
        else:
            ceaser=ceaser+chr((ord(ch)-shiftingVal+97)%26+97)
    return ceaser
print("the Main Text is", txt)
print("the Encripted text is",encription(txt,sval))
encriptText=encription(txt,sval)
print("the decription is ", decription(encriptText,sval))