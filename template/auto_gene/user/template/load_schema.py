#encoding:utf-8

def excel_to_list (filename, sheets=[], skip_header=1, header_as_key=False):
    import xlrd
    #读取excel文件，返回一个或多个列表（一个sheet对应一个列表），每个列表相当于一个table
    def sheet_to_table (table):
        def value (r,c):
            return str(table.cell(r,c).value).strip()
        
        nrows = table.nrows
        ncols = table.ncols
        temp  = []
        for i in range(skip_header, nrows):
            line = None
            if not header_as_key :
                line = []
                for j in range(0, ncols):
                     line.append ( value(i,j) )
            else:
                line = {}
                for j in range(0, ncols):
                    line[value(0,j)] = value(i,j)
            temp.append (line)
        return temp
    
    data = xlrd.open_workbook (filename)
    result = None
    if not sheets:
        #取第一个sheet
        result = sheet_to_table (data.sheets()[0])
    else:
        result = []
        for sheet in sheets:
             result.append ( sheet_to_table (data.sheet_by_name(sheet)) )
    return result
    
def gene_sql (data, default_fields):
    '''
    generate the create table sql 
    '''
    tables = []
    for line in data:
        tmp = line.pop('table_name').strip()
        if not tmp or tmp.startswith('#'):
            continue
        
        for table in tables:
            if tmp == table.get('name'):
                table['fields'].append (line)
                break
        else:
            #this else will run if not trigger "break"
            tables.append ( {'name':tmp, 'fields':[line,]} )
    
    for table in tables:
        sql = 'create table %s ('  %  table['name']
        tmp = []
        fk  = []
        for field in (default_fields + table['fields']):
            line = ' %s %s %s %s'   % (field.get('field'), field.get('type'),  \
                                       ('null' if field.get('null')=='y' else 'not null' ),  \
                                       ('' if not field.get('default') else 'default '+ field.get('default'))) 
            if field.get('unique'):
                line += ' unique '
            if field.get('PK'):
                line += ' primary key auto_increment '
            if field.get('FK'):
                fk.append (' foreign key(%s) REFERENCES %s(id)' % (field.get('field'), field.get('FK')))
            tmp.append (line)
        sql += ','.join(fk+tmp) + ' ); '
        print sql
        
    
def gene_view (data):
    pass

def gene_read (data):
    pass

def gene_edit (data):
    pass
            
def gene_list (data):
    pass
        
        
if __name__ == "__main__":
    page, table, default_field = excel_to_list ("../temp/schema.xlsx", ['admin', 'table', 'default_fields'], 1, True)
    gene_sql (table, default_field)
        