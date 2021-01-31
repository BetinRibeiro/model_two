# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    empresa = db.empresa(usuario.empresa)
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
    total = db(db.pessoa.empresa==empresa.id).count()
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1
    if total==0:
        paginas=1
    if pagina > paginas:
        redirect(URL(args=[paginas]))
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db(db.pessoa.empresa==empresa.id).select(
      limitby=limites,orderby=~db.pessoa.id
      )
    consul=(request.args(1))
    if (consul):
        registros = db((db.pessoa.empresa==empresa.id)&((db.pessoa.cpf.contains(consul))|(db.pessoa.razaosocial_nome.contains(consul)))).select(limitby=(0,paginacao))
        paginas=1
        #faz a atualização
    for row in registros:
        total_contatos = db((db.contrato_aluguel.locatario==row.id)).count()
        #atualiza quantidade de contratos do cliente
        if total_contatos>0:
            row.q_contratos=total_contatos
        else:
            row.q_contratos=0
        #atualizar quantidade de parcelas
        total_parcelas = db((db.recebimento_contrato.cliente==row.id)).count()
        #atualiza quantidade e valores das parcelas
        
        if total_parcelas>0:
            row.q_parcelas_total=total_parcelas
            sum = db.recebimento_contrato.valor_original.sum()
            valor_total = db((db.recebimento_contrato.cliente==row.id)).select(sum).first()[sum]
            row.valor_total=valor_total
        else:
            row.q_parcelas_total=0
            row.valor_total=0
        q_parcelas_pagas = db((db.recebimento_contrato.cliente==row.id)&(db.recebimento_contrato.status=="Quitado")).count()
        #atualiza quantidade e valores das parcelas Quitadas
        if q_parcelas_pagas>0:
            row.q_parcelas_pagas=q_parcelas_pagas
            sum = db.recebimento_contrato.valor_recebido.sum()
            valor_recebido = db((db.recebimento_contrato.cliente==row.id)&(db.recebimento_contrato.status=="Quitado")).select(sum).first()[sum]
            row.valor_recebido=valor_recebido
        else:
            row.q_parcelas_pagas=0
            row.valor_recebido=0
        q_parcelas_atrasadas = db((db.recebimento_contrato.cliente==row.id)&(db.recebimento_contrato.status=="Atrasado")).count()
        #atualiza quantidade e valores das parcelas Atrasado
        if q_parcelas_atrasadas>0:
            row.q_parcelas_atrasadas=q_parcelas_atrasadas
            sum = db.recebimento_contrato.valor_original.sum()
            valor_debito = db((db.recebimento_contrato.cliente==row.id)&(db.recebimento_contrato.status=="Atrasado")).select(sum).first()[sum]
            row.valor_debito=valor_debito
        else:
            row.q_parcelas_atrasadas=0
            row.valor_debito=0
        q_parcelas_aguardadas = db((db.recebimento_contrato.cliente==row.id)&(db.recebimento_contrato.status=="Aguardando")).count()
        #atualiza quantidade e valores das parcelas Aguardando
        if q_parcelas_aguardadas>0:
            row.q_parcelas_aguardadas=q_parcelas_aguardadas
            sum = db.recebimento_contrato.valor_original.sum()
            valor_aguardando = db((db.recebimento_contrato.cliente==row.id)&(db.recebimento_contrato.status=="Aguardando")).select(sum).first()[sum]
            row.valor_aguardando=valor_aguardando
        else:
            row.q_parcelas_aguardadas=0
            row.valor_aguardando=0
        row.update_record()
        #total_contatos = db((db.contrato_aluguel.pessoa==row.id)&(db.contrato_aluguel.status=="Ativo")).count()
    return dict(rows=registros, pagina=pagina, paginas=paginas, total=total, empresa=empresa, usuario=usuario, consul=consul)

