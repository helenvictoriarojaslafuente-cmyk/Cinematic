import streamlit as st
import os
import Funciones
st.set_page_config(page_title="Cinematic", page_icon="🎬", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #141414; color: #ffffff; }
    .netflix-title { color: #E50914; font-weight: 800; font-size: 3rem; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
    .hero-banner { background: linear-gradient(to right, rgba(0,0,0,0.8), rgba(0,0,0,0.2)), url('https://nflxext.com'); padding: 50px; border-radius: 10px; margin-bottom: 20px; }
    .movie-card { background-color: #1f1f1f; padding: 15px; border-radius: 8px; text-align: center; transition: transform 0.3s; height: 100%; }
    .movie-card:hover { transform: scale(1.05); }
    .stButton>button { background-color: #E50914; color: white; border-radius: 4px; font-weight: bold; border: none; width: 100%; }
    .stButton>button:hover { background-color: #b20710; color: white; }
    </style>
""", unsafe_allow_html=True)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "role" not in st.session_state:
    st.session_state.role = None
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "cart" not in st.session_state:
    st.session_state.cart = []
if "lista_usuarios" not in st.session_state:
    st.session_state.lista_usuarios = [
        {"usuario": "jhostin", "contraseña": "7383", "rol": "administrador"},
        {"usuario": "helen", "contraseña": "2211", "rol": "administrador"},
        {"usuario": "george", "contraseña": "2838", "rol": "administrador"},
        {"usuario": "andrew", "contraseña": "1038", "rol": "administrador"}]
if "peliculas" not in st.session_state:
    st.session_state.peliculas = {}
    for p, datos in Funciones.peliculas.items():
        if len(datos) == 1 and isinstance(datos, str) and "," in datos:
            parts = [x.strip() for x in datos.split(",")]
            gen = parts
            anio = int(parts) if parts.isdigit() else 2028
            est = int(parts) if parts.isdigit() else 0
        elif len(datos) >= 3:
            gen, anio, est = datos, datos, datos
        else:
            gen, anio, est = "Accion", 2026, 0       
        clean_name = "".join(c if c.isalnum() else "_" for c in p).lower()
        st.session_state.peliculas[p] = {
            "genero": gen,
            "año": int(anio) if str(anio).isdigit() else 2026,
            "estrellas": int(est) if str(est).isdigit() else 5,
            "precio": 9.99,
            "imagen": f"img/{clean_name}.png"}
if "sugerencias" not in st.session_state:
    st.session_state.sugerencias = []
if not st.session_state.logged_in:
    if st.session_state.page == "welcome":
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 class='netflix-title'>CINEMATIC</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("INGRESAR", use_container_width=True):
                st.session_state.page = "login"
                st.rerun()            
    elif st.session_state.page == "login":
        st.markdown("<h1 class='netflix-title' style='font-size: 2rem;'>Inicia Sesión</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            with st.form("login_form"):
                usuario_input = st.text_input("Usuario")
                password_input = st.text_input("Contraseña", type="password")
                submit_login = st.form_submit_button("Entrar")
                if submit_login:
                    encontrado = False
                    for u in st.session_state.lista_usuarios:
                        if u["usuario"].lower() == usuario_input.strip().lower() and u["contraseña"] == password_input.strip():
                            st.session_state.logged_in = True
                            st.session_state.user = u["usuario"]
                            st.session_state.role = u["rol"]
                            st.session_state.page = "main"
                            encontrado = True
                            break
                    if encontrado:
                        st.success("¡Acceso concedido!")
                        st.rerun()
                    else:
                        st.error("Usuario o contraseña incorrectos.")
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>¿No tienes una cuenta?</p>", unsafe_allow_html=True)
            if st.button("Crear cuenta nueva"):
                st.session_state.page = "register"
                st.rerun()                
    elif st.session_state.page == "register":
        st.markdown("<h1 class='netflix-title' style='font-size: 2rem;'>Crear Cuenta Nueva</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            nuevo_user = st.text_input("Nombre de usuario")
            nueva_pass = st.text_input("Nueva contraseña", type="password")
            if st.button("Siguiente"):
                if nuevo_user.isalpha() and nueva_pass.isdigit() and len(nueva_pass) == 4:
                    st.session_state.temp_nuevo_user = nuevo_user
                    st.session_state.temp_nueva_pass = nueva_pass
                    st.session_state.page = "terms"
                    st.rerun()
                else:
                    st.error("El usuario debe tener solo letras y la contraseña exactamente 4 números.")
            if st.button("Volver al Inicio"):
                st.session_state.page = "login"
                st.rerun()               
    elif st.session_state.page == "terms":
        st.markdown("<h2 style='color: #E50914;'>Términos y Condiciones de Uso</h2>", unsafe_allow_html=True)
        st.write("Por favor, lee detenidamente las siguientes condiciones antes de unirte a Cinematic:")
        st.text_area("TÉRMINOS Y CONDICIONES DE USO Y SERVICIO", """
        
Bienvenido a nuestro sitio

Los presentes Términos y Condiciones regulan el acceso, navegación y uso del sitio web, aplicaciones móviles y plataformas digitales de [Nombre de la Tienda de Películas] (en adelante, "la Empresa", "nosotros" o "la Tienda"). Al acceder, registrarse o realizar cualquier transacción en nuestra plataforma, usted (en adelante, "el Usuario" o "el Cliente") acepta de manera expresa, automática e incondicional todos los términos aquí descritos. Si no está de acuerdo con estos términos, deberá abstenerse de utilizar el sitio y sus servicios.

Lo que necesita saber sobre su cuenta

Para acceder a ciertas funcionalidades de la Tienda, como realizar compras, rentar contenido o guardar listas de reproducción, el Usuario debe registrarse y crear una cuenta de perfil única y personal.
• Exactitud de los datos: El Usuario se obliga a proporcionar información verídica, exacta, actual y completa durante el proceso de registro y a mantenerla actualizada.
• Seguridad de las credenciales: El Cliente es el único responsable de salvaguardar la confidencialidad de su contraseña y nombre de usuario. Cualquier actividad realizada bajo su cuenta se considerará autorizada por él.
• Uso personal e intransferible: Las cuentas son estrictamente personales. No está permitido vender, ceder, transferir ni compartir el acceso a la cuenta con terceras personas.
• Cancelación de la cuenta: La Empresa se reserva el derecho de suspender, restringir o cancelar de forma definitiva cualquier cuenta que infrinja estos términos, sin necesidad de previo aviso y sin derecho a indemnización alguna.

Cómo funcionan nuestras ventas y licencias

[Nombre de la Tienda de Películas] ofrece contenidos audiovisuales bajo diferentes modalidades, las cuales se rigen por las siguientes reglas:

1. Formato Físico (DVD, Blu-ray, 4K Ultra HD)

• Disponibilidad: El catálogo físico está sujeto a existencias de inventario. Si un producto no está disponible tras la compra, se notificará al Cliente y se reembolsará el dinero.
• Envíos y entregas: Los tiempos de envío son estimados y pueden variar por causas ajenas a la Empresa (logística de terceros, aduanas, clima). El riesgo de pérdida se transfiere al Cliente al momento de la entrega por parte de la paquetería.

2. Formato Digital (Compra / Venta Digital)

• Licencia de uso: La "compra" de una película digital no otorga la propiedad del archivo audiovisual al Cliente. Se le concede una licencia no exclusiva, revocable, personal y no transferible para visualizar el contenido de manera privada y con fines no comerciales.
• Acceso continuo: El acceso a la película digital se mantendrá disponible en la nube de la plataforma mientras la Empresa conserve los derechos de distribución de dicho título. La Empresa no se hace responsable si un estudio de cine retira los derechos de una obra.

3. Renta Digital (Alquiler)

• Ventanas de tiempo: Al rentar una película, el Cliente dispone de un plazo estándar de 30 días para iniciar la reproducción. Una vez iniciada la película por primera vez, el Cliente dispondrá de un periodo de 48 horas continuas para verla tantas veces como desee. Expirado el plazo, el contenido desaparecerá automáticamente de su biblioteca.

Precios, pagos y facturación

• Modificación de precios: Todos los precios expuestos en la Tienda están sujetos a cambios sin previo aviso. Las promociones y descuentos tienen una vigencia limitada y específica.
• Impuestos y cargos adicionales: Los precios mostrados incluyen o desglosan los impuestos aplicables según la legislación de [País/Región]. El Cliente es responsable de cualquier cargo impuesto por su proveedor de tarjeta de crédito o banco (como comisiones por transacciones internacionales).
• Métodos de pago: Se aceptan tarjetas de crédito, débito, plataformas de pago electrónico autorizadas y tarjetas de regalo de la Tienda. Al ingresar un método de pago, el Cliente garantiza que tiene el derecho legal de utilizarlo.

Políticas de cambios, devoluciones y reembolsos

Debido a la naturaleza del producto, las políticas varían según el formato:
• Productos Digitales (Compras y Rentas): No se admiten cambios, devoluciones ni reembolsos una vez que se ha iniciado la transmisión (streaming) o la descarga del archivo audiovisual, salvo por fallas técnicas imputables directamente a la plataforma que impidan la visualización total del contenido.
• Productos Físicos: El Cliente dispone de un plazo de [Número, ej. 14] días naturales desde la recepción del producto para solicitar una devolución. El artículo debe devolverse cerrado, en su empaque original sellado de fábrica (celofán intacto) y sin muestras de uso. Los costos de envío por devolución correrán a cargo del Cliente, a menos que el producto haya llegado defectuoso o dañado de origen.

Derechos de autor y propiedad intelectual

Todo el contenido disponible en [Nombre de la Tienda de Películas] —incluyendo, de forma enunciativa pero no limitativa: películas, tráilers, audios, textos, logotipos, gráficos, interfaces de usuario, códigos fuente y software— es propiedad exclusiva de la Empresa o de sus respectivos licenciantes (estudios de cine, distribuidores) y está protegido por las leyes de propiedad intelectual internacionales.
Queda estrictamente prohibido:
1. Copiar, reproducir, redistribuir, transmitir, retransmitir, exhibir públicamente o vender el contenido de la plataforma.
2. Utilizar herramientas informáticas de extracción de datos, ripeo, grabación de pantalla o decodificación de sistemas de protección contra copia (DRM).
3. Utilizar el contenido de la Tienda para alimentar, entrenar o desarrollar sistemas de Inteligencia Artificial o algoritmos de aprendizaje automático.

Reglas de conducta en la plataforma

El Usuario se compromete a utilizar la plataforma de manera legal, ética y pacífica. Queda prohibido:
• Publicar reseñas de películas que contengan lenguaje obsceno, difamatorio, racista, de odio o que constituyan acoso.
• Intentar vulnerar la seguridad del sitio web, inyectar virus informáticos, malware o realizar ataques de denegación de servicio (DDoS).
• Utilizar la sección de comentarios o reseñas para promocionar productos de terceros o enviar spam.

Limitación de responsabilidad técnica

La Empresa se esfuerza por mantener la plataforma activa las 24 horas del día, los 7 días de la semana. Sin embargo, no garantiza un servicio ininterrumpido o libre de errores.
• Calidad de reproducción: La calidad de transmisión (HD, 4K, HDR, etc.) de los contenidos digitales depende directamente de las especificaciones del dispositivo del Cliente, de su proveedor de internet y del ancho de banda disponible. La Empresa no es responsable por problemas de congelamiento de pantalla o almacenamiento en búfer causados por conexiones deficientes.
• Mantenimiento del sitio: El acceso al sitio puede suspenderse temporalmente y sin previo aviso debido a fallas del sistema, labores de mantenimiento, actualizaciones tecnológicas o causas de fuerza mayor.

Modificaciones a estos términos

Nos reservamos el derecho de modificar, actualizar o reformar este documento en cualquier momento para adaptarlo a novedades legislativas, cambios en el modelo de negocio o mejoras técnicas. Cualquier cambio será publicado en esta misma sección, indicando la fecha de la última actualización. El uso continuo de la plataforma posterior a dicha publicación constituye la aceptación de las nuevas condiciones.

Jurisdicción y ley aplicable

Para la interpretación, cumplimiento y resolución de cualquier controversia derivada de los presentes Términos y Condiciones, las partes se someten expresamente a la legislación vigente en [Ciudad/País], renunciando a cualquier otro fuero que pudiera corresponderles por razón de sus domicilios presentes o futuros.
Si tiene alguna pregunta, duda o reclamación respecto a estos Términos y Condiciones, puede ponerse en contacto con nuestro equipo legal a través del correo electrónico 
        """, height=200)
        aceptar_terminos = st.checkbox("He leído y acepto los Términos y Condiciones")
        if st.button("Finalizar Registro"):
            if aceptar_terminos:
                nuevo_perfil = {
                    "usuario": st.session_state.temp_nuevo_user,
                    "contraseña": st.session_state.temp_nueva_pass,
                    "rol": "cliente"}
                st.session_state.lista_usuarios.append(nuevo_perfil)
                st.success("¡Cuenta creada exitosamente! Ya puedes iniciar sesión.")
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error("Debes aceptar los términos y condiciones para continuar.")
else:
    if st.session_state.page == "checkout":
        st.markdown("<h1 class='netflix-title' style='font-size: 2rem;'>Pasarela de Pago - Cinematic</h1>", unsafe_allow_html=True)
        total_pagar = sum(item['precio'] for item in st.session_state.cart)
        st.write(f"### Total a pagar: ${total_pagar:.2f}")
        with st.form("payment_form"):
            st.write("Introduce los datos de tu tarjeta")
            nombre_tarjeta = st.text_input("Nombre en la tarjeta")
            numero_tarjeta = st.text_input("Número de tarjeta", max_chars=16)
            exp_tarjeta = st.text_input("Fecha de expiración (MM/AA)")
            cvv_tarjeta = st.text_input("CVV", type="password", max_chars=3)
            btn_pagar = st.form_submit_button("Confirmar y Pagar")
            if btn_pagar:
                if len(numero_tarjeta) == 16 and len(cvv_tarjeta) == 3:
                    ultimos_digitos = numero_tarjeta[-4:]
                    st.balloons()
                    st.success(f" ¡Compra realizada con éxito! Tarjeta terminada en ****{ultimos_digitos}. ¡Que disfrutes tus películas! 🍿")
                    st.session_state.cart = []
                else:
                    st.error("Por favor, ingresa un número de tarjeta válido de 16 dígitos y un CVV de 3 dígitos.")
        if st.button("Volver al Catálogo"):
            st.session_state.page = "main"
            st.rerun()
    else:
        col_logo, col_user, col_cart = st.columns([2, 2, 1])
        with col_logo:
            st.markdown("<h2 style='color: #E50914; margin:0;'>CINEMATIC</h2>", unsafe_allow_html=True)
        with col_user:
                    st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Cerrar Sesión"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.role = None
            st.session_state.cart = []
            st.session_state.page = "welcome"
            st.rerun()
        with col_cart:
            cart_total = sum(item['precio'] for item in st.session_state.cart)
            with st.popover(f"🛒 Carrito ({len(st.session_state.cart)}) - ${cart_total:.2f}"):
                if not st.session_state.cart:
                    st.write("Tu carrito está vacío.")
                else:
                    for idx, movie in enumerate(st.session_state.cart):
                        st.write(f"- {movie['titulo']} (${movie['precio']})")
                    if st.button("Comprar ahora"):
                        st.session_state.page = "checkout"
                        st.rerun()
        st.markdown("---")               
        if st.session_state.role == "administrador":
            st.markdown("<h2>Panel de Control - Administrator</h2>", unsafe_allow_html=True)
            admin_op = st.selectbox("Selecciona una acción de gestión", [
                "Ver Catálogo Completo",
                "Agregar Nueva Película",
                "Subir / Modificar Precio de Película",
                "Eliminar Película",
                "Revisar Buzón de Sugerencias"])
            if admin_op == "Ver Catálogo Completo":
                for p, datos in st.session_state.peliculas.items():
                    st.write(f"🎬 **{p}** ({datos['año']}) | Género: {datos['genero']} | Precio: ${datos['precio']} | Estrellas: {datos['estrellas']}")
            elif admin_op == "Agregar Nueva Película":
                nueva_peli = st.text_input("Nombre de la película")
                nuevo_genero = st.selectbox("Género", ["Accion", "Comedia", "Drama", "Ciencia Ficción", "Fantasía", "Terror", "Romance", "Animación", "Musical", "Documental"])
                nuevo_anio = st.number_input("Año de estreno", min_value=1900, max_value=2030, value=2026)
                nuevo_precio = st.number_input("Precio ($)", min_value=0.0, value=9.99)
                if st.button("Guardar Película"):
                    if nueva_peli:
                        clean_name = "".join(c if c.isalnum() else "_" for c in nueva_peli).lower()
                        st.session_state.peliculas[nueva_peli] = {
                            "genero": nuevo_genero,
                            "año": nuevo_anio,
                            "estrellas": 5,
                            "precio": nuevo_precio,
                            "imagen": f"img/{clean_name}.png"}
                        st.success(f"¡Película '{nueva_peli}' agregada correctamente!")
                    else:
                        st.error("El nombre no puede estar vacío.")
            elif admin_op == "Subir / Modificar Precio de Película":
                peli_a_modificar = st.selectbox("Selecciona la película", list(st.session_state.peliculas.keys()))
                precio_actual = st.session_state.peliculas[peli_a_modificar]['precio']
                st.write(f"Precio actual: ${precio_actual}")
                nuevo_precio = st.number_input("Nuevo precio ($)", min_value=0.0, value=precio_actual)
                if st.button("Actualizar Precio"):
                    st.session_state.peliculas[peli_a_modificar]['precio'] = nuevo_precio
                    st.success(f"¡El precio de '{peli_a_modificar}' se actualizó a ${nuevo_precio}!")
            elif admin_op == "Eliminar Película":
                peli_a_eliminar = st.selectbox("Selecciona película a eliminar", list(st.session_state.peliculas.keys()))
                if st.button("Eliminar definitivamente"):
                    del st.session_state.peliculas[peli_a_eliminar]
                    st.success(f"Película '{peli_a_eliminar}' eliminada del sistema.")
                    st.rerun()
            elif admin_op == "Revisar Buzón de Sugerencias":
                if not st.session_state.sugerencias:
                    st.write("El buzón está vacío.")
                else:
                    for s in st.session_state.sugerencias:
                        st.write(f"📌 {s}")                        
        elif st.session_state.role == "cliente":
            col_search1, col_search2 = st.columns(2)
            with col_search1:
                buscador_input = st.text_input("🔍 Buscar película por título:")
            with col_search2:
                generos_disponibles = ["Todos", "Accion", "Comedia", "Drama", "Ciencia Ficción", "Fantasía", "Terror", "Romance", "Animación", "Musical", "Documental"]
                genero_seleccionado = st.selectbox("Filtrar por Género:", generos_disponibles)
                
            st.markdown("""
                <div class='hero-banner'>
                    <h1>Estreno Destacado de la Semana</h1>
                    <p>Disfruta de las mejores producciones cinematográficas en alta definición.</p>
                </div>
            """, unsafe_allow_html=True)
            
            pelis_filtradas = st.session_state.peliculas
            if genero_seleccionado != "Todos":
                pelis_filtradas = {k: v for k, v in pelis_filtradas.items() if v['genero'] == genero_seleccionado}
            if buscador_input:
                pelis_filtradas = {k: v for k, v in pelis_filtradas.items() if buscador_input.lower() in k.lower()}
                
            if not pelis_filtradas:
                st.warning("No se encontraron películas que coincidan con los filtros seleccionados.")
            else:
                st.markdown("### 🔥 Resultados del Catálogo")
                cols_vistos = st.columns(4)
                idx = 0
                for p, datos in pelis_filtradas.items():
                    with cols_vistos[idx % 4]:
                        if os.path.exists(datos["imagen"]):
                            st.image(datos["imagen"], use_column_width=True)
                        else:
                            st.info(f" [Colocar imagen: {datos['imagen']}]")
                        st.markdown(f"""
                            <div class='movie-card'>
                                <h4>{p}</h4>
                                <p><b>Género:</b> {datos['genero']}</p>
                                <p><b>Año:</b> {datos['año']}</p>
                                <p><b>Precio:</b> ${datos['precio']}</p>
                                <p>⭐ {datos['estrellas']} Estrellas</p>
                            </div>
                        """, unsafe_allow_html=True)
                        if st.button(f"Agregar al Carrito", key=f"cart_peli_{p}"):
                            st.session_state.cart.append({"titulo": p, "precio": datos['precio']})
                            st.success(f"¡'{p}' agregado al carrito!")
                            st.rerun()
                    idx += 1
                    
            st.markdown("<br><hr>", unsafe_allow_html=True)
            st.markdown("### 💡 ¿No encuentras tu película?")
            idea_peli = st.text_input("Propón un título para el catálogo:")
            if st.button("Enviar Propuesta"):
                if idea_peli:
                    st.session_state.sugerencias.append(f"'{idea_peli}' propuesto por {st.session_state.user}")
                    st.success("¡Gracias por tu sugerencia! El administrador la revisará.")
                    
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Cerrar Sesión"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.role = None
            st.session_state.cart = []
            st.session_state.page = "welcome"
            st.rerun()