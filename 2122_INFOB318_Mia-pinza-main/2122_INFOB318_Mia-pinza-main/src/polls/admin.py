from django.contrib import admin

from .models import Commande
from .models import Produit
from .models import Bordereau


class ProduitsAdmin(admin.ModelAdmin):
    """
    cette class permet de gérer du côté administrateur les utilisateur du site ,
     les commandes passer et le different produits de la carte
    """
    list_display = ('nom', 'prix', 'contenue')


admin.site.register(Produit, ProduitsAdmin)
admin.site.register(Commande)
admin.site.register(Bordereau)
