# -*- coding: utf-8 -*-
import datetime
@auth.requires_login()
def index():
    usuario_empresa = db.usuario_empresa(db.usuario_empresa.usuario==auth.user.id)
    rows = db((db.recebimento_contrato.empresa==usuario_empresa.empresa)&(db.recebimento_contrato.status=="Aguardando")).select()
    mes=request.now.month
    dia=request.now.day
    ano=request.now.year
    data_hoje=datetime.date(ano, mes, dia)
    for row in rows:
        if not row.data_vencimento>data_hoje:
            row.status="Atrasado"
        row.update_record()
    if not usuario_empresa:
        redirect(URL('acs_cadastro','cadastro_basico'))
    return locals()
