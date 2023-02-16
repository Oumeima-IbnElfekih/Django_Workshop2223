from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def Participant_number(self,obj):
        val=obj.participations.count()
        return val
    list_display =('title','category','state','Participant_number','created_at','evt_date',)
    list_filter =('state','category',)
    search_fields=['title','category']
    list_per_page= 5
    ordering=('-title','-created_at','evt_date',)
    readonly_fields=('updated_at','created_at')
    autocomplete_fields=['organizer']
    fieldsets =(
        
        ('Event State' , {
             'fields' : ('state',)
            
            }) ,
        
        ('About' ,
         {   'classes' :('collapse',),
             'fields' :('title','description','image','category','nbe_participant','organizer')
         }
          ),
        ('Dates',
         { 'classes' :('collapse',),
             'fields' :('evt_date','updated_at','created_at')
         }
         )
        
        
        
        
    )
   
class ParticipationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Participation,ParticipationAdmin)


