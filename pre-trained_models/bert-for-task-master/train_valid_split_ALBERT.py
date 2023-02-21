# Train-Validation Split


# To adapt my journal_articles cleansed data to the format that ALBERT requries, I need to reform my data. 
# My adaptation is to meet the data format requirement in https://github.com/jiangxinyang227/bert-for-task 

# This file is written by me, Freda Xiaoyun Yu, on Feb 06. 

##### 文本分类数据格式
# * title \<SEP> content \<SEP> label：有的数据中含有标题，有的只有正文，标题，正文，标签之间用\<SEP>符号分隔。

# I need to further split the training and validation datasets. 

import random
import os
from sklearn.model_selection import train_test_split

random.seed(15)


my_root = "D:\\yxy_jupyter\\journal_articles_labelled"  
# this folder contains all 000.txt to 599.txt files with "\<SEP> + label" in the end. 


def train_valid_split_yxy(root): 
    # with open(root + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as files: 
    for i in range(6):     # 6 categories
        current_root = root + "\\" + str(i) + "\\"
        store_files = []   # temp, for storing all the files
        print("01")

        for j in range(100): 
            num = i*100 + j
            j3 = str(num).zfill(3)
            current_file = open(current_root + str(j3) + ".txt", encoding='gb18030', errors='ignore')
            read = current_file.read()
            store_files.append([read, j3])   # j is an int; j3 is a string. 

        print("All files number in this category: ", len(store_files))
        print("Type of store_files[5][0]: ", type(store_files[5][0]))

        # to ensure each category has the same number of training files, and the same number of validation files: 
        train_valid, test_set = train_test_split(store_files, test_size=0.20, random_state=15)
        train_set, validation_set = train_test_split(train_valid, test_size=0.25, random_state=15)
        # train:valid:test = 60:20:20

        print("02")

        path = "D:/yxy_jupyter/journal_articles_splitted/" + str(i) + "/"
        os.makedirs(path)
        print("03")

        path_train = path + "train" + "/"
        path_validation = path + "validation" + "/"
        path_test = path + "test" + "/"

        os.makedirs(path_train)
        os.makedirs(path_validation)
        os.makedirs(path_test)

        print("04")
        print(path_train)

        for each in train_set: 
            with open(path_train + "%s.txt"%(str(each[1])), "a", encoding='gb18030', errors='ignore') as file:    # each[1]  is the id, e.g. 324
                file.write(each[0])   # write in the content
        for each in validation_set: 
             with open(path_validation + "%s.txt"%(str(each[1])), "a", encoding='gb18030', errors='ignore') as file:    # each[1]  is the id, e.g. 324
                file.write(each[0])    # write in the content
        for each in test_set: 
             with open(path_test + "%s.txt"%(str(each[1])), "a", encoding='gb18030', errors='ignore') as file:    # each[1]  is the id, e.g. 324
                file.write(each[0])    # write in the content

        print("05")

    return print("Have splitted train-validation-test for all categories. ")

train_valid_split_yxy(my_root)




