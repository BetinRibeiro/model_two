# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields['auth_user'] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

db.define_table('empresa',
                #proprietario é o proprio criador
                Field('proprietario','reference auth_user', label='Proprietario', writable=False, readable=False, default=1),
                #definir em validadores que é uma imagem
                Field('logo', 'upload', label='Logo Empresa'),
                #dados empresariais
                Field('razaosocial', 'string', label='Razão Social',requires = IS_UPPER()),
                Field('nomefantasia', 'string', label='Nome Fantasia',requires = IS_UPPER()),
                Field('cnpj', 'string', label='CNPJ',default="00.000.000/0001-00"),
                Field('inscricaoestarual', 'string', label='Insc. Est',default="00000"),
                Field('inscricaomunicipal', 'string', label='Insc. Mun',default="00000"),
                Field('crt', 'string', label='CRT',default="00000"),
                #endereço
                Field('cep', 'string', label='CEP',default="60000-000"),
                Field('lougradouro', 'string', label='Lougradouro',default="Rua",requires = IS_UPPER()),
                Field('numero', 'string', label='Numero',default="0",requires = IS_UPPER()),
                Field('bairro', 'string', label='Bairro',default="Centro",requires = IS_UPPER()),
                Field('uf', 'string', label='UF',default="CE",requires = IS_UPPER()),
                Field('cidade', 'string', label='Cidade', default='Juazeiro do Norte',requires = IS_UPPER()),
                Field('complemento', 'string', label='Complemento',default="Sem Complemento",requires = IS_UPPER()),
                #contato
                Field('email', 'string', label='Email',default="sem@email.com"),
                Field('telefone', 'string', label='Telefone',default="(88)3500-0000"),
                Field('celular', 'string', label='Celular',default="(88)99000-0000"),
                #inteiros vindos de outras tabelas
                Field('q_clientes', 'integer', label='Q Clientes', writable=False, readable=False, default=0),
                Field('q_imoveis', 'integer', label='Q Imoveis', writable=False, readable=False, default=0),
                Field('q_contratos', 'integer', label='Q Contratos', writable=False, readable=False, default=0),
                Field('q_parcelas_total', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_pagas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_atrasadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_aguardadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                #Valores vindos de outras tabelas
                Field('valor_total', 'double', label='Total Valor', writable=False, readable=False, notnull=True, default=0),
                Field('valor_recebido', 'double', label='Total Recebido', writable=False, readable=False, notnull=True, default=0),
                Field('valor_debito', 'double', label='Total Debito', writable=False, readable=False, notnull=True, default=0),
                Field('valor_aguardando', 'double', label='Total Aguardando', writable=False, readable=False, notnull=True, default=0),
                Field('valor_desp_empresa', 'double', label='Total Desp', writable=False, readable=False, notnull=True, default=0),
                Field('valor_desp_imovel', 'double', label='Total Desp Imovel', writable=False, readable=False, notnull=True, default=0),
                #controle gerancial do desenvolvedor
                Field('limite_cliente', 'integer', label='Limite Cliente', writable=False, readable=False, default=100),
                Field('limite_imoveis', 'integer', label='Limite Imoveis', writable=False, readable=False, default=100),
                Field('limite_logins', 'integer', label='Limite Login', writable=False, readable=False, default=4),
                Field('limite_contratos', 'integer', label='Limite Contratos', writable=False, readable=False, default=100),
                Field('limite_parcelas', 'integer', label='Limite Parcelas', writable=False, readable=False, default=2400),
                #informações extras do desenvolvedor
                Field('data_desaceleracao', 'date', label="Desaceleração", writable=False, readable=False, default=request.now, notnull=True),
                Field('data_bloqueio', 'date', label="Data Bloqueio", writable=False, readable=False, default=request.now, notnull=True),
                Field('ativo', 'boolean', writable=False, readable=False, default=True),
                auth.signature,
                format='%(nomefantasia)s')

db.define_table('usuario_empresa',
                Field('usuario','reference auth_user', writable=False, readable=False, label='Usuario'),
                Field('empresa','reference empresa', writable=False, readable=False, label='Empresa'),
                Field('nome', 'string', label='Nome',requires = IS_UPPER()),
                Field('tipo', 'string', label='tipo',default='Administrador'),
                Field('ativo', 'boolean', writable=False, readable=False, default=True),
                format='%(nome)s')

#no cadastro fisico ou juridico definido no inicio
db.define_table('pessoa',
                Field('empresa','reference empresa', label='empresa', writable=False, readable=False),
                Field('representante','reference usuario_empresa', label='Representante', writable=False, readable=False),
                Field('tipo', 'string', label='Tipo', writable=False, readable=False, default='Física'),
                Field('razaosocial_nome', 'string', label='RS/NC',notnull=True,requires = IS_UPPER()),
                Field('sexo', 'string', label='Sexo', default='M',notnull=True, writable=False, readable=False ,requires = IS_UPPER()),
                Field('estado_civil', 'string', label='Est. Civil',notnull=True , writable=False, readable=False, default='Solteiro(a)'),
                Field('apelido_nome_fantasia', 'string', label='AP/NF', writable=True, readable=True,requires = IS_UPPER()),
                Field('cpf', 'string', label='CPF/CNPJ',notnull=True ),
                Field('org_espedidor_cpf', 'string', default='SSP', writable=True, readable=True,notnull=True , label='org esp.'),
                Field('rg', 'string', label='RG',notnull=True ),
                Field('org_espedidor_rg', 'string', default='SSP', writable=True, readable=True,notnull=True , label='org esp.'),
                #endereço
                Field('cep', 'string', label='CEP', default='63050-000'),
                Field('lougradouro', 'string', label='Lougradouro'),
                Field('numero', 'string', label='Numero',requires = IS_UPPER()),
                Field('bairro', 'string', default='Centro', label='Bairro'),
                Field('uf', 'string', label='UF', default='CE',requires = IS_UPPER()),
                Field('cidade', 'string', label='Cidade', default='Juazeiro do Norte'),
                Field('complemento', 'string', label='Complemento'),
                #dados pessoais
                Field('email', 'string', label='Email', default='sem@email.com'),
                Field('telefone', 'string', label='Telefone', default='(88)3555-5555'),
                Field('celular', 'string',notnull=True , default='(88)98888-8888', label='Celular'),
                #inteiros vindos de outras tabelas
                Field('q_contratos', 'integer', label='Q Contratos', writable=False, readable=False, default=0),
                Field('q_parcelas_total', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_pagas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_atrasadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_aguardadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                 #Valores vindos de outras tabelas
                Field('valor_total', 'double', label='Total Valor', writable=False, readable=False, notnull=True, default=0),
                Field('valor_recebido', 'double', label='Total Recebido', writable=False, readable=False, notnull=True, default=0),
                Field('valor_debito', 'double', label='Total Debito', writable=False, readable=False, notnull=True, default=0),
                Field('valor_aguardando', 'double', label='Total Aguardando', writable=False, readable=False, notnull=True, default=0),
                #para tipos de bloqueios e conferencia
                Field('ativo', 'boolean', writable=False, readable=False, default=True),
                Field('conferido', 'boolean', writable=False, readable=False, default=False),
                auth.signature,
                format='%(razaosocial_nome)s')

db.define_table('imovel',
                Field('empresa','reference empresa', label='empresa', writable=False, readable=False),
                Field('proprietario','reference pessoa', label='Proprietario', writable=False, readable=False),
                #classificação
                Field('tipo', 'string', default='Residencial'),
                Field('subtipo', 'string', default='Casa'),
                #endereço
                Field('cep', 'string', label='CEP', default='63050-000'),
                Field('lougradouro', 'string', label='Lougradouro',requires = IS_UPPER()),
                Field('numero', 'string', label='Numero',requires = IS_UPPER()),
                Field('bairro', 'string', default='Centro', label='Bairro',requires = IS_UPPER()),
                Field('uf', 'string', label='UF', default='CE',requires = IS_UPPER()),
                Field('cidade', 'string', label='Cidade', default='Juazeiro do Norte',requires = IS_UPPER()),
                Field('complemento', 'string', label='Complemento',requires = IS_UPPER()),
                Field('status', 'string',default='Disponivel', writable=False, readable=False),
                #dados de valorização do imovel
                Field('preco', 'double',label="Preço", notnull=True, writable=False, readable=False, default=0),
                #inteiros vindos de outras tabelas
                Field('q_contratos', 'integer', label='Q Contratos', writable=False, readable=False, default=0),
                Field('q_parcelas_total', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_pagas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_atrasadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                Field('q_parcelas_aguardadas', 'integer', label='Q Parcelas', writable=False, readable=False, default=0),
                 #Valores vindos de outras tabelas
                Field('valor_total', 'double', label='Total Valor', writable=False, readable=False, notnull=True, default=0),
                Field('valor_recebido', 'double', label='Total Recebido', writable=False, readable=False, notnull=True, default=0),
                Field('valor_debito', 'double', label='Total Debito', writable=False, readable=False, notnull=True, default=0),
                Field('valor_aguardando', 'double', label='Total Aguardando', writable=False, readable=False, notnull=True, default=0),
                Field('valor_desp_total', 'double',label="Despesa Total", notnull=True, writable=False, readable=False, default=0),
                Field('disponivel', 'boolean', writable=False, readable=False, default=True),
                Field('conferido', 'boolean', writable=False, readable=False, default=False),
                auth.signature,
                format='%(subtipo)s %(lougradouro)s  %(numero)s')

db.define_table('despesa_empresa',
                Field('empresa','reference empresa', writable=False, readable=False, label='Empresa'),
                Field('data_ocorrencia', 'date', label="Data", readable=True, writable=True, default=request.now, notnull=True),
                Field('descricao', 'string',label='Descrição', writable=True, readable=True),
                Field('valor', 'double', label='Valor', notnull=True, default=0),
                Field('conferido', 'boolean', writable=False, readable=False, default=False),
                auth.signature,
                format='%(descricao)s')
