# encoding:utf-8
import logging,random
from django.shortcuts import get_object_or_404
from piston.handler import BaseHandler
from piston.utils import FormValidationError, rc
from feng.models import Order, ORDER_STATUS, Account
from feng.forms import OrderForm

log = logging.getLogger("root")

__author__ = 'quxl'


class OrderHandler(BaseHandler):
    allowed_methods = ['POST','GET']
    model = Order

    def create(self, request, *args, **kwargs):
        f = OrderForm(request.POST, request=request)
        if f.is_valid():
            inst = f.save(commit=False)
            inst.master = request.user
            inst.status =ORDER_STATUS.UNACCEPT
            inst.save()
            return inst.valueDict
        else:
            raise FormValidationError(f)

    def read(self, request, *args, **kwargs):
        orders = request.user.orders.using('read').all()#此处 从 只读数据库 读取数据，降低 写数据的 压力
        return [o.valueDict for o in orders ]


class OrderAcceptHandler(BaseHandler):
    allowed_methods = ['POST']
    model = Order

    def deal_order(self,account,price):
        if account.balance >=price:
            account.balance = account.balance-price
            account.save()
            return True
        else:
            return False


    def inspect_user_status(self):
        #调用外部接口
        #这里随机返回 True 和 False
        return random.choice([True])


    def create(self, request, *args, **kwargs):
        if kwargs.get('order_id',False):
            if self.inspect_user_status():
                order = get_object_or_404(self.model,id=kwargs.get('order_id',0))
                account = get_object_or_404(Account,master = request.user)
                if self.deal_order(account,order.price):
                    order.status= ORDER_STATUS.ACCEPT
                    order.save()
                    return order.valueDict
                else:
                    return {"message":"余额不足"}
            else:
                return {"message":"用户状态不正常"}
        else:
            return rc.NOT_FOUND