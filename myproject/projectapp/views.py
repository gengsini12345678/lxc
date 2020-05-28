from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from . import models


def index(request):
    '''
    首页视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'projectapp/index.html')
    elif request.method == 'POST':
        pass


def register(request):
    '''
    注册视图处理函数
    :param reuqest:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'projectapp/register.html')

    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        userpass = request.POST['userpass']
        re_userpass = request.POST['re_userpass']
        realname = request.POST['realname']

        # 验证数据
        if len(username) < 6:
            return render(request, "projectapp/register.html",
                          {"error_msg": "用户名不能小于六位"})
        if len(userpass) < 6:
            return render(request, "projectapp/register.html",
                          {"error_msg": "密码不能小于六位"})
        if re_userpass != userpass:
            return render(request, "projectapp/register.html",
                          {"error_msg": "两次的密码不一致"})
        # 保存数据
        try:
            usertable = models.UserTable.objects.get(username=username)
            return render(request, 'projectapp/register.html',
                          {"error_msg": "改用户名已存在，请重新注册"})
        except:
            # 创建用户注册
            # 对密码进行加密
            userpass = make_password(userpass)
            usertable = models.UserTable(username=username, userpass=userpass, realname=realname)
        usertable.save()
        return render(request, "projectapp/login.html", {"error_msg": "注册成功"})


def login_user(request):
    '''
    用户登录视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'projectapp/login.html')
    elif request.method == 'POST':
        # 获取用户名和密码
        username = request.POST['username']
        userpass = request.POST['userpass']

        # 获取usertable对象
        usertable = models.UserTable.objects.get(username=username)

        # 判断用户名或密码是否正确
        if check_password(userpass, usertable.userpass):
            request.session['login_user'] = usertable
            return redirect(reverse('projectapp:index'))
        else:
            return render(request, 'projectapp/login.html', {'error_msg': '用户名或者密码错误'})


            # try:
            #     userpass = check_password(userpass)
            #     usertable = models.UserTable.objects.get(username=username,userpass=userpass)
            #     print(usertable.userpass)
            #
            #
            # except:
            #
            #     return render(request,'projectapp/login.html',{'error_msg':'登录失败'})


def add_product(request):
    '''
    添加产品视图函数
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'projectapp/add_products.html')
    elif request.method == 'POST':
        # 获取数据
        pro_name = request.POST.get('pro_name')
        pro_code = request.POST.get('pro_code')
        product_type = request.POST.get('product_type')
        pro_price = request.POST.get('pro_price')
        pro_kuwei = request.POST.get('pro_kuwei')
        content = request.POST.get('content')
        user = request.session['login_user']
        productadmin = models.ProductAdmin(pro_code=pro_code, pro_kuwei=pro_kuwei, pro_name=pro_name,
                                           pro_price=pro_price, pro_type=product_type, pro_intro=content, user=user)
        productadmin.save()
        request.session['productadmin'] = productadmin
        return redirect(reverse("projectapp:product_info", kwargs={'id': productadmin.id}))
        # return render(request,'projectapp/index.html')


def product_info(request, id):
    '''
    产品详情页面
    :param request:
    :param id:
    :return:
    '''
    product = models.ProductAdmin.objects.get(pk=id)
    # 跳转到产品详情页面
    return render(request, 'projectapp/product_info.html', {"product": product})


def product_list(request):
    '''
    查看所有的产品
    :param request:
    :return:
    '''
    if request.method == "GET":
        # alist = models.Wanda.objects.all()
        # 获取当前用户
        user = request.session['login_user']
        # print(user.id)
        # 查询当前用户添加的产品
        pro_admin = models.ProductAdmin.objects.filter(user_id=user.id).order_by("-id")
        # print(pro_admin)
        return render(request, 'projectapp/product_list.html', {'pro_admin': pro_admin})


