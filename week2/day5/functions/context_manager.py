from datetime import datetime

class Timer:
    time : datetime

    def __enter__(self):
        self.time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        tracked_time = datetime.now() - self.time
        print(f"It took {tracked_time} to finish")