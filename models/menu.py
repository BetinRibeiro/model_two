# -*- coding: utf-8 -*-
# Menu 
# ----------------------------------------------------------------------------------------------------------------------
if "0424" in auth.user.first_name:
    
    response.menu = [
    (T('Cabeçalho'), False, URL('acs_administrativo', 'cabecalho'), []),
    (T('Artigos'), False, '#', [
                (T('Postagem01'), False, URL('acs_administrativo', 'post01'), []),
                (T('Postagem02'), False, URL('acs_administrativo', 'post02'), []),
        ]),
    (T('Vantagens'), False, '#', [
                (T('Vantagem01'), False, URL('acs_administrativo', 'van01'), []),
                (T('Vantagem02'), False, URL('acs_administrativo', 'van02'), []),
                (T('Vantagem03'), False, URL('acs_administrativo', 'van03'), []),
        ]),
    (T('Equipe'), False, '#', [
                (T('Servidor01'), False, URL('acs_administrativo', 'serv01'), []),
                (T('Servidor02'), False, URL('acs_administrativo', 'serv02'), []),
                (T('Servidor03'), False, URL('acs_administrativo', 'serv03'), []),
                (T('Servidor04'), False, URL('acs_administrativo', 'serv04'), []),
        ]),
]
else:
    if auth.user:
        response.menu = [
        (T('Home'), False, URL('acs_sistema', 'index'), []),
        (T('Clientes'), False, URL('acs_clientes', 'index'), []),
        (T('Imóveis'), False, URL('acs_imoveis', 'index'), []),
        (T('Recebimentos'), False, URL('acs_recebimentos', 'index'), [])
    ]
    else:
        response.menu = [
        (T('Home'), False, URL('default', 'index'), [])
    ]
