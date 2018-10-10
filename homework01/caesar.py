def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    word=[]
    for i in plaintext:
        i=ord(i)
        if i>119:   
            i=i-23
        else:
            i=i+3
        i=chr(i)
        word.append(i)   
    ciphertext=(''.join(word))
    print(ciphertext)
    return ciphertext



def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    word0=[]
    for i in ciphertext:
        i=ord(i)
        if i<100:
            i=i+23
        else:
            i=i-3
        i=chr(i)
        word0.append(i)
    plaintext=(''.join(word0))
    print(plaintext)
    return plaintext
