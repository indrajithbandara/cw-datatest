import ctypes
h = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\user32.dll")
h.MessageBoxW(0, u'内容', u'标题', 0)