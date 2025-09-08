import psycopg2.pool


# Global dictionary to store pools based on a config key
connection_pools = {}

def get_pool(server_config):
    key = f"{server_config['db_host']}:{server_config['db_port']}/{server_config['db_name']}"

    if key not in connection_pools:
        connection_pools[key] = psycopg2.pool.ThreadedConnectionPool(
            minconn=server_config['min_conn'],
            maxconn=server_config['max_conn'],
            user=server_config["db_user"],
            password=server_config["db_password"],
            host=server_config["db_host"],
            port=server_config["db_port"],
            database=server_config["db_name"]
        )
    return connection_pools[key]



def get_connection(server=None):
    pool = None

    if server:
        pool = get_pool(server)

    """Get a connection from the pool."""

    print("get connection pool")
    return pool.getconn()


def release_connection(server, conn):

    pool = None

    if server:
        pool = get_pool(server)

    """Release a connection back to the pool."""
    pool.putconn(conn)

    print("release connection")


def close_pool(server):
    key = f"{server['db_host']}:{server['db_port']}/{server['db_name']}"
    if key in connection_pools:
        connection_pools[key].closeall()
        del connection_pools[key]

    print("close pool")