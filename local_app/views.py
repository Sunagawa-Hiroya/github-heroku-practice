from django.http import HttpResponse


def testfunc(request):
    return HttpResponse('Hello my App!!! 自動的にビルドしたよ！')


def create_message(request):
    print(request.body)
    return HttpResponse('Lineに返信！！見えてる？, コンソールに出ている？')
