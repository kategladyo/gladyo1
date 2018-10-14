def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """ 
    # PUT YOUR CODE HERE
    k=True
    if n>0 and n<4:
        return k
    else: 
        for i in range(2,n):
            if n%i==0:
                k=not k
                break 
    return k

    pass

def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    del_a=[]
    del_b=[]
    nod=1
    for i in range(1,int(a/2)+1):
        if a%i==0:
            del_a.append(i)
    for i in range(2, int(b/2)+1):
        if b%i==0:
            del_b.append(i)
    for i in del_a:
        if i in del_b:
            nod=i
    return nod
    pass




def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n=p*q
    phi = (p-1)(q-1)

def multiplicative_inverse(e, phi):
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    def gcd_extended(a, b):
        if not b:
            return (a, 1, 0)
        else:
            d, x, y = gcd_extended(b, a % b)
            return (d, y, x - y * (a // b))

    d, x, y = gcd_extended(e, phi)
    return x % phi
    pass
    

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))