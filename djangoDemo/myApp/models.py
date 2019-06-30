from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField()
    def __str__(self):
        return '%s-%d-%d'%(self.gname, self.ggirlnum, self.gboynum)

class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager, self).get_queryset().filter(isDelete='False')

    def createStudent(self, name, age, gender, contend, grade, isDel=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        
        return stu
    

class Students(models.Model):
    # 自定义模型管理器
    # 当自定义模型管理器,objects就不存在了
    stuObj0 = models.Manager()
    stuObj1 = StudentsManager()

    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    # db_column='age'
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey(Grades,on_delete=models.CASCADE)

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%d'%(self.sname,  self.sage)

    class Meta:
        # 数据表名
        db_table = 't_student'
        # 查询时以id排序， '-id'为降序
        ordering = ['id'] 

    @classmethod
    def createStudent(cls, name, age, gender, contend, grade, isDel=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontend=contend,sgrade=grade, isDelete=isDel)
        return stu
