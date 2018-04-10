#coding:utf-8
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import os
import pymysql
import scipy.signal as signal
from numpy import random
from pandas import DataFrame
import datetime
import time
import datetime
from dateutil.relativedelta import relativedelta
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import re

def currentTime_toString():
    ISOTIMEFORMAT = '%Y-%m-%d-%H-%M-%S'
    currenttime_str = time.strftime(ISOTIMEFORMAT, time.localtime())
    return currenttime_str

def login_MySQL(db_parameter={}):
    db_host = db_parameter['host']
    db_port = db_parameter['port']
    db_user = db_parameter['user']
    db_pass = db_parameter['passwd']
    db_name = db_parameter['db']
    conn = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_name)
    return  conn

def get_codeID_by_codeWind(parameter_dict,code_wind, type):
    conn = login_MySQL(parameter_dict)
    sql = r'select code_id from stock where code_wind= %s and type=%s'%(code_wind, type)
    df = pd.read_sql(sql, conn)
    code_id = df.ix[0,0]
    return code_id


def get_modelName_dict(file_dir, stock_code):
    for dirpath, dirnames, filename_list in os.walk(file_dir):
        modelName_dict = {}
        for filename in filename_list:
            filename = filename.split('.')[0]
            filename_component_list = filename.split('_')
            stock_code_ = filename_component_list[0]
            train_startTime = filename_component_list[3]
            train_endTime = filename_component_list[4]
            if stock_code == stock_code_:
                key = train_startTime+'-'+train_endTime
                modelName_dict[key] = filename
    return modelName_dict

def get_UnixTime_by_string(time_str_list, time_format='%Y%m%d%H%M'):
    unixTime_millisecond_list = []
    for time_str in time_str_list:
        curr = datetime.datetime.strptime(str(time_str), time_format)
        tmp_time = time.mktime(curr.timetuple())
        unixTime_millisecond = (int(tmp_time * 1000))
        unixTime_millisecond_list.append(unixTime_millisecond)
    return unixTime_millisecond_list
if __name__ == '__main__':
    pass
    # modelName_list = get_modelName_dict(stock_code='000016', day_minite_type='minuteSimulative',
    #                                     labels_type='BottomTopUpDown',
    #                                     starttime=201501010930, endtime=201712010930,
    #                                     model_path='/mnt/aidata/AI_trend_model_3/models/BottomTopUpDown/')
    # file_dir = '/mnt/aidata/AI_trend_model_3/models/BottomTopUpDown/'
    # stock_code = '000016'
    # dict = get_modelName_dict(file_dir, stock_code)
    # print(dict)

    currentTime = '201201231500'
    print get_UnixTime_by_string(currentTime)

