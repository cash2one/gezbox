from django.contrib.auth.models import User
from django.db import models


class Order(models):
    """
    风先生订单模型
    """
    c_time = models.DateTimeField(auto_created=True)#订单产生时间
    master = models.ForeignKey(User, related_name="orders")
    status = models.CharField(max_length=50)#订单状态，根据业务逻辑需求，在form里做相应限制
    ftime  = models.DateTimeField(blank=True,null=True)#订单完成时间


    def _valueDict(self):
        return {"id": self.id, "ctime": self.ctime, "master": self.master}

    valueDict = property(_valueDict)#用与自组织返回数据

    class Meta:
        ordering = ['-ctime', '-id']

    def pre_save(self):
        """
            一个订单产生前做些额外处理,例如发送短信通知，向风先生设备PUSH消息，通知其抢单。等等。
        """
        pass


    def save(self):
        self.pre_save()
        super(Order, self).updata()

    def __unicode__(self):
        return str(self.valueDict)


class Account(models):
    """
    储蓄账户模型
    """
    master = models.OneToOneField(User, related_name="fund")
    balance = models.FloatField()


class PorterProfile(models):
    """
    风先生信息
    """
    user = models.OneToOneField(User,related_name="porter")#django.auth.user  的关联
    orders = models.ForeignKey(Order,related_name="porter")#用于 拼接 order 反向查询 是谁在派送
    #其他信息，例如 性别，年龄，头像，电话，身份证等个人信息

    def __unicode__(self):
        return str({"type":"PorterProfile","id":self.id})