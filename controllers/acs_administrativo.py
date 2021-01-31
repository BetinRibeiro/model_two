# -*- coding: utf-8 -*-
import datetime
@auth.requires_login()
def index():
    return dict(message="Acesso Administrativo")


@auth.requires_login()
def alterar_dados():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    empresa = db.empresa(usuario.empresa)
    request.function=('Alterar Dados da Empresa')
    db.empresa.id.writable=False
    db.empresa.id.readable=False
    form = SQLFORM(db.empresa, empresa.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def relatorio():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    empresa = db.empresa(usuario.empresa)
    q_clientes = db((db.pessoa.empresa==empresa.id)).count()
    empresa.q_clientes=q_clientes
    q_imoveis = db((db.imovel.empresa==empresa.id)).count()
    empresa.q_imoveis=q_imoveis
    q_contratos = db((db.contrato_aluguel.empresa==empresa.id)).count()
    empresa.q_contratos=q_contratos
    q_parcelas_total = db((db.recebimento_contrato.empresa==empresa.id)).count()
    empresa.q_parcelas_total=q_parcelas_total
    valor_total=0
    if q_parcelas_total>0:
        sum = db.recebimento_contrato.valor_original.sum()
        valor_total = db((db.recebimento_contrato.empresa==empresa.id)).select(sum).first()[sum]
    empresa.valor_total=valor_total
    q_parcelas_pagas = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=="Quitado")).count()
    empresa.q_parcelas_pagas=q_parcelas_pagas
    valor_recebido=0
    if q_parcelas_pagas>0:
        sum = db.recebimento_contrato.valor_recebido.sum()
        valor_recebido = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=="Quitado")).select(sum).first()[sum]
    empresa.valor_recebido=valor_recebido
    q_parcelas_atrasadas = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=="Atrasado")).count()
    empresa.q_parcelas_atrasadas=q_parcelas_atrasadas
    valor_debito=0
    if q_parcelas_atrasadas>0:
        sum = db.recebimento_contrato.valor_original.sum()
        valor_debito = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=="Atrasado")).select(sum).first()[sum]
    empresa.valor_debito=valor_debito
    
    q_parcelas_aguardadas = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=="Aguardando")).count()
    empresa.q_parcelas_aguardadas=q_parcelas_aguardadas
    valor_aguardando=0
    if q_parcelas_aguardadas>0:
        sum = db.recebimento_contrato.valor_recebido.sum()
        valor_aguardando = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=="Aguardando")).select(sum).first()[sum]
    empresa.valor_aguardando=valor_aguardando
    
    empresa.update_record()
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

    recebimento_total = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).count()

    total_geral = 0
    if recebimento_total>0:
      sum = db.recebimento_contrato.valor_original.sum()
      total_geral = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).select(sum).first()[sum]
    #####################
    recebimento_contrato = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Quitado')&(db.recebimento_contrato.data_recebimento>=primeira_data)&(db.recebimento_contrato.data_recebimento<ultima_data)).count()

    total_recebido = 0
    if recebimento_contrato>0:
      sum = db.recebimento_contrato.valor_recebido.sum()
      total_recebido = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Quitado')&(db.recebimento_contrato.data_recebimento>=primeira_data)&(db.recebimento_contrato.data_recebimento<ultima_data)).select(sum).first()[sum]
    #####################
    aguardando_contrato = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Aguardando')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).count()
    
    total_aguardando = 0
    if aguardando_contrato>0:
      sum = db.recebimento_contrato.valor_original.sum()
      total_aguardando = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Aguardando')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).select(sum).first()[sum]
        
        #####################
    q_debito_total = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Atrasado')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).count()
    
    total_debito = 0
    if q_debito_total>0:
      sum = db.recebimento_contrato.valor_original.sum()
      total_debito = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Atrasado')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).select(sum).first()[sum]
         #####################
    despesa_empresa = db((db.despesa_empresa.empresa==empresa.id)&(db.despesa_empresa.data_ocorrencia>=primeira_data)&(db.despesa_empresa.data_ocorrencia<ultima_data)).count()

    total_despesa_empresa = 0
    if despesa_empresa>0:
      sum = db.despesa_empresa.valor.sum()
      total_despesa_empresa = db((db.despesa_empresa.empresa==empresa.id)&(db.despesa_empresa.data_ocorrencia>=primeira_data)&(db.despesa_empresa.data_ocorrencia<ultima_data)).select(sum).first()[sum]
        
        #####################
    despesa_imoveis = db((db.despesa_imovel.empresa==empresa.id)&(db.despesa_imovel.data_ocorrencia>=primeira_data)&(db.despesa_imovel.data_ocorrencia<ultima_data)).count()

    total_despesa_imoveis = 0
    if despesa_imoveis>0:
      sum = db.despesa_imovel.valor.sum()
      total_despesa_imoveis = db((db.despesa_imovel.empresa==empresa.id)&(db.despesa_imovel.data_ocorrencia>=primeira_data)&(db.despesa_imovel.data_ocorrencia<ultima_data)).select(sum).first()[sum]
    
    return locals()


@auth.requires_login()
def cabecalho():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    cabecalho = db.cabecalho(db.cabecalho.id>0)
    db.cabecalho.id.writable=False
    db.cabecalho.id.readable=False
    form = SQLFORM(db.cabecalho, cabecalho.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def post01():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    artigo = db.artigo(db.artigo.id==1)
    db.artigo.id.writable=False
    db.artigo.id.readable=False
    form = SQLFORM(db.artigo, artigo.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)
@auth.requires_login()
def post02():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    artigo = db.artigo(db.artigo.id==2)
    db.artigo.id.writable=False
    db.artigo.id.readable=False
    form = SQLFORM(db.artigo, artigo.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)
@auth.requires_login()
def van01():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    caracteristica = db.caracteristica(db.caracteristica.id==1)
    db.caracteristica.id.writable=False
    db.caracteristica.id.readable=False
    form = SQLFORM(db.caracteristica, caracteristica.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def van02():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    caracteristica = db.caracteristica(db.caracteristica.id==2)
    db.caracteristica.id.writable=False
    db.caracteristica.id.readable=False
    form = SQLFORM(db.caracteristica, caracteristica.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)


@auth.requires_login()
def van03():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    caracteristica = db.caracteristica(db.caracteristica.id==3)
    db.caracteristica.id.writable=False
    db.caracteristica.id.readable=False
    form = SQLFORM(db.caracteristica, caracteristica.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)


@auth.requires_login()
def serv01():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    desenvolvedor = db.desenvolvedor(db.desenvolvedor.id==1)
    db.desenvolvedor.id.writable=False
    db.desenvolvedor.id.readable=False
    form = SQLFORM(db.desenvolvedor, desenvolvedor.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def serv02():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    desenvolvedor = db.desenvolvedor(db.desenvolvedor.id==2)
    db.desenvolvedor.id.writable=False
    db.desenvolvedor.id.readable=False
    form = SQLFORM(db.desenvolvedor, desenvolvedor.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def serv03():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    desenvolvedor = db.desenvolvedor(db.desenvolvedor.id==3)
    db.desenvolvedor.id.writable=False
    db.desenvolvedor.id.readable=False
    form = SQLFORM(db.desenvolvedor, desenvolvedor.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def serv04():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    desenvolvedor = db.desenvolvedor(db.desenvolvedor.id==4)
    db.desenvolvedor.id.writable=False
    db.desenvolvedor.id.readable=False
    form = SQLFORM(db.desenvolvedor, desenvolvedor.id, deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('default','index'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)
