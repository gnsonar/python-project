import os


def clean_txt_files():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    files = os.listdir(os.path.curdir)
    for f in files:
        if f.__str__().endswith('.txt'):
            os.remove(f)


clean_txt_files()