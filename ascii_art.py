# import time from ascii_magic import AsciiArt
from src.converter import image_to_ascii

def main():
    ascii_text = image_to_ascii("assets/em.png", columns=120)
    print(ascii_text)

if __name__ == "__main__":
    main()