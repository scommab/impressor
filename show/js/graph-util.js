(function(){
function getAttr(el, key) {
  var data = el.attr(key);
  if (data === undefined) {
    return data
  }
  if (data[0] == "[" || data[0] == "{") {
    // This looks like a json object
    return $.parseJSON(data);
  }
  return data
}

function getJsonOrRespond(params, src, draw) {
  if(src === undefined) {
    draw(params);
  }
  $.getJSON(src, function(d) {
    params["data"] = d;
    draw(params);
  })
}
function getBarData(el, draw) {
  var $t = $(el);
  var src = getAttr($t,"src");
  var params = {
    hideHover: true,
    element: getAttr($t,"id"),
    xkey: getAttr($t,"xkey"),
    src: getAttr($t,"src"),
    ykeys: getAttr($t,"ykeys"),
    labels: getAttr($t,"labels"),
    data: getAttr($t,"data")
  }
  getJsonOrRespond(params, src, draw);
}
function getLineData(el, draw) {
  var $t = $(el);
  var src =getAttr($t,"src");
  var params = {
    hideHover: true,
    element: getAttr($t,"id"),
    xkey: getAttr($t,"xkey"),
    ykeys: getAttr($t,"ykeys"),
    labels: getAttr($t,"labels"),
    data: getAttr($t,"data")
  };
  getJsonOrRespond(params, src, draw);

}
function getDonutData(el, draw) {
  var $t = $(el);
  var src = getAttr($t,"src");
  var params = {
    element: getAttr($t,"id"),
    xkey: getAttr($t,"xkey"),
    data: getAttr($t,"data")
  };
  getJsonOrRespond(params, src, draw);
}
var init = function() {
  $(".bar_chart").each(function() {
    getBarData(this, function(params) {
      new Morris.Bar(params);
    });
  });
  $(".line_chart").each(function() {
    getLineData(this, function(params) {
      new Morris.Line(params);
    });
  });
  $(".donut_chart").each(function() {
    getDonutData(this, function(params) {
      new Morris.Donut(params);
    })
  });
}
window.drawGraphs = init;
})();
