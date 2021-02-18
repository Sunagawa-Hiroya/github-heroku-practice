from django.http import HttpResponse
import json


def testfunc(request):
    return HttpResponse('Hello my App!!! 自動的にビルドしたよ！')


@csrf_exempt
def create_message(request):
    # print(request.body)
    print('OK!!!!')
    if request.method == 'POST':
        print('this is post method')
        print('jsondataはこれです: ' + json.loads(request.body.decode('utf-8')))
    else:
        print('this is get method')

    return HttpResponse('Lineに返信！！見えてる？, コンソールに出ている？')
