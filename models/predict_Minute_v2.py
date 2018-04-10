#coding:utf-8

import numpy as np
from load_data_from_database import query_kdata
import sys
sys.path.append('/mnt/aidata/QuantitativePlatform/lib')
import time
import datetime
#as get_model_name
from tool import Model
from tool import get_model_name
import config
import os
import common_tool
import pandas as pd
import django_config


stock_type = {'SZ_stock': '1', 'SH_stock': '2', 'SZ_index': '100', 'SH_index': '200'}
db_parameter = {'host': '192.168.1.11', 'port': 3306,
                                         'user': 'zqfordinary', 'passwd': 'Ab123456','db': 'stock'}

taskType = 'BottomTopUpDown'
minute_model_dir = '/mnt/aidata/AI_trend_model_3/models/' + taskType + '/'
day_model_dir = '/mnt/aidata/AI_trend_model_2/models/' + taskType + '/'
day_timeFormat = '%Y%m%d'
minute_timeFormat = '%Y%m%d%H%M'
def get_all_model_name(stock_code):

    modelName_list = get_model_name(stock_code=stock_code, day_minite_type='minuteSimulative',
                                    labels_type='BottomTopUpDown',
                                    starttime=201501010930, endtime=201712010930,
                                    model_path='/mnt/aidata/AI_trend_model_3/models/BottomTopUpDown/')
    print('%i models geted!' % len(modelName_list))
    return modelName_list

def model_predict(stock_code, model_path, df):

    # modelName_list = get_all_model_name(stock_code)
    # model_path = minute_model_dir + modelName_list[0]
    m = Model(model_path)
    # for i in range(10):
    #     print m.predict(df)
    return m.predict(df)

def get_day_close(code_id,startTime='20180320',endTime='20180320'):

    sql = 'SELECT DATE,close FROM index_date WHERE DATE>='+startTime+' and Date <= '+endTime+' AND code_id ='+code_id
    df_1 = query_kdata(sql)
    df_1.DATE
    sql = 'SELECT DATE,close FROM index_date WHERE DATE<'+startTime+' AND code_id = '+code_id+' ORDER BY DATE DESC LIMIT 120'
    df = query_kdata(sql)
    df_backward = df.iloc[::-1, :]
    df = pd.concat([df_backward, df_1], axis=0, ignore_index=True)
    return df

def get_minute_close(code_id,startTime='201803200930',endTime='201803201500'):
    sql = 'SELECT TIME,close FROM index_min WHERE TIME>='+startTime + ' and TIME <='+endTime+ ' AND code_id = '+code_id

    df_1 = query_kdata(sql)
    df_1.TIME

    sql = 'SELECT TIME,close FROM index_min WHERE TIME<'+startTime+' AND code_id = '+code_id+' ORDER BY TIME DESC LIMIT 120'
    df = query_kdata(sql)
    df_backward = df.iloc[::-1, :]
    df = pd.concat([df_backward, df_1], axis=0, ignore_index=True)
    return df

def get_data(parameter_dict,dayOrMinute='day'):

    stock_code = parameter_dict['stock_code']
    startTime = parameter_dict['startTime']
    endTime = parameter_dict['endTime']
    modelName = parameter_dict['modelName']

    code_wind = stock_code
    code_id = common_tool.get_codeID_by_codeWind(db_parameter, code_wind, type=stock_type['SH_index'])
    if dayOrMinute=='day':
        model_dir = day_model_dir
        df = get_day_close(str(code_id), startTime, endTime)
        date_list = df.DATE.tolist()[120:]
        time_format = day_timeFormat

        # get unix time
        date_unixType_list = common_tool.get_UnixTime_by_string(date_list, time_format)
        date_list = date_unixType_list
    elif dayOrMinute=='minute':
        model_dir = minute_model_dir
        df = get_minute_close(str(code_id), startTime, endTime)
        date_list = df.TIME.tolist()[120:]

        date_list = range(len(date_list))
    modelName_dict = common_tool.get_modelName_dict(model_dir, stock_code)
    fullModelPath = model_dir + modelName_dict[modelName]

    predict_list = model_predict(stock_code, fullModelPath, df)

    close_list = df.close.tolist()
    close_array = np.array(close_list[120:])
    date_array = np.array(date_list)
    predict_int = np.array(predict_list)

    time_close  = [[time,close] for time,close in zip(date_list,close_array)]

    bottomTopUpDown = {'bottom':0, 'up':1, 'top':2, 'down':3}
    bottom_data = [[time,close] for time,close in zip(date_array[np.where(predict_int==bottomTopUpDown['bottom'])[0]],close_array[np.where(predict_int==0)[0]])]
    up_data = [[time,close] for time,close in zip(date_array[np.where(predict_int==bottomTopUpDown['up'])[0]],close_array[np.where(predict_int==1)[0]])]
    top_data = [[time,close] for time,close in zip(date_array[np.where(predict_int==bottomTopUpDown['top'])[0]],close_array[np.where(predict_int==2)[0]])]
    down_data = [[time,close] for time,close in zip(date_array[np.where(predict_int==bottomTopUpDown['down'])[0]],close_array[np.where(predict_int==3)[0]])]
    # print time_close
    return time_close,(bottom_data,up_data,top_data,down_data)

if __name__ == '__main__':
    # time_close, (bottom_data, up_data, top_data, down_data) = get_data(stock_code = '000016',startTime='201803200930',endTime='201803201500')
    # # print time_close,len(time_close),len(bottom_data+up_data+top_data+down_data)
    # print bottom_data
    # print '\n'
    # print up_data
    # print '\n'
    # print time_close
    # model_predict('000016', model_dir, None)
    # time_format = '%Y%m%d%H%M%S'
    # currentTime = '201803191404'
    # curr = time.strptime(currentTime, time_format)
    # timeStamp = int(time.mktime(curr)) * 1000

    # print timeStamp
    pass
    print django_config.get_stock_type()

