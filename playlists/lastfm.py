import requests
import os

def search_artist(method,artist):                
    API_KEY = os.getenv('LAST_FM_KEY')
    USER_AGENT = 'Playitt'
    BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
    headers = {'user-agent':USER_AGENT}
    payload = {'api_key':API_KEY,'method': method,'format':'json','artist':artist,}
    res = requests.get(BASE_URL,headers=headers,params=payload)
    return res

def search_song(method,artist,track):                
    API_KEY = os.getenv('LAST_FM_KEY')
    USER_AGENT = 'Playitt'
    BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
    headers = {'user-agent':USER_AGENT}
    payload = {'api_key':API_KEY,'method': method,'format':'json','artist':artist,'track':track,'autocorrect':1}
    res = requests.get(BASE_URL,headers=headers,params=payload)
    return res

def search_song(method,artist,track):                
    API_KEY = "f6ed275447598cb0e951fc8e741635b0"
    USER_AGENT = 'Playitt'
    BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
    headers = {'user-agent':USER_AGENT}
    payload = {'api_key':API_KEY,'method': method,'format':'json','artist':artist,'track':track,'autocorrect':1}
    res = requests.get(BASE_URL,headers=headers,params=payload)
    return res