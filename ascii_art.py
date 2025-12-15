import time
from ascii_magic import AsciiArt

art = AsciiArt.from_image(
    './image/em.png'
)

ascii_text = art.to_ascii(columns=120)

for line in art.to_ascii().split('\n'):
    print(line)
    time.sleep(0.05)
