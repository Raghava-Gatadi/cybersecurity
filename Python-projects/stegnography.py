from PIL import Image
import requests
from io import BytesIO
import numpy as np

def image_url_to_bits(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB") 
    width, height = image.size
    image_array = np.array(image)
    flat_image_array = image_array.flatten()
    binary_representation = [format(pixel, '08b') for pixel in flat_image_array]
    binary_string = ''.join(binary_representation)
    
    return binary_string, [width, height, 3]

def image_path_to_bits(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB") 

    image_array = np.array(image)
    flat_image_array = image_array.flatten()
    binary_representation = [format(pixel, '08b') for pixel in flat_image_array]
    binary_string = ''.join(binary_representation)
    
    return binary_string
def text_to_bits(text):
    binary_representation = ''.join(format(ord(char), '08b') for char in text)
    return binary_representation

def binary_to_text(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    text = ''.join([chr(int(char, 2)) for char in chars])

    return text

def text_insertion(image_binary, text_binary, image_shape):
    if len(text_binary) > len(image_binary) // 8:
        raise ValueError("Text binary is too long to be embedded in the image binary")

    for i in range(0,len(text_binary)):
        image_binary = image_binary[:8*i+7] + text_binary[i] + image_binary[8*i+8:]
        
    pixel_values = [int(image_binary[i:i+8], 2) for i in range(0, len(image_binary), 8)]
    image_array = np.array(pixel_values, dtype=np.uint8)
    image_array = image_array.reshape(image_shape)
    image = Image.fromarray(image_array, 'RGB')
    image_path = "stegno_image.png"
    image.save(image_path)
    print(f"Image saved at {image_path}")

def text_retreival(image_binary):
    text_binary = ""
    for i in range(0,len(image_binary)//8):
        text_binary += image_binary[8*i+7]
    text = binary_to_text(text_binary)
    text = text.split('~')
    return text[0]


def text_encoding():    
    image_url = input("Provide the image link: ")
    image_binary, image_shape = image_url_to_bits(image_url)
    text = input("Enter text to hide in image: ") + "~"
    text_binary = text_to_bits(text)

    text_insertion(image_binary, text_binary, image_shape)

def text_deconding():
    image_path = input("Enter the encoded image path(relative path): ")
    image_binary = image_path_to_bits(image_path)
    decoded_text = text_retreival(image_binary)
    print(f"Decoded text: {decoded_text}")
    
while True:
    option = int(input("Enter 1 for text encoding, 2 for text decoding: "))
    if option ==1:
        text_encoding()
    elif option==2:
        text_deconding()
    else:
        print("Invalid option\nThank you fell free to try again")
        break
    