"""
@File    :   stack.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/11 20:34   LiuHe      1.0         ʵ������ջ������ջ
"""
from �������ݽṹ import LinkNode


class ArrayStack(object):
    """
    ����ջ
        ��ջ
        ��ջ
        �鿴ջ��Ԫ��
        ��ӡջ
        ջ����
    """
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, data):
        self._data.append(data)

    def pop(self):
        if self.is_empty():
            print("��ǰջ��")
        else:
            return self._data.pop()

    def top(self):
        if self.is_empty():
            print("��ǰջ��")
        else:
            return self._data[-1]

    def print_stack(self):
        pass


class LinkStack(object):
    """
    ����ջʵ��
        ��ջ
        ��ջ
        �鿴ջ��Ԫ��
        ��ӡջ
        �鿴ջ����
    """
