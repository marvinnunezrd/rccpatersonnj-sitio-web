# Datos institucionales reales (Base_de_Datos_RCC_Paterson.xlsx, calendario Google, guias pastorales)

COMITE = [
    ("Rev. Yasid Salas", "Director Espiritual", "St. Therese de Lisieux, Paterson"),
    ("Teresa Amparo", "Coordinadora General Diocesana", "St. Paul, Clifton"),
    ("Librada Rosario", "Sub-Coordinadora Diocesana", "Our Lady of Lourdes, Paterson"),
    ("Dariberkis Taveras-Beato", "Secretaria Diocesana", "St. Stephen, Paterson"),
    ("Alis Amparo", "Tesorero", "St. John the Baptist, Paterson"),
    ("Juana De Jesús", "Directora Escuela de Formación de Líderes (EFL)", "St. Therese de Lisieux, Paterson"),
    ("Marvin Núñez", "Director de Ministerios de Música y Comunicación/Publicidad", "St. Anthony of Padua, Passaic"),
    ("Marizabel Pérez", "Coordinadora Ministerio de Intercesión", "St. Anthony of Padua, Passaic"),
]

ZONA_COORDINADORES = [
    ("Zona A", "Santos Arroyo"),
    ("Zona B", "María Santana"),
    ("Zona C", "Juan Matías"),
    ("Zona D", "(Vacante)"),
]

