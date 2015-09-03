__author__ = 'koala'
# filter some special characters
# maybe not necessary....
import re


def filter_weibo(path_original, path_filtered):
    f1 = open(path_original, "r")
    f2 = open(path_filtered, "w")

    for line in f1.readlines():
        r = re.sub(r'#', '', line)
        r = re.sub(r'\'', '', r)
        f2.write(r)

    f1.close()
    f2.close()