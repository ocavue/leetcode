"""
submits:
- date: 2020-09-08
  minutes: 50
  cheating: false

comment: |
  这道题出的太差了，根本搞不懂  「记录最多8条错误记录，循环记录」的含义
"""

"""
简单错误记录

题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。


处理：


1、 记录最多8条错误记录，循环记录（或者说最后只输出最后出现的八条错误记录），对相同的错误记录（净文件名（保留最后16位）称和行号完全匹配）只记录一条，错误计数增加；


2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；


3、 输入的文件可能带路径，记录文件名称不能带路径。


输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

示例1
输入
    E:\V1R2\product\fpgadrive.c   1325
输出
    fpgadrive.c 1325 1
"""

from collections import defaultdict
from queue import Queue


def get_filename(filepath: str) -> str:
    if "\\" in filepath:
        f = filepath.split("\\")[-1]
    else:
        f = filepath.split("/")[-1]
    if len(f) > 16:
        f = f[-16:]
    return f


counter = defaultdict(int)
# queue = Queue()
in_queue = {}
pairs = []


def record(filepath: str, line_num: int):
    filename = get_filename(filepath)
    pair = (filename, line_num)
    counter[pair] += 1
    pairs.append(pair)

    # if pair in in_queue:
    #     pairs = []
    #     while not queue.empty():
    #         pairs.append(queue.get())
    #     for p in pairs:
    #         if p != pair:
    #             queue.put(p)
    #     queue.put(pair)
    # else:
    #     queue.put(pair)
    #     in_queue[pair] = True

    #     if queue.qsize() > 8:
    #         poped = queue.get()
    #         del in_queue[poped]


def export():
    export_pairs = set()
    start = 0
    for i in range(len(pairs) - 1, -1, -1):
        pair = pairs[i]
        export_pairs.add(pair)
        if len(export_pairs) == 8:
            start = i
            break
    for pair in pairs[start:]:
        if pair in export_pairs:
            export_pairs.remove(pair)
            print(pair[0], pair[1], counter[pair])


def get_input():
    while True:
        try:
            line = input()
            yield line.split(" ")
        except:
            break


def run():
    for f, l in get_input():
        record(f, l)
    export()


# def get_input():
#     while True:
#         try:
#             line_or_lines = input()
#             for line in line_or_lines.splitlines():
#                 yield line.split(" ")
#         except:
#             break


