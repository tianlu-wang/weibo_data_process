__author__ = 'koala'
# extract topics
import re


def extract(path_0, path_original, path_topic):
    f1 = open(path_0, "r")
    f2 = open(path_original, "w")
    f3 = open(path_topic, "w")

    pattern1 = re.compile(r'(.*)(\"mt\":\s\")(.*)(\",\s\"user\")(.*)')
    pattern2 = re.compile(r'(.*)(\')(.*)')
    pattern3 = re.compile(r'(.*)(\#.*\#)(.*)')
    i = 0
    for line in f1.readlines():
        m1 = re.match(pattern1, line, flags=0)  # filter the redundant information
        if m1:
            m2 = re.match(pattern2, m1.group(3), flags=0)  # filter '
            if m2:
                m3 = re.match(pattern3, m2.group(1) + m2.group(3), flags=0)  # filter the #
                if m3:
                    f3.write(m3.group(2) + "\n")
                    f2.write(m3.group(1) + m3.group(3) + "\n")
                else:
                    f2.write(m2.group(1) + m2.group(3) + "\n")
            else:
                m3 = re.match(pattern3, m1.group(3), flags=0)  # filter the #
                if m3:
                    f3.write(m3.group(2) + "\n")
                    f2.write(m3.group(1) + m3.group(3) + "\n")
                else:
                    f2.write(m1.group(3) + "\n")
        else:
            print('no match')
            print i  # which line not match
        i += 1

    f1.close()
    f2.close()
    f3.close()



