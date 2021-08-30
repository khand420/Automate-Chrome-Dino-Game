import pyautogui
from PIL  import Image, ImageGrab
# from numpy import asarray
import time
# while True:
#     pyautogui.keyDown('k')
#     kkkkkkkkkkkkkkkkkkkkkk kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):

    # draw the rectangele for Birds
    for i in range(460, 470):
        for j in range(105, 195):
            if data[i, j] < 100:
                hit("down")
                return 




    for i in range(450, 470):
        for j in range(105, 230):
            if data[i, j]  < 100:
                hit("up")
                return 


    
                         
    return 



if __name__ == "__main__":
    print("Hey...Dino Game about to start in 3 second")   
    time.sleep(3)
    # hit('up')


    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            # hit("up")
        # print(asarray(image))


        # # draw the rectangele for cactus
        # for i in range(460, 470):
        #     for j in range(105, 230):
        #         data[i, j] = 0

        # # draw the rectangele for Birds
        # for i in range(460, 470):
        #     for j in range(105, 195):
        #         data[i, j] = 171
         
        # image.show()
        # # break        

    
        

                
