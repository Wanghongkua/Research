import os
import time
import setting


def doc2array():
    """Extract content from database
    returns array of string
            array of files name
    """
    time1 = time.time()

    f_num = 0
    doc_names = []
    texts = []

    cwd = os.path.join(os.getcwd(), setting.database)
    for filename in os.listdir(cwd):

        #  add to file list
        doc_names.append(filename)

        f_num += 1

        f_path = os.path.join(cwd, filename)

        with open(f_path, 'r') as content_file:
            content = content_file.read()

            texts.append(content)

    print("Time for build_index(): ", end='')
    print(time.time() - time1)

    print(len(texts))

    return texts, doc_names
