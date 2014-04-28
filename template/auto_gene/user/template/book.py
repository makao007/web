#encoding:utf-8

user = {
    'name'   :   'user',
    'title'  :  u'用户',
    'sub_title':u'用户',
    'url': '/admin/user',
    'remark':u'用户',
    'table_name': 'user',
    'fields':[
        {'name':'code', 'null':'n', 'title':u'编号',    'type':'varchar(20)',   'default':''},
        {'name':'name', 'null':'n', 'title':u'姓名',    'type':'varchar(20)',   'default':''},
        {'name':'sex',  'null':'n', 'title':u'性别',    'type':'tinyint',       'default':''},
        {'name':'tel',  'null':'y', 'title':u'手机',    'type':'tinyint',       'default':''}, 
        {'name':'password', 'null':'n', 'title':u'密码','type':'char(32)',      'default':''},  
        {'name':'role', 'null':'n', 'title':u'角色',    'type':'tinyint',       'default':''},  #1:普通读者, 2:图书管理员， 3:超级管理员
    ],
}

book = {
    'name'   :   'book',
    'title'  :  u'书籍',
    'sub_title':u'书籍',
    'url': '/admin/book',
    'remark':u'',
    'table_name': 'book',
    'fields':[
        {'name':'name',    'null':'n', 'title':u'巡查类型',       'type':'int',            'default':''    },
        {'name':'title',        'null':'n', 'title':u'标题',          'type':'varchar(1000)',   'default':''   },
        {'name':'ord',          'null':'n', 'title':u'顺序',          'type':'tinyint',         'default':1    },
        {'name':'valid',        'null':'y', 'title':u'是否显示',      'type':'tinyint',         'default':1     },   
    ],
}

insp_plan = {
    'name'   :   'insp_plan',
    'title'  :  u'巡查计划',
    'sub_title':u'巡查计划',
    'url': '/admin/insp_plan',
    'remark':u'',
    'table_name': 'insp_plan',
    'fields':[
        {'name':'user_id',      'null':'n', 'title':u'巡查员',        'type':'int',             'default':''   },
        {'name':'insp_date',    'null':'n', 'title':u'标题',          'type':'varchar(1000)',   'default':''   },
        {'name':'dept_id',      'null':'n', 'title':u'部门',          'type':'tinyint',         'default':''   },
        {'name':'chain_id',     'null':'n', 'title':u'分店',          'type':'int',             'default':''   },
    ],
}

insp_value = {
    'name'   :   'insp_value',
    'title'  :  u'巡查值',
    'sub_title':u'巡查值',
    'url': '/admin/insp_value',
    'remark':u'',
    'table_name': 'insp_value',
    'fields':[
        {'name':'insp_plan_id',    'null':'n', 'title':u'巡查计划',       'type':'int',             'default':''    },
        {'name':'insp_item_id',    'null':'n', 'title':u'巡查项目',       'type':'int',             'default':''   },
        {'name':'value',           'null':'n', 'title':u'巡查值（是否）',  'type':'tinyint',         'default':''   },
        {'name':'remark',          'null':'n', 'title':u'巡查异常记录',    'type':'varchar(1000)',   'default':''    },
    ],
}

data = [test_item, insp_type, insp_item, insp_plan, insp_value]