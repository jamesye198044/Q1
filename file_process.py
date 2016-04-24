#!/usr/bin/python
#
#Filename: file_process.py

import sys
import os
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='file_process.log',
                    filemode='w')

def readfile(filename):
    """open the file and parse each line item and select the float number into a tmp list"""

    tmp = []
    with open(filename) as f:
        for line in f:
            for item in line.split():
                try:
                    tmp.append(float(item))
                except Exception as e:
                    logging.error(e.message)

    logging.info('Tempalte list is: %s ' % tmp)

    return tmp


def totalnumber(tmp):
    """count the total number of tmp list"""

    total_number = len(tmp)

    log_message = "Total number is: %d " % total_number

    logging.info(log_message)

    print log_message

    return total_number

def totalsum(tmp):
    """cound the total sum of tmp list"""

    total_sum = 0
    for i in tmp:
        total_sum += float(i)

    log_message = "Total sum is: %f " % total_sum
    logging.info(log_message)

    print log_message

    return total_sum

if __name__ == "__main__":

    filename = sys.argv[1]

    if os.path.exists(filename):

        tmp = readfile(filename)
        totalnumber(tmp)
        totalsum(tmp)

    else:
        log_message = "File not found: %s " % filename
        logging.warning(log_message)


