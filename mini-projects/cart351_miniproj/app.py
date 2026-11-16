from PIL import Image # pillow
import sys # to access the files

path = sys.argv[0]
img = Image.open('1.jpg')

#resizing image
width, height = img.size
aspect_ratio = height/width
new_width = 150
new_height = aspect_ratio*new_width
img = img.resize((new_width, int(new_height)))

#greyscaling image
img = img.convert("L") #makes it grey
pixel = img.get_flattened_data()

#characters used for ASCII
characters = [ "@", "#", "$", "%", "^", "&", "!", "*", ";", ":", ",", "."]

#pixels of the image into ASCII
new_pixel = [characters[pixels//25] for pixels in pixel]
new_pixel = "".join(new_pixel)

#alignment of characters
new_pixel_count = len(new_pixel)
final_image = [new_pixel[index:index+new_width] for index in range(0, new_pixel_count, new_width)]
final_image = "\n".join(final_image)

#create a new text file to store data
#2.txt is the new name
with open("2.txt", "w") as f:
    f.write(final_image)