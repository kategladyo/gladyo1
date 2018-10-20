def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    keyword = list(keyword)
    plaintext = list(plaintext)
    while len(keyword) < len(plaintext):
        keyword = keyword + keyword
    ciphertext = ''
    # создаем словарь ключей
    key = {chr(a): b for (a, b) in zip(range(65, 91), range(26))}
    k = 0
    for i in range(97, 123):
        key[chr(i)] = k
        k += 1
    # непосредственно сдвигаем буквы
    for i in range(0, len(plaintext)):
        m = plaintext[i]
        if m >= 'a' and m <= 'z':
            m = chr(ord(m) + key[keyword[i]])
            if m > 'z':
                m = chr(ord(m) - 26)
        if m >= 'A' and m <= 'Z':
            m = chr(ord(m) + key[keyword[i]])
            if m > 'Z':
                m = chr(ord(m) - 26)
        ciphertext += m
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    keyword = list(keyword)
    ciphertext = list(ciphertext)
    while len(keyword) < len(ciphertext):
        keyword += keyword
    plaintext = ''
    # создаем словарь ключей
    key = {chr(a): b for (a, b) in zip(range(65, 91), range(26))}
    k = 0
    for i in range(97, 123):
        key[chr(i)] = k
        k += 1
    # непосредственно возвращаем буквы на место
    for i in range(0, len(ciphertext)):
        m = ciphertext[i]
        if m >= 'a' and m <= 'z':
            m = chr(ord(m) - key[keyword[i]])
            if m < 'a':
                m = chr(ord(m) + 26)
        if m >= 'A' and m <= 'Z':
            m = chr(ord(m) - key[keyword[i]])
            if m < 'A':
                m = chr(ord(m) + 26)
        plaintext += m
    return plaintext
