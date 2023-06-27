def total(request):
    tot = 0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            tot += int(value["total"])
    return {"total" :tot}

def cantidad(request):
    cant = 0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].itemos():
            cant += int(value["cantidad"])
    return {"cantidades":cant}
