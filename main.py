from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import argparse


parser = argparse.ArgumentParser(description="Generate Elzero python course thumbnail.")

parser.add_argument("-f", "--file", help="Original thumbnail to write on it.")
parser.add_argument("-s", "--name", help="The name of the video", required=True)
parser.add_argument("-n", "--number", help="The number of the video", type=int, required=True)
parser.add_argument("-o", "--output", help="Output file name")

# Prase the arguments here
args = parser.parse_args()

file =  args.file if args.file else "elzero.jpg"
videoName = args.name
videoNumber = str(args.number)


# Adding # sign and zeroz
if len(videoNumber) < 3:
    videoNumber = "#" + ((3 - len(videoNumber)) * "0") + videoNumber


outputFile = args.output + ".jpg" if args.output else "output/elzero_output.jpg"



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

# Successfull message
print(f"Thumbnail generated successfully for {videoName} {videoNumber}")