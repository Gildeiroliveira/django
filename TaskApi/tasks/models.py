from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(verbose_name='Nome', 
                            max_length=30, 
                            null=False, 
                            blank=False,
                            help_text='Breve descrição ')
    done = models.BooleanField(verbose_name='pronto?', default=False)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
    
    def __str__(self) -> str:
        return self.name