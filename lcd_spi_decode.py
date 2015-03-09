#!/usr/bin/env python
import sys
import re

BUSPIRATE_RE = re.compile(r"\(0x([0-9a-zA-Z]{2})\)")
DECAWAVE_LCD_RE = re.compile(r"(LAST|AVG8):.*(\d{1,3}\.\d{1,3}).*m")

def hex2bin(x):
    assert len(x) == 2
    return "{0:b}".format(int(x, 16)).zfill(8)

def bin2dec(data):
    return int(data, 2)

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


if __name__ == "__main__":

    synced = False
    while True:

        # There is a reason why I'm reading this way rather than doing for line
        # in stdin: buffering issues
        line = sys.stdin.readline()

        # cut newline
        line = line[:-1]

        if not synced:
            sys.stderr.write("Syncing - got: {}".format(line))
            if line == "Sync":
                synced = True
        else:

            # Parse bus pirate formatting like [0x00(0x12)]
            data = BUSPIRATE_RE.findall(line)

            # Convert those to a string of padded binary
            data_binary = "".join([hex2bin(x) for x in data])

            # Shift those bits by 1 because decawave is weird as shit
            data_shifted = data_binary[1:]

            # Split them back into chunks of 8 bits
            characters = list(chunks(data_shifted, 8))

            # Convert those bit chunks into ints then ascii
            ascii_characters = [chr(bin2dec(x)) for x in characters]

            message = "".join(ascii_characters)
            parsed =  DECAWAVE_LCD_RE.findall(message)

            if len(parsed) > 0:
                if parsed[0][0] == "LAST":
                    print "LAST: ", parsed[0][1]
                else:
                    print "AVG8: ", parsed[0][1]
            sys.stdout.flush()
