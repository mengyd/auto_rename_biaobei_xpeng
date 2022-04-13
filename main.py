import os, unicodedata

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def isOriginRawData(s):
    if (s.endswith('.raw') or s.endswith('.raw_tmp')) and s.startswith('xp_record_file_'):
        return True
    return False

def readIndex(filename):
    f1 = open(filename, 'r', encoding='UTF-8', errors='ignore')
    index = {}
    for s in f1.readlines():
        contents = s.split('\t')
        print(contents)
        if isNumber(contents[0]) and isNumber(contents[1].strip('\n')):
            index[contents[0]] = contents[1].strip('\n')
            print(index)
    return index
    
def readFilenames(filename_repo):
    filenames = {}
    with os.scandir(filename_repo) as filelist:
        for file in filelist:
            filename = file.name.split('.')[0]
            if filename.split('_')[5] == '5' or filename.split('_')[5] == '6':
                fileindex = filename.split('_')[5]
            else:
                fileindex = filename.split('_')[5] + '_' + filename[-1]
            filenames[fileindex] = filename
    print(filenames)
    return filenames


def rename(data_repo, filename_repo, index_file):
    mobile_data_relation = {
    '1':'1_1', '2':'1_2', '3':'2_1', '4':'2_2', 
    '5':'3_1', '6':'3_2', '7':'4_1', '8':'4_2', 
    '9':'5', '10':'6'}
    filenames = readFilenames(filename_repo)
    index = readIndex(index_file)
    with os.scandir(data_repo) as datalist:
        for data in datalist:
            dataname = data.name.split('.')[0]
            datanumber = dataname.split('_')[-1]
            if datanumber in index:
                mobilefile = index[datanumber]
                newname = filenames[mobile_data_relation[mobilefile]]+'.raw'
                if not os.path.exists(data_repo+'\\'+newname):
                    try:
                        print(data.name+' : '+newname)
                        os.rename(data.path, data_repo+'\\'+newname)
                    except Exception:
                        pass
            elif isOriginRawData(data.name) :
                os.remove(data.path)



if __name__ == '__main__':
    while True:
        data_repo = input("数据文件夹:")
        data_repo = data_repo.strip('"')
        if data_repo and os.path.isdir(data_repo):
            print(data_repo)
            break

    while True:
        filename_repo = input("语料文件夹:")
        filename_repo = filename_repo.strip('"')
        if filename_repo and os.path.isdir(filename_repo):
            break

    while True:
        index_file = input("索引文件:")
        index_file = index_file.strip('"')
        if index_file and os.path.exists(index_file):
            break

    rename(data_repo, filename_repo, index_file)
        # pause
    os.system('pause')