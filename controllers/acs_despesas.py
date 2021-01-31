# -*- coding: utf-8 -*-
import datetime
@auth.requires_login()
def index():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    empresa = db.empresa(usuario.empresa)
    mes=request.now.month
    ano=request.now.year
    if len(request.args) == 0:
        redirect(URL(args=[mes,ano]))
    mes=request.args(0, cast=int)
    ano=request.args(1, cast=int)
    primeira_data=datetime.date(ano, mes, 1)
    ultima_data=datetime.date(ano, mes, 1)
    nos=request.now.year
    if (mes==12):
        ultima_data=datetime.date(ano+1, 1, 1)
    else:
        ultima_data=datetime.date(ano, mes+1, 1)
    rows = db((db.despesa_empresa.empresa==empresa.id)&(db.despesa_empresa.data_ocorrencia>=primeira_data)&(db.despesa_empresa.data_ocorrencia<ultima_data)).select(orderby=db.despesa_empresa.data_ocorrencia)
    consul=(request.args(2))
    if (consul):
        rows = db((db.despesa_empresa.empresa==empresa.id)&(db.despesa_empresa.data_ocorrencia>=primeira_data)&(db.despesa_empresa.data_ocorrencia<ultima_data)&(db.despesa_empresa.descricao.contains(consul))).select(limitby=(0,35))
    return locals()


@auth.requires_login()
def cadastrar():
    response.view = 'generic.html' # use a generic view
    request.function='Cadastrar Despesa'
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    db.despesa_empresa.empresa.default=usuario.empresa
    form = SQLFORM(db.despesa_empresa).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)


@auth.requires_login()
def alterar():
    response.view = 'generic.html' # use a generic view
    despesa_empresa = db.despesa_empresa(request.args(0, cast=int))
    db.despesa_empresa.id.writable=False
    db.despesa_empresa.id.readable=False
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    if usuario.empresa!=despesa_empresa.empresa:
        redirect(URL('default','index'))
    form = SQLFORM(db.despesa_empresa, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)
