import subprocess
from common_python_logic import open_read_file_box
from dbConnectionPool import get_connection, release_connection
import pandas as pd


def start_process_script_to_servers(process_to = 'all'):
    conn = None
    cursor = None

    try:
        # pending connect vpn


        file_path = 'resources/query_runner.sql'

        # Step 1: Read the .sql file
        with open(file_path, 'r') as file:
            sql_query = file.read()

        # data base list
        connection_db = {
            'all':[
                ('dev','project 1'),
                ('dev', 'project 2'),
                ('dev', 'project 3'),
                ('prod','project 1'),
                ('prod', 'project 2'),
                ('prod', 'project 3')
            ]
        }

        # connect db
        db_list = connection_db.get(process_to, process_to)
        print("db_list ::: ",db_list)

        list_of_conn_pool = []

        for server, db in db_list:
            # print("server, db ::: ",server, db)
            
            # read database config
            config = open_read_file_box( db+'_postgres', server)
            print("config :: ",config)

            conn = get_connection(config)
            cursor = conn.cursor()

            # process query and fetch or migrate only that query read sql file.

            # Execute the query
            cursor.execute(sql_query)

            # fetch if that are select query
            # data = cursor.fetchall()
            # print("data ::: ", len(data))
 
            # commit the changes
            conn.commit()

            list_of_conn_pool.append((config, conn, cursor))

    except Exception as e:
        print("----------->",e)

    finally:
        for server_config, conn, cursor in list_of_conn_pool:
            if cursor:
                cursor.close()
            if conn:
                release_connection(server_config, conn)

start_process_script_to_servers()