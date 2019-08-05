import os

def change_env(py2_env_position):
    cmd = py2_env_position +' '+'~/py2.py'
    os.system(cmd)


change_env('/home/junlong/anaconda3/envs/book/bin/python')