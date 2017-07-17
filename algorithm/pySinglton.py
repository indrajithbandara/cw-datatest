def singleton(cls, *args, **kwargs):
  instances = {}
  def _singleton():
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]
  return _singleton
  
@singleton
class MyClass3(object):
  a = 1
  
one = MyClass3()
two = MyClass3()
  
print id(one)  # 29660784
print id(two)  # 29660784
print one == two  # True
print one is two  # True