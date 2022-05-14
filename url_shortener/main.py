import pyshorteners as sh

if __name__ == '__main__':

    url = input("Вставьте URL адрес :")

    shortener = sh.Shortener()

    print(f"URL после сокращения : {shortener.tinyurl.short(url)}")
    print(shortener.available_shorteners)
