import threading

class Singleton(object):
   
    objs  = {}
    objs_locker =  threading.Lock()

    def __new__(cls, *args, **kv):
        if cls in cls.objs:
            return cls.objs[cls]['obj']

        cls.objs_locker.acquire()
        try:
            if cls in cls.objs: ## double check locking
                return cls.objs[cls]['obj']
            obj = object.__new__(cls)
            cls.objs[cls] = {'obj': obj, 'init': False}
            setattr(cls, '__init__', cls.decorate_init(cls.__init__))
        finally:
            cls.objs_locker.release()
   
    @classmethod
    def decorate_init(cls, fn):
        def init_wrap(*args):
            if not cls.objs[cls]['init']:
                fn(*args)
                cls.objs[cls]['init'] = True
            return

        return init_wrap

if __name__ == '__main__':
    Singleton.decorate_init(1,'2')
    Singleton.decorate_init(1,'3')