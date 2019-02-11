import os
import datetime

def create_file(self,path,file_name,file_time):
    if os.path.exists("%s\%s" % (path, file_name)) == False:#判断文件是否存在
        os.chdir(path)
        os.mkdir(file_name)
        os.chdir("%s\%s" % (path, file_name))
        os.mkdir(file_time)
    else:
        os.chdir("%s\%s" % (path, file_name))
        os.mkdir(file_time)
    file_path = os.chdir("%s\%s\%s" % (path, file_name, file_time))#切换到子目录
    return file_path
def sql_shell(self,databases,sql_file_name):#sql语句
    sql_common = "mysqldump -uroot -pzzq %s > %s"%(databases,sql_file_name)
    os.system(sql_common)
    #判断mysql备份是否存在
    if os.path.exists(sql_file_name) == True:
        print("databases blackup seccessed")
    else:
        print("databases blackup unseccess")
    file_size = os.path.getsize(sql_file_name)
    file_size_mb = str(round(file_size / float(1024 * 1024), 2))
