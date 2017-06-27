#-*-coding:utf-8-*-
#note:下载地址转换(xunlei,flashget,qq,http)
__author__ = 'huligong'

'''
当要转换快车地址时，参数必须用分号引起来，不然会有一个bug，因为符号'&'的关系
'''
import base64
import sys

def http_thunder(url):
    ''' http to thunder'''
    data = 'AA' + url + 'ZZ'
    return 'thunder://'+ base64.b64encode(data)

def http_flashget(url):
    '''http to flashget '''
    data = '[FLASHGET]' + url + '[FLASHGET]'
    return 'flashget://' + base64.b64encode(data) + '&'

def http_qqdl(url):
    '''http to qqdl'''
    return 'qqdl://' + base64.b64encode(url)

def thunder_http(thunder):
    '''thunder to http'''
    if not thunder.startswith('thunder://'):
        print '不合法的迅雷下载地址'
        exit(1)
    data = thunder[10:]
    decode_data = base64.b64decode(data)
    url = decode_data[2:-2].decode('gb2312')
    return url

def flashget_http(flashget):
    '''flashget to http'''
    if not flashget.startswith('flashget://'):
        print '不合法的快车地址'
        exit(1)
    flashget=flashget.split('&')
    data = flashget[0][11:]
    decode_data = base64.b64decode(data)
    url = decode_data[10:-10].decode('gb2312')
    return url

def qqdl_http(qqdl):
    '''qqdl to http'''
    if not qqdl.startswith('qqdl://'):
        print '不合法的qq旋风地址'
        exit(1)
    data = qqdl[7:]
    decode_data = base64.b64decode(data)
    return decode_data.decode('gb2312')

def main():
    #httpurl= thunder_http('')
    #print httpurl
    pass

if __name__ == '__main__' :
    main()