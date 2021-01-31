# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    if not usuario:
        redirect(URL('default','index'))
    empresa = db.empresa(usuario.empresa)
    paginacao = 35
    if len(request.args) == 0:
        pagina = 1
    else:
        try:
            pagina = int(request.args[0])
        except ValueError:
            redirect(URL('erro', vars={
                  'msg':'Numero da página inválido'
                  }))
    if pagina <= 0:
        redirect(URL(args=1))
    total = db((db.usuario_empresa.empresa==empresa.id)&(db.usuario_empresa.ativo==True)).count()
    if total<1:
        redirect(URL('cadastrar'))
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1
    if pagina > paginas:
        redirect(URL(args=[paginas]))
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db((db.usuario_empresa.empresa==empresa.id)&(db.usuario_empresa.ativo==True)).select(
      limitby=limites,orderby=~db.usuario_empresa.id
      )
    consul=(request.args(1))
    if (consul):
        registros = db((db.usuario_empresa.empresa==empresa.id)&(db.usuario_empresa.nome.contains(consul))).select(limitby=(0,paginacao))
    return dict(rows=registros, pagina=pagina, paginas=paginas, total=total, empresa=empresa,usuario=usuario)


@auth.requires_login()
def cadastrar():
    response.view = 'generic.html' # use a generic view
    request.function='Cadastrar novo Usuario'
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    if not usuario:
        redirect(URL('default','index'))
    #db.usuario_empresa.empresa.default=usuario.empresa
    #db.usuario_empresa.empresa.writable=False
    #db.usuario_empresa.empresa.readable=False
    form = SQLFORM(db.auth_user).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        db.usuario_empresa.insert(usuario=form.vars.id, empresa=usuario.empresa, nome=form.vars.first_name, tipo='Usuario')
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)


@auth.requires_login()
def alterar():
    response.view = 'generic.html' # use a generic view
    request.function='Alterar Acesso'
    db.auth_user.id.writable=False
    db.auth_user.id.readable=False
    form = SQLFORM(db.auth_user, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        usuario=db.usuario_empresa(db.usuario_empresa.usuario==request.args(0, cast=int))
        usuario.nome=form.vars.first_name+" "+form.vars.last_name
        usuario.update_record()
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def atribuicao():
    response.view = 'generic.html' # use a generic view
    usuario=db.usuario_empresa(db.usuario_empresa.usuario==request.args(0, cast=int))
    db.usuario_empresa.id.writable=False
    db.usuario_empresa.id.readable=False
    form = SQLFORM(db.usuario_empresa, usuario.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)
