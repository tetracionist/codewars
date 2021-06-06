# In response to https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):

    string=""
    for i in text.split():
        if i == "?":
            string=string + " "+"?"
        elif i == "!":
            string=string + " "+"!"
        else:
            string=string + " "+i[1:]+i[0]+"ay"
            print(string)
            
    return string.strip()
