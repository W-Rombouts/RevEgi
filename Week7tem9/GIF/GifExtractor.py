from PIL import Image

def extractFrames(image):
    frame = Image.open(image)
    nframes = 0
    while frame:
        frame.save(str(nframes)+'.gif', 'GIF')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break;
    return True

extractFrames('banana_3.gif')