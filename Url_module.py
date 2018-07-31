import json
import urllib.parse
import urllib.request
API_Key = 'Fmjtd%7Cluu821u7ll%2Cbw%3Do5-94an9f'
Base_MQ_url = 'http://open.mapquestapi.com'

def MapQuestError(Exception):
    return 'No Route Found'

def url_encode(location:list)->str:
    ''' takes in locations and returns the mapquest url for the directions'''
    query_parameters = []
    for stops in location:
        query_parameters.append(stops)
    return Base_MQ_url + '/directions/v2/route?'+ 'key=' + API_Key + '&' + urllib.parse.urlencode(query_parameters)


    

def list_of_stops(stops: int):
    _list = []
    first_stop = ('from' , str(input()))
    _list.append(first_stop)
    for stop in range(stops - 1):
        new_stops = ('to' , str(input()))
        _list.append(new_stops)
    
    return _list


def get_result(url:str) -> 'json':
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return( json.loads(json_text))
    finally:
        if response != None:
            response.close()
