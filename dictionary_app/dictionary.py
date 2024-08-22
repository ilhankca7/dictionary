import json
import os

# JSON dosyasının yolu
JSON_FILE = 'dictionary.json'

def load_data():
    """JSON dosyasından veriyi yükler."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    """Veriyi JSON dosyasına kaydeder."""
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_word(word, definition):
    """Sözlüğe yeni bir kelime ekler."""
    data = load_data()
    if word in data:
        print(f"Kelime '{word}' zaten mevcut.")
    else:
        data[word] = definition
        save_data(data)
        print(f"Kelime '{word}' eklendi.")

def search_word(word):
    """Sözlükten bir kelimenin anlamını arar."""
    data = load_data()
    definition = data.get(word)
    if definition:
        print(f"{word}: {definition}")
    else:
        print(f"Kelime '{word}' bulunamadı.")

def delete_word(word):
    """Sözlükten bir kelimeyi siler."""
    data = load_data()
    if word in data:
        del data[word]
        save_data(data)
        print(f"Kelime '{word}' silindi.")
    else:
        print(f"Kelime '{word}' bulunamadı.")

def main():
    """Ana menü ve kullanıcı etkileşimleri."""
    while True:
        print("\nSözlük Uygulaması")
        print("1. Kelime Ekle")
        print("2. Kelime Ara")
        print("3. Kelime Sil")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3/4): ")

        if choice == '1':
            word = input("Eklemek istediğiniz kelime: ")
            definition = input("Kelimenin anlamı: ")
            add_word(word, definition)
        elif choice == '2':
            word = input("Aramak istediğiniz kelime: ")
            search_word(word)
        elif choice == '3':
            word = input("Silmek istediğiniz kelime: ")
            delete_word(word)
        elif choice == '4':
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == '__main__':
    main()
