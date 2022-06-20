import PIL.Image as Image
import io
import base64
import json

# Opening JSON file
with open('1.json') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))

    # Print the data of dictionary

    for image in data:
        b = base64.b64decode(image)
        img = Image.open(io.BytesIO(b))
        img.show()
