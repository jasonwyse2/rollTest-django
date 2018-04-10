# from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello world ! ")
from django.http import HttpResponse
from django.shortcuts import render
from models.predict_Minute_v2 import get_data
from models.common_tool import get_modelName_dict
import models.django_config

import json
taskType = 'BottomTopUpDown'
minute_model_dir = '/mnt/aidata/AI_trend_model_3/models/' + taskType + '/'
day_model_dir = '/mnt/aidata/AI_trend_model_2/models/' + taskType + '/'
def intraday_area(request):
    context = {}
    return render(request, 'intraday_area.html', context)

def intraday_minute(request):
    stock_code = '000016'
    date = '20180322'
    modelName_dict = get_modelName_dict(minute_model_dir, stock_code)
    modelName_list = sorted(modelName_dict.keys(), reverse=True)
    modelName = modelName_list[0]
    parameter_dict = {'stock_code':stock_code,'startTime':date+'0930','endTime':date+'1500','modelName':modelName}
    time_close, (bottom_data, up_data, top_data, down_data)=get_data(parameter_dict,dayOrMinute='minute')
    context = {'time_close':time_close,'bottom_data':bottom_data,'up_data':up_data,'top_data':top_data,'down_data':down_data}

    data_dict = {'context':context,'modelNames':modelName_list,'stock_code':stock_code,'date':date}
    data = {'data':json.dumps(data_dict)}
    return render(request, 'intraday_minute.html', data)

def minute(request):
    time_close, (bottom_data, up_data, top_data, down_data)=get_data()
    context = {'time_close':time_close,'bottom_data':bottom_data,'up_data':up_data,'top_data':top_data,'down_data':down_data}

    return render(request, 'minute.html', {'context':json.dumps(context)})

def dynamic_update(request):
    context = {}
    return render(request, 'dynamic_update.html', context)

def IntradayMinutePrediction(request):
    underlying = request.POST['underlying']
    date = request.POST['date']
    # modelName = request.getParemeter("modelName")
    modelName = request.POST['modelName']
    stock_code = underlying
    date = date.replace('-','')
    startTime = date+'0930'
    endTime = date+'1500'
    parameter_dict = {'stock_code':stock_code,'startTime':startTime,'endTime':endTime,'modelName':modelName}
    time_close, (bottom_data, up_data, top_data, down_data) = get_data(parameter_dict,dayOrMinute='minute')
    data = {'time_close': time_close, 'bottom_data': bottom_data, 'up_data': up_data, 'top_data': top_data,
               'down_data': down_data}
    return HttpResponse(json.dumps(data), content_type='application/json')

def InterdayTrendPrediction(request):
    underlying = request.POST['underlying']
    startDate = request.POST['startDate']
    endDate = request.POST['endDate']
    # modelName = request.getParemeter("modelName")
    modelName = request.POST['modelName']
    taskType = request.POST['taskType']
    print taskType
    stock_code = underlying
    startTime = startDate.replace('-','')


    endTime = endDate.replace('-','')
    parameter_dict = {'stock_code':stock_code,'startTime':startTime,'endTime':endTime,'modelName':modelName}
    time_close, (bottom_data, up_data, top_data, down_data) = get_data(parameter_dict,dayOrMinute='day')
    data = {'time_close': time_close, 'bottom_data': bottom_data, 'up_data': up_data, 'top_data': top_data,
               'down_data': down_data}
    return HttpResponse(json.dumps(data), content_type='application/json')


def interday_trend(request):
    stock_code = '000016'
    startDate = '20170321'
    endDate = '20180321'
    modelName_dict = get_modelName_dict(day_model_dir, stock_code)
    modelName_list = sorted(modelName_dict.keys(), reverse=True)
    modelName = modelName_list[0]
    parameter_dict = {'stock_code': stock_code, 'startTime': startDate , 'endTime': endDate,
                      'modelName': modelName}
    time_close, (bottom_data, up_data, top_data, down_data) = get_data(parameter_dict,dayOrMinute='day')
    context = {'time_close': time_close, 'bottom_data': bottom_data, 'up_data': up_data, 'top_data': top_data,
               'down_data': down_data}
    # print time_close
    data_dict = {'context': context, 'modelNames': modelName_list, 'stock_code': stock_code, 'startDate': startDate,
                 'endDate': endDate}
    print endDate
    data = {'data': json.dumps(data_dict)}
    return render(request, 'interday_trend.html', data)

def intraday_area(request):
    stock_code = '000016'
    date = '20180322'
    modelName_dict = get_modelName_dict(minute_model_dir, stock_code)
    modelName_list = sorted(modelName_dict.keys(), reverse=True)
    modelName = modelName_list[0]
    parameter_dict = {'stock_code': stock_code, 'startTime': date + '0930', 'endTime': date + '1500',
                      'modelName': modelName}
    time_close, (bottom_data, up_data, top_data, down_data) = get_data(parameter_dict, dayOrMinute='minute')

    context = {'time_close': time_close, 'bottom_data': bottom_data, 'up_data': up_data, 'top_data': top_data,
               'down_data': down_data}

    data_dict = {'context': context, 'modelNames': modelName_list, 'stock_code': stock_code, 'date': date}
    data = {'data': json.dumps(data_dict)}
    # return render(request, 'intraday_minute.html', data)

    return render(request, 'intraday_area.html')

def IntradayModelName(request):
    stock_code = request.POST['underlying']
    modelName_dict = get_modelName_dict(minute_model_dir, stock_code)
    modelName_list = sorted(modelName_dict.keys(), reverse=True)
    data_dict = {'modelNames': modelName_list}
    data = {'data': json.dumps(data_dict)}
    # print(data_dict)
    return HttpResponse(json.dumps(data_dict), content_type='application/json')

def InterdayModelName(request):
    stock_code = request.POST['underlying']
    modelName_dict = get_modelName_dict(day_model_dir, stock_code)
    modelName_list = sorted(modelName_dict.keys(), reverse=True)
    data_dict = {'modelNames': modelName_list}
    data = {'data': json.dumps(data_dict)}
    print(data_dict)
    return HttpResponse(json.dumps(data_dict), content_type='application/json')
if __name__ == '__main__':
    request =0
    interday_trend(request)
