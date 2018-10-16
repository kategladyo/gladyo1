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
    # my code
    word = []
    for i in plaintext:
        i = ord(i)
        if i > 119 and i < 123:
            i = i - 23
        elif i > 96 and i < 120:
            i = i + 3
        elif i > 87 and i < 91:
            i = i - 23
        elif i > 64 and i < 88:
            i = i + 3
        i = chr(i)
        word.append(i)
    ciphertext = (''.join(word))
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
    #my code
    word0 = []
    for i in ciphertext:
        i = ord(i)
        if i > 64 and i < 68:
            i = i + 23
        elif i > 96 and i < 100:
            i += 23
        elif i > 99 and i < 123:
            i = i - 3
        elif i > 67 and i < 91:
            i -= 3
        i = chr(i)
        word0.append(i)
    plaintext = (''.join(word0))
    return plaintext
