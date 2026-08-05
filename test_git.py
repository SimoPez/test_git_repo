import time
import os
import shutil
import git
import subprocess
import sys

process = 0

def update_script():

    print('Yeah')

    if 'test_git_old' in os.listdir('.'):
        shutil.rmtree('./test_git_old')

    os.makedirs("./test_git_old")
    for f in os.listdir('./test_git_repo/test_git'):
        if '.py' in f:
            with open(f'./test_git_repo/test_git/{f}', 'r') as py_f:
                f_to_copy = py_f.read()
            with open(f'./test_git_old/{f}', 'w') as f_to_paste:
                f_to_paste.write(f_to_copy)

    os.makedirs("./test_git_old/test_git_utils")
    for f in os.listdir('./test_git_repo/test_git/test_git_utils'):
        if '.py' in f:
            with open(f'./test_git_repo/test_git/test_git_utils/{f}', 'r') as py_f:
                f_to_copy = py_f.read()
            with open(f'./test_git_old/test_git_utils/{f}', 'w') as f_to_paste:
                f_to_paste.write(f_to_copy)

    shutil.rmtree('./test_git')
    shutil.copytree('./test_git_repo/test_git', './test_git')

    
def update_and_run(cnt):

    global process

    if 'test_git_repo' in os.listdir('.'):
        shutil.rmtree('./test_git_repo')

    git.Git('./test_git_repo').clone('https://github.com/SimoPez/test_git_repo.git')
    files = {}
    for f in os.listdir('./test_git_repo/test_git'):
        if '.py' in f:
            with open(f'./test_git_repo/test_git/{f}', 'r') as py_f:
                files[f] = py_f.read()
    
    for f in os.listdir('./test_git_repo/test_git/test_git_utils'):
        if '.py' in f:
            with open(f'./test_git_repo/test_git/test_git_utils/{f}', 'r') as py_f:
                files[f'test_git_utils/{f}'] = py_f.read()

    updated_script = 0

    for f in os.listdir('./test_git'):
        if '.py' in f:
            with open(f'./test_git/{f}', 'r') as py_f:
                if files[f] != py_f.read():
                    update_script()
                    updated_script = 1
                    break
    
    if updated_script == 0:
        for f in os.listdir('./test_git/test_git_utils'):
            if '.py' in f:
                with open(f'./test_git/test_git_utils/{f}', 'r') as py_f:
                    if files[f'test_git_utils/{f}'] != py_f.read():
                        update_script()
                        updated_script = 1
                        break

    shutil.rmtree('./test_git_repo')

    if updated_script == 1:
        process.terminate()
        process = subprocess.Popen([sys.executable, './test_git/main.py', '-cnt', f'{cnt}'])

if __name__ == '__main__':
    
    print('Run automation')

    process = subprocess.Popen([sys.executable, './test_git/main.py', '-cnt', '3'])

    while(True):
        print('Yo!')
        update_and_run(3)
        time.sleep(30)
        
