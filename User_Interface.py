import json
import urllib.parse
import urllib.request
import Output_Module
import Url_Module

def number_of_stops():
    ''' takes in an input of the number of stops for the trip'''
    number = int(input())
    if number <= 1:
        raise Exception
    else:
        return number

def number_of_output():
    ''' takes in an input of the number output'''
    i = int(input())
    if i<=5 and i>0:
        return i
    else:
        raise Url_Module.MapQuestError()

def desired_output(json_result: 'json',num:int):
    outputs = []
    for i in range(num):
        n = input()
        outputs.append(n)
    for i in outputs:
        if i == 'LATLONG':
            s = Output_Module.lat_long()
            s.calculate(json_result)
        elif i == 'STEPS':
            s = Output_Module.Directions()
            s.calculate(json_result)
        elif i == 'TOTALTIME':
            s = Output_Module.Time()
            s.calculate(json_result)
        elif i == 'TOTALDISTANCE':
            s = Output_Module.Distance()
            s.calculate(json_result)
        elif i == 'ELEVATION':
            s = Output_Module.Elevation()
            s.calculate(json_result)

if __name__ == '__main__':
    try:
        number = number_of_stops()
        stops = Url_Module.list_of_stops(number)
        url = Url_Module.url_encode(stops)
        result = Url_Module.get_result(url)
        output_num = number_of_output()
        output = desired_output(result, output_num)
    except:
        print('NO ROUTE FOUND')
