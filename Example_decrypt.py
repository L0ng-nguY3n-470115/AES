from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_aes_cbc(ciphertext, key):
    # Tách IV ra từ bản mã
    iv = ciphertext[:16] # 
    ciphertext = ciphertext[16:]
    
    # Tạo đối tượng AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Giải mã và trả về bản rõ
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

# Ví dụ sử dụng
decrypted_text = decrypt_aes_cbc(ciphertext, key)
print(decrypted_text)
