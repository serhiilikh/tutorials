alphabet = ["a", "b", "c", "d"]
l = len(alphabet)
cypher = 1
def encode(word):
    position = 0
    res = ""
    for char in word:
        if char == alphabet[position]:
            position += cypher
            while position >= l:
                position -= l
            res += alphabet[position]
        else:
            position += 1
    return res
print(encode("abcd"))
