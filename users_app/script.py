from .models import Status

name1 = "Available"
name2 = "Not Available"
x = Status.objects.create(name=name1)
x.save()
y = Status.objects.create(name=name2)
y.save()