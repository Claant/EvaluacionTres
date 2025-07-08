from flask import Flask, render_template, request
app = Flask(__name__)

# PAGINA PRINCIPAL INDEX.HTML
@app.route('/')
def home():
    return render_template('index.html')


# PAGINA EJERCICIO1.HTML
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


# PAGINA EJERCICIO2.HTML
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')



# FUNCION EJERCICIO 1 QUE PROCESA EL PROMEDIO DE LAS TRES NOTAS Y LA ASISTENCIA
@app.route('/ejercicio1', methods=['GET', 'POST'])
def Ejercicio1():
    if request.method== 'POST':
        # SE PROCESAN LOS DATOS RECIBIDOS DEL FORMULARIO
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        # SE OBTIENE EL PROMEDIO Y SE UTILIZA LA ASISTENCIA COMO CRITERIO
        # PARA LA APROBACION O REPROBACION
        asistencia= float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        if asistencia >= 75 and promedio >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)
        return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def Ejercicio2():
    if request.method== 'POST':
        # SE PROCESAN LOS DATOS RECIBIDOS DEL FORMULARIO
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        longitud_palabra=[nombre1,nombre2,nombre3]
        palabra=[0]
        for i in range(1, len(longitud_palabra)):
            if len(palabra)< len(longitud_palabra[i]):
                palabra=longitud_palabra[i]
                longitud_total=len(palabra)
        return render_template('ejercicio2.html', palabra=palabra, longitud_total=longitud_total)
        return render_template('ejercicio2.html')


if __name__== '__main__':
    app.run()
