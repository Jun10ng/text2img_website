import os

def change_env(env_position):
    cmd = env_position +' '+'~/py2.py'
    os.system(cmd)


change_env('/home/junlong/anaconda3/envs/book/bin/python')