# Grupos de oración, uno por diccionario. "horario": la Base de Datos no registra la hora
# exacta de cada grupo (solo el dia) -- 2026-08-20 Marvin pidio usar "7:00 pm - 9:30 pm" como
# horario provisional para los grupos mientras se confirma el horario real de cada uno.
# "direccion" y "zona" fueron verificadas/cruzadas 2026-08-20 contra la hoja "Parrocos (Referencia)"
# de Base_de_Datos_RCC_Paterson.xlsx (columna "Ciudad / Zona") y sitios oficiales de cada parroquia.
GRUPOS_ORACION = [
    {"dia": "Lunes", "horario": "7:00 pm – 9:30 pm", "grupo": "St. Anthony of Padua", "parroquia": "St. Anthony of Padua, Paterson",
     "direccion": "138 Beech St, Paterson, NJ 07501", "coordinador": "Mario Hernández", "telefono": "(201) 932-4591", "zona": "Zona A"},
    {"dia": "Lunes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Luz de Cristo\"", "parroquia": "St. Anthony of Padua, Passaic",
     "direccion": "101-103 Myrtle Ave, Passaic, NJ 07055", "coordinador": "Angela Mieses", "telefono": "(973) 687-1119", "zona": "Zona C"},
    {"dia": "Lunes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Luz y Vida\"", "parroquia": "Catedral San Juan Bautista, Paterson",
     "direccion": "381 Grand St, Paterson, NJ 07505", "coordinador": "Alis Amparo", "telefono": "(973) 356-2543", "zona": "Zona A"},

    {"dia": "Martes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Alfa y Omega\"", "parroquia": "St. Stephen, Paterson",
     "direccion": "86 Martin St, Paterson, NJ 07501", "coordinador": "Sandra García", "telefono": "(973) 816-7291", "zona": "Zona A"},
    {"dia": "Martes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"María Auxiliadora\"", "parroquia": "St. Mary Help of Christians, Paterson",
     "direccion": "410 Union Ave, Paterson, NJ 07502", "coordinador": "Luz Rivas", "telefono": "(862) 213-7760", "zona": "Zona B"},
    {"dia": "Martes", "horario": "7:00 pm – 9:30 pm", "grupo": "Our Lady of Lourdes", "parroquia": "Our Lady of Lourdes, Paterson",
     "direccion": "440 River St, Paterson, NJ 07524", "coordinador": "Rosy Taveras", "telefono": "(973) 849-5180", "zona": "Zona B"},
    {"dia": "Martes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Luz de María\"", "parroquia": "St. Mary Assumption, Passaic",
     "direccion": "181 Market St, Passaic, NJ 07055", "coordinador": "Crecita Reyes", "telefono": "(973) 653-7911", "zona": "Zona C"},
    {"dia": "Martes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Ríos de Agua Viva\"", "parroquia": "St. Brendan, Clifton",
     "direccion": "154 East First St, Clifton, NJ 07011", "coordinador": "María García", "telefono": "(973) 930-8429", "zona": "Zona C"},
    {"dia": "Martes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Vive Jesús: El Amor\"", "parroquia": "St. Paul, Clifton",
     "direccion": "124 Union Ave, Clifton, NJ 07011", "coordinador": "Roberto Boiter", "telefono": "(646) 879-4655", "zona": "Zona C"},

    {"dia": "Miércoles", "horario": "7:00 pm – 9:30 pm", "grupo": "Our Lady of Victories", "parroquia": "Our Lady of Victories, Paterson",
     "direccion": "169 Broadway, Paterson, NJ 07501", "coordinador": "Israel Torres", "telefono": "(862) 271-9966", "zona": "Zona B"},
    {"dia": "Miércoles", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Los Amigos de Jesús\"", "parroquia": "St. Therese de Lisieux, Paterson",
     "direccion": "80 13th Ave, Paterson, NJ 07504", "coordinador": "Reyna Nuesi", "telefono": "(201) 832-3010", "zona": "Zona B"},
    {"dia": "Miércoles", "horario": "7:00 pm – 9:30 pm", "grupo": "\"La Anunciación\"", "parroquia": "Sts. Cyril & Methodius, Clifton",
     "direccion": "218 Ackerman Ave, Clifton, NJ 07011", "coordinador": "Andrea Hernández", "telefono": "(973) 930-3850", "zona": "Zona C"},

    {"dia": "Jueves", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Alfa y Omega\"", "parroquia": "St. Joseph, Paterson",
     "direccion": "399 Market St, Paterson, NJ 07501", "coordinador": "Antonia Hernández (Henríquez)", "telefono": "(862) 600-4353", "zona": "Zona A"},
    {"dia": "Jueves", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Resurrección de Jesús\"", "parroquia": "St. Gerard Majella, Paterson",
     "direccion": "501 West Broadway, Paterson, NJ 07522", "coordinador": "Edelmira Chollet (-Reyes)", "telefono": "(201) 341-3949", "zona": "Zona B"},
    {"dia": "Jueves", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Santísima Trinidad\"", "parroquia": "Holy Trinity, Passaic",
     "direccion": "226 Harrison St, Passaic, NJ 07055", "coordinador": "Tony Jiménez", "telefono": "(973) 653-8469", "zona": "Zona C"},
    {"dia": "Jueves", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Camino y Vida\"", "parroquia": "Sacred Heart & Holy Rosary, Dover",
     "direccion": "4 Richards Ave, Dover, NJ 07801", "coordinador": "Karla Osorto", "telefono": "(973) 349-4700", "zona": "Zona D"},

    {"dia": "Viernes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Verdad y Vida\"", "parroquia": "Our Lady of Fatima & St. Nicholas, Passaic",
     "direccion": "153 Washington Pl, Passaic, NJ 07055", "coordinador": "Susano José (Joseito)", "telefono": "(862) 571-7598", "zona": "Zona C"},
    {"dia": "Viernes", "horario": "7:00 pm – 9:30 pm", "grupo": "\"Sal y Luz del Mundo\"", "parroquia": "St. Margaret of Scotland, Morristown",
     "direccion": "6 Sussex Ave, Morristown, NJ 07960", "coordinador": "Daniel Cornejo", "telefono": "(202) 286-0759", "zona": "Zona D"},
]

