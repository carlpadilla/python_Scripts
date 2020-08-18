from PIL import Image, ImageFilter

img = Image.open('./Pokedex/charmander.jpg')
filtered_img = img.filter(ImageFilter.BLUR)


filtered_img.save('Blurred.png', 'png')
filtered_img.show()
print(img)
