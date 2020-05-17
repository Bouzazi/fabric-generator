import sys, os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
''' Import config file '''
from config import *
''' Import required functions. '''
from functions import returnFabricTypeName
from functions import returnFabricParts
from functions import returnLines
from functions import setTempColor
from functions import randomString

''' Time Initialistaion '''
startTime = datetime.now()
print('Generation started at {}'.format(startTime))

''' Handling input variables '''
fabric_name = sys.argv[1].replace("_"," ") # Fabric name (String < 42 characters)
fabric_masterfile = sys.argv[2] # Fabric masterfile name (String)
fabric_extension = sys.argv[3] # Fabric masterfile name (jpg/png/tiff)
fabric_id = sys.argv[4] # Fabric id (5*int-5*int)
seamless = int(sys.argv[5]) # Seamless check (0/1)
inches = int(sys.argv[6]) # Inches
keep_ratio = int(sys.argv[7]) # Respect ratio, for pictures in fabric
background_color = sys.argv[8] # Custom color
path1 = sys.argv[9] # First path, for source files (images, fonts) location.
path2 = sys.argv[10] # Second path, for generated files location.
path3 = sys.argv[11] # Third path, for masterfiles location.
if sys.argv[12] != 'all': # All variations choice
    choice = int(sys.argv[12]) # Size choice (56/42)
    cut_type = sys.argv[13] #  Cut type (full/half/quarter)
    fabric_type = sys.argv[14] # Fabric type (14aida/16aida/18aida/28evenweave/32evenweave/36evenweave/28linen/32linen/36linen/40linen)
    try:
        client_link = sys.argv[15]
    except:
        client_link = ''
else:
    try:
        client_link = sys.argv[13]
    except:
        client_link = ''

''' Create fabric result diretory before generation '''
try:
    os.makedirs(path2+fabric_name.replace(' ', '_'))
except FileExistsError:
    pass
except PermissionError:
    print("Couldn't create directories. Check your folder permissions.")
    exit()

''' Global variables '''
LOGO_LOCATION = path1 + "logoF_110.png"
HAND_ICON_LOCATION = path1 + "handIcon_80.png"
CMYK_LOCATION = path1 + "cmyk.png"
FONT_LOCATION = path1 + "cour.ttf"
CLIENT_LINK = client_link if len(client_link) != 0 else '' # < 20 characters
FABRIC_ID = "#"+str(fabric_id)
SEAMLESS = False if seamless == 0 else True
INCHES = inches * 150 # 150 DPI (Pixels per Inche)

''' Change templates colors to custom color '''
randomTemplateString = randomString()
setTempColor('42', background_color, path1, HEADER, randomTemplateString)
setTempColor('56', background_color, path1, HEADER, randomTemplateString)

''' Split name to two string if long '''
if len(fabric_name) > 22:
    fabric_name_1, fabric_name_2 = returnLines(fabric_name)

''' Open template objects for later manipulation. '''
cmyk = Image.open(CMYK_LOCATION).convert("RGBA")
logo = Image.open(LOGO_LOCATION)
handIcon = Image.open(HAND_ICON_LOCATION)
font = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)

''' Open the fabric file + convert it to RGBA for later manipulation. '''
fabric = Image.open(path3 + fabric_masterfile+'.'+fabric_extension).convert("RGBA")

