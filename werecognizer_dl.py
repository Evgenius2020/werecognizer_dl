import requests
import json
import sys

demo_url = 'https://spikecv-demo.sysbio.ru'

def get_masks(img_path, save_files=True):
    request = requests.post(
        demo_url + '/sendfile/savefiles=' + str(save_files).lower(), 
        files={'file2upload': open(img_path,'rb')} )

    response = request.json()
    masks_file = response['masks']

    open(img_path[:img_path.rfind('.')] + '_masks.png' , 'wb').write(requests.get(demo_url + '/image/' + masks_file).content)

    # del response['orig']
    # del response['masks']
    # del response['result']

    return response

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ' + sys.argv[0] + " 'img_path'")
    else:
        print(get_masks(sys.argv[1]))