import json

class data:  
    data = []

    def read(self):
        with open('data/data.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getTiendas(self): 
        tiendas = []
        for row in self.data:
            tienda = row['cadenaComercial']
            if tienda not in tiendas:
                tiendas.append(tienda)
        return tiendas

    def getProductos(self): 
        productos = []
        for row in self.data:
            producto = row['producto']
            if producto not in productos:
                productos.append(producto)
        return productos       
        
    def getPrecios(self, cadenaComercial, producto):
        infoPrecios = []  
        for row in self.data:
            tiendaI = row['cadenaComercial']
            productoI = row['producto']
            if tiendaI == cadenaComercial and productoI == producto:
                infoPrecios.append([row['nombreComercial'], productoI, row['precio']])
        return infoPrecios       
                
