import web 
from data import data
from web import form

render = web.template.render('templates/', base = 'base')

urls = ('/(.*)', 'index' )
app = web.application(urls, globals())
data = data()  
data.read() 
myform = form.Form(  
            form.Dropdown('Tiendas', data.getTiendas()),
            form.Dropdown('Producto',data.getProductos()) ) 

class index:  
    def GET(self, results):      
        form = myform
        return render.index(form, None) 

    def POST(self, results):  
        form = myform  
        if not form.validates(): 
            return render.index(form)
        else:
            user_data = web.input()   
            tienda = user_data.Tiendas
            producto = user_data.Producto
            results = data.getPrecios(tienda,producto) 
            return render.index(form, results) 
              

if __name__=="__main__": 
    app.run()