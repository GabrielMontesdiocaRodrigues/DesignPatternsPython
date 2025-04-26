class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self): 
        print(f"Drawing image {self.filename}")

class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None

    def draw(self): 
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename) 
        self.bitmap.draw()

def draw_image(image):

    print(f'About to draw image')
    image.draw()
    print(f'Done drawing image')

if __name__ == '__main__':
    bmp = LazyBitmap('image.jpg')
    draw_image(bmp)
    draw_image(bmp)