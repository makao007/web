#encoding:utf-8

def gene_sql(data):
    
    fields = []
    for item in data.get('fields'):
        t_null = '' if item.get('null').lower().strip()=='y' else 'not null'
        t_default = '' if not item.get('default') else ('default ' + str(item.get('default')))
        
        temp = '%s %s %s %s'  % (item.get('name'), item.get('type'), t_null, t_default)
            
        fields.append (temp)
    sql = '''create table %s (id int primary key auto_increment, %s) ''' % (data.get('table_name'), ','.join(fields))
    print sql
    return sql
    
def gene_html (data):
    pass
    

def gene_py (data):
    pass
    
def gene (data):
    gene_sql(data)
    gene_html(data)
    gene_py(data)
    
    
if __name__ == "__main__":
    test_item = {
        'name':'user', 
        'title':u'用户', 
        'sub_title': u'用户',
        'link': '/admin/user', 
        'remark':u'集团内部的用户不会外开放使用,员工帐号', 
        'table_name': 'Usr',
        'fields':[
            {'name':'uid',  'null':'n', 'title':u'用户ID',  'type':'varchar(20)',   'default':''},
            {'name':'code', 'null':'n', 'title':u'编号',    'type':'varchar(20)',   'default':''},
            {'name':'name', 'null':'n', 'title':u'姓名',    'type':'varchar(20)',   'default':''},
            {'name':'role', 'null':'n', 'title':u'角色',    'type':'tinyint',       'default':1},
            {'name':'area', 'null':'y', 'title':u'区域',    'type':'tinyint',       'default':1},
        ],
    }
    gene (test_item)