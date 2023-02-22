# SPDX-FileCopyrightText: Copyright ELECFREAKS
# SPDX-License-Identifier: MIT

"""
`picoed.display`
====================================================

CircuitPython driver for the Pico:ed matrix display.

"""

try:
    from adafruit_is31fl3731 import IS31FL3731
except:
    raise ImportError(
        "no module named 'adafruit_is31fl3731'. see: https://github.com/adafruit/Adafruit_CircuitPython_IS31FL3731.git"
    )

_BITMAP = (
    bytes((0x00, 0x00, 0x00, 0x00, 0x00)),
    bytes((0x00, 0x00, 0x5f, 0x00, 0x00)),
    bytes((0x00, 0x07, 0x00, 0x07, 0x00)),
    bytes((0x14, 0x7f, 0x14, 0x7f, 0x14)),
    bytes((0x24, 0x2a, 0x7f, 0x2a, 0x12)),
    bytes((0x23, 0x13, 0x08, 0x64, 0x62)),
    bytes((0x36, 0x49, 0x55, 0x22, 0x50)),
    bytes((0x00, 0x05, 0x03, 0x00, 0x00)),
    bytes((0x00, 0x1c, 0x22, 0x41, 0x00)),
    bytes((0x00, 0x41, 0x22, 0x1c, 0x00)),
    bytes((0x08, 0x2a, 0x1c, 0x2a, 0x08)),
    bytes((0x08, 0x08, 0x3e, 0x08, 0x08)),
    bytes((0x00, 0x50, 0x30, 0x00, 0x00)),
    bytes((0x08, 0x08, 0x08, 0x08, 0x08)),
    bytes((0x00, 0x60, 0x60, 0x00, 0x00)),
    bytes((0x20, 0x10, 0x08, 0x04, 0x02)),
    bytes((0x3e, 0x51, 0x49, 0x45, 0x3e)),
    bytes((0x00, 0x42, 0x7f, 0x40, 0x00)),
    bytes((0x42, 0x61, 0x51, 0x49, 0x46)),
    bytes((0x21, 0x41, 0x45, 0x4b, 0x31)),
    bytes((0x18, 0x14, 0x12, 0x7f, 0x10)),
    bytes((0x27, 0x45, 0x45, 0x45, 0x39)),
    bytes((0x3c, 0x4a, 0x49, 0x49, 0x30)),
    bytes((0x01, 0x71, 0x09, 0x05, 0x03)),
    bytes((0x36, 0x49, 0x49, 0x49, 0x36)),
    bytes((0x06, 0x49, 0x49, 0x29, 0x1e)),
    bytes((0x00, 0x36, 0x36, 0x00, 0x00)),
    bytes((0x00, 0x56, 0x36, 0x00, 0x00)),
    bytes((0x00, 0x08, 0x14, 0x22, 0x41)),
    bytes((0x14, 0x14, 0x14, 0x14, 0x14)),
    bytes((0x41, 0x22, 0x14, 0x08, 0x00)),
    bytes((0x02, 0x01, 0x51, 0x09, 0x06)),
    bytes((0x32, 0x49, 0x79, 0x41, 0x3e)),
    bytes((0x7e, 0x11, 0x11, 0x11, 0x7e)),
    bytes((0x7f, 0x49, 0x49, 0x49, 0x36)),
    bytes((0x3e, 0x41, 0x41, 0x41, 0x22)),
    bytes((0x7f, 0x41, 0x41, 0x22, 0x1c)),
    bytes((0x7f, 0x49, 0x49, 0x49, 0x41)),
    bytes((0x7f, 0x09, 0x09, 0x01, 0x01)),
    bytes((0x3e, 0x41, 0x41, 0x51, 0x32)),
    bytes((0x7f, 0x08, 0x08, 0x08, 0x7f)),
    bytes((0x00, 0x41, 0x7f, 0x41, 0x00)),
    bytes((0x20, 0x40, 0x41, 0x3f, 0x01)),
    bytes((0x7f, 0x08, 0x14, 0x22, 0x41)),
    bytes((0x7f, 0x40, 0x40, 0x40, 0x40)),
    bytes((0x7f, 0x02, 0x04, 0x02, 0x7f)),
    bytes((0x7f, 0x04, 0x08, 0x10, 0x7f)),
    bytes((0x3e, 0x41, 0x41, 0x41, 0x3e)),
    bytes((0x7f, 0x09, 0x09, 0x09, 0x06)),
    bytes((0x3e, 0x41, 0x51, 0x21, 0x5e)),
    bytes((0x7f, 0x09, 0x19, 0x29, 0x46)),
    bytes((0x46, 0x49, 0x49, 0x49, 0x31)),
    bytes((0x01, 0x01, 0x7f, 0x01, 0x01)),
    bytes((0x3f, 0x40, 0x40, 0x40, 0x3f)),
    bytes((0x1f, 0x20, 0x40, 0x20, 0x1f)),
    bytes((0x7f, 0x20, 0x18, 0x20, 0x7f)),
    bytes((0x63, 0x14, 0x08, 0x14, 0x63)),
    bytes((0x03, 0x04, 0x78, 0x04, 0x03)),
    bytes((0x61, 0x51, 0x49, 0x45, 0x43)),
    bytes((0x00, 0x00, 0x7f, 0x41, 0x41)),
    bytes((0x02, 0x04, 0x08, 0x10, 0x20)),
    bytes((0x41, 0x41, 0x7f, 0x00, 0x00)),
    bytes((0x04, 0x02, 0x01, 0x02, 0x04)),
    bytes((0x40, 0x40, 0x40, 0x40, 0x40)),
    bytes((0x00, 0x01, 0x02, 0x04, 0x00)),
    bytes((0x20, 0x54, 0x54, 0x54, 0x78)),
    bytes((0x7f, 0x48, 0x44, 0x44, 0x38)),
    bytes((0x38, 0x44, 0x44, 0x44, 0x20)),
    bytes((0x38, 0x44, 0x44, 0x48, 0x7f)),
    bytes((0x38, 0x54, 0x54, 0x54, 0x18)),
    bytes((0x08, 0x7e, 0x09, 0x01, 0x02)),
    bytes((0x08, 0x14, 0x54, 0x54, 0x3c)),
    bytes((0x7f, 0x08, 0x04, 0x04, 0x78)),
    bytes((0x00, 0x44, 0x7d, 0x40, 0x00)),
    bytes((0x20, 0x40, 0x44, 0x3d, 0x00)),
    bytes((0x00, 0x7f, 0x10, 0x28, 0x44)),
    bytes((0x00, 0x41, 0x7f, 0x40, 0x00)),
    bytes((0x7c, 0x04, 0x18, 0x04, 0x78)),
    bytes((0x7c, 0x08, 0x04, 0x04, 0x78)),
    bytes((0x38, 0x44, 0x44, 0x44, 0x38)),
    bytes((0x7c, 0x14, 0x14, 0x14, 0x08)),
    bytes((0x08, 0x14, 0x14, 0x18, 0x7c)),
    bytes((0x7c, 0x08, 0x04, 0x04, 0x08)),
    bytes((0x48, 0x54, 0x54, 0x54, 0x20)),
    bytes((0x04, 0x3f, 0x44, 0x40, 0x20)),
    bytes((0x3c, 0x40, 0x40, 0x20, 0x7c)),
    bytes((0x1c, 0x20, 0x40, 0x20, 0x1c)),
    bytes((0x3c, 0x40, 0x30, 0x40, 0x3c)),
    bytes((0x44, 0x28, 0x10, 0x28, 0x44)),
    bytes((0x0c, 0x50, 0x50, 0x50, 0x3c)),
    bytes((0x44, 0x64, 0x54, 0x4c, 0x44)),
    bytes((0x00, 0x08, 0x36, 0x41, 0x00)),
    bytes((0x00, 0x00, 0x7f, 0x00, 0x00)),
    bytes((0x00, 0x41, 0x36, 0x08, 0x00)),
    bytes((0x18, 0x04, 0x18, 0x20, 0x18)),
)

