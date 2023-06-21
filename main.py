import random

#test values

def generate_cypher():
    while True:
        cypher = []
        for i in range(4):
            cypher.append(random.randint(0, 27))
        
        det_mat = cypher[0]*cypher[3] - cypher[1]*cypher[2]
        det_mod2 = det_mat%2
        det_mod13 = det_mat%13

        if det_mod2 and det_mod13 != 0:
            break
        elif det_mod2 or det_mod13 == 0:
            pass
    
    return cypher

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
        #Accounts for spaces by replacing them with the letter v
        #Can be replaced with strip() function, but will decide after feedback
        if sentence[i] == ' ':
            couple.append(alphabet.index('v'))
        else:
            couple.append(alphabet.index(sentence[i]))

        i += 1
        if i%2 == 0:
            couple_matrices.append(couple)
            couple = []

        #Will make any uneven words repeat the last letter to make even
        elif i == len(sentence) and i%2 != 0:
            couple.append(alphabet.index(sentence[i-1]))
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
    
    while i < len(couples):
        result = mult_mat(cypher, couples[i])

        final.append([result[0]%26, result[1]%26])
            
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
    return merged

def inverse_mat(matrix):
    determinant = matrix[0]*matrix[3] - matrix[1]*matrix[2]
    det_mod = pow(determinant, -1, 26)
    inverse_matrix = [(matrix[3]*det_mod)%26, (-matrix[1]*det_mod)%26, (-matrix[2]*det_mod)%26, (matrix[0]*det_mod)%26]

    return inverse_matrix

def decrypt(cypher, enc_couples, alphabet):
    decrypted = []
    letters = []
    i = 0
    j = 0

    while i < len(enc_couples):
        result = mult_mat(cypher, enc_couples[i])
        decrypted.append([result[0]%26, result[1]%26])
        i += 1

    while j < len(decrypted):
        temp1 = decrypted[j][0]
        temp2 = decrypted[j][1]
        letter1 = alphabet[temp1]
        letter2 = alphabet[temp2]

        letters.append([letter1,letter2])
        j += 1
    
    return [decrypted, letters]

def get_cypher_user():
    joined = [0,0,0,0]
    joined[0] = int(input("What is the first value of the encrypting matrix? "))
    joined[1] = int(input("What is the second value of the encrypting matrix? "))
    joined[2] = int(input("What is the thrid value of the encrypting matrix? "))
    joined[3] = int(input("What is the fourth value of the encrypting matrix? "))

    return joined


def main():
    alphabet = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    cypher = generate_cypher()

    print("""Welcome to the all-in-one Hill Cypher tool. 
    While this encryption method may be old, it still makes the majority of 1st year Engineering students cry, so it must be decent.
    This program has several options, which you can select using the numbers corresponding to the function:
    1. Encrypt a message
    2. Decrypt a message (with a known cipher)
    3. Crack a cipher and decrypt the message
    
    You may also quit by selecting '0'""")

    while True:

        user = input("\nSelect which function you would like to use: ")

        if user == '1':
            sentence = input("Sentence to encrypt: ").replace(' ', '').lower()
            couple_enc = make_couples(sentence, alphabet)
            enc = encrypt(cypher, couple_enc, alphabet)
            mess_enc = merge_letters(enc[1])
            print(f"Your encrypted message is: {mess_enc}")
            print(f"The cipher used to encrypt it is: {cypher}. Share it only with the recipient of the message!")
        if user == '2':
            known_cyph = get_cypher_user()
            message = input("Sentence to decrypt: ")
            couple_dec = make_couples(message.lower(), alphabet)
            inv_cyph = inverse_mat(known_cyph)
            dec = decrypt(inv_cyph, couple_dec, alphabet)
            mess_dec = merge_letters(dec[1])
            print(f"Here is the decrypted message: {mess_dec}")
        if user == '3':
            pass
        if user == '0':
            print("Thanks for using Hill Cypher, see you next time")
            break

main()
