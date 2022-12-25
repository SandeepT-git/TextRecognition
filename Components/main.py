import cv2 as cv
import pytesseract
import os

#Tesseract local path set from local machine - Mac OS
pytesseract.pytesseract.tesseract_cmd =r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'

def file_path_exists(file_path):
    image_abs_path = os.path.abspath(file_path)
    #assert os.path.exists(list_img_path)
    return os.path.exists(image_abs_path)

def get_text_extracted_from_image(list_img_path):
    list_data_set=[]
    
    image_path = cv.imread(list_img_path)
    result = pytesseract.image_to_string(image_path)
    list_data_set.append(result)

    return list_data_set


if __name__ == '__main__':
    image_path = "Images/image_1.jpg"
    
    if file_path_exists(image_path):
        list_data_set = get_text_extracted_from_image(image_path)
        print(list_data_set)
    else:
        print('File within the file path doesnot exists')