class Image():
    NO = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0x22, 0x14, 0x08, 0x14, 0x22, 0x41, 0x00, 0x00, 0x00, 0x00, 0x00))
    SQUARE = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3E, 0x22, 0x22, 0x22, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))
    RECTANGLE = bytes((0xFF, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0xFF))
    RHOMBUS = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x14, 0x22, 0x41, 0x22, 0x14, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00))
    TARGET = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x1C, 0x36, 0x63, 0x36, 0x1C, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00))
    CHESSBOARD = bytes((0x2A, 0x55, 0x2A, 0x55, 0x2A, 0x55, 0x2A, 0x55, 0x2A, 0x55, 0x2A, 0x55, 0x2A, 0x55, 0x2A, 0x55, 0x2A))
    HAPPY = bytes((0x00, 0x00, 0x00, 0x00, 0x10, 0x20, 0x46, 0x40, 0x40, 0x40, 0x46, 0x20, 0x10, 0x00, 0x00, 0x00, 0x00))
    SAD = bytes((0x00, 0x00, 0x00, 0x00, 0x40, 0x22, 0x12, 0x10, 0x10, 0x10, 0x12, 0x22, 0x40, 0x00, 0x00, 0x00, 0x00))
    YES = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x10, 0x20, 0x10, 0x08, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00))
    HEART = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x0E, 0x1F, 0x3F, 0x7E, 0x3F, 0x1F, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00))
    TRIANGLE = bytes((0x00, 0x00, 0x40, 0x60, 0x50, 0x48, 0x44, 0x42, 0x41, 0x42, 0x44, 0x48, 0x50, 0x60, 0x40, 0x00, 0x00))
    CHAGRIN = bytes((0x00, 0x00, 0x00, 0x00, 0x22, 0x14, 0x08, 0x40, 0x40, 0x40, 0x08, 0x14, 0x22, 0x00, 0x00, 0x00, 0x00))
    SMILING_FACE = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x36, 0x50, 0x50, 0x50, 0x36, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00))
    CRY = bytes((0x60, 0x70, 0x70, 0x38, 0x02, 0x02, 0x64, 0x50, 0x50, 0x50, 0x64, 0x02, 0x02, 0x38, 0x70, 0x70, 0x60))
    DOWNCAST = bytes((0x00, 0x00, 0x00, 0x02, 0x0A, 0x11, 0x08, 0x40, 0x40, 0x40, 0x08, 0x11, 0x0A, 0x02, 0x00, 0x00, 0x00))
    LOOK_RIGHT = bytes((0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x26, 0x2F, 0x06, 0x00, 0x06, 0x0F, 0x06, 0x00, 0x00, 0x00))
    LOOK_LEFT = bytes((0x00, 0x00, 0x00, 0x06, 0x0F, 0x06, 0x00, 0x06, 0x2F, 0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))
    TONGUE = bytes((0x00, 0x00, 0x00, 0x00, 0x04, 0x12, 0x14, 0x70, 0x70, 0x70, 0x16, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00))
    PEEK_RIGHT = bytes((0x00, 0x00, 0x04, 0x04, 0x04, 0x0C, 0x0C, 0x40, 0x40, 0x40, 0x04, 0x04, 0x04, 0x0C, 0x0C, 0x00, 0x00))
    PEEK_LEFT = bytes((0x00, 0x00, 0x0C, 0x0C, 0x04, 0x04, 0x04, 0x40, 0x40, 0x40, 0x0C, 0x0C, 0x04, 0x04, 0x04, 0x00, 0x00))
    TEAR_EYES = bytes((0x00, 0x00, 0x00, 0x06, 0x7F, 0x06, 0x20, 0x40, 0x40, 0x40, 0x20, 0x06, 0x7F, 0x06, 0x00, 0x00, 0x00))
    PROUD = bytes((0x01, 0x07, 0x0F, 0x0F, 0x0F, 0x0F, 0x47, 0x41, 0x41, 0x41, 0x27, 0x0F, 0x0F, 0x0F, 0x0F, 0x07, 0x01))
    SNEER_LEFT = bytes((0x00, 0x00, 0x00, 0x0C, 0x08, 0x0C, 0x2C, 0x40, 0x40, 0x40, 0x2C, 0x08, 0x0C, 0x0C, 0x00, 0x00, 0x00))
    SNEER_RIGHT = bytes((0x00, 0x00, 0x00, 0x0C, 0x0C, 0x08, 0x2C, 0x40, 0x40, 0x40, 0x2C, 0x0C, 0x08, 0x0C, 0x00, 0x00, 0x00))
    SUPERCILIOUS_LOOK = bytes((0x00, 0x00, 0x00, 0x0E, 0x0C, 0x0E, 0x00, 0x20, 0x20, 0x20, 0x00, 0x0E, 0x0C, 0x0E, 0x00, 0x00, 0x00))
    EXCITED = bytes((0x60, 0x70, 0x70, 0x3E, 0x01, 0x06, 0x30, 0x50, 0x50, 0x50, 0x30, 0x06, 0x01, 0x3E, 0x70, 0x70, 0x60))

    def __new__(cls, value=None):
        if value is not None and isinstance(value, str):
            data = []
            for pixel_y in range(7):
                if pixel_y < 6:
                    if value[(pixel_y + 1) * 18 - 1] != ":":
                        raise ValueError('Each line of data must be separated with a ":"')
                for pixel_x in range(17):
                    data.append([pixel_x, pixel_y, int(value[pixel_y * 18 + pixel_x])])
            return data
        else:
            return [[0, 0, 0]]



