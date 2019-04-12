#!/usr/bin/python3
from PIL import ImageGrab

if __name__ == "__main__":
    img = ImageGrab.grabclipboard()
    # or ImageGrab.grab() to grab the whole screen!
    print(img)
    img.save('paste.jpg', 'JPEG')