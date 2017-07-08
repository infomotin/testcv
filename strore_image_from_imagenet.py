import cv2
import os
from six.moves import urllib
import numpy as np
import sys
import io
def storing_image():
    if not os.path.exists('row_pic'):
                os.mkdir('row_pic',755)
    with io.open('url.txt','r') as link:
        for row_url in link.readlines():
            print row_url
            neg_image_urls = urllib.request.urlopen(row_url).read().decode('utf-8')
            #for count of dir file
            file_no = os.listdir('row_pic')
            pic_num = len(file_no)
            print pic_num
            if pic_num == 0:
                pic_no=1
            else:
                pic_no = pic_num
            for url_open in neg_image_urls.split('\n'):
                try:
                    print url_open
                    urllib.request.urlretrieve(url_open, "row_pic/"+str(pic_no)+".jpg")
                    img = cv2.imread("row_pic/"+str(pic_no)+".jpg",cv2.IMREAD_GRAYSCALE)
                
                    resized_image = cv2.resize(img, (100, 100))
                    cv2.imwrite("row_pic/"+str(pic_no)+".jpg",resized_image)
                    print pic_no
                    pic_no += 1


                except Exception as e:
                        print(str(e))
#call function 
storing_image()                
def find_uglies():
  if not os.path.exists('uglies'):
                os.mkdir('uglies',755)
  
  
    match = False
    for file_type in ['row_pic']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
def create_pos_n_neg():
    for file_type in ['row_pic']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'row_pic':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)            
    
    
