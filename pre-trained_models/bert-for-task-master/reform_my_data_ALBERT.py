# To adapt my journal_articles cleansed data to the format that ALBERT requries, I need to reform my data. 
# My adaptation is to meet the data format requirement in https://github.com/jiangxinyang227/bert-for-task 

# This file is written by me, Freda Xiaoyun Yu, on Feb 06. 

##### 文本分类数据格式
# * title \<SEP> content \<SEP> label：有的数据中含有标题，有的只有正文，标题，正文，标签之间用\<SEP>符号分隔。


my_root = "D:\\yxy_jupyter\\journal_articles"

# a           means: cannot be read; can write; allow not existing; cannot amend original content; can only write afterwards. 

def reform_data(roots): 

    for m in range(600): 
        m_str = str(m)   # the string version of the x id
        x_id = m_str.zfill(3)  # the 3-digits version of the string m, still a string

        if m>=0 and m<100:      # the first category, y = 0
            with open(roots + "/0/" + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as file: 
                file.write(" " + "\<SEP>" + "0")     # write in the label
        elif m>=100 and m<200:  # y = 1
            with open(roots + "/1/" + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as file: 
                file.write(" " + "\<SEP>" + "1")     # write in the label
        elif m>=200 and m<300: 
            with open(roots + "/2/" + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as file: 
                file.write(" " + "\<SEP>" + "2")     # write in the label
        elif m>=300 and m<400: 
            with open(roots + "/3/" + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as file: 
                file.write(" " + "\<SEP>" + "3")     # write in the label
        elif m>=400 and m<500: 
            with open(roots + "/4/" + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as file: 
                file.write(" " + "\<SEP>" + "4")     # write in the label
        elif m>=500 and m<600: 
            with open(roots + "/5/" + "%s.txt"%(str(x_id)), "a", encoding='gb18030', errors='ignore') as file: 
                file.write(" " + "\<SEP>" + "5")     # write in the label

    return print("Have added  \<SEP>  to all the data files. ")


reform_data(my_root)

