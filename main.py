
alphabet = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', ' ', '']

#test values
cypher = [1,2,3,4]
couples = [[4, 1], [14, 9], [5, 12], [26, 19], [21, 3], [11, 19]]


def mult_mat(mat1, mat2):
    result = [0,0]
    
    result[0] = mat1[0]*mat2[0] + mat1[1]*mat2[1]
    result[1] = mat1[2]*mat2[0] + mat1[3]*mat2[1]

    return result

def make_couples(sentence, alphabet):
    i = 0
    couple = []
    couple_matrices = []
    while i < len(sentence):
        couple.append(alphabet.index(sentence[i]))
        i += 1
        if i%2 == 0:
            couple_matrices.append(couple)
            couple = []
        elif i == len(sentence) and i%2 != 0:
            couple.append(alphabet.index(''))
            couple_matrices.append(couple)
    return couple_matrices

def make_encryption():
    i = 0
    cypher_matrix_str = []
    cypher_matrix = []
    print("""The encryption matrix is a 2x2, which looks like this:
    |a  b|
    |c  d|""")
    numbers = str(input("Select the 4 numbers you would like to use for the encryption, following the order a,b,c,d: "))

    while i < len(numbers):
        cypher_matrix_str.append(numbers[i])
        i += 1
    cypher_matrix = [ int(x) for x in cypher_matrix_str ]
    return cypher_matrix

def encrypt(cypher, couples, alphabet):
    final = []
    letters = []
    i = 0
    j = 0
    k = 0
    
    while i < len(couples):
        result = mult_mat(cypher, couples[i])

        final.append([result[0]%27, result[1]%27])

        ''' This is a failed attempt at taking the "modulus"...There's a function for that already...

        if result[0] > 26 and result[1] <= 26:
            final.append([result[0] - 27, result[1]])
        elif result[1] > 26 and result[0] <=26:
            final.append([result[0], result[1] - 26])
        elif result[0] > 26 and result[1] > 26:
            final.append([result[0] - 26, result[1] - 26])
        else:
            final.append([result[0], result[1]])
        '''
            
        i += 1
    
    while j < len(final):
        temp1 = final[j][0]
        temp2 = final[j][1]
        letter1 = alphabet[temp1]
        letter2 = alphabet[temp2]

        letters.append([letter1,letter2])
        j += 1
    
    return [final, letters]

def merge_letters(letter_couples):
    merging = []
    for i in range(len(letter_couples)):
        temp = ''.join(letter_couples[i])
        merging.append(temp)
    merged = ''.join(merging)
    print(merged)

sent = input("Sentence: ")
couple = make_couples(sent.lower(), alphabet)
print(couple)
enc = encrypt(cypher, couple, alphabet)
print(enc)
merge_letters(enc[1])


