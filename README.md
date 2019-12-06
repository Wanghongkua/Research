## Package Requirements
1. stop_words
2. gensim 2.2.0
3. scikit-learn 0.19.1

## Training Data
There are 3 training data sets, and the differences are data size and content. “**NSWSC_txt**” and “**simple**” are law cases, while “**dataset**” is some articles of different topics, such as “environment” and “tech”. The smallest one is called “**dataset**”, and then is “**simple**”, and the largest one is called “**NSWSC_txt**”. The “dataset” only requires several minutes of training time, but “**NSWSC_txt**” requires several hours of training time. Once trained, the program would run very fast. The way to change dataset is located in “setting.py” file. Just change the global “database” variable to any of those 3.

## Search Method
The search method is to use “python3.6” to call “search.py” file with 2 arguments. The first one is the search query and the second one is the max number if file required. For example: 
![Search Example](./search pattern.jpg)
This would search “food poisoning from KFC” in all files and the number of file returned would be 20.

## Result Format
The result is simply the file name and similarity to the search query. The more similar the file to the search query, the smaller of the number would be.

## Result Presentation
There are 4 examples in my PPT.

For the first one, I just copied and pasted an entire large paragraph of a file, so it should list only that file.

The second one is a small part of a file.

The third one is the most interesting one. The search query is “food poisoning from KFC”, but the 4th result showing does not contain the word food. It does have chicken in the file. In this case it shows that the program can perform concept search.

The forth one is similar to the third one.
