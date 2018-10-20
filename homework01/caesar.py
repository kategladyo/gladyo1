def encrypt_caesar(plaintext: str) -> str:
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
    ciphertext = ''
    for ch in plaintext:
        if ch >= 'x' and ch <= 'z':
            ch = chr(ord(ch) - 23)
        elif ch >= 'a' and ch < 'x':
            ch = chr(ord(ch) + 3)
        elif ch >= 'X' and ch <= 'Z':
            ch = chr(ord(ch) - 23)
        elif ch >= 'A' and ch < 'X':
            ch = chr(ord(ch) + 3)
        ciphertext += ch
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
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
    # my code
    plaintext = ''
    for ch in ciphertext:
        if ch >= 'a' and ch <= 'c':
            ch = chr(ord(ch) + 23)
        elif ch >= 'd' and ch <= 'z':
            ch = chr(ord(ch) - 3)
        elif ch >= 'A' and ch <= 'C':
            ch = chr(ord(ch) + 23)
        elif ch >= 'D' and ch <= 'Z':
            ch = chr(ord(ch) - 3)
        plaintext += ch
    return plaintext
