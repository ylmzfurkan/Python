def replace_word():

    # str adlı değişkene örnek cümleyi tanımla.
    str = "Hi guys, I am Furkan , and hi hi hi hi"

    # Kullanıcıdan değiştirilecek kelimeyi iste ve word_to_replace adlı değişkene ata.
    word_to_replace = input("Değiştirilecek kelimeyi girin: ")

    # Kullanıcıdan yerine geçecek kelimeyi iste ve word_replacement adlı değişkene ata.
    word_replacement = input("Yerine geçecek kelimeyi girin: ")

    # Cümle içinde belirlenen kelimeyi, kullanıcının girdiği kelime ile değiştir ve sonucu yazdır.
    print(str.replace(word_to_replace , word_replacement))

replace_word()


