import psutil
import sched
import time
import datetime
import csv
import os

s = sched.scheduler(time.time, time.sleep)
directory = raw_input("Enter output CSV directory:  \n")
print 'Thanks for entering the output directory, which is {} \n'.format(directory)

interval = raw_input('Enter interval in seconds:')
interval = float(interval)
print 'Thanks for entering the interval, which is {} \n'.format(interval)

namer = os.path.join(directory, 'resource_monitor.csv')
header_list = ['Time', 'Total Memory (byte)', 'Available Memory (byte)', 'Memory Used (%)', 'Used Memory (byte)', 'Free Memory (byte)', 'CPU Usage (%)', 'IO Read','IO Write','IO Read (byte)', 'IO Write (byte)', 'IO Read Time','IO Write Time']
with open(namer, 'a') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(header_list)


def resource_monitor(sc):
    print "Gathering Stats..."

    current_time = datetime.datetime.now().time()
    print 'Current Time {}'.format(current_time)

    cpu_list = []
    cpu_percent = psutil.cpu_percent()
    string_cpu_percent = str(cpu_percent)

    cpu_list.append(string_cpu_percent)
    print 'Current CPU Usage {}% '.format(cpu_percent)

    io_data = psutil.disk_io_counters(perdisk=False)
    io_data_string = str(io_data)
    io_list = io_data_string.split(',')

    mem_usage = psutil.virtual_memory()
    string_mem_usage = str(mem_usage)
    mem_list= [current_time]

    mem_split = string_mem_usage.split(',')
    for x in mem_split:
        if '.' in x:
            no_period = x[-2:]
            mem_list.append(no_period)
        else:
            new_x = int(filter(str.isdigit, x))
            mem_list.append(new_x)

    mem_list.append(string_cpu_percent)

    for y in io_list:
        new_y = int(filter(str.isdigit, y))
        mem_list.append(new_y)

    print 'Current MEM Usage {} '.format(string_mem_usage)
    print 'Current IO Usage {} \n'.format(io_data_string)

    with open(namer, 'a') as myfile:
        wr = csv.writer(myfile)

        wr.writerow(mem_list)

    s.enter(interval, 1, resource_monitor, (sc,))

s.enter(interval, 1, resource_monitor, (s,))
s.run()
