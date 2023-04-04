def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                new_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    while True:
        mode = input("Şifrelemek için 'e', çözmek için 'd', çıkmak için 'q' girin: ").lower()
        if mode == "q":
            break
        if mode not in ["e", "d"]:
            print("Geçersiz giriş. Lütfen 'e', 'd' veya 'q' girin.")
            continue

        text = input("Metni girin: ")
        shift = int(input("Kaydırma miktarını girin (1-25): "))

        if mode == "e":
            result = encrypt(text, shift)
        else:
            result = decrypt(text, shift)

        print(f"Sonuç: {result}\n")
