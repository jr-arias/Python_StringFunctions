def PadRight(string, paddingChar, integer):
    #return string padded with the chars
    return string+(paddingChar*integer)

def StringToByteArray(string):
    #returns a bool if all of the characters are letters of the alphabet
    byte_array = [ord(c) for c in string]
    return byte_array
	
def StringIsAlpha(string):
    #returns a bool if all of the characters are letters of the alphabet
    byte_array = [ord(c) for c in string]
    for byte in byte_array:
        if (byte < 65 or byte > 91) and (byte < 97 or byte > 122):
            return False

    return True

def StringInsert(string, string2, position):
    #return new modified string
    char_array = list(string)
    char_array.insert(position, string2)
    new_string = ''.join(char_array)
    return new_string

def ByteToChar(byte):
    #return corresponding char associated with that byte
    char = chr(byte)
    return char

def StringRepeatFromChar(char, number):
    #return string made of that char repeated that number of times
    return char * number

def StringCombine(array, char):
    #return a string made from each string in the array joined by the char given
    new_string = char.join(array)
    return new_string

import random
def StringMix(string):
    #return a string with the characters randomly shuffled
    letters = list(string)
    random.shuffle(letters)
    new_word = ''.join(letters)
    return new_word

def StringToUpper(string):
    #return an uppercase version of the string
    new_string = string.upper()
    return new_string

def StringToLower(string):
    #return an lowercase version of the string
    new_string = string.lower()
    return new_string

def StringCharIndex(string, char):
    #return the integer index of the first occurence of the char within the string, -1 if DNE
    for i, letter in enumerate(string):
        if letter == char:
            return i
    return -1

def StringReverse(string):
    #return a reversed version of that string (using slices: start stop step)
    new_string = string[::-1]
    return new_string

def StringRepeat(string, number):
    #return the string repeated the number of times specified by int
    return string*number

def IsPasswordStrong(string):
    #returns a bool indicating if the string passed can be considered a strong password
    #criteria: one cap letter, one lowercase letter, one number, one special char, >8 chars
    lower_char, upper_char, spec_char, num = 0, 0, 0, 0
    password = string
    if (len(password) >= 8):
        for char in password:
            # counting lowercase alphabets 
            if (char.islower()):
                lower_char +=1            
            # counting uppercase alphabets
            if (char.isupper()):
                upper_char +=1            
            # counting digits
            if (char.isdigit()):
                num +=1            
            # counting the mentioned special characters
            if((ord(char)>32 and ord(char)<47) or (ord(char)>58 and ord(char)<65)):
                spec_char +=1           
    if (lower_char>=1 and upper_char>=1 and spec_char>=1 and num>=1 and lower_char + upper_char + spec_char + num==len(password)):
        return True
    else:
        return False

def ArraySum(array):
    #returns the sum of the values in the array
    sum = 0
    for num in array:
        sum = sum + num
    return sum

def ArrayMean(array):
    #returns the mean of the values in array
    sum = 0
    length = len(array)

    for num in array:
        sum = sum + num
    
    mean = sum/length
    return "{:.2f}".format(mean)

print(PadRight('Hey', 'h', 4))
print(StringToByteArray('jose'))
print(StringIsAlpha('ha7ppy'))
print(StringInsert('01235', '4', 5))
print(ByteToChar(97))
print(StringRepeatFromChar('a', 5))
print(StringCombine(['1','2','3'], 'x'))
print(StringMix('wally'))
print(StringToUpper('toUpper'))
print(StringToLower('ToLowER'))
print(StringCharIndex('abracadabra', 'r'))
print(StringReverse('abracadabra'))
print(StringRepeat('sup', 3))
print(IsPasswordStrong('Hello!12'))
print(IsPasswordStrong('hello!12'))
print(ArraySum([1,2,3]))
print(ArrayMean([10, 20, 30]))