
Páginas web
-----------
- /            Inicio
- /about/      Sobre nosotros
- /menu/       Menú (público)
- /book/       Formulario de reserva
- /reservations/  Reservas por fecha

Endpoints de la API
-------------------
Todas las rutas van con el prefijo http://127.0.0.1:8000

1. Menú (público)
   GET    /api/menu-items/            Lista de platos. No requiere autenticación.
   GET    /api/menu-items/<id>/       Detalle de un plato. No requiere autenticación.
   POST   /api/menu-items/            Crear plato. Solo administrador.
   PUT    /api/menu-items/<id>/       Editar plato. Solo administrador.
   DELETE /api/menu-items/<id>/       Borrar plato. Solo administrador.

2. Reservas (requiere auth)
   GET    /api/bookings/?date=AAAA-MM-DD   Reservas de una fecha. no requiere autenticación.
   POST   /api/bookings/                   Crear reserva. Requiere autenticación.

   Cuerpo JSON para POST:
       {
           "name": "Ana",
           "persons": 2,
           "reservation_date": "2030-05-10"
       }

3. Registro de usuarios
   POST   /api/registration/
   Cuerpo JSON:
       {
           "username": "maria",
           "password": "Lemon-pass-123"
       }

4. Obtener token de autenticación
   POST   /api/api-token-auth/
   Cuerpo JSON:
       {
           "username": "maria",
           "password": "Lemon-pass-123"
       }
 
