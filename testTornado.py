# -*- coding: UTF-8 -*-
import settings
import urllib
from tornado import httpclient
import json
  
class douban:
    authurl = 'https://www.douban.com/service/auth2/'
    user_info_url = 'https://api.douban.com/v2/user/~me'
  
    def get_authorization_code(self):
        params = {
            "client_id":settings.oauth2['douban']['key'],
            "redirect_uri":settings.oauth2['redirect_url'],
            "response_type":"code",
            "scope":"douban_basic_common",
        }
        return self.authurl+'auth?'+urllib.urlencode(params)
  
    def get_access_token(self,code):
        params = {
            "client_id":settings.oauth2['douban']['key'],
            "client_secret":settings.oauth2['douban']['sercet'],
            "redirect_uri":settings.oauth2['redirect_url'],
            "grant_type":"authorization_code",
            "code":code,
        }
        url = self.authurl+'token'
        http_client = httpclient.HTTPClient()
        req = httpclient.HTTPRequest(url,method='POST',body=urllib.urlencode(params))
        response = http_client.fetch(req)
        return json.loads(response.body)
              
    def get_user_info(self,access_token):
        url = 'https://api.douban.com/v2/user/~me'
        http_client = httpclient.HTTPClient()
        req = httpclient.HTTPRequest(url,headers={"Authorization":"Bearer "+access_token})
        response = http_client.fetch(req)
        return json.loads(response.body)