class Display(IS31FL3731):
    """Supports the Pico:ed display by ELECFREAKS"""

    width = 17
    height = 7

    _current_frame = 0

    @staticmethod
    def pixel_addr(x, y):
        """Translate an x,y coordinate to a pixel index."""
        if x > 8:
            x = 17 - x
            y += 8
        else:
            y = 7 - y
        return x * 16 + y

    def _draw(self, buffer, brightness):
        self._current_frame = 0 if self._current_frame else 1
        self.frame(self._current_frame, show=False)
        self.fill(0)
        for x in range(self.width):
            col = buffer[x]
            for y in range(self.height):
                bit = 1 << y & col
                if bit:
                    self.pixel(x, y, brightness)
        self.frame(self._current_frame, show=True)

    def clear(self):
        self.fill(0)

    def scroll(self, value, brightness=30):
        if brightness < 0:
            brightness = 0
        if brightness > 255:
            brightness = 255

        buf = bytearray(self.width)
        text = str(value)

        if len(text) == 1:
            text += '  '
        elif len(text) == 2:
            text += ' '
        elif len(text) != 3:
            text += '   '

        if len(text) == 3:
            for buf_index in range(len(buf)):
                font = bytearray(_BITMAP[ord(text[buf_index // 6]) - 32])
                font.append(0)
                buf[buf_index] = font[buf_index % 6]
            self._draw(buf, brightness)
        else:
            for text_index in range(len(text) * 6):
                for buf_index in range(len(buf) - 1):
                    buf[buf_index] = buf[buf_index + 1]
                font = bytearray(_BITMAP[ord(text[text_index // 6]) - 32])
                font.append(0)
                buf[len(buf) - 1] = font[text_index % 6]
                self._draw(buf, brightness)

    def show(self, value, brightness=30):
        self.clear()
        if isinstance(value, (int, float, str)):
            self.scroll(value, brightness)

        elif isinstance(value, bytes):
            self._draw(value, brightness)
        else:
            for pixel in value:
                self.pixel(pixel[0], pixel[1], int(pixel[2] * 255 / 9))