source: http://witmax.cn/remove-google-redirect.html

ʹ�÷�����

 1������RemoveRedirect�������ѹ


2����Chrome��ַ������chrome://settings/extensionSettings�����á���չ���򡷹�ѡ������Աģʽ���������ڿ�������չ���򡭡�ѡ��ղŽ�ѹ�õ����ļ���

3��ˢ��Googleҳ�棬�㶨

����Google��������������Ͳ��������ת��ַ�ˡ�

P.S. ����һ�²��Դ�룬�ܼ򵥣�����ͨ��JS��Google�������ҳ�����MouseDownʱ��ɵ��ˣ��ñ�������

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