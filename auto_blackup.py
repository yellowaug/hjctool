# import os
# import datetime
# import psutil
# # time_format = '%Y-%m-%d %H-%M-%S'
# # sys_time = datetime.datetime.now().strftime(time_format)
# # print(sys_time)
# # path = r'e:\databases_backup'
# # mysql_key = 'zzq'
# # if os.path.exists('%s'%path) == False:#判断e:\databases_backup是否存在
# #     os.mkdir('%s'%path)
# #     os.chdir('%s'%path)
# #     os.mkdir('%sdabases'%sys_time)
# # else:
# #     os.chdir('%s'%path)
# #     a = os.mkdir('%sdabases'%sys_time)
# # os.chdir(r'%s\%sdabases'%(path,sys_time))
# # sys_path = os.getcwd()
# # print(sys_path)
# # os.system(r'mysqldump -uroot -p%s mysql > backup.sql'%mysql_key)

from datetime import datetime
import os
file_time =  datetime.now().strftime("%Y-%m-%d %H-%M-%S")
path = "e:"
flie_name = "blackup_sql"
sql_common = "mysqldump -uroot -pzzq mysql > databases_blackup.sql"
# key = 'zzq'
# #判断文件是否存在，若文件存在则继续，直到该文件夹下不包含该文件名
# while True==os.path.exists(str):
#     str = str + datetime.now().strftime("%Y%m%d_%H%M%S")
# os.makedirs(str)#创建文件夹
# sys_path = os.chdir(os.getcwd()+'\%s'%str)#进入新建立的文件夹内

if os.path.exists("%s\%s"%(path,flie_name)) == False:
    os.chdir(path)
    os.mkdir(flie_name)
    os.chdir("%s\%s"%(path,flie_name))
    os.mkdir(file_time)
else:
    os.chdir("%s\%s"%(path,flie_name))
    os.mkdir(file_time)
os.chdir("%s\%s\%s"%(path,flie_name,file_time))
print(os.getcwd())
os.system(sql_common)
if os.path.exists("databases_blackup.sql") == True:
    print("databases blackup seccessed")
else:
    print("databases blackup unseccess")
file_size = os.path.getsize("databases_blackup.sql")
file_size_mb = str(round(file_size/float(1024*1024),2))
with open("black_sql_logs.txt","a") as f:
    f.write(" sql blackup success "+" create_time:"+file_time+" size:"+file_size_mb+"MB"+"\n")
    f.close()