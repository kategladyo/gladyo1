def encrypt_vigenere(plaintext, keyword):
	"""
	>>> encrypt_vigenere("PYTHON", "A")
	'PYTHON'
	>>> encrypt_vigenere("python", "a")
	'python'
	>>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
	'LXFOPVEFRNHR'
	"""
	# PUT YOUR CODE HERE
	keyword=list(keyword)
	plaintext=list(plaintext)
	while len(keyword)<len(plaintext):
		keyword=keyword+keyword
	ciphertext=[]
	#создаем словарь ключей
	key={chr(a):b for (a,b) in zip(range(65,91), range(26))}
	k=0
	for i in range(97,123):
		key[chr(i)]=k
		k+=1
	
	
	for i in range(0,len(plaintext)):
		m=ord(plaintext[i])
		if m>64 and m<91:
			m=m+key[keyword[i]]
			if m>90:
				m-=26
		if m>96 and m<123:
			m=m+key[keyword[i]]
			if m>122:
				m-=26
		ciphertext.append(chr(m))
	ciphertext=''.join(ciphertext)
	
	return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    return plaintext
