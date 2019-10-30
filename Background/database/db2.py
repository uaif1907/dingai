from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.exc import DisconnectionError
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

ssh_host = "39.108.113.110"  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
ssh_user = ""  # 这是你在堡垒机上的用户名
ssh_password = ""  # 这是你在堡垒机上的用户密码
mysql_host = "127.0.0.1"  # 这是你mysql服务器的主机名或ip地址
mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
mysql_user = ""  # 这是你mysql数据库上的用户名
mysql_password = ""  # 这是你mysql数据库的密码
mysql_db = "" # mysql服务器上的数据库名

def checkout_listener(dbapi_con, con_record, con_proxy):
    try:
        try:
            dbapi_con.ping(False)
        except TypeError:
            dbapi_con.ping()
    except dbapi_con.OperationalError as exc:
        if exc.args[0] in (2006, 2013, 2014, 2045, 2055):
            raise DisconnectionError()
        else:
            raise


with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)
) as server:
    server.start()  # ssh通道服务启动
    local_port = str(server.local_bind_port)
    engine = create_engine(
        'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(mysql_user, mysql_password, '127.0.0.1', local_port,
                                                             mysql_db),
        pool_size=100,
        pool_recycle=3600)

    event.listen(engine, 'checkout', checkout_listener)  # 防止报连接池相关的错误
    Base.metadata.create_all(engine)  # 检测文件中所有继承了Base类的类,在mysqld中建立所有的表,类就是表
    Session = sessionmaker(bind=engine)
    session = Session()