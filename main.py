__author__ = 'koala'
# to find is there any morph entity in the weibo data set
from weibo.extract import *
from weibo.filter_weibo import *
from weibo.jieba_seg import *
from weibo.match import *

path0 = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/20130327/0327"
path0 = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/20130327/0327"
path_original = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/0327/0327"
path_topic = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/0327/0327_topic"
path_filtered = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/0327/0327_filtered"
path_segmentation = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/0327/0327_segmentation"
path_morph_entity = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/0327/morph_entity.txt"
path_result = "/Users/koala/Documents/lab/Blender/morph/dataset_sha/0327/0327_result"

extract(path0, path_original, path_topic)
filter_weibo(path_original, path_filtered)
jieba_seg(path_filtered, path_segmentation)
match(path_segmentation, path_result, path_morph_entity)
