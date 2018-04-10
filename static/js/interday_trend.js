
function draw_interday_trend(context,parameter){
　
 time_close = context['time_close']
 bottom_data = context['bottom_data']
 up_data = context['up_data']
 top_data = context['top_data']
 down_data = context['down_data']

 underlying = parameter['underlying']
 startDate = parameter['startDate']
 endDate = parameter['endDate']
 title_text = underlying + ' '+ startDate+ '-'+ endDate + 'Interday Prediction'
 time_closePercent = get_closePercent_by_close(time_close)
 close0 = time_close[0][1]
 radius_size = 5
 Highcharts.stockChart('container', {
        rangeSelector: {
            selected: 2
        },
        credits: {
	    enabled:false
	  },
	  chart: {type: 'scatter', zoomType: 'xy'},
    legend: {
            enabled: true,
            floating: false,
            align: 'left',
        verticalAlign: 'top',
        x: 70,
        y: 50,
        itemStyle : {
        	'fontSize' : '15px'
    	}
            //layout: 'vertical',

   },
   xAxis: {
     title: {enabled: true, text: 'Time'},
        startOnTick: false,
        endOnTick: false,
        showLastLabel: true,
        gridLineWidth: 1
    },
	  yAxis: [{
        title: {text: 'Price'},
        gridLineWidth: 1,
        itemStyle : {
        	'fontSize' : '25px'
    	   }
    }],
	  <!--xAxis: {  -->
          <!--type: 'datetime',  -->
          <!--tickPixelInterval: 150,  -->
     <!--labels: {  -->
     <!--formatter: function () { alert(22);   -->
                          <!--return Highcharts.dateFormat('%Y-%m-%d', this.value);    -->
                      <!--}   -->
     <!--}  -->
      <!--},  -->
	  scrollbar: {
            barBackgroundColor: 'gray',
            barBorderRadius: 7,
            barBorderWidth: 0,
            buttonBackgroundColor: 'gray',
            buttonBorderWidth: 0,
            buttonBorderRadius: 7,
            trackBackgroundColor: 'none',
            trackBorderWidth: 1,
            trackBorderRadius: 8,
//            trackBorderColor: '#CCC'
        },
        title: {
            text: '000016 Interday Trend Prediction'
        },

        tooltip: {
            split: false,
            shared: true
        },
       series: [
       {
        name: 'bottom',
        id: 'bottom',
        color: 'green',
         showInLegend: true,
        data: bottom_data,
         lineWidth:0,
        marker: {
                enabled: true,
                radius: radius_size,
                symbol:'triangle'
            },
            tooltip: {
                valueDecimals: 2
            },
            states: {
                hover: {
                    lineWidthPlus: 0
                }
            },
    }, {
        name: 'Up',
        id: 'up',
        color: 'violet',
        data: up_data,
         lineWidth:0,
        marker: {
                enabled: true,
                radius: radius_size,
                symbol:'triangle'
            },
            tooltip: {
                valueDecimals: 2
            },
            states: {
                hover: {
                    lineWidthPlus: 0
                }
            },
    },{
        name: 'Top',
        id: 'top',
        color: 'red',
        data: top_data,
        lineWidth:0,
        marker: {
                enabled: true,
                radius: radius_size,
                symbol:'triangle'
            },
            tooltip: {
                valueDecimals: 2
            },
            states: {
                hover: {
                    lineWidthPlus: 0
                }
            },
    },{
        name: 'Down',
        id: 'down',
        color: 'lightgreen',
        data: down_data,
        lineWidth:0,
        marker: {
                enabled: true,
                radius: radius_size,
                symbol:'triangle'
            },
            tooltip: {
                valueDecimals: 2
            },
            states: {
                hover: {
                    lineWidthPlus: 0
                }
            },
    },
       {
            name: 'Day Close Line',
            data: time_close,
            lineWidth: 1,
//            color: 'white',
//            yAxis:1,
            marker: {
                enabled: false,
                radius: 0.5,
                symbol:'triangle'
            },
            tooltip: {
                valueDecimals: 2
            },
            states: {
                hover: {
                    lineWidthPlus: 0
                }
            }
        }]
    });
 }

function init_page(data){
 context = data['context']
	stock_code = data['stock_code']
 startDate =  data['startDate']
 endDate =  data['endDate']

	parameters = {'underlying':stock_code,'startDate':startDate, 'endDate':endDate}
	draw_interday_trend(context,parameters)
 $("#underlying").val(data['stock_code'])
 formatDate_str = get_formatDate(startDate)
 $("#startDate").val(formatDate_str)
 formatDate_str = get_formatDate(endDate)
 $("#endDate").val(formatDate_str)

modelNames_array = data['modelNames']
update_modelOptions(modelNames_array)

}


function update_modelOptions(modelNames){
$("#modelSelect").empty()
for( var i=0;i<modelNames.length;++i){
  $("#modelSelect").append("<option value={0}>{1}</option>".format(modelNames[i],modelNames[i]))
 }
 $("#modelSelect:first").prop("selected", 'selected');
}

function get_submit_parameter(){

		underlying = $("#underlying").val()
		startDate = $("#startDate").val()
		endDate = $("#endDate").val()
		modelName = $("#modelSelect").val()
		taskType = $("#taskTypeSelect").val()
		submit_data_dict={'underlying':underlying,'startDate':startDate,'endDate':endDate,'modelName':modelName,
		'taskType':taskType}
		return submit_data_dict
	}

function update_highcharts_data(data){
 time_close = context['time_close']
 bottom_data = context['bottom_data']
 up_data = context['up_data']
 top_data = context['top_data']
 down_data = context['down_data']

 chart.update({
  series:[{
        name: 'Bottom',
        id: 'bottom',
        color: 'green',
        data: bottom_data
    }, {
        name: 'Up',
        id: 'up',
        color: 'violet',
        data: up_data
    },{
        name: 'Top',
        id: 'top',
        color: 'red',
        data: top_data
    },{
        name: 'Down',
        id: 'down',
        color: 'lightgreen',
        data: down_data
    },{
    	name:'Minute Line',
        type: 'line',
        id: 'line',
        color: 'lightblue',
        data: time_close,
        yAxis:1,
        marker:{
            symbol:'triangle',//圆点显示
            radius:0,
            states:{
                hover:{
                    enabled:false,
//                    radius:5
                }
            }
        }
    }]
 })
}




