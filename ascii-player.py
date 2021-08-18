import socket
import math
from time import sleep

film = ""

TCP_IP = '127.0.0.1'
TCP_PORT = 3131

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

LINES_PER_FRAME = 14
DELAY_NORMAL = 67
DELAY_FAST = 17
DELAY_VERYFAST = 1
global CURRENT_FRAME
CURRENT_FRAME = 0

g_updateDelay = DELAY_NORMAL
g_frameStep = 1
g_timerHandle = 0



def validateFrame(frameNumber):
    return (frameNumber > 0 and frameNumber < math.floor(len(film) / LINES_PER_FRAME))


def displayFrame(frameNumber):

    for line in range(1,14):
        lineText = film[ (CURRENT_FRAME * LINES_PER_FRAME) + line]
        if not lineText or len(lineText) < 1 :
            lineText = ' '
        print(lineText)

def Start():
    CURRENT_FRAME = 0
    Play()

def updateDisplay():
    global CURRENT_FRAME

    displayFrame(CURRENT_FRAME)

    if( g_frameStep != 0 ):
    
    	# read the first line of the current frame as it is a number containing how many times this frame should be displayed
        nextFrameDelay = int(film[CURRENT_FRAME * LINES_PER_FRAME ]) * g_updateDelay

        nextFrame = CURRENT_FRAME + g_frameStep

        if(validateFrame(nextFrame) == True):
            CURRENT_FRAME = nextFrame

        sleep(int(nextFrameDelay)/1000)
        updateDisplay()




def Play():
    g_frameStep = 1
    g_updateDelay = DELAY_NORMAL
    updateDisplay()


if(film):
    Play()

else:
    film = []
