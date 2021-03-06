# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    empresa = db.empresa(usuario.empresa)
    #coisa errada pra atualizar tudo mas não sei como fazer correto
    paginacao = 10
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
    total = db(db.imovel.empresa==empresa.id).count()
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1
    if total==0:
        paginas=1
    if pagina > paginas:
        redirect(URL(args=[paginas]))
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db(db.imovel.empresa==empresa.id).select(
      limitby=limites,orderby=~db.imovel.id
      )
    consul=(request.args(1))
    if (consul):
        registros = db((db.imovel.empresa==empresa.id)&((db.imovel.lougradouro.contains(consul))|(db.imovel.bairro.contains(consul)))).select(limitby=(0,paginacao))
        paginas=1
    #faz a atualização
    for row in registros:
        total_contatos = db((db.contrato_aluguel.imovel==row.id)).count()
        #atualiza quantidade de contratos do cliente
        if total_contatos>0:
            row.q_contratos=total_contatos
        else:
            row.q_contratos=0
        #atualizar quantidade de parcelas
        total_parcelas = db((db.recebimento_contrato.imovel==row.id)).count()
        #atualiza quantidade e valores das parcelas
        if total_parcelas>0:
            row.q_parcelas_total=total_parcelas
            sum = db.recebimento_contrato.valor_original.sum()
            valor_total = db((db.recebimento_contrato.imovel==row.id)).select(sum).first()[sum]
            row.valor_total=valor_total
        else:
            row.q_parcelas_total=0
            row.valor_total=0
        q_parcelas_pagas = db((db.recebimento_contrato.imovel==row.id)&(db.recebimento_contrato.status=="Quitado")).count()
        #atualiza quantidade e valores das parcelas Quitadas
        if q_parcelas_pagas>0:
            row.q_parcelas_pagas=q_parcelas_pagas
            sum = db.recebimento_contrato.valor_recebido.sum()
            valor_recebido = db((db.recebimento_contrato.imovel==row.id)&(db.recebimento_contrato.status=="Quitado")).select(sum).first()[sum]
            row.valor_recebido=valor_recebido
        else:
            row.q_parcelas_pagas=0
            row.valor_recebido=0
        q_parcelas_atrasadas = db((db.recebimento_contrato.imovel==row.id)&(db.recebimento_contrato.status=="Atrasado")).count()
        #atualiza quantidade e valores das parcelas Atrasado
        if q_parcelas_atrasadas>0:
            row.q_parcelas_atrasadas=q_parcelas_atrasadas
            sum = db.recebimento_contrato.valor_original.sum()
            valor_debito = db((db.recebimento_contrato.imovel==row.id)&(db.recebimento_contrato.status=="Atrasado")).select(sum).first()[sum]
            row.valor_debito=valor_debito
        else:
            row.q_parcelas_atrasadas=0
            row.valor_debito=0
        q_parcelas_aguardadas = db((db.recebimento_contrato.imovel==row.id)&(db.recebimento_contrato.status=="Aguardando")).count()
        #atualiza quantidade e valores das parcelas Aguardando
        if q_parcelas_aguardadas>0:
            row.q_parcelas_aguardadas=q_parcelas_aguardadas
            sum = db.recebimento_contrato.valor_original.sum()
            valor_aguardando = db((db.recebimento_contrato.imovel==row.id)&(db.recebimento_contrato.status=="Aguardando")).select(sum).first()[sum]
            row.valor_aguardando=valor_aguardando
        else:
            row.q_parcelas_aguardadas=0
            row.valor_aguardando=0
        q_despesa = db((db.despesa_imovel.imovel==row.id)&(db.despesa_imovel.valor>0)).count()
        #atualiza quantidade e valores das parcelas Aguardando
        if q_despesa>0:
            sum = db.despesa_imovel.valor.sum()
            valor_total = db((db.despesa_imovel.imovel==row.id)&(db.despesa_imovel.valor>0)).select(sum).first()[sum]
            row.valor_desp_total=valor_total
        else:
            row.valor_desp_total=0
        row.update_record()
    return dict(rows=registros, pagina=pagina, paginas=paginas, total=total, empresa=empresa, usuario=usuario, consul=consul)

@auth.requires_login()
def cadastrar():
    response.view = 'generic.html' # use a generic view
    request.function='Cadastrar novo Cliente'
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    db.imovel.empresa.default=usuario.empresa
    db.imovel.empresa.writable=False
    db.imovel.empresa.readable=False
    form = SQLFORM(db.imovel).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)

@auth.requires_login()
def acessar():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    imovel = db.imovel(request.args(0, cast=int))
    total_contratos = db(db.contrato_aluguel.imovel==imovel.id).count()
    if total_contratos>0:
        sum = db.contrato_aluguel.valor_recebido.sum()
        recebido_total=db((db.contrato_aluguel.imovel==imovel.id)).select(sum).first()[sum]
        if imovel.valor_recebido!=recebido_total:
            imovel.valor_recebido=recebido_total
            imovel.update_record()
    return locals()