AGENDA = [
  ("20","SEP","2026","Gran Asamblea Diocesana – Septiembre 2026","2:30 pm – 6:00 pm","Salón Principal de la Escuela Santa Teresita, 765 14th Ave, Paterson, NJ 07504","Predicación: Diácono José Luis Abreu · Música: Marvin Núñez","eventos/gran-asamblea-septiembre-2026.html"),
  ("26","SEP","2026","Encuentro Regional 2026 — Llamados a la Santidad","9:00 am – 6:00 pm","Parroquia Our Lady of Libera, 5808 John F Kennedy Blvd, West New York, NJ 07093","Predican Su Excelencia Pedro Bismarck Chau (Obispo Auxiliar de Newark) y Mons. Joseph Malagreca · Donación: $30 (incluye almuerzo)","eventos/encuentro-regional-2026.html"),
  ("24–25","OCT","2026","Gran Congreso de Sanación y Liberación","Sáb. 9:00 am – 5:00 pm · Dom. 2:30 pm – 6:00 pm","Ubicación por confirmar","Predicación: Osvaldo Fernández, P. Starli Castaños (sáb.) y P. Yasid Salas (dom.)"),
  ("15","NOV","2026","Gran Asamblea Diocesana – Noviembre 2026","2:30 pm – 6:00 pm","Salón Principal de la Escuela Santa Teresita, 765 14th Ave, Paterson, NJ 07504","Predicación: María Batista"),
  ("20","DIC","2026","Gran Asamblea Diocesana – Diciembre 2026","2:30 pm – 6:00 pm","Salón Principal de la Escuela Santa Teresita, 765 14th Ave, Paterson, NJ 07504",""),
]

# URLs de los sitios web oficiales de cada parroquia (verificadas 2026-08-22 --
# se confirmo cada sitio contra la direccion real de la parroquia antes de
# enlazarlo). Las llaves deben coincidir EXACTAMENTE con el texto usado en
# COMITE (tercer valor de cada tupla) y en GRUPOS_ORACION (campo "parroquia").
# Si una parroquia llega a faltar aqui, su nombre se muestra como texto plano
# (sin enlace) en vez de fallar la construccion del sitio.
PARROQUIA_URLS = {
    "St. Anthony of Padua, Paterson": "https://stanthonypaterson.com/",
    "St. Anthony of Padua, Passaic": "https://stanthonypassaic.org/",
    "Catedral San Juan Bautista, Paterson": "https://rcdopcathedral.org/",
    "St. John the Baptist, Paterson": "https://rcdopcathedral.org/",
    "St. Stephen, Paterson": "https://saintstephensparish.com/",
    "St. Mary Help of Christians, Paterson": "https://stmarypaterson.org/",
    "Our Lady of Lourdes, Paterson": "https://ollourdespaterson.org/",
    "St. Mary Assumption, Passaic": "https://stmarypassaic.org/",
    "St. Brendan, Clifton": "https://stbrendan-george.org/",
    "St. Paul, Clifton": "https://www.stpaulcnj.org/",
    "Our Lady of Victories, Paterson": "https://olvjude.org/",
    "St. Therese de Lisieux, Paterson": "https://www.sttheresepaterson.com/",
    "Sts. Cyril & Methodius, Clifton": "https://sscmrcchurch.org/",
    "St. Joseph, Paterson": "https://www.sanjosepaterson.org/",
    "St. Gerard Majella, Paterson": "https://stgerardmajella.org/",
    "Holy Trinity, Passaic": "https://holytrinitypassaic.com/",
    "Sacred Heart & Holy Rosary, Dover": "https://sacredheart-dover.com/",
    "Our Lady of Fatima & St. Nicholas, Passaic": "https://fatimanicholas.org/",
    "St. Margaret of Scotland, Morristown": "https://csmargaret.org/",
}

