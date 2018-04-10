class global_var(object):
    stock_type = {'SZ_stock': '1', 'SH_stock': '2', 'SZ_index': '100', 'SH_index': '200'}
    db_parameter = {'host': '192.168.1.11', 'port': 3306,
                    'user': 'zqfordinary', 'passwd': 'Ab123456', 'db': 'stock'}

    minute_model_dir = '/mnt/aidata/AI_trend_model_3/models/'
    day_model_dir = '/mnt/aidata/AI_trend_model_2/models/'
    day_timeFormat = '%Y%m%d'
    minute_timeFormat = '%Y%m%d%H%M'

def set_stock_type(stock_type):
    global_var.stock_type = stock_type
def get_stock_type():
    return global_var.stock_type

def set_db_parameter(stock_type):
    global_var.stock_type = stock_type
def get_db_parameter():
    return global_var.stock_type


def get_model_dir(dayOrMinute,taskType):
    if dayOrMinute=='day':
        model_dir = global_var.day_model_dir + taskType + '/'
    elif dayOrMinute=='minute':
        model_dir = global_var.day_model_dir + taskType + '/'
    return model_dir
