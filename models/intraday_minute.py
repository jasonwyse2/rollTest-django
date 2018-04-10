from django.http import HttpResponse
from django.shortcuts import render
from models.predict_Minute_v2 import get_data
from models.common_tool import get_modelName_dict
import models.django_config

import json
taskType = 'BottomTopUpDown'
minute_model_dir = '/mnt/aidata/AI_trend_model_3/models/' + taskType + '/'
day_model_dir = '/mnt/aidata/AI_trend_model_2/models/' + taskType + '/'

def load_page():
    pass

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

def IntradayModelName(request):
    stock_code = request.POST['underlying']
    modelName_dict = get_modelName_dict(minute_model_dir, stock_code)
    modelName_list = sorted(modelName_dict.keys(), reverse=True)
    data_dict = {'modelNames': modelName_list}
    data = {'data': json.dumps(data_dict)}
    # print(data_dict)
    return HttpResponse(json.dumps(data_dict), content_type='application/json')