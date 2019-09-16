def number_of_cores():
    import multiprocessing as mp
    return mp.cpu_count()


def time_of_deployment():
    import psutil, os, time
    pid = os.getpid()
    p = psutil.Process(pid)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))
    return timestamp


def is_service_running(service):
    import os
    cmd = 'service {0} status'.format(service)
    stat = os.system(cmd)
    if stat == 0:
        msg = 'running'
    elif stat == 768:
        msg = 'stopped'
    else:
        msg = 'unavailable'
    return msg