@auth.requires_login()
def alterar():
    response.view = 'generic.html' # use a generic view
    imovel = db.imovel(request.args(0, cast=int))
    if imovel.conferido==True:
        session.flash = 'Imovel está bloqueado'
        redirect(URL('acessar',args=imovel.id))
    db.imovel.id.writable=False
    db.imovel.id.readable=False
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    if usuario.empresa!=imovel.empresa:
        redirect(URL('default','index'))
    quant_contrato=db(db.recebimento_contrato.imovel==imovel.id).count()
    deletar=False
    if quant_contrato==0:
        deletar=True
        
    form = SQLFORM(db.imovel, request.args(0, cast=int), deletable=deletar)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('acessar',args=imovel.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)


@auth.requires_login()
def contratos():
    imovel = db.imovel(request.args(0, cast=int))
    total = db(db.contrato_aluguel.imovel==imovel.id).count()
    total_ativo = db((db.contrato_aluguel.imovel==imovel.id)&(db.contrato_aluguel.status=="Ativo")).count()
    if total_ativo:
        imovel.status="Ocupado"
        imovel.update_record()
    if total==0:
        session.flash = 'Sem Contratos'
        redirect(URL('acessar',args=imovel.id))
    rows = db(db.contrato_aluguel.imovel==imovel.id).select(orderby=~db.contrato_aluguel.id)
    return locals()


@auth.requires_login()
def recebimentos():
    imovel = db.imovel(request.args(0, cast=int))
    total = db(db.recebimento_contrato.imovel==imovel.id).count()
    total_quitados = db((db.recebimento_contrato.imovel==imovel.id)&(db.recebimento_contrato.status=="Aguardando")).count()
    if total_quitados:
        imovel.status="Ocupado"
        imovel.update_record()
    if total==0:
        session.flash = 'Sem Contratos'
        redirect(URL('acessar',args=imovel.id))
    rows = db((db.recebimento_contrato.imovel==imovel.id)&(db.recebimento_contrato.finalizado==True)).select(limitby=(0,50), orderby=~db.recebimento_contrato.id)
    return locals()


@auth.requires_login()
def despesas():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    imovel = db.imovel(request.args(0, cast=int))
    paginacao = 20
    if len(request.args) == 1:
        pagina = 1
    else:
        try:
            pagina = int(request.args[1])
        except ValueError:
            redirect(URL('erro', vars={
                  'msg':'Numero da página inválido'
                  }))
    if pagina <= 0:
        redirect(URL(args=[imovel.id,1]))
    total = db(db.despesa_imovel.imovel==imovel.id).count()
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1
    if total==0:
        paginas=1
    if pagina > paginas:
        redirect(URL(args=[imovel.id,paginas]))
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db(db.despesa_imovel.imovel==imovel.id).select(
      limitby=limites,orderby=~db.despesa_imovel.id
      )
    consul=(request.args(1))
    if (consul):
        registros = db((db.despesa_imovel.imovel==imovel.id)&((db.despesa_imovel.descricao.contains(consul)))).select(limitby=(0,paginacao))
        paginas=1
    
    totalreg=db(db.despesa_imovel.imovel==imovel.id).count()
    valor_total=0
    if totalreg>0:
        sum = db.despesa_imovel.valor.sum()
        valor_total = db(db.despesa_imovel.imovel==imovel.id).select(sum).first()[sum]
    imovel.valor_desp_total=valor_total
    imovel.update_record()
    return dict(rows=registros, pagina=pagina, paginas=paginas, total=total, imovel=imovel, usuario=usuario, consul=consul)


@auth.requires_login()
def cadastrar_despesa():
    response.view = 'generic.html' # use a generic view
    request.function='Cadastrar Despesa'
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    imovel = db.imovel(request.args(0, cast=int))
    db.despesa_imovel.imovel.default=imovel.id
    db.despesa_imovel.imovel.writable=False
    db.despesa_imovel.imovel.readable=False
    db.despesa_imovel.empresa.default=imovel.empresa
    db.despesa_imovel.empresa.writable=False
    db.despesa_imovel.empresa.readable=False
    form = SQLFORM(db.despesa_imovel).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('despesas',args=imovel.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)

@auth.requires_login()
def alterar_despesa():
    response.view = 'generic.html' # use a generic view
    despesa_imovel = db.despesa_imovel(request.args(0, cast=int))
    db.despesa_imovel.id.writable=False
    db.despesa_imovel.id.readable=False
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    if usuario.empresa!=despesa_imovel.empresa:
        redirect(URL('default','index'))
    form = SQLFORM(db.despesa_imovel, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('despesas',args=despesa_imovel.imovel))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def conferir():
    imovel = db.imovel(request.args(0, cast=int))
    if imovel.conferido==True:
        imovel.conferido=False
    else:
        imovel.conferido=True
    imovel.update_record()
    redirect(URL('acessar',args=imovel.id))
    return locals()

@auth.requires_login()
def disponiveis():
    
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    empresa = db.empresa(usuario.empresa)
    #coisa errada pra atualizar tudo mas não sei como fazer correto
    paginacao = 10
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
    total = db((db.imovel.empresa==empresa.id)&(db.imovel.status=="Disponivel")).count()
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1
    if total==0:
        session.flash = 'Imóveis Ocupados'
        redirect(URL('acs_administrativo','index'))
    if pagina > paginas:
        redirect(URL(args=[paginas]))
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db((db.imovel.empresa==empresa.id)&(db.imovel.status=="Disponivel")).select(
      limitby=limites,orderby=~db.imovel.id
      )
    return dict(rows=registros, pagina=pagina, paginas=paginas, total=total, empresa=empresa, usuario=usuario)
