import os
import nacl.secret
import nacl.utils
import sys

KEY_SIZE = nacl.secret.SecretBox.KEY_SIZE

def get_key():
    key_hex = os.environ.get("SECRETBOX_KEY")
    if key_hex is None:
        print("❌ SECRETBOX_KEY non défini !")
        sys.exit(1)
    key = bytes.fromhex(key_hex)
    if len(key) != KEY_SIZE:
        print(f"❌ Clé incorrecte ! {len(key)} octets trouvés, {KEY_SIZE} attendus")
        sys.exit(1)
    return key

def encrypt_file(input_file, output_file, key):
    box = nacl.secret.SecretBox(key)
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = box.encrypt(data)
    with open(output_file, "wb") as f:
        f.write(encrypted)

def decrypt_file(input_file, output_file, key):
    box = nacl.secret.SecretBox(key)
    with open(input_file, "rb") as f:
        data = f.read()
    decrypted = box.decrypt(data)
    with open(output_file, "wb") as f:
        f.write(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: encrypt/decrypt input output")
        sys.exit(1)

    key = get_key()
    action = sys.argv[1].lower()

    if action == "encrypt":
        encrypt_file(sys.argv[2], sys.argv[3], key)
    elif action == "decrypt":
        decrypt_file(sys.argv[2], sys.argv[3], key)
    else:
        print("Action invalide : encrypt/decrypt")