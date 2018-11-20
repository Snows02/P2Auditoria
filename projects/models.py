from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']

    def save(self, *args, **kwargs):
        createLigaments = self.id == None
        super(Project, self).save(*args, **kwargs)

        from numerals.models import SubNumeral

        subnumerals = SubNumeral.objects.all()

        for subnumeral in subnumerals:
            project_SubNumeral = Project_SubNumeral(project=self, subnumeral=subnumeral)
            project_SubNumeral.save()

class Project_SubNumeral(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    subnumeral = models.ForeignKey('numerals.SubNumeral', on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='files/subs/', null=True, blank=True)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s - %s - %i' % (self.project, self.subnumeral, self.level)

    class Meta:
        verbose_name = 'Project-SubNumeral Info'
        verbose_name_plural = 'Project-SubNumeral Info'
