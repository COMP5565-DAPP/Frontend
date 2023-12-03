"""
URL configuration for COMP5565_DAPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/processableDiamonds", admin.site.urls),
    path("process/view", views.processable_Diamonds, name='processView'),
    # '''
    # 返回处于mined状态下的所有矿石信息
    # {
    #     identification: 1204,                                       Int
    #     diamondStatus: 4,                                           Int
    #     currentOwner: 0x0a00D00DfE437EbADF080C928CfA139937D09899,   String
    #     unique_id: 10001                                            Int
    # }
    # ''',
    path("carve/view", views.carveable_Diamonds, name='carveView'),
    # '''
    # 返回处于processed状态下所有矿石信息，格式同上
    # ''',

    path("design/view/<str:address>", views.designable_Diamonds, name='designView'),
    # '''
    # 返回处于collected状态下所有矿石信息，input：当前address
    # ''',
    path("purchase/view", views.purchasable_Diamonds, name='purchaseView'),
    # '''
    # 返回处于designed状态下所有矿石信息
    # '''
    path("collect/view", views.collectable_Diamonds, name='collectView'),
    # '''
    # 返回处于carved状态下所有矿石信息
    # ''',
    path("owned/view/<str:address>", views.owned_Diamonds, name='ownedView'),
    # '''
    # 返回该地址下拥有的💎信息，Input：当前地址
    # ''',
    path("mine/mineDiamonds/<int:diamondID>/<int:companyNum>/<str:address>", views.mine_diamonds),
    # '''
    # 挖矿过程
    # Input：自定义的矿石ID，公司编号，公司在ganache上的地址
    # return：当前账户所拥有的所有矿石
    # ''',
    path("login/", views.login),
    # '''
    # 登陆
    # return：所有存储在mongodb中的账户信息
    # ''',
    path("register/<str:companyName>/<str:password>/<str:address>/<int:companyNum>/<int:companyType>", views.register),
    # '''
    # 注册
    # Input：用户名，密码，从ganache中获得的地址，公司编号，公司类型（注意公司类型根据枚举类型返回的是整型数据，比如mining公司为0，cutting公司为1）
    # return：所有存储在mongodb中的账户信息
    # ''',
    path("process/processDiamonds/<int:diamondID>/<int:companyNum>/<str:address>", views.process_diamonds),
    # '''
    # 切割公司获取矿石并切割
    # Input: 矿石的ID，公司编号，公司的账户地址
    # ''',
    # path("")
]