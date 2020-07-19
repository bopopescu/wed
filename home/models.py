from django.db import models

# Create your models here.


class CommonModel(models.Model):

    def toJson(self):
        ls_name = [filed.name for filed in self._meta.get_fields()]

        return {k: getattr(self, k) for k in ls_name}

    class Meta:
        abstract = True


class UserModel(CommonModel):
    username = models.CharField(verbose_name='用户账号', null=True, blank=True, max_length=100)
    password = models.CharField(verbose_name='密码', null=True, blank=True, max_length=255)
    status = models.CharField(verbose_name='状态', choices=[('enabled', '启用'), ('disabled', '禁用')], default='enabled', max_length=100)
    nickname = models.CharField(verbose_name='昵称', null=True, blank=True, max_length=255)
    avatar = models.CharField(verbose_name='头像', null=True, blank=True, max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


class MemberModel(models.Model):
    openid = models.CharField(verbose_name='微信用户id', null=True, blank=True, max_length=255)
    avatar = models.CharField(verbose_name='头像', null=True, blank=True, max_length=255)
    nickname = models.CharField(verbose_name='昵称', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.openid

    class Meta:
        db_table = 'member'


class CategoryModel(models.Model):
    img_path = models.CharField(verbose_name='图标路径', null=True, blank=True, max_length=255)
    pid = models.IntegerField(verbose_name='父类id', null=True, blank=True)
    path = models.CharField(verbose_name='路径', null=True, blank=True, max_length=255)
    name = models.CharField(verbose_name='分类名称', null=True, blank=True, max_length=50)
    types = models.CharField(verbose_name='类型', choices=[('photo', '婚摄'), ('dress', '装扮')], default='dress', max_length=20, db_column='type')
    style = models.CharField(verbose_name='样式', null=True, blank=True, max_length=50)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = '分类表'


class BannerModel(models.Model):
    img_path = models.CharField(verbose_name='图片路径', max_length=255, null=True, blank=True)
    img_url = models.URLField(verbose_name='图片跳转url', null=True, blank=True)
    title = models.CharField(verbose_name='图片标题', null=True, blank=True, max_length=255)
    description = models.CharField(verbose_name='图片描述', null=True, blank=True, max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'banner'
        verbose_name = '展示轮播'


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='外键')
    title = models.CharField(verbose_name='产品标题', null=True, blank=True, max_length=255)
    price = models.DecimalField(verbose_name='单价', max_digits=10, decimal_places=2, null=True, blank=True)
    product_type = models.CharField(choices=[('product', '产品'), ('production', '作品')], default='product', max_length=50)
    check_num = models.IntegerField(verbose_name='查看次数', null=True, blank=True)
    num = models.IntegerField(verbose_name='数量', null=True, blank=True)
    specification = models.CharField(verbose_name='规格参数', max_length=1000, null=True, blank=True)
    description = models.CharField(verbose_name='产品描述', null=True, blank=True, max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True, blank=True)
    update_time = models.DateTimeField(verbose_name='更新时间', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        verbose_name = '展示产品'


class ImagesModel(models.Model):
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, null=True, blank=True, verbose_name='关联外键')
    img_type = models.CharField(choices=[('default', '主图'), ('subordinate', '从图')], default='subordinate', max_length=50)
    img_path = models.ImageField(verbose_name='图片路径', null=True, blank=True)
    img_url = models.URLField(verbose_name='图片跳转url', null=True, blank=True)

    class Meta:
        db_table = 'images'
        verbose_name = '产品对应的图片'


class ChatMsgModel(models.Model):
    open_id = models.CharField(verbose_name='微信openid', max_length=255, null=True, blank=True)
    chat_type = models.CharField(choices=[('img', '图片'), ('msg', '信息')], default='msg', max_length=50)
    content = models.CharField(verbose_name='咨询内容', max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'chat_msg'
        verbose_name = '聊天留言信息'
