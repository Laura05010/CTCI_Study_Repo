# TODO:
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"


# APPROACHES:
# ---------------------------------------------------------------
# LAURA:
# -> Basically use that method where you split on whitespaces… then go through the list and do.
# -> for I in list:
# 	string += list[i] + “%20”
def URLify(sentence:str) -> str:
    content = sentence.split()
    final = ""
    for i in range(len(content)):
        if i == len(content) - 1:
            final += content[i]
        else:
            final += content[i] + "20%"
        i += 1
    return final

if __name__ == '__main__':
    print(URLify("I am happy I am good"))