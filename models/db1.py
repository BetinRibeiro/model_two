# -*- coding: utf-8 -*-
db.define_table('contrato_aluguel',
                Field('empresa','reference empresa', label='empresa', writable=False, readable=False),
                Field('imovel','reference imovel', label='Imovel', notnull=True),
                Field('locatario','reference pessoa', label='Locatário', notnull=True),
                Field('conjuge','reference pessoa', label='Cônjuge', writable=False, readable=False),
                Field('fiador','reference pessoa', label='Fiador', writable=False, readable=False),
                #descricao para consultar mais rápido
                Field('codigo', 'string', default='', writable=False, readable=False),
                #informaçoes para contrato
                Field('tipo', 'string', default='Residencial', notnull=True),
                Field('virgencia_meses', 'integer', label='Vigência em Meses', notnull=True, default=12),
                Field('data_inicial', 'date', label="Data Inicial", default=request.now, notnull=True),
                Field('valor_original', 'double', label='Valor do Aluguel', notnull=True, default=0),
                Field('valor_reajuste', 'double', label='Valor do Ajuste', writable=False, readable=False, notnull=True, default=0),
                Field('valor_caucao', 'double', label='Valor do Caução', writable=False, readable=False, notnull=True, default=0),
                Field('local_contrato', 'string', default='Juazeiro do Norte - CE', notnull=True),
                Field('data_contrato', 'date', label="Data do Contrato", default=request.now, notnull=True),
                #inteiros vindos de outras tabelas
                Field('q_parcelas_total', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_pagas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_atrasadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_aguardadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                 #Valores vindos de outras tabelas
                Field('valor_total', 'double', label='Total Valor', writable=False, readable=False, notnull=True, default=0),
                Field('valor_recebido', 'double', label='Total Recebido', writable=False, readable=False, notnull=True, default=0),
                Field('valor_debito', 'double', label='Total Debito', writable=False, readable=False, notnull=True, default=0),
                Field('valor_aguardando', 'double', label='Total Aguardando', writable=False, readable=False, notnull=True, default=0),
                Field('data_final', 'date', label="Data Final", writable=False, readable=False, default=request.now, notnull=True),
                Field('status', 'string',default='Ativo', writable=False, readable=False),
                #caso trabalhe com boletos do assas link de todos os pagamentos
                Field('cod_acesso_externo', 'string',default='', writable=False, readable=False),
                Field('conferido', 'boolean', writable=False, readable=False, default=False),
                auth.signature,
                format='%(codigo)s')

db.define_table('recebimento_contrato',
                Field('empresa','reference empresa', writable=False, readable=False, label='Empresa'),
                Field('imovel','reference imovel', writable=False, readable=False, label='Imovel'),
                Field('contrato','reference contrato_aluguel', writable=False, readable=False, label='Contrato'),
                Field('cliente','reference pessoa', writable=False, readable=False, label='Cliente'),
                #para facilitar a busca
                Field('codigo', 'string', default='', writable=False, readable=False),
                Field('data_vencimento', 'date', label="Data Vencimento", readable=False, writable=False, default=request.now, notnull=True),
                #só pode ser alterada quando o recebimento for efetuado
                Field('data_recebimento', 'date', label="Data Recebimento", readable=False, writable=False, default=request.now, notnull=True),
                Field('descricao', 'string',label='Descrição', writable=True, readable=True),
                #caso trabalhe com boletos do assas
                Field('cod_acesso_externo', 'string',default='', writable=False, readable=False),
                Field('valor_original', 'double', label='Valor Original', readable=False, writable=False, notnull=True, default=0),
                Field('valor_recebido', 'double', label='Valor Recebido', readable=False, writable=False, notnull=True, default=0),
                #Verificar quais tipo de recebimento são utilizados
                Field('tipo', 'string',default='Dinheiro', writable=False, readable=False),
                Field('status', 'string',default='Aguardando', writable=False, readable=False),
                Field('finalizado', 'boolean', writable=False, readable=False, default=False),
                Field('conferido', 'boolean', writable=False, readable=False, default=False),
                auth.signature,
                format='%(codigo)s')

db.define_table('despesa_imovel',
                Field('empresa','reference empresa', writable=False, readable=False, label='Empresa'),
                Field('imovel','reference imovel', writable=False, readable=False, label='Imovel'),
                Field('data_ocorrencia', 'date', label="Data", readable=True, writable=True, default=request.now, notnull=True),
                Field('descricao', 'string',label='Descrição', writable=True, readable=True),
                Field('valor', 'double', label='Valor', notnull=True, default=0),
                Field('conferido', 'boolean', writable=False, readable=False, default=False),
                auth.signature,
                format='%(descricao)s')
