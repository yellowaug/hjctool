import wmi
import datetime
class Comp_info(object):
    def __init__(self):
        self.com_p=wmi.WMI()
    def sys_name(self):
        system_name=[]
        s_name=self.com_p.Win32_Processor()
        for name in s_name:
            sys_name=name.SystemName #获取计算机系统名称
            system_name.append(sys_name)
        return system_name
    def cpu_info(self):
        cpu_infor_list=[]
        infos =self.com_p.Win32_Processor()
        for cpu in infos:
            c_name=cpu.Name
            # b=cpu.ProcessorId.strip() #打印当前进程数
            # sys_name=cpu.SystemName #获取计算机系统名称
            core_n=cpu.NumberOfCores
            # e=cpu.MaxClockSpeed
            # cpu_infor_list.append(sys_name)
            cpu_infor_list.append(c_name)
            cpu_infor_list.append(core_n)
        return cpu_infor_list
    def main_board(self):
        board_info_list=[]
        infos=self.com_p.WIN32_BaseBoard()
        for board in infos:
            b_name=board.Manufacturer #厂家
            b_product=board.Product #型号
            board_info_list.append(b_name)
            board_info_list.append(b_product)
            # print(b_name,b_product)
        return board_info_list
    def disk_info(self):
        disk_info_list=[]
        infos=self.com_p.Win32_DiskDrive()
        print(infos)
        # print(infos)
        for info_list in infos:
            disk_name=info_list.Model #获取硬盘名称
            disk_type=info_list.InterfaceType #获取硬盘接口类型
            disk_par=info_list.Partitions #获取硬盘分区数
            disk_size=int(info_list.Size)/(1024*1024*1024) #获取硬盘大小
            # disk_sysname=info_list.SystemName #获取计算机系统名称
            # disk_size=info_list.Size
            # print(info_list)
            # disk_info_list.append(disk_sysname)
            disk_info_list.append(disk_name)
            disk_info_list.append(disk_type)
            disk_info_list.append(disk_par)
            disk_info_list.append(int(disk_size))
            # print(disk_name,disk_type,disk_par,int(disk_size))
        return disk_info_list
    def mem_info(self):
        mem_infos=[]
        infos=self.com_p.Win32_PhysicalMemory()
        for info_list in infos:
            mem_name=info_list.Name
            mem_size=info_list.Capacity
            temp_size=int(mem_size)/(1024*1024*1024)
            mem_speed=info_list.Speed
            mem_infos.append(mem_name)
            mem_infos.append(str(temp_size))
            mem_infos.append(mem_speed)
            # print(info_list)
        return mem_infos
    def upload_time(self):
        time_info=[]
        datetime.datetime.now()
        timeformat = "%Y-%m-%d %H:%M:%S"
        upload_time = datetime.datetime.now().strftime(timeformat)
        time_info.append(upload_time)
        return time_info
#
a=Comp_info()
# s1=a.cpu_info()
# s2=a.main_board()
s3=a.disk_info()
# s4=a.mem_info()
print(s3)
# print(s1,s2,s3,s4)