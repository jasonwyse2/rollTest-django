
function draw_intraday_minute(context,parameter){
　
 time_close = context['time_close']
 bottom_data = context['bottom_data']
 up_data = context['up_data']
 top_data = context['top_data']
 down_data = context['down_data']

 underlying = parameter['underlying']
 date = parameter['date']
 title_text = underlying + ' '+ date+ ' '+ 'Intraday Minute'
 time_closePercent = get_closePercent_by_close(time_close)
 close0 = time_close[0][1]
Highcharts.chart('container', {
    chart: {type: 'scatter', zoomType: 'xy'},
    title: {text: title_text},
    subtitle: {text: '' },
    xAxis: {
     title: {enabled: true, text: 'Time'},
        startOnTick: false,
        endOnTick: false,
        showLastLabel: true,
        gridLineWidth: 1,
        crosshair: true,
        crosshair : {	　　　　　　　　　　 //其他图表类型需要配置样式
　　　　　　　width: 1,
　　　　　　　color: 'gray',
　　　　　　　dashStyle: 'Solid'
　　　　　},
    },
    yAxis: [{
        title: {text: 'Price'},
        gridLineWidth: 1,
        itemStyle : {
        	'fontSize' : '25px'
    	   },
    	   crosshair: true,
    	   crosshair : {	　　　　　　　　　　 //其他图表类型需要配置样式
　　　　　　　width: 1,
　　　　　　　color: 'gray',
　　　　　　　dashStyle: 'Solid'
　　　　　},
    },{
        title: {text: 'Percent(%)'},
        opposite:true,
        labels:{
         formatter:function(){
          return ((this.value-close0)/close0*100).toFixed(2)
         }
        }
    }],
    credits: {
	    enabled:false
	  },
    legend: {
//        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 70,
        y: 30,
        floating: false,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
        borderWidth: 1,
        itemStyle : {
        	'fontSize' : '15px'
    	}
    },
    plotOptions: {
        scatter: {
            marker: {
                radius: 4,
                states: {
                    hover: {
                        enabled: true,
                        lineColor: 'rgb(100,100,100)'
                    }
                }
            },
            states: {
                hover: {
                    marker: {
                        enabled: false
                    }
                }
            },
                    }
    },
    tooltip: {

       formatter: function () {
          var s = '<b>' + this.series.name +'</b>';
          s +=  '<br/>' + 'x: '+this.x + '<br/>'+
                'y: '+this.y +'<br/>' +
                'Change: '+((this.y-close0)/close0*100).toFixed(2)+'%';
          return s;
      },
    },
//        tooltip: {
//            shared: true, //是否共享提示，也就是X一样的所有点都显示出来
//            useHTML: true, //是否使用HTML编辑提示信息
//            headerFormat: '<small>{point.key}</small><table>',
//            pointFormat: '<tr><td style="color: {series.color}">{series.name}: </td>' +
//            '<td style="text-align: right"><b>{point.y}</b></td></tr>',
//            footerFormat: '</table>',
//            valueDecimals: 2 //数据值保留小数位数
//        },
    crosshairs: [{
                    width: 3,
                    color: 'green'
                }, {
                    width: 3,
                    color: 'green'
                }],
    series: [{
        name: 'Bottom',
        id: 'bottom',
        color: 'green',
        data: bottom_data,
        marker:{
            symbol:'triangle'
        },

    }, {
        name: 'Up',
        id: 'up',
        color: 'violet',
        data: up_data,
        marker:{
            symbol:'triangle'
        }
    },{
        name: 'Top',
        id: 'top',
        color: 'red',
        data: top_data,
        marker:{
            symbol:'triangle'
        }
    },{
        name: 'Down',
        id: 'down',
        color: 'lightgreen',
        data: down_data,
        marker:{
            symbol:'triangle'
        }
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
    }
    ]
});　
 }

function init_page(data){
 context = data['context']
	stock_code = data['stock_code']
 date =  data['date']

	parameters = {'underlying':stock_code,'date':date}
	draw_intraday_minute(context,parameters)
 $("#underlying").val(data['stock_code'])
 formatDate_str = get_formatDate(date)
 $("#date").val(formatDate_str)

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
		date = $("#date").val()
		modelName = $("#modelSelect").val()
		taskType = $("#taskTypeSelect").val()
		submit_data_dict={'underlying':underlying,'date':date,'modelName':modelName,'taskType':taskType}
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
        data: bottom_data,
        marker: {
            symbol: 'triangle'
        }
    }, {
        name: 'Up',
        id: 'up',
        color: 'violet',
        data: up_data,
        marker: {
            symbol: 'triangle'
        }
    },{
        name: 'Top',
        id: 'top',
        color: 'red',
        data: top_data,
        marker: {
            symbol: 'triangle'
        }
    },{
        name: 'Down',
        id: 'down',
        color: 'lightgreen',
        data: down_data,
        marker: {
            symbol: 'triangle'
        }
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




