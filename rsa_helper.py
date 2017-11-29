from random import randint


class PrimEratosthenes:

    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.number_is_prime = [True] * (self.upper_limit)
        self.number_is_prime[0] = self.number_is_prime[1] = False
        self.primes = []
        self.calculate()
        #self.print_prims()


    def calculate(self):

        for i in range(2, self.upper_limit):
            if self.number_is_prime[i]:
                self.primes.append(i)
                for j in range(i*i, self.upper_limit, i):
                    self.number_is_prime[j] = False

    def get_prime(self):
        i = randint(0,len(self.primes))
        return self.primes[i]


def is_prim(n):

    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, int(n**0.5), 2):
        if n % i == 0:
            return False

    return True


def power(x, m, n):
    """Calculate x^m modulo n using O(log(m)) operations."""
    a = 1
    while m > 0:
        if m % 2 == 1:
            a = (a * x) % n
        x = (x * x) % n
        m //= 2
    return a


def e_phi(p, q):  # only works for p,q = prim

    return (p-1)*(q-1)


def gcd(a, b):  # Euclid'# s algorithm calculates greatest common divisor  of a and b

    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
