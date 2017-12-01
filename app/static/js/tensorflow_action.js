canvas = document.getElementById('canvas');
if(canvas.getContext){
    context = canvas.getContext('2d');
}
context.lineWidth = 5;
context.strokeStyle = 'white';
canvas.onmousedown = function(e){
    e.preventDefault();
    var x = e.clientX - canvas.offsetLeft;
    var y = e.clientY - canvas.offsetTop;
    context.moveTo(x,y);
    canvas.onmousemove = function(e){
        e.preventDefault();
        var x = e.clientX - canvas.offsetLeft;
        var y = e.clientY - canvas.offsetTop;
        context.lineTo(x,y);
        context.stroke();
    };
    canvas.onmouseup = function(e){
            canvas.onmousemove = null;
    };
};

function submitimage(event) {
    $.ajax({
        type: 'POST',
        url: '/InputImage/' ,
        data: data ,
        success: success ,
        dataType: dataType
    });
}

function uploadPic(event) {
    var location = $("#image_png").attr("src");
    $.get("/InputImage/",{"location":location}, function(ret){
        $('#label_result').html(ret)
    })
}

function clearcanvas(event){
    var c=document.getElementById("canvas");
    var cxt=c.getContext("2d");
    cxt.fillStyle="#000000";
    cxt.beginPath();
    cxt.fillRect(0,0,c.width,c.height);
    cxt.closePath();
}

function copyimage(event){
    var img_png_src = canvas.toDataURL("image/png");  //将画板保存为图片格式的函数
    document.getElementById("image_png").src = img_png_src;
}

function downloadimage(event){
    // 图片导出为 png 格式
    var type = 'png';
    // 返回一个包含JPG图片的<img>元素
    var img_png_src = canvas.toDataURL("image/png");  //将画板保存为图片格式的函数
    // 加工image data，替换mime type
    imgData = img_png_src.replace(_fixType(type),'image/octet-stream');
    // 下载后的问题名
    var filename = 'image_' + (new Date()).getTime() + '.' + type;
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