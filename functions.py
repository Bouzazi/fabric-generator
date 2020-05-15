from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import string

''' One fabric part '''
class FabricPart:
    def __init__(self, size, location):
        self.size = size
        self.location = location

''' Return fabric parts to just paste in a loop '''
def returnFabricParts(cut_type, choice, seamless, INCHES, HEADER):
    WIDTH = 5490
    HEIGHT = 8400 if choice == 56 else 6300
    SAFETY_SPRAY = 37
    if INCHES != 0: HEADER = 0

    if cut_type == 'full':
        if seamless:
            return [
                FabricPart((WIDTH, HEIGHT-(HEADER*2)-(INCHES*2)), (0, HEADER+INCHES))
            ]
        else:
            return [
                FabricPart(
                    (WIDTH-(SAFETY_SPRAY*2)-(INCHES*2), HEIGHT-(HEADER*2)-(INCHES*2)),
                    (INCHES+SAFETY_SPRAY, HEADER+INCHES)
                )
            ]
    elif cut_type == 'half':
        half_height = ((HEIGHT-(HEADER*2+INCHES*2))//2)-INCHES
        if seamless:
            return [
                FabricPart((WIDTH, half_height), (0, HEADER+INCHES)),
                FabricPart((WIDTH, half_height), (0, HEIGHT-(HEADER+half_height)-INCHES))
            ]
        else:
            return [
                FabricPart(
                    (WIDTH-(SAFETY_SPRAY*2)-(INCHES*2), half_height),
                    (INCHES+SAFETY_SPRAY, HEADER+INCHES)
                ),
                FabricPart(
                    (WIDTH-(SAFETY_SPRAY*2)-(INCHES*2), half_height),
                    (INCHES+SAFETY_SPRAY, HEIGHT-(HEADER+half_height)-INCHES)
                )
            ]
    elif cut_type == 'quarter':
        half_height = ((HEIGHT-(HEADER*2+INCHES*2))//2)-INCHES
    
        if seamless:
            half_width = (WIDTH-INCHES*2)//2
            return [
                FabricPart((half_width, half_height), (0, HEADER+INCHES)),
                FabricPart((half_width, half_height), (half_width+INCHES*2, HEADER+INCHES)),
                FabricPart((half_width, half_height), (0, HEIGHT-(HEADER+half_height)-INCHES)),
                FabricPart((half_width, half_height), (half_width+INCHES*2, HEIGHT-(HEADER+half_height)-INCHES))
            ]
        else:
            half_width = (WIDTH-(INCHES*4)-(SAFETY_SPRAY*2))//2
            return [
                FabricPart(
                    (half_width, half_height),
                    (INCHES+SAFETY_SPRAY, HEADER+INCHES)
                ),
                FabricPart(
                    (half_width, half_height),
                    (half_width+INCHES*3+SAFETY_SPRAY, HEADER+INCHES)
                ),
                FabricPart(
                    (half_width, half_height),
                    (INCHES+SAFETY_SPRAY, HEIGHT-(HEADER+half_height)-INCHES)
                ),
                FabricPart(
                    (half_width, half_height),
                    (half_width+INCHES*3+SAFETY_SPRAY, HEIGHT-(HEADER+half_height)-INCHES)
                )
            ]

''' Return full fabric type name to draw on image '''
def returnFabricTypeName(fabric_type):
    if (fabric_type == "14aida"):
        return "14-Aida"
    elif (fabric_type == "16aida"):
        return "16-Aida"
    elif (fabric_type == "18aida"):
        return "18-Aida"
    elif (fabric_type == "28evenweave"):
        return "28-Evenweave"
    elif (fabric_type == "32evenweave"):
        return "32-Evenweave"
    elif (fabric_type == "36evenweave"):
        return "36-Evenweave"
    elif (fabric_type == "28linen"):
        return "28-Linen"
    elif (fabric_type == "32linen"):
        return "32-Linen"
    elif (fabric_type == "36linen"):
        return "36-Linen"
    elif (fabric_type == "40linen"):
        return "40-Linen"

''' Return two strings for each line '''
def returnLines(fabric_name):
    words = fabric_name.split(' ')
    firstLine = ''
    for i, word in enumerate(words):
        if len(firstLine+word) <= 22: 
            firstLine+=word+' '
        else:
            break
    return (firstLine, ' '.join(words[i:]))


''' Generate random string '''
def randomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))

''' Change template color '''
def setTempColor(temp, hex, path, HEADER, randomTemplate):
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    image = Image.open(path + temp +'-source.jpg')
    image.paste( rgb, [0,HEADER,image.size[0],image.size[1]])
    image.save(path + temp + '-' + randomTemplate + '-template.jpg', "JPEG")