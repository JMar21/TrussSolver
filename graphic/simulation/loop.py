import time

def main_loop(update_fn,redraw_fn,should_continue_fn,frame_rate=0.03):
    frame=1
    time_s=0
    last_elapsed = frame_rate
    while should_continue_fn(frame, time_s):
        update_start = time.time()
        update_fn(last_elapsed, time_s, frame)
        redraw_fn()
        update_end = time.time()
        elapsed = update_end - update_start
        remaining_time = frame_rate - elapsed
        if remaining_time > 0:
            time.sleep(remaining_time)
            last_elapsed = frame_rate
        else:
            last_elapsed = frame_rate

        frame +=1
        time_s += last_elapsed