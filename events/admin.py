from django.contrib import admin ,messages
from .models import *
from datetime import datetime
# Register your models here.
class ParticipationInline(admin.StackedInline):
    model =Participation
    extra=1
    readonly_fields=('date_participation',)
    can_delete=True


class ParticipantFilter(admin.SimpleListFilter):
    title='NBR Participant'
    parameter_name ='nbe_participant'
    def lookups(self,request,model_admin):
        return (('0',("No Participants")),('more',("More participants")))
    def queryset(self,request,queryset):
        if self.value() =='0':
            return queryset.filter(nbe_participant__exact=0)
        if self.value() =='more':
            return queryset.filter(nbe_participant__gt=0)
class DateFilter(admin.SimpleListFilter):
    title ='Event Date'
    parameter_name ='evt_date'
    def lookups(self,request,model_admin):
        return (('Past events',("Past events")),
                ('Upcomming Event',("Upcomming Event")),
                ('Today Event',("Today Event")))
    def queryset(self, request,queryset):
        if self.value() =='Past events':
            return queryset.filter(evt_date__lt=datetime.today())
        if self.value() =='Upcomming Event':
            return queryset.filter(evt_date__gt=datetime.today())
        if self.value() =='Today Event':
            return queryset.filter(evt_date__exact=datetime.today())

def accept_events(model_admin,request,queryset):
        rows_updated=queryset.update(state=True)
        if rows_updated ==1:
            msg="1 event"
        else:
            msg=f"{rows_updated} events"
        messages.success(request,message= "%s successfully accepted " %msg)
accept_events.short_description='Accept'
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def set_to_Refuse(self, request, queryset):
        rows_NoValid = queryset.filter(state=False)
        if rows_NoValid.count() > 0:
            messages.error(
                request, f"{rows_NoValid.count()} events are already marked as Not Accepted")
        else:
            rows_updated = queryset.update(state=False)
            if rows_updated == 1:
                message = "1 event was"
            else:
                message = f"{rows_updated} events were"
            self.message_user(request, level='success',
                              message="%s successfully marked as Not Accepted" % message)

    set_to_Refuse.short_description = "Refuse"
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
    actions=[accept_events,'set_to_Refuse']
    list_filter=('state','category',ParticipantFilter,DateFilter)
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


