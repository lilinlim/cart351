from PIL import Image #pillow
import os #operating system

#characters used for ASCII
#suggested order is darker to lighter characters
ASCII_CHARS = [ "@", "#", "$", "%", "^", "&", "!", "*", ";", ":", ",", "."]

#resizing image
def resize_image(image, new_width=55):
    #gets the original dimensions
    (original_width, original_height) = image.size
    #aspect ratio
    aspect_ratio = original_height / float(original_width)
    #new height
    new_height = int(aspect_ratio * new_width)
    #returns resize
    return image.resize((new_width, new_height))

#grayscale the image
def grayscale(image):
    return image.convert('L') #converts it to 8-bit grayscale

#
def pixels_to_ascii(image, range_width=25): #value makes the ascii darker or light
    pixels = list(image.getdata())
    ascii_chars = [ASCII_CHARS[pixel_value // range_width] for pixel_value in pixels]
    return "".join(ascii_chars)

def image_to_ascii(image, new_width=25):
    #resizes the image
    image = resize_image(image, new_width)

    #grayscales it
    image = grayscale(image)

    #pixelfies the image
    ascii_string = pixels_to_ascii(image)
    
    # Split into lines
    ascii_lines = [ascii_string[i:i + new_width] for i in range(0, len(ascii_string), new_width)]
    return "\n".join(ascii_lines)

#function to call in main.py bc it has the output
def convert_image_to_ascii(image_filepath, output_width=50):
    
    image = Image.open(image_filepath)
    
    # Convert to ASCII
    ascii_art = image_to_ascii(image, output_width)
    
    #saving to text file
    output_file = os.path.splitext(image_filepath)[0] + '.txt'

    #output_file means it won't rename it, compared to previous code where we forced named it
    with open(output_file, 'w') as f:
        f.write(ascii_art) #overwrites the file

    return ascii_art

#example to test that it works
# convert_image_to_ascii('1.jpg', 50)