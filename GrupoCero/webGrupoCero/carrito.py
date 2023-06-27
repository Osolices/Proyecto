class Carrito:
    def __init__(self, request):
        self.request = request
        self.session= request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, obra):
        id = str(obra.id_obra)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "id" : obra.id_obra,
                "foto" : obra.foto.url,
                "nombre" : obra.nombre,
                "precio" : obra.precio,
                "cantidad" : 1,
                "total": obra.precio,
            }    
        else:
            self.carrito[id]["cantidad"] +=1
            self.carrito[id]["total"] += obra.precio
        self.actualizar()

    def quitar(self, obra):
        id = str(obra.id_obra)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["total"] -= obra.precio

            if self.carrito[id]["cantidad"]== 0:
                self.eliminar(obra)
            self.actualizar()

    def eliminar (self,obra):
        id = str(obra.id_obra)
        if id in self.carrito.keys():
            del self.carrito[id]
            self.actualizar()
    
    def actualizar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def vaciar(self):
        self.carrito["carrito"] = {}
        self.session.modified =True