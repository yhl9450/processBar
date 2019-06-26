import time
import sys


class ProcessBar(object):
    """
    实例化时需要传入两个参数:target - 进度目标 , num - 进度条长度 ( 默认20 )
    使用时每次更新时调用 show_bar 函数，将当前进度传入
    """
    not_done = ''

    def __init__(self, target, num=40):
        self.num = num
        self.target = target
        for i in range(num):
            self.not_done = self.not_done + ' '

    def show_bar(self, current):
        done = ''
        not_done = self.not_done
        target = self.target
        num = self.num

        c_num = int(num * current / target)
        for i in range(c_num):
            done = done + '#'
            not_done = not_done[:-1]
        sys.stdout.write('\r[%s%s]' % (done, not_done))
        if current == target:
            print('Finished')
        sys.stdout.flush()


"""使用示例"""
if __name__ == '__main__':
    process_bar = ProcessBar(10, 20)
    for a in range(10):
        process_bar.show_bar(a + 1)
        time.sleep(1)
