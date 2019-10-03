#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@author: zhuxl
"""

import os
import re
import csv


def populate_filename_from_hyperlink(hyperlink):
    '''
    Populate filename from wj hyperlink in csv
    =Hyperlink(""https://wj.qq.com/sfile/survey/answer_file_show?survey_id=1504537&question_id=q-4-PMz4&file_name=0_598e735b686afphpQYku2Ce340.JPG&download=1""，""0_598e735b686afphpQYku2Ce340.JPG"")
    '''
    match = re.search(r'"(\S+)"，"(\S+)"', hyperlink) # test re at http://regexr.com
    if match:
        filename = match.group(2)

    return filename


def load_photo_name_data(csv_file, photo_index = 0, name_index = 0):
    ''' Load wj csv data with specified photo(as key) and name(as value) index to populate data '''
    if not os.path.exists(csv_file):
        print("The csv file [{}] is not exists.".format(csv_file))
        return False

    photo_name_data = dict()

    with open(csv_file) as data_file:
        reader = csv.reader(data_file, delimiter = ',', quotechar = '"')
        reader.next() # skip the header

        for row in reader:
            k = populate_filename_from_hyperlink(row[photo_index])
            photo_name_data[k] = row[name_index]

    return photo_name_data


def find_rename_photos(photos_dir, photo_name_data):
    ''' Find photos local and rename them with names data '''
    if not os.path.exists(photos_dir):
        print("The photos dir [{}] is not exists.".format(photos_dir))
        return False

    for k in photo_name_data:
        parts = k.split('.')

        photo_file = os.path.join(photos_dir, k)
        new_file = os.path.join(photos_dir, photo_name_data[k] + '.' + parts[1])

        print k, ' => ', new_file

        if os.path.exists(photo_file):
            os.rename(photo_file, new_file)
        else:
            print photo_file, ' is NOT exist so skipped. <=', photo_name_data[k]


def rename_photos(csv_file, photo_index, name_index, photos_dir):
    ''' Roll it all '''
    photo_name_data = load_photo_name_data(csv_file, photo_index, name_index)
    find_rename_photos(photos_dir, photo_name_data)


def main():
    rename_photos('1504537_seg_1.csv', 9, 4, 'q-4-PMz4')


if __name__ == '__main__':
    main()