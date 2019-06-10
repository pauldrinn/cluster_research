#removing '>' from all files
import os
[os.rename(f, f.replace('>', '')) for f in os.listdir('.') if not f.startswith('.')]

#removing unnecessary '/n'
import os
for allfiles in os.listdir('./clustersfasta/hmmed'):
    if allfiles.endswith('aligned'): 
        with open('./clustersfasta/hmmed/'+allfiles,'r+') as a:
            stringy = a.read()
            stringy1 = stringy.replace('\n', '')
            stringy2 = stringy1.replace('>','\n>')
            stringy3 = stringy2.replace('.1','.1\n')
            a.seek(0)
            a.truncate()
            a.write(stringy3)