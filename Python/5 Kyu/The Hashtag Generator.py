# Solution for https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    # use list processing to split out apply title case to each word
    # then join together and concatenate with hashtag
    
    s2 = s.split(" ")
    s3 = [i.title() for i in s2] 
    s4 = "".join(s3)
    return "#"+s4 if len(s4) > 0 and len(s4) < 140 else False
