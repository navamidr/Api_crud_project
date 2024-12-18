from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Person



@receiver(post_save,sender=Person)

def log_user(sender,instance,created,**kwargs):
    if created:
        if  not instance.user_id:
            instance.user_id = f"USER-{Person.objects.count()}{instance.name[:10].capitalize()}"
            instance.save(update_fields=['user_id'])
        print(f"new person created: ID {instance.user_id},{instance.name},{instance.age} years old,{instance.job},from:{instance.place}.")
    else:
        print(f"user update: ID {instance.user_id},{instance.name},{instance.age} years old,{instance.job},from:{instance.place}.")


@receiver(post_delete,sender=Person)

def user_delet(sender,instance,**kwargs):
    print(f"user deleted:ID {instance.user_id},{instance.name}.")
