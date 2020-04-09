from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

file = "elzero.jpg";
videoName = "Tuples & Methods \nPart 2"
videoNumber = "25"

# Adding # sign and zeroz
if len(videoNumber) < 3:
    videoNumber = "#" + ((3 - len(videoNumber)) * "0") + videoNumber


outputFile = "output/elzero_output.jpg"



# Open the image
img = Image.open(file)

draw = ImageDraw.Draw(img)  # Draw object

# Fonts
videoNameFont = ImageFont.truetype("fonts/Nunito-Bold.ttf", 72)
videoNumberFont = ImageFont.truetype("fonts/gadugib.ttf", 78)


# Write on the image
vidoeNamePosition = (84, 210)
videoNameColor = (255, 255, 255) # white color

vidoeNumberPosition = (15, 595)
videoNumberColor = (2, 52, 94) # #02345e

draw.text(vidoeNamePosition, videoName, videoNameColor, font=videoNameFont)

draw.text(vidoeNumberPosition, videoNumber, videoNumberColor, font=videoNumberFont)


img.save(outputFile)