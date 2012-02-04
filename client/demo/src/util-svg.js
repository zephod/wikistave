// SVGUtil utility object operates on SVG path strings. 
// @requires Underscore.js
var SVGUtil = SVGUtil || {};

SVGUtil.translatePath = function(path, x_off, y_off) {
  return SVGUtil.transformPath(path, function(x, y) { return {x: (x+x_off), y: (y+y_off)}; });
}
SVGUtil.scalePath = function(path, scale) {
  return SVGUtil.transformPath(path, function(x,y) { return {x: x*scale, y: y*scale}; });
}
SVGUtil.integerPath = function(path) {
  return SVGUtil.transformPath(path, function(x, y) { return { x: Math.round(x), y: Math.round(y) };});
}
// Pass any function which takes parameters (x, y) and returns an object with attributes {x: .., y: ..}
// The path must be expressed with commas in the middle of all x,y pairs
SVGUtil.transformPath = function(pathString, transform) {
  path = _.map(path, function(element) { 
    if (element.indexOf(',')>-1) {
      var xy = element.split(',');
      var transformed = transform(parseFloat(xy[0]), parseFloat(xy[1]));
      return transformed.x + ',' + transformed.y;
    }
    return element;
  });
  return path;
}

// Pull apart the (arbitrarily formatted) string of SVG paths into an array of characters and numbers
SVGUtil.pathStringToArray = function(str) {
  var out = [];
  var x = 0;
  function typeOf(character) {
    if (/[0-9.,-]/.test(character)) return 'number';
    if (/[a-zA-Z]/.test(character)) return 'character';
    return 'other';
  }
  while (x<str.length) {
    var currentType=typeOf(str.charAt(x));
    var y=x+1;
    while (typeOf(str.charAt(y))==currentType) y++;
    if (currentType=='number' || currentType=='character') {
      out.push(str.substring(x,y));
    }
    x=y;
  }
  return out;
}

var debug = SVGUtil.pathStringToArray;
