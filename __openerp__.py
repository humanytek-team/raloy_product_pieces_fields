# -*- coding: utf-8 -*-
{
    'name': 'Piezas por tarima y presentacion en productos',
    'version': '1.1',
    'summary': 'En el producto se agregan los campos "Piezas por tarima" y "Piezas por presentacion", en las lineas de albaranes aparece el campo descriptivo "Categoria interna del producto" y el campo "Unidad de almacenamiento (UdA)".',
    'category': 'Raloy',
    'description': """
    En el producto se agregan los campos "Piezas por tarima" y "Piezas por presentacion", en las lineas de albaranes aparece el campo descriptivo "Categoria interna del producto" y el campo "Unidad de almacenamiento (UdA)".
    """,
    'author': 'Humanytek',
    'website': 'http://www.humanytek.com',
    'depends': ['product','stock'],
    'data': [
        'product_template_view.xml',
        'stock_picking_view.xml',
        'stock_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: