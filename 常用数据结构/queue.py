"""
@File    :   queue.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/12 19:44   LiuHe      1.0         ʵ�ֶ���
"""


class Queue:
    """
    ʵ�ֶ���
        �������
        ������
        �п�
        ���г���
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)