MINISTERIOS = [
  ("m_intercesion","Intercesión","El corazón orante de la Renovación: sostiene en oración a la comunidad, los eventos y a cada líder diocesano.","ministerios/intercesion.html"),
  ("m_hombres","Hombres de Alabanza","Ministerio Diocesano de Acompañamiento Espiritual para el hombre: fraternidad, oración y sanación interior para vivir con fe su llamado como hijo de Dios, esposo y padre.","ministerios/hombres-alabanza.html"),
  ("m_mujeres","Mujeres de Alabanza","Ministerio Diocesano de Acompañamiento Espiritual para la mujer: escucha, oración y acompañamiento en momentos de dolor, inspirado en María.","ministerios/mujeres-alabanza.html"),
  ("m_comunicacion","Comunicación y Publicidad","Evangelización a través de los medios: diseño, redes sociales e identidad de marca de toda la RCC Paterson.","#ministerios"),
  ("m_musica","Ministerios de Música","Coordina, forma y anima a todos los grupos de música de la RCC Paterson. La música es oración, no espectáculo.","ministerios/musica.html"),
  ("m_youth","RCC Youth","Acompaña a los jóvenes en su encuentro personal con Jesucristo y los envía como evangelizadores a sus familias y escuelas.","#ministerios"),
  ("escudo_efl","Escuela de Formación de Líderes","Forma y madura servidores capaces de liderar con sabiduría y fidelidad, desde lo humano, lo espiritual y lo doctrinal.","ministerios/escuela-formacion-lideres.html"),
  ("m_sve","Seminario de Vida en el Espíritu","La puerta de entrada a la Renovación: siete sesiones que renuevan la fe bautismal y abren a los dones del Espíritu Santo.","#ministerios"),
]

# Departamentos internos de apoyo (no son ministerios). Decision de Marvin
# 2026-08-22: sin logo propio ni iconos estilo emoji/redes sociales; solo
# mencion textual (nombre, descripcion y contacto de coordinadores) en su
# propia seccion del sitio. Telefonos en el mismo formato que GRUPOS_ORACION
# para reutilizar _tel_href() sin cambios.
DEPARTAMENTOS = [
    {
        "nombre": "Librería",
        "descripcion": "Cuenta con toda clase de objetos religiosos y sacramentales que ayudan a fortalecer la vida espiritual, tanto de los servidores como de todos los hermanos que asisten a nuestros eventos. Está presente en cada uno de ellos, para que la comunidad pueda acercarse y adquirirlos. No cuenta con catálogo en línea: para hacer un pedido o preguntar por la existencia de algún artículo, comunicarse directamente con el departamento a través de los siguientes contactos.",
        "coordinadores": [
            ("Luisa Mejía", "(862) 271-4805"),
            ("Cruz Acevedo", "(862) 262-1741"),
        ],
    },
    {
        "nombre": "Nutrición",
        "descripcion": "Se encarga de que, en cada evento, los hermanos reciban el sustento — alimento y bebida — que necesitan, siempre bajo el cuidado de quien coordina el departamento. Según el tipo de evento, este sustento se ofrece de manera gratuita o a la venta a un precio módico. Interesados en donar alimentos o unirse como voluntarios pueden contactar a:",
        "coordinadores": [
            ("Luis González", "(973) 879-3469"),
        ],
    },
    {
        "nombre": "Higiene",
        "descripcion": "Vela por que el salón, los baños y las demás áreas estén debidamente acondicionados en materia de higiene, antes, durante y después de cada evento — no solo en la Casa de la Renovación (Santa Teresita), sino en cualquier lugar donde nos reunamos. Interesados en donar artículos de higiene o unirse como voluntarios pueden contactar a:",
        "coordinadores": [
            ("Elizabeth Francisco", "(862) 899-2799"),
        ],
    },
    {
        "nombre": "Decoración",
        "descripcion": "Se encarga de que cada evento tenga el esplendor que merece, acorde a nuestra fe y a nuestros símbolos, y acorde también al lugar donde nos reunimos — como Dios lo merece y como merecen quienes le servimos y quienes lo buscamos. Interesados en donar o unirse como voluntarios pueden contactar a:",
        "coordinadores": [
            ("Dionicia Matías", "(862) 218-3385"),
            ("Juana Santana", "(917) 937-8169"),
            ("Nancy Ruiz", "(973) 405-0954"),
        ],
    },
]
