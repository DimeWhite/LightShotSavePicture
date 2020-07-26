from LightShot import LightShot
import string

chars = []
for i in range(0, 10):
    chars.append(i)
for i in string.ascii_lowercase:
    chars.append(i)

Light = LightShot()
while True:
    try:
        pictures = Light.get_picture(Light.create_url(chars))
        Light.save_picture("D:\Python\lightshot\save", pictures[0], pictures[1])
    except:
        pass