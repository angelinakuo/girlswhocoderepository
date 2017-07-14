from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
my_image = Image.open("spaceneedle.jpg")
image_list = my_image.getdata()
image_list = list(image_list)

recolored = [] #list that will hold the pixel data for the new image.

for pixel in image_list:
    RGB = pixel[0] + pixel[1] + pixel[2]
    if RGB <182:
        recolored.append(darkBlue)
    elif RGB <364:
        recolored.append(red)
    elif RGB <546:
        recolored.append(lightBlue)
    else:
        recolored.append(yellow)

new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
