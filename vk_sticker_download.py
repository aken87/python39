import string
import random
import os
import sys
import _thread
import httplib2
import time
#https://vk.com/sticker/1-1-512
#https://vk.com/sticker/1-21920-512

#[+] Valid: https://vk.com/sticker/G2U.png
 #  https://vk.com/sticker/1-1-512

THREAD_AMOUNT = int(1)
INVALID = [0, 503, 5082, 4939, 4940, 4941, 12003, 5556]

def scrape_pictures(thread):
    while True:
        url = 'https://vk.com/sticker/'
        sticker_Id = 1
        if sticker_Id == 1:
            url += '1-' + (str(sticker_Id)) + '-512' +'.png'       
            print(url)
            
        filename = url.rsplit('/', 1)[-1]
        # print (filename)

        h = httplib2.Http('.cache' + thread)
        response, content = h.request(url)
        out = open(filename, 'wb')
        out.write(content)
        out.close()

        file_size = os.path.getsize(filename)
        if file_size in INVALID:
            print("[-] Invalid: " + url)
            os.remove(filename)
        else:
            print("[+] Valid: " + url)

for thread in range(1, THREAD_AMOUNT + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(scrape_pictures, (thread,))
    except:
        print('Error starting thread ' + thread)
print('Succesfully started ' + thread + ' threads.')

while True:
    time.sleep(1)
