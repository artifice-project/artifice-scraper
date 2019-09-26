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


def disk_space_percent(path='/'):
    '''
    Returns the amount of USED DISK SPACE on the given path.
    Value is returned as a percentage, rounded to 1 decimal.
    '''
    import os
    statvfs = os.statvfs(path)
    total = statvfs.f_frsize * statvfs.f_blocks     # Size of filesystem in bytes
    actual = statvfs.f_frsize * statvfs.f_bfree     # Actual number of free bytes
    avail = statvfs.f_frsize * statvfs.f_bavail     # Number of free bytes that ordinary users
                                                    # are allowed to use (excl. reserved space)
    used = (total - avail) / total
    as_percent = round(used * 100, 1)
    return as_percent
