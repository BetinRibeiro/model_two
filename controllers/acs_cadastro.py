# -*- coding: utf-8 -*-
@auth.requires_login()
def cadastro_basico():
    response.view = 'generic.html' # use a generic view
    empresa=db.empresa.insert(
        razaosocial=auth.user.first_name+" "+auth.user.last_name+" LTDA",
        nomefantasia=auth.user.first_name+" "+auth.user.last_name,
    email=auth.user.email)
    db.usuario_empresa.insert(empresa=empresa,usuario=auth.user.id, nome=empresa.nomefantasia, tipo="Proprietário")
    redirect(URL('acs_sistema','index'))
    return locals()
