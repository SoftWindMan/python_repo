#coding=utf-8
from showNovel import *
from userOperate import *
from downloadNovel import *
from colored import *

showNovel = ShowNovel()
userOperate = UserOperate()
colored = Colored()

novelTypeName = None
while True:
    showNovel.show_novel_type()
    action_one = raw_input(colored.red('请选择小说类型编号：'))
    if action_one == 'q' or action_one == 'Q':
        break
    else:
        novelTypeName, pages = userOperate.choice_novel_type(action_one)
        index = 1
        showNovel.show_all_novel_under_novel_type_name(novelTypeName, index, pages)

        while True:
            action_two = raw_input(colored.red('请选择相应的小说编号或动作：'))
            if action_two == 'q' or action_two == 'Q':
                break
            elif action_two == 'n' or action_two == 'N':
                index += 1
                if index <= pages:
                    showNovel.show_all_novel_under_novel_type_name(novelTypeName, index, pages)
            elif action_two == 's' or action_two == 'S':
                action_three = raw_input(colored.red('请输入跳转的页码：'))
                index = int(action_three)
                showNovel.show_all_novel_under_novel_type_name(novelTypeName, index, pages)
            else:
                novelName, novelUrl = userOperate.choice_novel(novelTypeName, index, action_two)

                print('*** 准备下载小说【{}】***'.format(novelName))
                downloadNovel = DownloadNovel(novelName, novelUrl)
                downloadNovel.download_novel()
