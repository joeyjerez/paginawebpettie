from app.models import Producto

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        #else:
        self.carro = carro

    def agregarProductoCarrito(self,producto):
        if(str(producto.sku) not in self.carro.keys()):
            self.carro[producto.sku]={
                "producto_id":producto.sku
               ,"nombre": producto.nombre
               ,"precio": str(producto.precio)
               ,"cantidad":1
               #,"imagen":producto.image_url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.sku):
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = int(value["precio"])+producto.precio
                    break
        self.guardarCarrito()
    
    def guardarCarrito(self):
        self.session ["carro"] =self.carro
        self.session.modified = True
    
    def eliminarDelCarrito(self,producto):
        producto.sku = str(producto.sku)
        if producto.sku in self.carro:
            del self.carro[producto.sku]
            self.guardarCarrito()

    def restarDelCarrito(self,producto):
        for key, value in self.carro.items():
            if key == str(producto.sku):
                value["cantidad"] = value["cantidad"]-1
                value["precio"] = int(value["precio"])-producto.precio                
            if value["cantidad"] < 0 or value["precio"] == 0:
                self.eliminarDelCarrito(producto) 
                break

        self.guardarCarrito()

    def limparCarrito(self):
        self.session["carro"] = {}
        self.session.modified = True