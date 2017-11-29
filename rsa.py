from rsa_helper import *
import random
import sys
import base64

def generate_keys():

    filename = "crypto.conf"
    p = q = e = d = 0
    #check whether keys are defined in the file, if not gnerate them
    try:
        with open(filename) as f:
            data = f.readlines()

            if len(data) == 2:
                p = int(data[0])
                q = int(data[1])
                if (is_prim(p) or is_prim(q)) == False:
                    raise ValueError('arguments need to be primes')


            elif len(data) == 4:
                p = int(data[0])
                q = int(data[1])
                if not is_prim(p) or not is_prim(q):
                    raise ValueError('arguments need to be primes')
                e = int(data[2])
                d = int(data[3])
            else:
                raise ValueError('Incorrect arguments given in file, there needs to be either 2 or 4 numbers')
        f.close()

    except Exception as error:
        # prime numbers
        print error
        print "No correctly formated crypto.conf file found, generating new keys."
        Primes = PrimEratosthenes(30000)
        p = Primes.get_prime()
        q = Primes.get_prime()

        while p==q: # p and q need to be different.
            q = Primes.get_prime()

        e, d = generate_keys_from_primes(p, q)

        f = open(filename, 'w')
        f.write(str(p) + '\n')
        f.write(str(q) + '\n')
        f.write(str(e) + '\n')
        f.write(str(d) + '\n')

    return p, q, e, d

def generate_keys_from_primes(p, q):
    # RSA modul
    assert (p!=q)
    assert (is_prim(p) and is_prim(q))
    phi = e_phi(p, q)

    #  determine e such that gcd (e, phi(N)) == 1
    e = random.randrange(1,phi)
    while gcd(e, phi) !=1:
        e = random.randrange(1, phi)

    # determine d so that e*d = 1 mod phi
    d = multiplicative_inverse(e, phi)

    return e, d

def encrypt(public_key, plaintext):
    key, n = public_key


    cipher = [power(ord(char),key, n) for char in plaintext]
    c1 = ""

    for i in cipher:
        c1 += str(i) + "|"

    return base64.b64encode(c1)


def decrypt(private_key, ciphertext):
    #Unpack the key into its components

    c = base64.b64decode(ciphertext)
    c = c.split("|")
    del c[-1]
    #print c
    key, n = private_key
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(power(long(char),key, n)) for char in c]
    #Return the array of bytes as a string
    return ''.join(plain)

if __name__ == '__main__':

    p = q = e = d = 0
    plaintext = encrypted = decrypted = ""

    #plaintext = "Hallo"
    #encrypted =

    if(sys.argv[1] == "key-gen" ):
        p, q, e, d = generate_keys()

    elif (sys.argv[1] == "encrypt"):
        p, q, e, d = generate_keys()
        assert(len(sys.argv) == 3)
        plaintext = sys.argv[2]
        #plaintext = "secret message"
        encrypted = encrypt((d, p * q), plaintext)

    elif (sys.argv[1] == "decrypt"):
        p, q, e, d = generate_keys()
        assert (len(sys.argv) == 3)
        encrypted = sys.argv[2]
        decrypted = decrypt((e, p * q), encrypted)

    print "Primes:", p , q
    print "Privatekey:" , e
    print "Publickey:" , d


    print plaintext
    print encrypted
    print decrypted