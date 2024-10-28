import cv2


def img_load_resize(path:str,height : int, width : int) -> tuple:
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,img_black_white = cv2.threshold(img_gray,127, 255,cv2.THRESH_BINARY)
    img_final = cv2.resize(img_black_white,(width,height))
    return img_final,height,width




def img_to_ascii():
    img,altezza, larghezza = img_load_resize("photo.jpg",200,200)
    result = ""
    for i in range(altezza - 1 ):
        for j in range(larghezza - 1):
            if img[i][j] == 255:
                result += "*"
            else:
                result += " "
        result += "\n"
                
    print(result)     

if __name__ == "__main__":
    img_to_ascii()
