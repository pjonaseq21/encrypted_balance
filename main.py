from encrypt import encrypt_file,get_key
from decrypt import decrypt_file
import os
from summarize import summarize

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            print(os.path.join(root, filename))
            return os.path.join(root, filename)
    return None

def main():
    file_path = 'starting_file.txt'
    if find_file("starting_file.txt.enc","./"):
        print("znaleziono zaszyfrowany plik \n")
        key = input()
        decrypted_file = decrypt_file(f"{file_path}.enc", key)
        integrer_value = decrypted_file.decode("utf-8")
    

        print("Wpisz 1 zeby zmienic wartosc")
        print("Wpisz 2 zeby zobaczyc ostatnia wartosc")
        switch = input()
        match switch:
            case "1":
                with open("starting_file.txt","a") as f:
                    f.write(str(integrer_value))
                    f.close()
                summarize("starting_file.txt")
                os.remove("starting_file.txt.enc")
                encrypt_file("starting_file.txt",key)
                os.remove("starting_file.txt")
            case "2":
                print(integrer_value)
    else:
        print("nie wykryto zaszyfrowanego pliku uzywam pliku txt podaj klucz bezpieczenstwa do zaszyfrowania \n")
        key = input()
        encrypt_file("starting_file.txt",key)
        os.remove("starting_file.txt")

if __name__ == "__main__":
    main()