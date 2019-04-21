from django.http.response import HttpResponse
import hashlib
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def check_signature(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = '113508'

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')����#�����������encode('utf-8'),����ᱨ��
        print('hashstr befor sha1', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1', hashstr)
        if hashstr ==signature:
            return HttpResponse(echostr)����#���뷵��echostr
        else:
            return HttpResponse('error')����#�ɸ���ʵ����Ҫ����
    else:
        return HttpResponse('sucessful')����#�ɸ���ʵ����Ҫ����