import tkinter as tk
from hjctool import setip
from hjctool import instersql
from hjctool import get_ip
from hjctool import reset
from hjctool import check_net
from hjctool import check_sql
import sql_ctr
import computer_info
import wmi
import pymysql
import datetime
win = tk.Tk()
win.title("华景城电脑信息采集工具")
win.geometry("280x300")
# button = tk.Button(text="取消",width=8,height=1)
# button.place(x=180,y=135,anchor="nw")
label_list = ["姓名","房间号","OA账号"]
for i in range(3):
    label = tk.Label(win,text=label_list[i],height=1)
    label.grid(row=i,padx=10,pady=10)
entry_name=tk.Entry(win,width=20)
entry_name.place(x=90,y=15,anchor="nw")
var = tk.StringVar()
#定义按钮的功能
def insert_sql():
    global var
    var_name = entry_name.get()
    var_room = entry_room.get()
    var_class = entry_class.get()
    stat_code = check_net()
    try:
        if stat_code == 1:
            # var.set("局域网连接正常")
            sql_code = check_sql()
            if sql_code == 0:
                ip_info = get_ip()
                instersql(ip_info,var_name,var_room,var_class)
                setinfo = setip()
                for info_item in setinfo:
                    print(info_item)
                var.set("本机IP地址信息登记成功")
                print("本机IP地址信息登记成功")
            else:
                var.set ("数据已存在，请勿重复录入")
                print("数据已存在，请勿重复录入")
        else:
            var.set("请联系网管处理问题")
    except Exception as e:
        var.set("IP设置异常，请联系网管")
        print("IP设置异常，请联系网管",e)
def reset_ip():
    global var
    stat_code = check_net()
    if stat_code == 1:
        reset()
        var.set("IP地址恢复成功")
    else:
        var.set("请联系网管处理问题")
def up_load():
    cp_info = computer_info.Comp_info()
    s_name = cp_info.sys_name()
    cpu_infos = cp_info.cpu_info()
    board_infos = cp_info.main_board()
    disk_infos = cp_info.disk_info()
    mem_infos = cp_info.mem_info()
    u_time=cp_info.upload_time()
    temp_sname = str(s_name)
    temp_cpuinfos = str(cpu_infos)
    temp_boardinfos = str(board_infos)
    temp_diskinfos = str(disk_infos)
    temp_meminfos = str(mem_infos)
    temp_time=str(u_time)
    sql_c = sql_ctr.Sql_manager()
    try:
        print("正在采集数据，并上传服务器,请等待。。。")
        var.set("正在采集数据，并上传服务器,请等待。。。")
        sql_c.ins_computer_info_sql(temp_sname, temp_cpuinfos, temp_boardinfos, temp_diskinfos, temp_meminfos,upload_time=temp_time)
        print("完成数据写入服务器数据库")
        var.set("信息采集完成，\n数据成功写入服务器数据库")
    except Exception as e:
        print(e)
    print(s_name)
    print(cpu_infos)
    print(board_infos)
    print(disk_infos)
    print(mem_infos)

#输入框模块程序
meassge = tk.Label(win,textvariable=var,font=('Arial', 10),width=30,height=5)
meassge.place(x=5,y=200,anchor="nw")
entry_room=tk.Entry(win,width=20)
entry_room.place(x=90,y=55,anchor="nw")
entry_class=tk.Entry(win,width=20)
entry_class.place(x=90,y=95,anchor="nw")
#按钮模块程序
button_set = tk.Button(text="登记",width=8,height=1,command=insert_sql)
button_set.place(x=20,y=135,anchor="nw")
button = tk.Button(text="恢复IP",width=8,height=1,command=reset_ip)
button.place(x=100,y=135,anchor="nw")
button = tk.Button(text="上传硬件信息",width=10,height=1,command=up_load)
button.place(x=180,y=135,anchor="nw")

win.mainloop()

