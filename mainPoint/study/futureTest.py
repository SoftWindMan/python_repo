#coding=utf-8
# GIL��the Global Interpreter Lock��ֱ��Ϊ��ȫ�ֽ�������
# ִ�ж��̵߳�ʱ�򲢲����̰߳�ȫ�ģ�����Ϊ�˳�����ȶ��ԣ���һ��ȫ�ֽ��������ܹ�ȷ���κ�ʱ��ֻ��һ��Python�߳�ִ�С�
# GIL�ı׶�:
# GIL�Լ����ܼ��͵ĳ�������Ӱ�졣��Ϊ�����ܼ��͵ĳ�����Ҫռ��ϵͳ��Դ��GIL�Ĵ��ڣ��൱��ʼ���ڽ��е��߳����㣬������Ȼ�����ˡ�
# IO�ܼ���Ӱ�첻���ԭ�����ڣ�IO��input/output���������ʾͱ��������ƿ�������������ķѵ�ʱ�䣬�̴߳󲿷�ʱ���ڵȴ������������Ƕ��һ��ȣ����̣߳����ǵ����ȣ����̣߳�����ν�ġ�

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
    # �̳߳�
    # for url in URLS:
    #     future = threadExecutor.submit(load_url, url)
    #     print(future.done())
    # print('--- Main Thread ---')

    # ���̳�
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
    # # print(wait(f_list)) # Ĭ��ALL_COMPELED
    # print(wait(f_list, return_when='FIRST_COMPLETED'))
    # # print(wait(f_list, return_when='FIRST_EXCEPTION'))
    # print('--- Main Thread ---')

    ###### add_done_callback()
    # ���̳߳ص��ø÷���ʱ,�̳߳ص�״̬�����̱��SHUTDOWN״̬����ʱ�����������̳߳�������κ����񣬷��򽫻��׳�RejectedExecutionException�쳣�����ǣ���ʱ�̳߳ز��������˳���ֱ����ӵ��̳߳��е������Ѿ�������ɣ��Ż��˳���
    for url in URLS:
        threadExecutor.submit(get, url).add_done_callback(task)
    print('--- Main Thread ---')
    threadExecutor.shutdown()