if __name__ == "__main__":
    for line in r"""G:\rp\onajqj\maahmq 631
E:\njfgjkcrh 641
C:\co\zk\ao\bxgxjfgrwckfxekeqro 629
D:\mf\si\jmfdahkeffyjjsf 646
E:\wn\arefkiz 633
C:\gpjleb\cinhhx\zjydgr\njfgjkcrh 640
E:\nwrrhx\qyw\bxgxjfgrwckfxekeqro 636
G:\usgsl\ywr\tve\cqekvaxypemktyurn 647
C:\jftbig\arefkiz 650
F:\rgk\cai\arefkiz 640
D:\tvse\vs\dhzrmy\njfgjkcrh 634
E:\coba\qbs\xagq\njfgjkcrh 628
F:\wnfsmf\oxrvbv\njfgjkcrh 632
C:\khqx\nv\jmfdahkeffyjjsf 637
F:\hm\ra\uaxckn\bxgxjfgrwckfxekeqro 647
D:\soq\jmfdahkeffyjjsf 642
F:\moxnw\szxcdhlaytgj 639
E:\avcop\jd\vwtrt\njfgjkcrh 650
E:\hou\vv\szxcdhlaytgj 631
C:\uozkwd\bxgxjfgrwckfxekeqro 650
F:\jmfdahkeffyjjsf 650
E:\hgoxms\nwax\szxcdhlaytgj 633
F:\vylww\zhh\cqekvaxypemktyurn 643
C:\njfgjkcrh 637
F:\bfn\dxwjje\jmfdahkeffyjjsf 632
E:\bxgxjfgrwckfxekeqro 634
G:\gwuusj\ized\qq\szxcdhlaytgj 646
F:\arefkiz 644
G:\zsw\uewu\arefkiz 634
E:\ja\zg\njfgjkcrh 644
D:\gfute\ju\wuy\szxcdhlaytgj 636
C:\mpgcx\kcgi\arefkiz 645
C:\zayn\jmfdahkeffyjjsf 648
F:\kkplu\avvw\hbzmwj\jmfdahkeffyjjsf 648
E:\maahmq 631
E:\hs\xnto\jmfdahkeffyjjsf 645
G:\cqekvaxypemktyurn 633
D:\maahmq 646
E:\jmfdahkeffyjjsf 636
G:\hbvm\szxcdhlaytgj 642""".splitlines():
        f, l = line.split(" ")
        record(f, l)

    # record(r"C:\gtu\vcy\jk\zwthkipl", 636)
    # record(r"G:\rsle\lsax\yalcxu\vwhysms", 637)
    # record(r"F:\fzqz", 640)
    # record(r"E:\lswb\styce\thjnbxdvg", 645)
    # record(r"F:\up\qflvvayylipvj", 635)
    # record(r"C:\pivw\rkd", 644)
    # record(r"E:\tlkbjb\pcvnvm\qh\fzqz", 633)
    # record(r"E:\ezke\xvrdkuesnjerakzhs", 641)
    # record(r"E:\qflvvayylipvj", 639)
    # record(r"F:\ybpxk", 644)
    # record(r"G:\rfdr\faxpyhyznsssbo", 630)
    # record(r"E:\xktax\osekgaqy", 646)
    # record(r"C:\te", 633)
    # record(r"G:\albed\ffc\jclzfq\h", 631)
    # record(r"F:\zsshil\pkue\mazocurlwufmkkrw", 635)
    # record(r"E:\dmj\uefo\syabgm\qflvvayylipvj", 643)
    # record(r"F:\pgdiwvceluyzft", 634)
    # record(r"D:\xiqck\dta\lnh", 639)
    # record(r"E:\nu\nz\wwjpch\fzqz", 650)
    # record(r"E:\gfsahypjzwfglvou", 644)
    # record(r"G:\qh\thjnbxdvg", 641)
    # record(r"C:\cp\voause\mf\hebgpyzpyyybiywpv", 632)
    # record(r"E:\de\vet\vdooytekbghohqz", 631)
    # record(r"E:\cox\pvg\tlrlr", 640)
    # record(r"G:\hkc\fllkwmwlgiqahxbfs", 638)
    # record(r"E:\apjnogffvkwnv", 637)
    # record(r"E:\nldefh\ar\oqsb\uyobrilaabapini", 630)
    # record(r"F:\wgotle\ar\wgh\hebgpyzpyyybiywpv", 639)
    # record(r"G:\nrekjavm", 634)
    # record(r"C:\mvngfg\lfjnvz\xvrdkuesnjerakzhs", 634)
    # record(r"F:\exne\vh\kqh\fzqz", 641)
    # record(r"F:\lepvz", 642)
    # record(r"G:\qg\hcbh\uknyte\pgdiwvceluyzft", 636)
    # record(r"F:\ho\cn\uyobrilaabapini", 637)
    # record(r"E:\xbc\fzqz", 642)
    # record(r"G:\ju\nmdd\fzqz", 643)
    # record(r"G:\lzpmdx\rxp\ybpxk", 629)
    # record(r"D:\fc\lnh", 629)
    # record(r"D:\dsgvo\zwthkipl", 631)
    # record(r"G:\pujc\cgorfjzkqmnjathbiip", 640)
    # record(r"G:\vfhyp\cs\rrt", 638)
    # record(r"F:\oteh\ti\urajfw\tlrlr", 636)
    # record(r"C:\crdp\qwptjlorrmnv", 642)
    # record(r"D:\kcl\fqzs\zlm\pgdiwvceluyzft", 640)
    # record(r"G:\faxpyhyznsssbo", 639)
    # record(r"D:\swnhezhgdcwwbmkyqt", 637)
    # record(r"D:\azo\sry\faxpyhyznsssbo", 633)
    # record(r"C:\beqt\eh\dm\dlhehjccfdgrrzyj", 642)
    # record(r"F:\lepvz", 635)
    export()
