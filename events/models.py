from django.db import models
from users.models import Person
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
# Create your models here.
# def date_valid(val):
#     if val <= date.today():
#         raise ValidationError("la date doit être supérieur à la date d'aujourd'hui")
#     return val
def title_valid(val):
    if not val[0].isupper():      
        raise  ValidationError("le titre doit commencer par une majuscule")
    return
class Event(models.Model):
    title = models.CharField(max_length=255,blank=False, validators=[title_valid])
    description = models.TextField()
    image =models.ImageField(upload_to='images/')
    CHOIX =(
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport','Sport')
    )
    category =models.CharField('category',choices=CHOIX , max_length=8)
    state =models.BooleanField(default=False)
    nbe_participant =models.IntegerField(default=0,
            validators=[MinValueValidator(limit_value=0,message='le nombre de participant doit être positif')])
    evt_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(Person,on_delete=models.CASCADE)
    participations = models.ManyToManyField(Person ,related_name= 'participations' , through='Participation')
    def __str__(self):
        return f" The event title is {self.title} wtih category {self.category}"
    class Meta:
        constraints =[
            models.CheckConstraint(
                check=models.Q(
                   evt_date__gte= date.today() 
                ),
                name='the event date is invalid'
                
                ),
        ]
        verbose_name =('Evenement')
        verbose_name_plural ='Evenements'
        
    
    
class Participation(models.Model):
    Person = models.ForeignKey(Person , on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    date_participation= models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('Person','event')
        
    