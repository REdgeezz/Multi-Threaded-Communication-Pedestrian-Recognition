"""
Author: Huanzhong Ma
Finished Time: 16-6-2024
Function: Some initialization data and some parameters (You can modify them as you please)
"""

SEPARATOR = '@@@@'.encode()

SIZE_SEP = len(SEPARATOR)

SIZE_BYTE = 2**10

SEP_RECV = '@'.encode()

SIZE_SEP_RECV = len(SEP_RECV)

SIZE_BYTE_RECV = 10

NUM_FRAME = 8

FIN = '$_$'.encode()

SIZE_FIN = len(FIN)

urls = {'pedestrian': 'https://cn.bing.com/images/search?q=%E8%A1%8C%E4%BA%BA%E5%9B%BE%E7%89%87&qs=n&form=QBIR&sp=-1&lq=0&pq=%E8%A1%8C%E4%BA%BAtu%27p&sc=0-6&cvid=794AAB8165804E36A188F854CEE384AD&ghsh=0&ghacc=0&first=1'}

DATA_PATH = r'F:/pycharmproject_all/Multi-threaded-communication-main/data'

RES_PATH = r'F:/pycharmproject_all/Multi-threaded-communication-main/result'

BODY_DETECTOR = r"../demo/haarcascade_fullbody.xml"
FACE_DETECTOR = r"../demo/haarcascade_frontalface_alt.xml"

LOG_PATH = r'F:/pycharmproject_all/Multi-threaded-communication-main/log'
