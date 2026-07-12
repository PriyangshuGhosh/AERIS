import time

SERVER_START_TIME = time.time()

REQUEST_COUNT = 0

TOTAL_LATENCY = 0.0


def record_request(latency):

    global REQUEST_COUNT
    global TOTAL_LATENCY

    REQUEST_COUNT += 1
    TOTAL_LATENCY += latency


def uptime():

    seconds = int(time.time() - SERVER_START_TIME)

    h = seconds // 3600

    m = (seconds % 3600) // 60

    s = seconds % 60

    return f"{h:02}:{m:02}:{s:02}"


def average_latency():

    if REQUEST_COUNT == 0:
        return 0

    return round(TOTAL_LATENCY / REQUEST_COUNT, 3)