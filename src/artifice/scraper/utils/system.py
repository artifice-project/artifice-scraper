def number_of_cores():
    import multiprocessing as mp
    return mp.cpu_count()


def time_of_deployment():
    import psutil, os, time
    pid = os.getpid()
    p = psutil.Process(pid)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time()))
    return timestamp
