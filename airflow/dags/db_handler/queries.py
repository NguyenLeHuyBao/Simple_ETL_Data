class PostgresStatements:
    # Make sure list queries and list_columns correspond with list tables
    # list_tables = ['users', 'orders', 'transactions', 'menus']
    list_tables = ['users']
    list_queries = [
        'SELECT user_id, name, email, mobile FROM public.users',
        'SELECT order_id, item_id, num, price FROM public.orders',
        'SELECT user_id, order_id, paid_price, status FROM public.transactions',
        'SELECT item_id, name, price FROM public.menus'
    ]
    list_columns = [
        ['user_id', 'name', 'email', 'mobile'],
        ['order_id', 'item_id', 'num', 'price'],
        ['user_id', 'order_id', 'paid_ price', 'status'],
        ['item_id', 'name', 'price']
    ]


class MysqlStatements:
    # Make sure list queries and list_columns correspond with list tables
    # list_tables = ['users', 'orders', 'transactions', 'menus']
    list_tables = ['users']
    list_queries = [
        'SELECT user_id, name, email, mobile FROM report.users',
        'SELECT order_id, item_id, num, price FROM report.orders',
        'SELECT user_id, order_id, paid_price, status FROM report.transactions',
        'SELECT item_id, name, price FROM report.menus'
    ]
    list_columns = [
        ['user_id', 'name', 'email', 'mobile'],
        ['order_id', 'item_id', 'num', 'price'],
        ['user_id', 'order_id', 'paid_ price', 'status'],
        ['item_id', 'name', 'price']
    ]
