
from rembg import remove

from PIL import Image

# input_path = 'clgot.jpeg'
# input_path = 'image.png'
input_path = 'img.png'

output_path = 'clgot.png'

inp = Image.open(input_path)

output = remove(inp)

output.save(output_path)

Image.open("clgot.png")
