import os


def doc2array(database):
    """Extract content from database
    returns array of string
            array of files name
    """
    f_num = 0
    filenames = []
    texts = []

    cwd = os.path.join(os.getcwd(), database)
    for filename in os.listdir(cwd):

        #  add to file list
        filenames.append(filename)

        f_num += 1

        f_path = os.path.join(cwd, filename)

        with open(f_path, 'r') as content_file:
            content = content_file.read()

            texts.append(content)
    return texts, filenames
