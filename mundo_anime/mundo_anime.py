import reflex as rx

def index() -> rx.Component:
    return rx.container(
        # Botón para cambiar el tema
        rx.color_mode.button(position="absolute", top="1rem", right="1rem"),
        
        # Contenedor principal de la página
        rx.vstack(
            # Contenedor para el título, texto y botones en la parte superior
            rx.hstack(
                # Columna de imágenes a la izquierda
                rx.vstack(
                    rx.image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShGtR5WLBTwk0nSUtsTDKuK0ZJOtIEYhuJng&s",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4ZJhG3QU42u7GnU6vXXlMrdUS11MLw7LM4w&s",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="4",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_right="2rem",  # Espaciado entre las imágenes y el contenido de la derecha
                ),
                
                # Espaciador para centrar el título y texto
                rx.spacer(flex="1"),  # Esto asegura que el contenido se quede centrado
                
                # Contenedor para el título, texto y botones en la parte derecha
                rx.vstack(
                    # Contenedor con título y texto
                    rx.vstack(
                        # Título centrado
                        rx.heading("¡bienvenido al mundo anime!", size="2xl", color="white", text_align="center"),
                        
                        # Descripción centrada
                        rx.text(
                            "app anime es una aplicación móvil diseñada para conectar a los amantes del anime con una amplia gama de generos . "
                            "Su nombre evoca la imagen de un manantial de generos , haciendo referencia a la abundancia y variedad de opciones que ofrece la aplicación.",
                            size="md",
                            color="white",
                            max_width="40rem",
                            text_align="center",  # Centrado del texto
                            margin_top="1rem",  # Margen superior para el texto
                        ),
                        spacing="6",  # Espaciado entre el título y el texto
                        align="center",  # Alineación centrada
                    ),
                    
                    # Botones en la parte superior derecha
                    rx.hstack(
                        # Botón "Regístrate aquí"
                        rx.link(
                            rx.button("¡Regístrate aquí!", color_scheme="green"),
                            href="https://forms.gle/BfwikmNBEuvo3EeT9",
                            is_external=True,
                        ),  
                        # Botón "Facebook" 
                        rx.link(
                            rx.button(rx.icon(tag="facebook"), color_scheme="blue"),
                            href="https://facebook.com",
                            is_external=True,
                        ),
                        # Botón "Instagram"
                        rx.link(
                            rx.button(rx.icon(tag="instagram"), color_scheme="pink"),
                            href="https://instagram.com",
                            is_external=True,
                        ),
                        spacing="4",  # Espaciado entre los botones
                        align="end",  # Alineación de los botones a la derecha
                    ),
                    
                    # Espaciado para que los botones no se peguen al contenido
                    margin_top="2rem",
                ),
                
                # Columna de imágenes a la derecha
                rx.vstack(
                    rx.image(
                        src="https://i0.wp.com/www.hanamidango.com/wp-content/uploads/2023/02/Anime-taquilla-espanola-2023-Hanami-Dango-00.jpg?fit=1920%2C1080&ssl=1",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="data:image/jpeg;base64,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",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="4",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_left="2rem",  # Espaciado entre las imágenes y el contenido de la izquierda
                ),
                
                spacing="6",  # Espaciado general entre las columnas
                justify="space-between",  # Distribución equitativa de espacio entre las columnas
                align="center",  # Alineación centrada entre las columnas
            ),
            
            # Fondo y padding de la página
            bg="#000000",  # Fondo negro
            padding="2rem",
            min_height="100vh",  # Asegura que la página ocupe toda la altura de la pantalla
        ),
    )


# Crear la aplicación
app = rx.App()
app.add_page(index)