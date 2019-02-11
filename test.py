'''
Python 获取本机磁盘列表 by 郑瑞国
'''

import string
import os


def get_disklist():
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c + ':'
        if os.path.isdir(disk):
            disk_list.append(disk)
    a =os.path.isdir(r"h:\\")

    # a =os.path.ismount(r"h:\\")
    print(a)
    return disk_list


if __name__ == '__main__':
    print(get_disklist())
