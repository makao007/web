source: http://witmax.cn/remove-google-redirect.html

使用方法：

 1、下载RemoveRedirect插件，解压


2、在Chrome地址栏输入chrome://settings/extensionSettings，设置》扩展程序》勾选开发人员模式》载入正在开发的扩展程序…》选择刚才解压得到的文件夹

3、刷新Google页面，搞定

这样Google的搜索结果点击后就不会出现跳转地址了。

P.S. 看了一下插件源码，很简单，就是通过JS把Google搜索结果页的鼠标MouseDown时间干掉了（好暴力！）

var url = window.location.href.toLowerCase();
if (url.indexOf("www.google.com.hk") >= 0 || url.indexOf("www.google.com") >= 0 || url.indexOf("/search") >= 0)
{
    var all = document.querySelectorAll("*");
    for (var i = 0; i < all.length; i ++)
    {
        all[i].onmousedown = null;
        all[i].setAttribute("onmousedown", " ");
    }
}