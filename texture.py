import struct

class Texture(object):
    def __init__(self, filename):
        with open(filename, "rb") as image:
            # Se carga la información de la imagen, asumiendo
            # que tiene un formato BMP de 24 bits.
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(18)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for y in range(self.height):
                pixelRow = []

                for x in range(self.width):
                    b, g, r = struct.unpack('=BBB', image.read(3))
                    pixelRow.append([r / 256, g / 256, b / 256])

                self.pixels.append(pixelRow)

    def getColor(self, u, v):
        if 0 <= u < 1 and 0 <= v < 1:
            x = int(u * self.width)
            y = int(v * self.height)
            return self.pixels[y][x]  # Reversing y and x indexing
        else:
            return None