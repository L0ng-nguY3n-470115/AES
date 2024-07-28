from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_aes_cbc(plaintext, key):
    # Tạo IV ngẫu nhiên
    iv = get_random_bytes(16) 
    
    # Tạo đối tượng AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Mã hóa dữ liệu và trả về bản mã cùng với IV
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv + ciphertext

# Ví dụ sử dụng
key = get_random_bytes(16)  # 48347070595f42495274685f44615959
plaintext = "Đây là một thông điệp bí mật"
ciphertext = encrypt_aes_cbc(plaintext, key)
print(ciphertext)
