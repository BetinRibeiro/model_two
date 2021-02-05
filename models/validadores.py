# -*- coding: utf-8 -*-
#validadores da empresa
#validador de imagem
#db.empresa.logo.requires = IS_IMAGE(extensions=('jpeg','png','jpg'), maxsize=(1200, 800))
#validador de formatação de data
db.empresa.data_bloqueio.requires = IS_DATE(format=('%d-%m-%Y'))
db.empresa.data_desaceleracao.requires = IS_DATE(format=('%d-%m-%Y'))
#validadores de contato
db.empresa.celular.requires = IS_MATCH('^\(?\d{2}\)?\d{5}\-?\d{4}$', error_message='Formato (00)00000-0000'),
db.empresa.telefone.requires = IS_MATCH('^\(?\d{2}\)?\d{4}\-?\d{4}$', error_message='Formato (00)0000-0000'),
#validadores de endereco
db.empresa.uf.requires=IS_IN_SET(['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF'])
db.empresa.cep.requires = IS_MATCH('^\d{5}\-?\d{3}$', error_message='Formato 63000-000'),
#validador de email
db.empresa.email.requires = IS_EMAIL(error_message='Email Invalido!')

#usuario da empresa
db.usuario_empresa.tipo.requires = IS_IN_SET(['Usuario','Administrador','Proprietário'])

#validadores dos clientes
db.pessoa.razaosocial_nome.requires=[IS_UPPER(),IS_LENGTH(minsize=8, error_message='Nome muito pequeno')]
#validadores de contato
db.pessoa.telefone.requires = IS_MATCH('^\(?\d{2}\)?\d{4}\-?\d{4}$', error_message='Formato (00)0000-0000'),
db.pessoa.celular.requires = IS_MATCH('^\(?\d{2}\)?\d{5}\-?\d{4}$', error_message='Formato (00)0000-0000'),
#validadores de dados pessoais
db.pessoa.cpf.requires  = IS_MATCH('^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}|\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}$', error_message='cpf - 000.000.000-00 ou cnpj 00.000.000/0001-00'),
db.pessoa.org_espedidor_cpf.requires = IS_UPPER()
db.pessoa.org_espedidor_rg.requires = IS_UPPER()

db.pessoa.tipo.requires = IS_IN_SET(['Física','Jurídica'])
db.pessoa.sexo.requires = IS_IN_SET(['M','F'])
db.pessoa.estado_civil.requires = IS_IN_SET(['Solteiro(a)','Casado(a)'])

#validadores de endereço
db.pessoa.uf.requires=IS_IN_SET(['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF'])
db.pessoa.cep.requires = IS_MATCH('^\d{5}\-?\d{3}$', error_message='Formato 63000-000'),
#validador de email
db.pessoa.email.requires = IS_EMAIL(error_message='Email Invalido!')



#validadores dos imoveis
db.imovel.tipo.requires=IS_IN_SET(['Comercial', 'Residencial'])
db.imovel.subtipo.requires=IS_IN_SET(['Apartamento', 'Duplex', 'Casa', 'Chácara', 'Flat', 'Galpão', 'Kitnet', 'Prédio', 'Terreno'])

#validadores de endereço
db.imovel.uf.requires=IS_IN_SET(['RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL','SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF'])
db.imovel.cep.requires = IS_MATCH('^\d{5}\-?\d{3}$', error_message='Formato 63000-000'),
#validadores de estado
db.imovel.status.requires = IS_IN_SET(['Disponivel','Ocupado','Resenvado','Deletado'])



###validadores do contrato de locação
db.contrato_aluguel.virgencia_meses.requires=IS_IN_SET([6,12,24,36,48,60,120])
#validadores de datas
db.contrato_aluguel.data_inicial.requires = IS_DATE(format=('%d-%m-%Y'))
db.contrato_aluguel.data_final.requires = IS_DATE(format=('%d-%m-%Y'))
db.contrato_aluguel.data_contrato.requires = IS_DATE(format=('%d-%m-%Y'))
#validadores de estado
db.contrato_aluguel.tipo.requires=IS_IN_SET(['Comercial', 'Residencial'])
db.contrato_aluguel.status.requires=IS_IN_SET(['Ativo', 'Finalizado', 'Concelado'])

###validadores recebimento dos contratos
db.recebimento_contrato.data_vencimento.requires = IS_DATE(format=('%d-%m-%Y'))
db.recebimento_contrato.data_recebimento.requires = IS_DATE(format=('%d-%m-%Y'))
db.recebimento_contrato.tipo.requires = IS_IN_SET(['Dinheiro','Cheque','Boleto','Cartão','Trensferência','Pix'])
db.recebimento_contrato.status.requires = IS_IN_SET(['Aguardando','Quitado','Atrasado','Cancelado'])

###validadores de despesas
#validadores das despesas da empresa e imovel
db.despesa_imovel.data_ocorrencia.requires = IS_DATE(format=('%d-%m-%Y'))
db.despesa_empresa.data_ocorrencia.requires = IS_DATE(format=('%d-%m-%Y'))
