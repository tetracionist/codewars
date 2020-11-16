def longest(s1, s2):
    # concatenate strings and remove duplicates
    # Append each letter to a list and sort
    # Then join the list into a string
    s3="".join(set(s1+s2))
    charList=[]
    for i in s3:
        charList.append(i)
    
    charList.sort()
    s4="".join(charList)
    return s4
    
