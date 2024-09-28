from django.contrib.auth.models import User

Juho = User.objects.create_user("Juho", password="badpassword1234")
Pertsa = User.objects.create_user("Pertsa", password="badpassword1234")

Juho.save()
Pertsa.save()