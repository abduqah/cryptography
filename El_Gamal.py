import random
ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
      71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
      151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
      233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
      313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
      409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
      491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593,
      599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677,
      683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
      787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
      883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def modexp( base, exp, modulus ):
    return pow(base, exp, modulus)

def find_primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p-1) // p1
    while( 1 ):
        g = random.randint( 2, p-1 )
        if not (modexp( g, (p-1)//p1, p ) == 1):
            if not modexp( g, (p-1)//p2, p ) == 1:
                return g

def encrypt(text, key):
    cypher = ''
    for ch in text:
        m = ord(ch)
        #print('m = ', m)
        k = int(random.random()*(key[0]-2)) + 1
        y = (key[1]**k)%key[0]
        #print('y = ' ,y)
        z = ((key[2]**k) * m)%key[0]
        #print('z = ', z)
        cypher += chr(y) + chr(z)
    return cypher
def decrypt(cypher, x, p):
    text = ''
    #print(len(cypher))
    for ch1, ch2 in zip(cypher[::2], cypher[1::2]):
        y = ord(ch1)
        #print('y d = ', y)
        z = ord(ch2)
        #print('z d = ', z)
        r = (y**(p-1-x))%p
        #print('r = ', r)
        m = (r * z)%p
        text += chr(m)
    return text
def bob(publickey):
    with open('Massege', 'r') as f:
        cypher = encrypt(f.read().rstrip(), publickey)
        with open('Cypher', 'w') as fc:
            fc.write(cypher)
    return
def alice():
    p = 991
    a = 27
    x = 53
    d = (a**x)%p
    print('d = ', d)
    publicKey = (p, a, d)
    #print('public key : ' ,publicKey)
    bob(publicKey)
    with open('Cypher', 'r') as f:
        cypher = f.read()
        text = decrypt(cypher, x, p)
        with open('Massege', 'w') as fm:
            fm.write(text)
    return

alice()