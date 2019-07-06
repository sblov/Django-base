from django.db import models

class faceJavManager(models.Manager):
    def get_queryset(self):
        return super(faceJavManager, self).get_queryset().filter()

# Create your models here.
class faceJav(models.Model):
    fjObject = faceJavManager()

    title = models.CharField(db_column ='title', max_length=50)
    imgUrl = models.CharField(db_column ='IMGURL', max_length=500)
    pageUrl = models.CharField(db_column ='PAGEURL', max_length=500)
    description = models.CharField(db_column ='description',max_length=500 )
    updateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'title:%s;img:%s;page:%s;descr:%s'%(self.title, self.imgUrl, self.pageUrl, self.description)

    class Meta:
        db_table = 't_facejav'
        ordering = ['-id']

    @classmethod
    def createFaceJav(cls, tit, img, page, des):
        fj = cls(title=tit, imgUrl=img, pageUrl=page, description=des)
        return fj
    
class User(models.Model):
    username = models.CharField(db_column = 'name', max_length=20)
    password = models.CharField(db_column = 'password', max_length=50)

    class Meta:
       db_table = 't_xfun_user'
       ordering = ['id']

