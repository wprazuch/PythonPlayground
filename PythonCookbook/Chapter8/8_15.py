class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, name):
        return getattr(self._a, name)


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('getattr: ', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)
