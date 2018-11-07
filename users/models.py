from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#aca se especifica que si se borra este dato, todos los datos vinculados a él seran tambien eliminados
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')#guardar la imagen en la base de datos.

    def __str__(self):
        return self.user.username+' ' + 'Profile'#se debe instalar pip install Pillow, para que soporte imagenes
        # Se usa el comando py manage.py makemigrations para preparar la base de datos.
        #por ultimo se ingresa py manage.py migrate
    def save(self):
        super().save()
    
        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:# esto sirve para reducir el tamaño de la imagen y mejorar la velocidad de la pagina
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
