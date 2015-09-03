__author__ = 'koala'
# do segmentation
# -*- coding:utf8 -*-z
import jieba
import codecs
jieba.load_userdict("weibo/usrdict.txt")


def jieba_seg(path_filtered, path_segmentation):
    inputFile = codecs.open(path_filtered, 'r', 'utf-8')
    outputFile = codecs.open(path_segmentation, 'w', 'utf-8')

    for line in inputFile.readlines():
        seg_list = jieba.cut(line, cut_all=True)
        outputFile.write(" ".join(seg_list))




