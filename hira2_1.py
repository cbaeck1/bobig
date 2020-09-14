import os, sys, csv
import time
import threading

'''
# 심평원데이터 레코드마지막에 콤마가 있어 제거
# 신청번호에 - 가 없음
'''

#base_dir = '/esb_nfs/esbmst/indigo/201800002/1'
#out_dir = base_dir +'/new_data'
#data_filenames = os.listdir(base_dir +'/data/A0001/1/')
#header_filenames = os.listdir(base_dir +'/header')

if __name__ == "__main__":
    base_dir = sys.argv[1]
    out_dir = sys.argv[2] 
    data_dir = sys.argv[3] 
    header_dir = sys.argv[4]

data_filenames = os.listdir(data_dir)
header_filenames = os.listdir(header_dir)
# print(base_dir, out_dir, data_dir, header_dir)


def do_something(header_filename, header_tmp, data_filename):
    print('start...', header_filename, header_tmp, data_filename)
    # full_filename = os.path.join(dirname, filename)
    # print(data_filename)
    # IF_DL_502_201800002_A0001_TWJHC300_9_120_20200531.txt -> IF_DL_502_201800002_A0001_TWJHC300
    data_1 = data_filename.split('_')
    data_tmp = data_1[0] + data_1[1] + data_1[2] + data_1[3] + data_1[4] + data_1[5] 
    data_total = data_1[6]

    if header_tmp == data_tmp:
        file_header = open(header_dir +'/' +header_filename, mode='rt', encoding='utf-8')
        file_content = open(data_dir +'/' +data_filename, mode='rt', encoding='utf-8')
        file_write = open(out_dir +'/' +data_filename, mode='wt', encoding='utf-8', newline='')
        full_txt = ""
        full_txt = file_header.read()
        full_txt = full_txt +'\r'
        file_write.write(full_txt)

        writer = csv.writer(file_write, delimiter=',')
        # print(base_dir +'/' +data_filename)
        contentreader = csv.reader(file_content, delimiter=',')
        for readRow in contentreader:
            newRow = []
            # 신청ID - 추가
            newRow.append(readRow[0][0:4] + '-' + readRow[0][4:9])
            #  리스트의 마지막은 제외
            newRow = newRow + readRow[1:-1]
            writer.writerow(newRow)

        file_header.close()
        file_content.close()
        file_write.close()
    else:
        print('not start' , header_filename, header_tmp, data_filename)
    print('Done...')

for h_filename in header_filenames:
    # full_filename = os.path.join(dirname, filename)
    # IF_DL_502_201800002_A0001_TWJHC300 -> IF_DL_502_201800002_A0001_TWJHC300
    # print(h_filename)
    header = h_filename.split('_')
    h_tmp = header[0] +header[1] +header[2] +header[3] +header[4] +header[5] 

    start = time.perf_counter()
    threads = []
    for d_filename in data_filenames:
        t = threading.Thread(target=do_something, args=[h_filename, h_tmp, d_filename])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')




