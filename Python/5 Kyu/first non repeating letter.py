def first_non_repeating_letter(string):
    # count how many letters using two arrays 
    # that use the same index structure
    letters = []
    letters_count = []
      
    # use a for loop to iterate over the string
    # look for cases where upper and lowercase characters might exist
    # and include these in the count
    for i in range(len(string)):
        if string[i].upper() in letters:
            letters_count[letters.index(string[i].upper())] += 1
        elif string[i].lower() in letters:
            letters_count[letters.index(string[i].lower())] += 1
        elif string[i] not in letters:
            letters.append(string[i])
            letters_count.append(1)
        else:
            letters_count[letters.index(string[i])] += 1
    
    # try to find the first index that has a count of 1
    # if we cannot find this, return blank
    try:
        letter = letters[letters_count.index(1)]
    except:
        letter = "" 
    
    return letter
