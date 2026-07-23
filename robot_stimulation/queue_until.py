import queue

def put_last(q:queue.Queue,data,max_size:int):
    while q.qsize()>=max_size:
        try:
            q.get_nowait()
        except queue.Empty:
            break
    q.put(data)