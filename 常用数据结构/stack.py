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
        for i in reversed(self._data):
            print(i)


class LinkStack(object):
    """
    ����ջʵ��
        ��ջ
        ��ջ
        �鿴ջ��Ԫ��
        ��ӡջ
    """
    def __init__(self):
        self._data = LinkNode.LinkNode

    def push(self, data):
        if self._data.is_empty():
            print("��ǰջ��")
        else:
            self._data.insert(pos=0, value=data)

    def pop(self):
        if self._data.is_empty():
            print("��ǰջ��")
        else:
            self._data.remove(pos=0)

    def top(self):
        if self._data.is_empty():
            print("��ǰջ��")
            return None
        else:
            return self._data._head.get_value()

    def show(self):
        if self._data.is_empty():
            print("��ǰջ��")
        else:
            self._data.show()

