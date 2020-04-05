import os.path, time
files = ['file1.txt', 'file2.txt', 'file3.txt']
changes =  {'file1.txt':os.path.getmtime('file1.txt'),'file2.txt':os.path.getmtime('file2.txt'),'file3.txt':os.path.getmtime('file3.txt')}
while True:
    for f in files:
        if changes.get(f) < os.path.getmtime(f):
            print(f'File {f} has been modified')
            changes[f] = os.path.getmtime(f)
        else:
            print('No changes, going to sleep.')
    time.sleep(2)