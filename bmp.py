"""A module for dealing with BMP bitmap image files."""


def write_grayscale(filename, pixels):
    """Create and write a grayscale BMP file."""
    """
    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.

    Raises:
        OSError: If the file couldn't be written.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        # Next 4 bytes hold the file size as 32-bit.
        size_bookmark = bmp.tell()
        # little-endian integer. Zero placeholder for now.
        bmp.write(b'\x00\x00\x00\x00')

        # Unused 16-bit integer - should be zero.
        bmp.write(b'\x00\x00')
        # Unused 16-bit integer - should be zero.
        bmp.write(b'\x00\x00')

        # The next four bytes hold the integer offset.
        # to the pixel data. Zero placeholder for now.
        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        # Image header
        # Image header size in bytes - 40 decimal
        bmp.write(b'\x28\x00\x00\x00')
        # Image width in pixels
        bmp.write(_int32_to_bytes(width))
        # Image height in pixels
        bmp.write(_int32_to_bytes(height))
        # Number of image planes
        bmp.write(b'\x01\x00')
        # Bits per pixel 8 for grayscale
        bmp.write(b'\x08\x00')
        # No compression
        bmp.write(b'\x00\x00\x00\x00')
        # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')
        # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')
        # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')
        # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')
        # All colors are important
        bmp.write(b'\x00\x00\x00\x00')

        # Color palette - a linear grayscale
        for c in range(256):
            # Blue, Green, Red, Zero
            bmp.write(bytes((c, c, c, 0)))

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        # BMP Files are bottom to top
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            # Pad row to multiple of four bytes
            padding = b'\x00' * ((4 - (len(row) % 4)) % 4)
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian formart."""
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def _bytes_to_int32(b):
    """Convert a byte object containing four bytes into an integer."""
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)


def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image."""
    """
    Args:
        filename: The filename of a BMP file.

    Returns:
        A tuple containing two integers with the width and height in pixels.

    Raises:
        ValueError: If the file was nto a BMP file.
        OSError: If there was a problem reading the file.
    """
    with open(filename, 'rb') as f:
        # First  two magic bytes expected in a BMP file.
        magic = f.read(2)
        # Validate first two magic bytes of file are BMP file.
        if magic != b'BM':
            raise ValueError("{} is not a BMP file".format(filename))

        # Image dimensions stored 18 bytes in file.
        f.seek(18)
        # Width and height bytes of image.
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))
