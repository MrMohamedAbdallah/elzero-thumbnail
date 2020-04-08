from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

file = "elzero.jpg";
videoName = "Tuples & Methods \nPart 2"
outputFile = "output/elzero_output.jpg"



# Open the image
img = Image.open(file)

draw = ImageDraw.Draw(img)  # Draw object

videoNameFont = ImageFont.truetype("fonts/Nunito-Bold.ttf", 75)


# Write on the image
vidoeNamePosition = (84, 236)
videoNameColor = (255, 255, 255) # white color

draw.text(vidoeNamePosition, videoName, videoNameColor, font=videoNameFont)

img.save(outputFile)