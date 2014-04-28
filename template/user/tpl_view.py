#encoding:utf-8

def check (user_id, xid, other_cond):
    cond = {}
    cond['id'] = xid
    cond['user_id'] = user_id

    if other_cond:
        cond.update (other_cond)

    if not m_user.exists (**cond):
        return False

    return True


#list some records
class {{{{name}}}}_list:
    @need_login
    def GET(self):

        pass


class {{{{name}}}}_edit:
    @need_login
    def GET(self):
        pass


    @need_login
    def POST(self):
        pass


class {{{{name}}}}_delete:

    @need_login
    def GET(self, xid):


        pass




