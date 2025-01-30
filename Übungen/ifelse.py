cpus = cpuinfo.get_cpu_info()["count"]

minimumCpu = 4
optimumCpu = 8

if cpus >= minimumCpu and cpus >= optimumCpu:
    print("You have minimum and optimum C")