@auth.requires_login()
def cadastrar():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    response.view = 'generic.html' # use a generic view
    request.function='Cadastrar novo Cliente'
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    db.pessoa.empresa.default=usuario.empresa
    db.pessoa.empresa.writable=False
    db.pessoa.empresa.readable=False
    db.pessoa.tipo.notnull=True
    db.pessoa.cpf.notnull=True
    db.pessoa.org_espedidor_cpf.notnull=True
    db.pessoa.rg.notnull=True
    db.pessoa.org_espedidor_rg.notnull=True
    db.pessoa.cep.notnull=True
    db.pessoa.telefone.notnull=True
    db.pessoa.celular.notnull=True
    form = SQLFORM(db.pessoa).process()
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
    cliente = db.pessoa(request.args(0, cast=int))
    limites = (0, 5)
    rows = db(db.contrato_aluguel.locatario==cliente.id).select(
      limitby=limites,orderby=~db.contrato_aluguel.id)
    return locals()

@auth.requires_login()
def alterar():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    cliente = db.pessoa(request.args(0, cast=int))
    if usuario.empresa!=cliente.empresa:
        redirect(URL('default','index'))
    request.function=('Alterar Dados do Cliente')
    db.pessoa.id.writable=False
    db.pessoa.id.readable=False
    form = SQLFORM(db.pessoa, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Dados atualizados'
        redirect(URL('acessar',args=cliente.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def cadastrar_contrato():
    response.view = 'generic.html' # use a generic view
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    cliente = db.pessoa(request.args(0, cast=int))
    if usuario.empresa!=cliente.empresa:
        redirect(URL('default','index'))
    request.function='Cadastrar Contrato'
    tipo_contrato = (request.args(1, cast=str))
    total = db((db.imovel.empresa==usuario.empresa)&(db.imovel.status=='Disponivel')).count()
    if total<=0:
        session.flash = 'Não tem Imoveis Disponiveis'
        redirect(URL('acs_imoveis','index'))
    if tipo_contrato=='fiador':
        db.contrato_aluguel.fiador.writable=True
        db.contrato_aluguel.fiador.readable=True
        db.contrato_aluguel.fiador.requires = IS_IN_DB(db((db.pessoa.empresa == usuario.empresa)&(db.pessoa.id!=cliente.id)), 'pessoa.id', '%(razaosocial_nome)s')
    elif tipo_contrato=='caucao':
        db.contrato_aluguel.valor_caucao.writable=True
        db.contrato_aluguel.valor_caucao.readable=True
    db.contrato_aluguel.imovel.writable=True
    db.contrato_aluguel.imovel.requires = IS_IN_DB(db((db.imovel.empresa == usuario.empresa)&(db.imovel.status=='Disponivel')), 'imovel.id', '%(subtipo)s %(lougradouro)s  %(numero)s')
    db.contrato_aluguel.locatario.default=cliente.id
    db.contrato_aluguel.empresa.default=cliente.empresa
    db.contrato_aluguel.locatario.writable=False
    
    form = SQLFORM(db.contrato_aluguel).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        imovel = db.imovel(form.vars.imovel)
        imovel.status="Ocupado"
        imovel.update_record()
        redirect(URL('acessar',args=cliente.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)

@auth.requires_login()
def atualizar_status_imoveis():
    usuario = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    cliente = db.pessoa(request.args(0, cast=int))
    rows = db(db.imovel.empresa==usuario.empresa).select()
    for row in rows:
        total_contatos = db((db.contrato_aluguel.imovel==row.id)&(db.contrato_aluguel.status=="Ativo")).count()
        if total_contatos>0:
            row.status="Ocupado"
        else:
            row.status="Disponivel"
        row.update_record()
    redirect(URL('acessar',args=cliente.id))
    return locals()


@auth.requires_login()
def conferir():
    pessoa = db.pessoa(request.args(0, cast=int))
    if pessoa.conferido==True:
        pessoa.conferido=False
    else:
        pessoa.conferido=True
    pessoa.update_record()
    redirect(URL('acessar',args=pessoa.id))
    return locals()
