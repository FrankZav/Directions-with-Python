import json
import urllib.parse
import urllib.request
import Url_Module

API_Key = 'Fmjtd%7Cluu821u7ll%2Cbw%3Do5-94an9f'
Base_MQ_url = 'http://open.mapquestapi.com'

class Distance:
    def calculate(self,json_result):
        '''Returns total distance of the trip'''
        print ('')
        print('TOTAL DISTANCE')
        miles = ((json_result['route']['distance']))
        print (round(miles,0), 'miles')
class Time:
    def calculate(self, json_result):
        ''' Returns the total time of the trip'''
        print('')
        print ('TOTAL TIME')
        time = ((json_result['route']['time'])/60)
        print (round(time,0), 'minutes')

class Directions:
    def calculate(self, json_result):
        '''Returns the total distance of the trip'''
        print('')
        print('DIRECTIONS')
        for items in json_result['route']['legs']:
            for item in items['maneuvers']:
                print(item['narrative'])

class lat_long:
    def calculate(self, json_result):
        ''' Displays latitude and longitude'''
        print('')
        print('LATLONGS')
        for items in json_result['route']['locations']:
            lat = round(items['displayLatLng']['lat'],2)
            long = round(items['displayLatLng']['lng'],2)

            if lat < 0:
                lati = str(abs(lat)) + 'S'
            elif lat > 0:
                lati = str(lat) + 'N'
            if long < 0:
                longi = str(abs(long))+'W'
            elif long > 0:
                longi = str(long) +'E'
            print(lati, longi)

class Elevation:
    def calculate(self, json_result)->str:
        coord = ''
        for items in json_result['route']['locations']:
            lat = str(round(items['displayLatLng']['lat'],2))
            long = str(round(items['displayLatLng']['lng'],2))
            coord = coord + lat + ',' + long + ','
        url = Base_MQ_url+'/elevation/v1/profile?key=' + API_Key +'&shapeFormat=raw&latLngCollection=' + coord
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        self = json.loads(json_text)
        print('')
        print ('ELEVATION')
        for items in self['elevationProfile']:
            print(items['height'])
        
