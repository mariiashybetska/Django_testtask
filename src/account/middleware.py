import time

from account.models import Logger

'''
Create middleware that stores all requests and execution time.
'''


class CustomLogger:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_start = time.time()

        response = self.get_response(request)

        request_time = time.time() - time_start
        request_path = request.path

        if request.user.id is None:
            request.user.id = 0

        Logger.objects.create(
            path=request_path,
            method=request.method,
            r_time=request_time,
            user_id=request.user.id
        )

        return response

