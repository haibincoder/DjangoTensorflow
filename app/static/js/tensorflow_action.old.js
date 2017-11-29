var canvas = document.getElementById('canvas');  //获取标签
var ctx = canvas.getContext("2d");


var fillStyle = "black";
ctx.fillRect(0,0,600,300);
var onoff = false;  //按下标记
var oldx = -10;
var oldy = -10;
//设置颜色
var linecolor = "white";
var linw = 4;
canvas.addEventListener("mousemove",draw,true);  //鼠标移动事件
canvas.addEventListener("mousedown",down,false);  //鼠标按下事件
canvas.addEventListener("mouseup",up,false);  //鼠标弹起事件
function down(event){
onoff = true;
oldx = event.pageX - 10;
oldy = event.pageY - 10;
}
function up(){
onoff = false;
}
function draw(event){
if (onoff==true) {
var newx = event.pageX - 10;
var newy = event.pageY - 10
ctx.beginPath();
ctx.moveTo(oldx,oldy);
ctx.lineTo(newx,newy);
ctx.strokeStyle = linecolor;
ctx.lineWidth = linw;
ctx.lineCap = "round";
ctx.stroke();


oldx = newx;
oldy = newy;
}
}
function copyimage(event)
{
var img_png_src = canvas.toDataURL("image/png");  //将画板保存为图片格式的函数
document.getElementById("image_png").src = img_png_src;
}

function downloadimage(event)
{
// 图片导出为 png 格式
var type = 'png';
// 返回一个包含JPG图片的<img>元素
var img_png_src = canvas.toDataURL("image/png");  //将画板保存为图片格式的函数
// 加工image data，替换mime type
imgData = img_png_src.replace(_fixType(type),'image/octet-stream');
// 下载后的问题名
var filename = '个人画板_' + (new Date()).getTime() + '.' + type;
// download
saveFile(imgData,filename);
}

/**
* 在本地进行文件保存
* @param  {String} data     要保存到本地的图片数据
* @param  {String} filename 文件名
*/
var saveFile = function(data, filename){
   var save_link = document.createElementNS('http://www.w3.org/1999/xhtml', 'a');
   save_link.href = data;
   save_link.download = filename;

   var event = document.createEvent('MouseEvents');
   event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
   save_link.dispatchEvent(event);
};

/**
* 获取mimeType
* @param  {String} type the old mime-type
* @return the new mime-type
*/
var _fixType = function(type) {
   type = type.toLowerCase().replace(/jpg/i, 'jpeg');
   var r = type.match(/png|jpeg|bmp|gif/)[0];
   return 'image/' + r;
};