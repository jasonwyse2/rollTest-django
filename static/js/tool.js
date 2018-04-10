//function init_page(){
// context = {{ context|safe }}
//	var underlying = {{ stock_code|safe }}
//	var date =  {{ date|safe }}
//	parameters = {'underlying':underlying,'date':date}
//	draw_intraday_minute(context,parameters)
//}
String.prototype.format = function(){
    var args = arguments;
    return this.replace(/\{(\d+)\}/gm, function(ms, p1){return typeof(args[p1]) == 'undefined' ? ms : args[p1]});
}


function get_formatDate(date){
 year = date.substr(0,4)
 month = date.substr(4,2)
 day = date.substr(6,2)
 date_array = [year, month, day]
 formatDate_str = date_array.join('-')
 return formatDate_str
}

function get_UnixTime(time){
 year = time.substr(0,4)
 month = time.substr(4,2)
 day = time.substr(6,2)
 hour = time.substr(8,2)
 minute = time.substr(10,2)
 date_array = [year, month, day]
 formatDate_str = date_array.join('-')
 return formatDate_str
}

function get_closePercent_by_close(time_close){
 close0 = time_close[0][1]
// alert(close0)
 var time_closePercent = []
 max_close = close0
 min_close = close0
 for( var i=0;i<time_close.length;++i){
  if(time_close[i][1]>max_close) max_close = time_close[i][1]
  if(time_close[i][1]<min_close) min_close = time_close[i][1]
 }
 for( var i=0;i<time_close.length;++i){
  time_closePercent[i] = time_close[i]
  close = time_close[i][1]
//  num = new Number((close-close0)/close0)
//  time_closePercent[i] = num.toFixed(4)
time_closePercent[i] = (close-close0)/close0
 }
// [max_close, min_close, time_closePercent]
 return time_closePercent
}
