import time
def measure_latency(function, *args,**kwargs):
    start_time = time.perf_counter()
    result = function(*args,**kwargs)
    end_time = time.perf_counter()
    latency = end_time - start_time
    return {
        "result":result,
        "latency_seconds":latency
    }