''' Generates one image and saves it '''
def generate(cut_type, choice, fabric_type):
    ''' Based on the size choice, select a template. '''
    template = Image.open(path1 + str(choice)+'-'+ randomTemplateString +"-template.jpg")

    ''' Draw variable. '''
    draw = ImageDraw.Draw(template)

    ''' Upper stamp '''
    
    ''' Stamp seperator. '''
    draw.text((SEP1, 23), "|", font=font, fill=TEXT_COLOR)
    draw.text((SEP2, 23), "|", font=font, fill=TEXT_COLOR)
    draw.text((SEP1, 35), "|", font=font, fill=TEXT_COLOR)
    draw.text((SEP2, 35), "|", font=font, fill=TEXT_COLOR)
    ''' Safety spray '''
    draw.text((5453, -10), "|", font=font, fill=TEXT_COLOR)

    ''' Left section '''
    ''' Pasting icons. '''
    template.paste(cmyk, (CMYK_X, CMYK_Y), cmyk)
    template.paste(logo, (LOGO_X, LOGO_Y), logo)
    template.paste(handIcon, (HAND_X,HAND_Y), handIcon)
    ''' Website stamp. '''
    draw.text((HAND_X-len(WEBSITE_LINK)*CHAR_WIDTH-25, LINE1_Y), WEBSITE_LINK , font=font, fill=TEXT_COLOR)
    ''' Fabric ID stamp '''
    draw.text((HAND_X-len(FABRIC_ID)*CHAR_WIDTH-25, LINE2_Y), FABRIC_ID , font=font, fill=TEXT_COLOR)
    ''' Fabric name '''
    if len(fabric_name) > 22:
        draw.text((NAME_X, LINE1_Y), fabric_name_1, font=font, fill=TEXT_COLOR)
        draw.text((NAME_X, LINE2_Y), fabric_name_2, font=font, fill=TEXT_COLOR)

        
    else:
        draw.text((NAME_X, LINE_Y), fabric_name, font=font, fill=TEXT_COLOR)
    ''' Client link if provided '''
    ''' Fabric type '''
    fabric_type_name = returnFabricTypeName(fabric_type).replace('-', ' ')
    if len(CLIENT_LINK) != 0:
        draw.text((HALF_WIDH-(len(fabric_type_name)*CHAR_WIDTH)-75, LINE1_Y), fabric_type_name, font=font, fill=TEXT_COLOR)
        draw.text((HALF_WIDH-(len(CLIENT_LINK)*CHAR_WIDTH)-62, LINE2_Y), CLIENT_LINK, font=font, fill=TEXT_COLOR)
    else:
        draw.text((HALF_WIDH-(len(fabric_type_name)*CHAR_WIDTH)-35, LINE_Y), fabric_type_name, font=font, fill=TEXT_COLOR)


    ''' Right section '''
    fabric_type_name = returnFabricTypeName(fabric_type).replace('-', ' ')
    if len(CLIENT_LINK) != 0:
        draw.text((HALF_WIDH+80, LINE1_Y), fabric_type_name, font=font, fill=TEXT_COLOR)
        draw.text((HALF_WIDH+80, LINE2_Y), CLIENT_LINK, font=font, fill=TEXT_COLOR)
    else:
        draw.text((HALF_WIDH+80, LINE_Y), fabric_type_name, font=font, fill=TEXT_COLOR)

    template.paste(logo, (WIDTH-LOGO_X-100, LOGO_Y), logo)
    template.paste(handIcon, (WIDTH-HAND_X-85,HAND_Y), handIcon)
    draw.text((WIDTH-HAND_X+60, LINE1_Y), WEBSITE_LINK, font=font, fill=TEXT_COLOR)
    draw.text((WIDTH-HAND_X+60, LINE2_Y), FABRIC_ID , font=font, fill=TEXT_COLOR)
    if len(fabric_name) > 22:
        draw.text((WIDTH-LOGO_X-125-(len(fabric_name_1)*CHAR_WIDTH), LINE1_Y), fabric_name_1, font=font, fill=TEXT_COLOR)
        draw.text((WIDTH-LOGO_X-125-(len(fabric_name_2)*CHAR_WIDTH), LINE2_Y), fabric_name_2, font=font, fill=TEXT_COLOR)
    else:
        draw.text((WIDTH-LOGO_X-125-(len(fabric_name)*CHAR_WIDTH), LINE_Y), fabric_name, font=font, fill=TEXT_COLOR)

    ''' Lower stamp '''
    uppper_stamp = template.crop((0,0,WIDTH,150)).convert('RGBA').rotate(180)
    template.paste(uppper_stamp, (0, 8250), uppper_stamp) if choice == 56 else template.paste(uppper_stamp, (0, 6150), uppper_stamp)

    ''' Resizing and pasting fabric '''
    for fabPart in returnFabricParts(cut_type, choice, SEAMLESS, INCHES, HEADER):
        if (keep_ratio):
            '''specialFabric = fillColor.resize(fabPart.size)
            template.paste(specialFabric, fabPart.location, specialFabric)'''

            ''' Resize image with keeping ratio and pasting it on the space filler ''' 
            ''' Get new sizes and locations '''
            x = fabPart.location[0]
            y = fabPart.location[1]
            nx = x
            ny = y

            w = fabPart.size[0]
            h = fabPart.size[1]
            nw = w
            nh = h
            m = min(w,h)
            if m == w:
                nh = nw * (fabric.size[1] / fabric.size[0])
                ny = y + ((h - nh)//2)
            else:
                nw = nh * (fabric.size[0] / fabric.size[1])
                nx = x + ((w - nw)//2)

            newLocation = (int(nx),int(ny))
            specialSize = (int(nw),int(nh))
            fabricSize = fabric.resize(specialSize)
            template.paste(fabricSize, newLocation, fabricSize)
        else:
            fabricSize = fabric.resize(fabPart.size)
            template.paste(fabricSize, fabPart.location, fabricSize)

    ''' Create image final structured name '''
    file_name = fabric_name.replace(' ', '_')+"-"+cut_type+"-"+returnFabricTypeName(fabric_type)+"-36x"+str(choice)+".jpg"

    ''' Finally save the image as JPEG '''
    template.save(path2 + fabric_name.replace(' ', '_')+'/'+file_name, "JPEG")

''' Generate all variations or one specific '''
if sys.argv[12] == 'all':
    print('Generating all 60 variations')
    for cut_type in CUT_TYPES:
        for choice in CHOICES:
            for fabric_type in FABRIC_TYPES:
                generate(cut_type, choice, fabric_type)
else:
    generate(cut_type, choice, fabric_type)

''' Script finished execution '''
print("Generation completed, took {}".format(datetime.now() - startTime))
print("Cleaning...")
os.remove(path1 + '42-'+ randomTemplateString +"-template.jpg")
os.remove(path1 + '56-'+ randomTemplateString +"-template.jpg")