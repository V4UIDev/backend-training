def morseEncrypt(message):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    messageTranslateList = list(message.upper())
    messageValue = len(messageTranslateList)
    i = 0
    morseList = []

    while i < messageValue:
        try:
            morseList.append(MORSE_CODE_DICT[messageTranslateList[i]])
            morseList.append(' ')
            i = i + 1
        except:
            if messageTranslateList[i] == ' ':
                morseList.append(' ')
                i = i + 1
            else:
                i = i + 1
    return ''.join(morseList)

def morseDecrypt(message):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

    MORSE_CODE_DICT_REVERSED = {value:key for key,value in MORSE_CODE_DICT.items()}

    messageTranslateList = message.split(' ')
    messageValue = len(messageTranslateList)
    i = 0
    characterList = []

    while i < messageValue:
        try:
            characterList.append(MORSE_CODE_DICT_REVERSED[messageTranslateList[i]])
            characterList.append(' ')
            i = i + 1
        except:
            if messageTranslateList[i] == ' ':
                morseList.append(' ')
                i = i + 1
            else:
                i = i + 1
    return ''.join(characterList)

    return messageTranslateList

print("Type 1 for Encryption, 2 for Decryption.")
print(" ")
choice = input()

if choice == '1':
    print("Type a message to encrypt:")
    message = input()
    print(morseEncrypt(message))
if choice == '2':
    print("Type a message to decrypt:")
    message = input()
    print(morseDecrypt(message))

