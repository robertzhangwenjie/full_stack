import pymysql
# 告诉django用pymysql来代替默认的MySQLdb(只支持python2)
pymysql.install_as_MySQLdb()