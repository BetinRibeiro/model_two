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
    recebimento_contrato = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Quitado')&(db.recebimento_contrato.data_recebimento>=primeira_data)&(db.recebimento_contrato.data_recebimento<ultima_data)).count()
    total_recebido = 0
    if recebimento_contrato>0:
      sum = db.recebimento_contrato.valor_recebido.sum()
      total_recebido = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Quitado')&(db.recebimento_contrato.data_recebimento>=primeira_data)&(db.recebimento_contrato.data_recebimento<ultima_data)).select(sum).first()[sum]
    aguardando_contrato = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Aguardando')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).count()
    total_aguardando = 0
    if aguardando_contrato>0:
      sum = db.recebimento_contrato.valor_original.sum()
      total_aguardando = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Aguardando')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).select(sum).first()[sum]
    q_debito_total = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Atrasado')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).count()
    total_debito = 0
    if q_debito_total>0:
      sum = db.recebimento_contrato.valor_original.sum()
      total_debito = db((db.recebimento_contrato.empresa==empresa.id)&(db.recebimento_contrato.status=='Atrasado')&(db.recebimento_contrato.data_vencimento>=primeira_data)&(db.recebimento_contrato.data_vencimento<ultima_data)).select(sum).first()[sum]
    despesa_empresa = db((db.despesa_empresa.empresa==empresa.id)&(db.despesa_empresa.data_ocorrencia>=primeira_data)&(db.despesa_empresa.data_ocorrencia<ultima_data)).count()
    total_despesa_empresa = 0
    if despesa_empresa>0:
      sum = db.despesa_empresa.valor.sum()
      total_despesa_empresa = db((db.despesa_empresa.empresa==empresa.id)&(db.despesa_empresa.data_ocorrencia>=primeira_data)&(db.despesa_empresa.data_ocorrencia<ultima_data)).select(sum).first()[sum]
    despesa_imoveis = db((db.despesa_imovel.empresa==empresa.id)&(db.despesa_imovel.data_ocorrencia>=primeira_data)&(db.despesa_imovel.data_ocorrencia<ultima_data)).count()
    total_despesa_imoveis = 0
    if despesa_imoveis>0:
      sum = db.despesa_imovel.valor.sum()
      total_despesa_imoveis = db((db.despesa_imovel.empresa==empresa.id)&(db.despesa_imovel.data_ocorrencia>=primeira_data)&(db.despesa_imovel.data_ocorrencia<ultima_data)).select(sum).first()[sum]
    return locals()
