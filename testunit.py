#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime
import unittest

class LuaTest(unittest.TestCase):
    def runTest(self):
        print 'anything'
    def setUp(self): 
        #预置环境
        print '--------------LuaTestsetUp--------------\n'
    def tearDown(self):  
        #清理环境
        print '--------------LuaTestclear--------------\n'  
        
    def test_lua(self):
        print 'test_lua'        
   
    def test_lualog(self):               
        print 'test_lualog'
        
def casesuite():
    suite = unittest.TestSuite()
    suite.addTest(LuaTest("test_lua"))
    suite.addTest(LuaTest("test_lualog"))
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    # unittest.main(exit = False,verbosity=2)#它是全局方法，把它屏蔽后，不在suite的用例就不会跑，exit = False表示中间有用例失败也继续执行；还有比较常用的verbosity=2，表示显示def名字
    casesuite()#执行suite