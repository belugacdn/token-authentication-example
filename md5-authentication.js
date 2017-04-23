var url = require("url");
var crypto = require('crypto');
var host = url.parse(process.argv[2]).host;
var path = url.parse(process.argv[2]).pathname;
var prot = url.parse(process.argv[2]).protocol
var secret = "xa5aileeph6nah5ooQu";
var d = new Date();
var t = d.getTime() / 1000;
var expire = parseInt(t) + 360 ;
var sign = path+'?expires='+expire+'&pass='+secret;
var md5 = crypto.createHash('md5').update(sign).digest("hex");
var secure = "?token=" + md5 + "&expires=" + expire;
console.log(prot+ "//"+ host+ path+ secure);
