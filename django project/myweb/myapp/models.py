from django.db import models

# Create your models here.

class Stu(models.Model):
    '''自定义Stu表对应的Model类'''
    #定义属性：默认主键自增id字段可不写
    id = models.AutoField("学号",primary_key=True)
    name = models.CharField("姓名",max_length=16)
    age = models.SmallIntegerField("年龄")
    sex = models.CharField("性别",max_length=1)
    classid=models.CharField("班级",max_length=8)

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%d:%s:%s"%(self.id,self.name,self.age,self.sex,self.classid)

    # 自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table="stu"
        verbose_name = 'Student Information'  
        verbose_name_plural = 'Student Info'

class TouHou(models.Model):
    name = models.CharField("游戏名",max_length=255)
    release_date = models.DateField("发行日期")
    game_id = models.IntegerField("游戏编号")
    game_type = models.CharField("游戏类别",max_length=255)

    def __str__(self):
        return f'{self.name} - {self.game_id}'


    class Meta:
        db_table = 'TouHou-List'