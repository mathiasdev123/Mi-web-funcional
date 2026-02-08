"""un simple flask"""

from flask import Flask, request

import random

app = Flask(__name__)

nombres = ["Isaias", "Pedro", "Mathias", "Eliud"]

facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route("/")
def hello_world():
    """estoy imprimiendo hello world"""
    return f'<h1>Hello, {random.choice(nombres)}!</h1><a href="/random-facts">¡Ver un dato aleatorio!</a>'

@app.route("/random-facts")
def datos():
    """estoy imprimiendo un dato random"""
    return f'<h1>{random.choice(facts_list)}!</h1>'

@app.route("/secret", methods=['GET', 'POST'])
def secret():
    """pagina secreta"""
    info_seguridad = "Esperando datos..."
    puntos = 0
    if request.method == 'POST':
        password = request.form.get('clave_usuario')
        puntos += len(password) * 2
        if any(c.isdigit() for c in password): puntos += 5
        if any(not c.isalnum() for c in password): puntos += 10
        caracteres_unicos = len(set(password))
        if caracteres_unicos < len(password):
            descuento = len(password) - caracteres_unicos
            puntos -= descuento * 3  # Penalizamos por cada letra repetida
        if puntos > 25:
            info_seguridad = f"Nivel MIT: ¡Caos Total! 🚀 ({puntos} pts)"
        elif puntos > 10:
            info_seguridad = f"Nivel Medio: Aceptable ⚖️ ({puntos} pts)"
        else:
            info_seguridad = f"Baja Entropía: Demasiada repetición o muy corta 💀 ({puntos} pts)"
    return f"""
    <html>
        <body>
            <h1>Analizador de Seguridad - Mathias Dev & Science</h1>
            <form method="POST">
                <input type="text" name="clave_usuario" placeholder="Contraseña">
                <button type="submit">Ejecutar Análisis</button>
            </form>
            <hr>
            <p><strong>Resultado:</strong> {info_seguridad}</p>
        </body>
    </html>
    """
    
app.run(debug=True)
