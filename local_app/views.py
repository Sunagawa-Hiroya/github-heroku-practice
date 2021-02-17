from django.http import HttpResponse


def testfunc(request):
    return HttpResponse('Hello my App!!! 自動的にビルドしたよ！')
