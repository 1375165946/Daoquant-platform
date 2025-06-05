from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from .models import User
import json


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(" 接收到前端数据：", data)

        usernumber = data.get('usernumber')
        password = data.get('password')
        name = data.get('name')

        print(f" 解析字段：usernumber={usernumber}, password={password}, name={name}")

        if not (usernumber and password and name):
            print(" 缺少字段")
            return JsonResponse({'msg': '缺少字段'}, status=400)

        if not usernumber.isdigit() or len(usernumber) != 11:
            print(" 账号格式错误")
            return JsonResponse({'msg': '账号必须是11位纯数字'}, status=400)

        if User.objects.filter(usernumber=usernumber).exists():
            print(" 账号已存在")
            return JsonResponse({'msg': '账号已存在'}, status=400)

        if User.objects.filter(name=name).exists():
            print(" 用户名已存在")
            return JsonResponse({'msg': '用户名已存在'}, status=400)

        User.objects.create(usernumber=usernumber, password=password, name=name)
        print(" 成功写入数据库！")
        return JsonResponse({'msg': '注册成功'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usernumber = data.get('usernumber')
        password = data.get('password')

        if not usernumber or not password:
            return JsonResponse({'msg': '账号和密码不能为空'}, status=400)

        try:
            user = User.objects.get(usernumber=usernumber)
        except User.DoesNotExist:
            return JsonResponse({'msg': '账号不存在'}, status=404)

        if user.password != password:
            return JsonResponse({'msg': '密码错误'}, status=401)

        #  登录成功：设置 session
        request.session['user_id'] = user.id
        request.session['user_name'] = user.name
        request.session['usernumber'] = user.usernumber

        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        return JsonResponse({
            'msg': '登录成功',
            'token': session_key,
            'user': {
                'id': user.id,
                'name': user.name,
                'usernumber': user.usernumber
            }
        })


def user_profile(request):
    # 示例逻辑：返回固定的个人信息
    return JsonResponse({
        'name': '测试用户',
        'msg': '这是一个示例的用户信息接口'
    })
