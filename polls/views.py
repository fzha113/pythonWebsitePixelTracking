from django.http import HttpResponse
from django.shortcuts import render


# get all info from header n this is a show function
def index(request):

    return render(request, "polls/intro.html")


def request_demo(request):
    # user = request.user
    # user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip

    # real_ip = x_forwarded_for.split(',')[0]
    # ip = request.META.get('REMOTE_ADDR')

    print(ip)

    f = open("/home/vestaCentral/mnt/pythonWebsite/pt.out", 'a')
    print("\n ip: {0}".format(ip), file = f)
    f.close()

    return HttpResponse()







