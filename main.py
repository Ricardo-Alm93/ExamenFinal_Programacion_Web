
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()

        try:
            edad = int(request.form.get("edad", ""))
            cantidad = int(request.form.get("cantidad", ""))

            if not nombre:
                error = "Debes ingresar tu nombre."
            elif edad < 0 or edad > 120:
                error = "Ingresa una edad válida."
            elif cantidad < 1:
                error = "Debes comprar al menos un tarro."
            else:
                precio_unitario = 9000
                total_original = precio_unitario * cantidad

                if edad < 18:
                    porcentaje = 0
                elif edad <= 30:
                    porcentaje = 15
                else:
                    porcentaje = 25

                descuento = total_original * porcentaje // 100
                total_final = total_original - descuento

                resultado = {
                    "nombre": nombre,
                    "original": f"${total_original:,}".replace(",", "."),
                    "porcentaje": porcentaje,
                    "descuento": f"${descuento:,}".replace(",", "."),
                    "final": f"${total_final:,}".replace(",", ".")
                }

        except ValueError:
            error = "Ingresa números válidos en edad y cantidad."

    return render_template(
        "ejercicio1.html",
        resultado=resultado,
        error=error
    )



@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    error = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "")

        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"

        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"

        else:
            error = "Usuario o contraseña incorrectos"

    return render_template(
        "ejercicio2.html",
        mensaje=mensaje,
        error=error
    )

@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")


if __name__ == "__main__":
    app.run(debug=True)
