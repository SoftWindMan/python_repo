#coding=utf-8
# GIL，the Global Interpreter Lock，直译为“全局解释锁”
# 执行多线程的时候并不是线程安全的，所以为了程序的稳定性，加一把全局解释锁，能够确保任何时候都只有一个Python线程执行。
# GIL的弊端:
# GIL对计算密集型的程序会产生影响。因为计算密集型的程序，需要占用系统资源。GIL的存在，相当于始终在进行单线程运算，这样自然就慢了。
# IO密集型影响不大的原因在于，IO，input/output，这两个词就表明程序的瓶颈在于输入所耗费的时间，线程大部分时间在等待，所以它们是多个一起等（多线程）还是单个等（单线程）无所谓的。

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
import requests
import time

URLS = ['https://www.baidu.com/', 'http://www.163.com', 'http://www.cnblogs.com/']
def load_url(url):
    response = requests.get(url)
    print('%s page is %d bytes' %(url, len(response.text)))

def get(url):
    print('GET {}'.format(url))
    response = requests.get(url)
    time.sleep(2)
    if response.status_code == 200:
        return {'url':url, 'content':response.text}
def parse(res):
    print('%s parse res is %s' % (res['url'], len(res['content'])))
    return '%s parse res is %s' % (res['url'], len(res['content']))
def save(res):
    print('save', res)
def task(res):
    res = res.result()
    par_res = parse(res)
    save(par_res)

if __name__ == '__main__':
    threadExecutor = ThreadPoolExecutor(max_workers=3)
    processExecutor = ProcessPoolExecutor(max_workers=3)
    ####### submit()
    # 线程池
    # for url in URLS:
    #     future = threadExecutor.submit(load_url, url)
    #     print(future.done())
    # print('--- Main Thread ---')

    # 进程池
    # for url in URLS:
    #     future = processExecutor.submit(load_url, url)
    #     print(future.done())
    # print('--- Main Thread ---')

    ###### map()
    # threadExecutor.map(load_url, URLS)
    # print('--- Main Thread ---')

    ###### wait()
    # f_list = []
    # for url in URLS:
    #     future = threadExecutor.submit(load_url, url)
    #     f_list.append(future)
    # # print(wait(f_list)) # 默认ALL_COMPELED
    # print(wait(f_list, return_when='FIRST_COMPLETED'))
    # # print(wait(f_list, return_when='FIRST_EXCEPTION'))
    # print('--- Main Thread ---')

    ###### add_done_callback()
    # 当线程池调用该方法时,线程池的状态则立刻变成SHUTDOWN状态。此时，则不能再往线程池中添加任何任务，否则将会抛出RejectedExecutionException异常。但是，此时线程池不会立刻退出，直到添加到线程池中的任务都已经处理完成，才会退出。
    for url in URLS:
        threadExecutor.submit(get, url).add_done_callback(task)
    print('--- Main Thread ---')
    threadExecutor.shutdown()