def update_product(request, proid):
    '''
    修改产品
    :param request:
    :param pro_id:
    :return:
    '''
    if request.method == 'GET':
        product = models.ProductAdmin.objects.get(pk=proid)
        print(product.pro_name)
        print("---", proid)
        print(type(proid))
        return render(request, "projectapp/update_product.html", {"product": product})
    elif request.method == 'POST':
        # 获取数据
        pro_name = request.POST.get('pro_name')
        pro_code = request.POST.get('pro_code')
        product_type = request.POST.get('product_type')
        pro_price = request.POST.get('pro_price')
        pro_kuwei = request.POST.get('pro_kuwei')
        content = request.POST.get('content')

        # 获取产品对象
        product = models.ProductAdmin.objects.get(pk=proid)
        product.pro_name = pro_name
        product.pro_name = pro_code
        product.pro_name = product_type
        product.pro_name = pro_price
        product.pro_name = pro_kuwei
        product.pro_name = content
        # 修改数据并且保存到数据库中
        product.save()
        return redirect(reverse("projectapp:product_list", kwargs={}))


def delete_porduct(request, pro_id):
    '''
    删除产品
    :param request:
    :return:
    '''
    # 通过id 来获取产品
    product = models.ProductAdmin.objects.get(pk=pro_id)
    product.delete()
    return redirect(reverse("projectapp:product_list", kwargs={}))


def search(request):
    '''
    搜索视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'POST':

        # 获取产品的名称和类别
        pro_name_list = []
        pro_type_list = ['精品', '轮胎', '耗材']
        pro = models.ProductAdmin.objects.all()
        for name in pro:
            pro_name_list.append(name.pro_name)
        # print(pro_name_list)

        # 获取搜索框的数据
        name = request.POST['search']
        if name:
            for type in pro_type_list:
                # 判断搜索框的值是否等于 产品类型
                if name == type:
                    pro_admin = models.ProductAdmin.objects.filter(pro_type=name)
                    return render(request, 'projectapp/product_list.html', {'pro_admin': pro_admin})
            for item in pro_name_list:
                # 判断搜索框的值是否等于 产品名称
                if name == item:
                    pro_admin = models.ProductAdmin.objects.filter(pro_name=name)
                    return render(request, 'projectapp/product_list.html', {'pro_admin': pro_admin})
        else:
            # 重定向到产品列表页面
            return redirect(reverse('projectapp:product_list', kwargs={}))


def add_product_sale(request):
    '''
    添加产品销售
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'projectapp/add_product_sale.html', {})
    elif request.method == 'POST':
        # 获取数据
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        sale_price = request.POST.get('sale_price')
        sale_number = request.POST.get('sale_number')
        total_money = request.POST.get('total_money')
        pro_info = request.POST.get('pro_info')
        produc = request.session['productadmin']

        product_sale = models.ProductSale(name=name, phone_number=phone_number, sale_price=sale_price,
                                          sale_number=sale_number, total_money=total_money, pro_info=pro_info,
                                          product_admin=produc)

        product_sale.save()
        return render(request, 'projectapp/index.html', {})


def sale_list(request):
    '''
    产品销售视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        pro_sale = models.ProductSale.objects.all()
        return render(request, 'projectapp/sale_list.html', {'pro_sale': pro_sale})


def delete_sale(request, pro_id):
    '''
    删除销售产品
    :param request:
    :param pro_id:
    :return:
    '''
    pro_sale = models.ProductSale.objects.get(pk=pro_id)
    pro_sale.delete()
    return redirect(reverse("projectapp:sale_list", kwargs={}))


def search_sale(request):
    '''
    搜索销售产品
    :param request:
    :return:
    '''
    if request.method == 'POST':

        # 获取搜索框的数据
        name = request.POST['search']
        pro_sale_list = []

        pro_sale = models.ProductSale.objects.all()
        for pro_name in pro_sale:
            pro_sale_list.append(pro_name.name)
        print(pro_sale_list)
        if name:
            for item in pro_sale_list:
                if name == item:
                    p_sale = models.ProductSale.objects.filter(name=name)
                    return render(request, 'projectapp/sale_list.html', {'pro_sale': p_sale})
        else:
            return redirect(reverse("projectapp:sale_list", kwargs={}))


def logout(request):
    '''
    退出视图处理函数
    :param request:
    :return:
    '''

    try:
        del request.session['login_user']
        return render(request, 'projectapp/login.html', {})
    except:
        return redirect(reverse('projectapp:index'))
