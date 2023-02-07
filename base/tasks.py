from celery import shared_task


@shared_task(bind=True)
def test_func(self, x, y):
    # print(f"Request: {self.request!r}")
    # print(f"X: {x}, Y: {y}")
    # return x + y
    for i in range(10):
        print(i)
    return "Done"
