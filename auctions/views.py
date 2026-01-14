from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages

# generic Viws
# user
from django.contrib.auth.decorators import login_required


def index(request):
    nome = Listing.objects.all()
    return render(
        request,
        "auctions/index.html",
        {
            "produtos": nome,
        },
    )


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# mostar conteudo do listnings/comentarios/bids/etc..
def listining(request, nome_id):
    # mostrar comentarios
    lista = Listing.objects.get(pk=nome_id)
    comentario = lista.lance.all()
    # verificar usuario
    verif_user = lista.criador != request.user
    # print(verif_user)
    # pegar todos os lances/pegar valor do vencedor
    lances = lista.lances.all()
    valor_vencedor = lances.order_by("-valor_lancado").first()
    if request.method == "POST":
        # verificar se o user esta logado
        if request.user.is_authenticated:
            # Ganhador
            if "close_listing" in request.POST:
                lista.ativo = False
                lista.save()
                return redirect("index")
            elif "Open_listing" in request.POST:
                lista.ativo = True
                lista.save()
                return redirect("index")
            # add watchlist
            if "add_watchlist" in request.POST:
                # verificando se exste esta watchist no banco de dados
                if Watchlist.objects.filter(
                    watch_user=request.user, watch_lance=lista
                ).exists():
                    messages.error(
                        request, "This item has already been added to the watch list!"
                    )
                else:
                    add_watchlist = Watchlist(
                        watch_user=request.user, watch_lance=lista
                    )
                    print(add_watchlist)
                    add_watchlist.save()
                    messages.success(request, "Watchlist added successfully!")
            # remove watchlist
            elif "remove_watchlist" in request.POST:
                print(lista.lance_watch.first())
                try:
                    remove_watchlist = lista.lance_watch.first()
                    remove_watchlist.delete()
                    messages.success(request, "Item removed from watchlist!")
                except:
                    messages.error(
                        request, "This item has not been added to the watch list!"
                    )
            # verificar Status do item
            elif not lista.ativo:
                print("inativo")
                messages.error(request, "This auction has now closed.")
                return redirect("listning", nome_id=nome_id)

            coment_text = request.POST.get("coment_Text").strip()
            bid_text = request.POST.get("bid_Text")
            # novo_cometario
            if coment_text:
                print(coment_text)
                creat_comment = Comment(
                    user=request.user, lance=lista, coment=coment_text
                )
                creat_comment.save()
                return redirect("listning", nome_id=nome_id)
            # novo_Bid
            elif bid_text:
                bid_int = int(bid_text)
                creat_bid = Bid(
                    lances_select=lista, lancador=request.user, valor_lancado=bid_int
                )
                valor_filtrado = lista.lances.filter(
                    valor_lancado=creat_bid.valor_lancado
                )
                print(valor_filtrado)
                # tanbem adiciona o maior no Bid.valor_lancado
                lista.lance_maior = bid_int
                # se o Bid estiver vazio ele adiciona altomaticamente
                if not lista.lances.exists():
                    print(bid_int)
                    print(lista.lance_atual)
                    if bid_int > lista.lance_atual:
                        creat_bid.save()
                        lista.save()
                        messages.success(request, "Bid successfully added!")
                        return redirect("listning", nome_id=nome_id)
                    else:
                        messages.error(request, "the supply is insufficient!")
                        return redirect("listning", nome_id=nome_id)
                else:
                    # ordena/maior valor
                    maior_valor = (
                        lista.lances.order_by("-valor_lancado").first().valor_lancado
                    )
                    # se houver numero repetido em listnings
                    if valor_filtrado:
                        messages.error(request, "the supply is insufficient!")
                    # adicionar o maior
                    elif bid_int > maior_valor:
                        creat_bid.save()
                        lista.save()
                        messages.success(request, "Bid successfully added!")
                        return redirect("listning", nome_id=nome_id)
                    else:
                        messages.error(request, "the supply is insufficient!")
        else:
            messages.error(
                request, "You are not registered, please log in before bidding"
            )

    return render(
        request,
        "auctions/listnings.html",
        {
            "listning": lista,
            "comment": comentario,
            "valor_lancado": lista.lances.order_by("-valor_lancado").first(),
            "verif_user": verif_user,
            "vencedor": valor_vencedor,
        },
    )


# caminho
def categories(request):
    object = Categorie.objects.all()
    return render(
        request,
        "auctions/categories.html",
        {
            "object": object,
        },
    )


# create_Listing
def create_Listing(request):
    categories_list = Categorie.objects.all()
    try:
        if "create_Listing" in request.POST:
            nome = request.POST.get("name_item")
            descrition = request.POST.get("coment_Text")
            url = request.POST.get("url_field")
            # pegar id de categoria
            cate_id = request.POST.get("categoria")
            cate = categories_list.get(pk=cate_id)
            lance_inicial = request.POST.get("bid_number")
            add = Listing(
                criador=request.user,
                nome_item=nome,
                descricao=descrition,
                imagemURL=url,
                categoria=cate,
                lance_atual=lance_inicial,
            )
            add.save()
            messages.success(request, "Listing successfully created!")
            return redirect("index")
    except:
        messages.error(request, "ERRo!")
    return render(
        request, "auctions/create_Listing.html", {"categories": categories_list}
    )


# categorias
def categories_list(request, nome_id):
    objeto_cate = Categorie.objects.get(pk=nome_id)
    cate_id = objeto_cate.id
    Listning_cate = Listing.objects.filter(categoria=cate_id)
    objects_cate = Listning_cate.all
    return render(
        request,
        "auctions/categories_list.html",
        {
            "list": objects_cate,
        },
    )


@login_required  # serve para garantir que apenas usuários autenticados possam acessar a view watchlist.
def watchlist(request):
    user = request.user
    nome_watch = Watchlist.objects.filter(watch_user=user)
    return render(request, "auctions/watchlist.html", {"watchlist": nome_watch})
