#!/usr/bin/python
""" show classic telnet star-wars"""
from time import sleep
DELAY_NORMAL = 67/100000


def main(film):
    """ main..."""
    frame_sleep = 0.01
    with open(film, 'r', encoding='ascii') as F:
        while frame_sleep > 0.0:
            #print(frame_sleep)
            sleep(frame_sleep)
            frame_sleep = int(F.readline())*DELAY_NORMAL
            scr =  "\033c" + ''.join([ F.readline() for _ in range(13) ])
            print(scr, end='')


if __name__ == '__main__':
    main("star-wars.ascii")
