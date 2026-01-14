from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Categorie(models.Model):
    nome_cate = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome_cate}"


# Listagens
class Listing(models.Model):
    criador = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="criador", null=True
    )
    nome_item = models.CharField(max_length=50, unique=True)
    descricao = models.TextField()
    imagemURL = models.URLField(
        max_length=500, verbose_name="URL da Imagem", null=True, blank=True
    )
    categoria = models.ForeignKey(
        Categorie, on_delete=models.PROTECT, related_name="categoria", null=True
    )
    lance_atual = models.IntegerField(default=0)
    lance_maior = models.IntegerField(default=0, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"nome:{self.nome_item}  |  Starting bid:{self.lance_atual}  |  Category:{self.categoria}"


# lances
class Bid(models.Model):
    lances_select = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="lances", null=True, blank=True
    )  # escoplher o item pra comprar/leiloar
    lancador = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="lancador", null=True, blank=True
    )  # usuarui que vai comprram
    valor_lancado = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"Current bid:{self.valor_lancado}  |  Creator:{self.lancador}  |  lance:{self.lances_select}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="comentario", null=True
    )
    lance = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="lance", null=True
    )
    coment = models.TextField()

    def __str__(self):
        return f"{self.user}  |  lancou:{self.lance}  |  Description:{self.coment}"


class Watchlist(models.Model):
    watch_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="nome_watch", null=True
    )
    watch_lance = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="lance_watch", null=True
    )

    def __str__(self):
        return f"o Carrinho do :{self.watch_user}  |  tem:{self.watch_lance}"
