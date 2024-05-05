message_to_encrypt = input("Enter your text: ")
Key = int(input("Enter the key: "))

# Encryption
encrypted_message = [(ord(i) + Key) for i in message_to_encrypt]
encrypted_message = [chr(i) for i in encrypted_message]
encrypted = "".join(encrypted_message)

# Decryption
decrypted_message = [(ord(i) - Key) for i in encrypted_message]
decrypted_message = [chr(i) for i in decrypted_message]
decrypted = "".join(decrypted_message)

print("The encrypted message is:", encrypted)
print("The decrypted message is:", decrypted)
