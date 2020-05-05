# from original post at : https://stackoverflow.com/questions/21903411/enable-python-to-connect-to-mysql-via-ssh-tunnelling

import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser

home = expanduser("~")
pkeyfilepath = "/home/vipul/.ssh/id_rsa"
mypkey = paramiko.RSAKey.from_private_key_file(pkeyfilepath)


sql_hostname = ""
sql_username = ""
sql_password = ""
sql_main_database = ""
sql_port = 3306
ssh_host = ""
ssh_user = ""
ssh_port = 22
sql_ip = ""

with SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_pkey=mypkey,
    remote_bind_address=(sql_hostname, sql_port),
) as tunnel:
    conn = pymysql.connect(
        host="127.0.0.1",
        user=sql_username,
        passwd=sql_password,
        db=sql_main_database,
        port=tunnel.local_bind_port,
    )
    query = """SELECT VERSION();"""

    data = pd.read_sql_query(query, conn)
    print(data)
    conn.close()
