#encoding:utf-8
import re
import datetime

from fetch import fetch

'''
		    <div class="postbox">
          <div class="entry lazyload">
         <a class="a_img" href="http://www.kiees.com/2014/04/29/321156.html" title="���֣�����΢���԰����� �����  ����179Ԫ����" target="_blank"><img rel="3" width="150" height="150" class="image-frame" src="http://gi1.md.alicdn.com/imgextra/i1/266835372/T2xNYmXQhaXXXXXXXX_!!266835372.jpg_360x360q90.jpg" alt="����΢���԰����� �����  ����179Ԫ����" /></a>
            <h2><a href="http://www.kiees.com/2014/04/29/321156.html" target="_blank">����΢���԰����� ����� <span style='color:#bb0200;'> ����179Ԫ����</span></a></h2>
             <div class="detail">����΢���԰����� ������������ɰ���������������⿹�������ѡ��30CM���̣�����ʽ���ȣ�������ˮȦ ����ʽ���̣�Ԥ�ȹ��ܣ���ը����������ͨ���״����Ͳ��Լ�������ˮȦ������������ʡ�͡�����ȫ�����򵥡�

</div>
'''

def extract (content):
	info  = []

	items = re.findall (r'''<a class="a_img" href="([^"]+)" title="([^"]+)" target="_blank"><img rel="3" width="150" height="150" class="image-frame" src="([^"]+)".*?</h2>\s+<div class="detail">(.*?)</div>''', content, re.I|re.S|re.M)
	
	for item in items:
		tmp = {}
		tmp['url']   = item[0].strip().replace('\n','')
		tmp['title'] = item[1].strip().replace('\n','').replace('���֣�','',1)
		tmp['image'] = item[2].strip().replace('\n','')
		tmp['summary'] = item[3].strip().replace('\n','')
		info.append (tmp)
	return info
	
def insert (info):
	def insert_to_mysql ():
		import MySQLdb    
		conn   = MySQLdb.connect(host="127.0.0.1",user="root",passwd="1234",db="shopping",charset="utf8")  
		cursor = conn.cursor()    
		
		for item in info:
		
			sql    = "select * from item where url = %s "
			param  = (item['url'],)
			n      = cursor.execute (sql, param)
			if n > 0:
				continue 
			sql    = "insert into item (title, image, summary, content, url, show_time, fetch_time, update_time) values (%s,%s,%s,%s,%s,%s,%s,%s) "
			param  = ( item['title'], item['image'], item['summary'], item.get('content',''), item['url'], item.get('show_time',''), datetime.datetime.now(), datetime.datetime.now() )
			n      = cursor.execute (sql, param)
			print n
		conn.commit()
		cursor.close()
		conn.close()
		
	insert_to_mysql()

		

def go (url='http://www.kiees.com/'):
	#����ֵ����
	page = fetch (url)
	info = extract (page)
	insert (info)
	
if __name__ == "__main__":
	go ()