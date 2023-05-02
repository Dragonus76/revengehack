import hashlib
import itertools
import string
import random
from Crypto.Cipher import AES

# Fonction pour ajuster la longueur de la clé
def pad_key(key, desired_length=16):
    return hashlib.sha256(key.encode()).digest()[:desired_length]

# Fonction pour générer des combinaisons de mots de passe avec des mutations
def generate_mutated_passwords(passwords, charset):
    mutated_passwords = []
    
    for password in passwords:
        for index, char in enumerate(password):
            for new_char in charset:
                mutated_password = list(password)
                mutated_password[index] = new_char
                mutated_passwords.append(''.join(mutated_password))
                
    return mutated_passwords

# Fonction pour générer des clés aléatoires
def generate_random_key(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

# Fonction pour déchiffrer les données avec AES
def decrypt_data_aes(data, key):
    padded_key = pad_key(key)  # Ajuster la longueur de la clé
    cipher = AES.new(padded_key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data.rstrip(b'\0')

# Fonction pour décrypter les mots de passe avec l'algorithme amélioré
def enhanced_brute_force(target_data, charset, min_length, max_length):
    for length in range(min_length, max_length + 1):
        random_key = generate_random_key(length)
        decrypted_data = decrypt_data_aes(target_data, random_key)
        
        for password in generate_mutated_passwords([random_key], charset):
            if decrypted_data == password.encode():
                return random_key, password
    return None, None

# Fonction principale pour décrypter les mots de passe
def enhanced_decrypt_password(target_data, min_length, max_length):
    charset = string.ascii_letters + string.digits + string.punctuation
    
    random_key, decrypted_password = enhanced_brute_force(target_data, charset, min_length, max_length)
    
    if decrypted_password is not None:
        return random_key, decrypted_password
    else:
        print("Aucun mot de passe trouvé.")
        return None, None

# Exemple d'utilisation
if __name__ == "__main__":
    target_data = b'\x9f\x97\x15\x85\x8b\xc2\x03\xe2\xee\x89\x1e\xfb\x1c\x91\x15\x6c'  # Données chiffrées avec le mot de passe "password" et une clé AES
    min_length = 4
    max_length = 10

    random_key, decrypted_password = enhanced_decrypt_password(target_data, min_length, max_length)
    print(f"Clé aléatoire: {random_key}")
    print(f"Mot de passe décrypté: {decrypted_password}")
