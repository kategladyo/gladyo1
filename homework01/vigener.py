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
<<<<<<< HEAD
	"""
	>>> decrypt_vigenere("PYTHON", "A")
	'PYTHON'
	>>> decrypt_vigenere("python", "a")
	'python'
	>>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
	'ATTACKATDAWN'
	"""
	# PUT YOUR CODE HERE
	keyword=list(keyword)
	ciphertext=list(ciphertext)
	while len(keyword)<len(ciphertext):
		keyword=keyword+keyword
	plaintext=[]
	#создаем словарь ключей
	key={chr(a):b for (a,b) in zip(range(65,91), range(26))}
=======
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    ciphertext=list(ciphertext)
    keyword=list(keyword)
    while len(keyword)<len(ciphertext):
		keyword=keyword+keyword
	plaintext=[]
    #создаем словарик ключей
    key={chr(a):b for (a,b) in zip(range(65,91), range(26))}
>>>>>>> feature/caesar
	k=0
	for i in range(97,123):
		key[chr(i)]=k
		k+=1
<<<<<<< HEAD
	
	
=======
>>>>>>> feature/caesar
	for i in range(0,len(ciphertext)):
		m=ord(ciphertext[i])
		if m>64 and m<91:
			m=m-key[keyword[i]]
			if m<65:
				m+=26
		if m>96 and m<123:
			m=m-key[keyword[i]]
			if m<97:
				m+=26
		plaintext.append(chr(m))
	plaintext=''.join(plaintext)
<<<<<<< HEAD
		
	return plaintext
=======


    return plaintext
>>>>>>> feature/caesar
