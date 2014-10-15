# encoding:utf-8
from django.contrib.auth.models import User
from django.db import models


def enum(**enums):
    return type('Enum', (), enums)

ORDER_STATUS = enum(UNACCEPT="UNACCEPT",ACCEPT="ACCEPT",PAYED="PAYED",COMPLETE="COMPLETE",CANCLE="CANCLE")# 订单状态 确认,未支付,支付,支付方式,完成,取消

class Order(models.Model):
    """
    风先生订单模型
    """
    ctime  = models.DateTimeField(auto_now_add=True)#订单产生时间
    master = models.ForeignKey(User, related_name="orders")
    status = models.CharField(max_length=50)#订单状态，根据业务逻辑需求，在form里做相应限制
    ftime  = models.DateTimeField(blank=True,null=True)#订单完成时间
    descr  = models.CharField(max_length=500)#订单描述
    price  = models.FloatField()
    #此处应该包含 商品和收货人信息等等。应作为外键处理。测试环境不做过多处理。
    def _valueDict(self):
        return {"id": self.id, "ctime": self.ctime, "master": self._dictMaster(),"status":self.status,"price":self.price}
    def _dictMaster(self):
        return {"username":self.master.username,'id':self.master.id,"email":self.master.email}

    valueDict = property(_valueDict)#用与自组织返回数据

    class Meta:
        ordering = ['-ctime', '-id']

    def pre_save(self):
        """
            一个订单产生前做些额外处理,例如发送短信通知，向风先生设备PUSH消息，通知其抢单。等等。
        """
        pass


    def save(self, force_insert=False, force_update=False, using=None):
        self.pre_save()
        super(Order, self).save(force_insert,force_update,using)

    def __unicode__(self):
        return str(self.valueDict)


class Account(models.Model):
    """
    储蓄账户模型
    """
    master = models.OneToOneField(User, related_name="fund")
    balance = models.FloatField()

    def __unicode__(self):
        return str({"type":"Account","id":self.id})

class PorterProfile(models.Model):
    """
    风先生信息
    """
    user = models.OneToOneField(User,related_name="porter")#django.auth.user  的关联
    orders = models.ForeignKey(Order,related_name="porter")#用于 拼接 order 反向查询 是谁在派送
    #其他信息，例如 性别，年龄，头像，电话，身份证等个人信息

    def __unicode__(self):
        return str({"type":"PorterProfile","id":self.id})