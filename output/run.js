$(function () {
  var mph = [], distance = [], weight = [], time = [], dates = [], mpm = [];

  for (var i = 0; i < 30; i++) {
    dates[i] = 0;
  }
  var today = Date.now()
  $.each(data, function (idx) {
    mph.push(Math.round(this.average_mph * 100) / 100);
    mpm.push(Math.round(this.mile_time * 100) / 100);
    distance.push(this.distance);
    weight.push(this.weight);
    time.push(this.run_time_seconds);
    var date_idx = Math.round((today - Date.parse(this.date_str)) / 86400000)
    if (date_idx < 30) {
      dates[date_idx] = 1;
    }
  });



  $('#date_sparkline').sparkline(dates, {
    width:100,
    height:25,
    type:'bar',
    barColor: '#859900'
  });
  $('#mph_sparkline').sparkline(mph,{
    width:100,
    height:25,
    type:'bar',
    chartRangeMin: 5,
    barColor: '#268bd2'
  });
  $('#distance_sparkline').sparkline(distance,{
    width:100,
    height:25,
    type:'bar',
    chartRangeMin: 0,
    barColor: '#6c71c2'
  });
  $('#weight_sparkline').sparkline(weight,{
    width:100,
    height:25,
    type:'bar',
    chartRangeMin: 150,
    barColor: '#dc322f'
  });
  $('#time_sparkline').sparkline(time,{
    width:100,
    height:25,
    type:'bar',
    chartRangeMin: 1100,
    barColor: '#cb4b16'
  });
  $('#mpm_sparkline').sparkline(mpm,{
    width:100,
    height:25,
    type:'bar',
    chartRangeMin: 6,
    barColor: '#b58900'
  });

});
