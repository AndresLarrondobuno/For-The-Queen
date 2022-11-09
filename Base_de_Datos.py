import sqlite3 as sql

habilidades_de_armas = { "perforar": {
                "nombre":"perforar",
                "efecto":'',
                "dano_en_area":False,
                "multiplicador_de_dano":1.1,
                'rolls':3
            },
            "desgarrar": {
                "nombre":"desgarrar",
                "efecto":'sangrado',
                "dano_en_area":False,
                "multiplicador_de_dano":1,
                'rolls':3
            },
            "sinfonia": {
                "nombre":"sinfonia",
                "efecto":'',
                "dano_en_area":True,
                "multiplicador_de_dano":0.9,
                'rolls':4
            },
            "ritardando": {
                "nombre":"ritardando",
                "efecto":'reducir_velocidad',
                "dano_en_area":False,
                "multiplicador_de_dano":0.8,
                'rolls':4
            },
            "tiro": {
                "nombre":"tiro",
                "efecto":'',
                "dano_en_area":False,
                "multiplicador_de_dano":0.9,
                'rolls':2
            },
            "tiro_de_francotirador": {
                "nombre":"tiro_de_francotirador",
                "efecto":'ignorar_armadura',
                "dano_en_area":False,
                "multiplicador_de_dano":0.9,
                'rolls':3
            },
            "maldecir": {
                "nombre":"maldecir",
                "efecto":'',
                "dano_en_area":False,
                "multiplicador_de_dano":1,
                'rolls':3
            },
            "explosion": {
                "nombre":"explosion",
                "efecto":'',
                "dano_en_area":True,
                "multiplicador_de_dano":0.9,
                'rolls':4
            }
}

items = {  "lanza": {
                "tipo":'arma',
                "habilidades": [habilidades_de_armas['perforar'], habilidades_de_armas['desgarrar']],
                "stats":{
                    'dano_base':9,     
                    'afinidad':'fuerza', 
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "arco_de_caza": {
                "tipo":'arma',
                "habilidades": [habilidades_de_armas['tiro'], habilidades_de_armas['tiro_de_francotirador']],
                "stats":{
                    'dano_base':6,      #armas
                    'afinidad':'observacion', #armas
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "laud_roto": {
                "tipo":'arma',
                "habilidades": [habilidades_de_armas['sinfonia'], habilidades_de_armas['ritardando']],
                "stats":{
                    'dano_base':6,      #armas
                    'afinidad':'talento', #armas
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "tomo_de_aprendiz": {
                "tipo":'arma',
                "habilidades": [habilidades_de_armas['maldecir'], habilidades_de_armas['explosion']],
                "stats":{
                    'dano_base':7,      #armas
                    'afinidad':'inteligencia', #armas
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "botas_viejas": {
                "tipo":'armadura',
                "habilidades":'',
                "stats":{
                    'dano_base':'',      #armas
                    'afinidad':'', #armas
                    'bonus_armadura':1,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "barba_de_dios": {
                "tipo":'consumible',
                "habilidades":'',
                "stats":{
                    'dano_base':'',      
                    'afinidad':'',
                    'efecto_en_tablero':'curacion',
                    'efecto_en_combate':'curacion',
                    'curacion_base': 18,
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "raiz_dorada": {
                "tipo":'consumible',
                "habilidades":'',
                "stats":{
                    'dano_base':'',      
                    'afinidad':'',
                    'efecto_en_tablero':'concentrarse',
                    'efecto_en_combate':'concentrarse',
                    'curacion_base': 0,
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "hiedra_bailarina": {
                "tipo":'consumible',
                "habilidades": '',
                "stats":{
                    'dano_base':'',      
                    'afinidad':'',
                    'efecto_en_tablero':'movilidad',
                    'efecto_en_combate':'aumentar_velocidad',
                    'curacion_base': 0,
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "panax": {
                "tipo":'consumible',
                "habilidades": '',
                "stats":{
                    'dano_base':'',      
                    'afinidad':'',
                    'efecto_en_tablero':'curar_veneno',
                    'efecto_en_combate':'curar_veneno',
                    'curacion_base': 0,
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },
            "hierba_del_erudito": {
                "tipo":'consumible',
                "habilidades": '',
                "stats":{
                    'dano_base':'',      
                    'afinidad':'',
                    'efecto_en_tablero':'ganar_xp',
                    'efecto_en_combate':'ganar_xp',
                    'curacion_base': 0,
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_concentracion':0,
                    'bonus_suerte':0}
                    },

    }

clases = {  "herrero": {
                "arma_inicial":'lanza',
                "habilidad_pasiva":'firmeza',
                "atributos":{
                    'vitalidad':85,
                    'fuerza':81,
                    'inteligencia':50,
                    'velocidad':61,
                    'talento':77,
                    'observacion': 57,
                    'suerte':55},
                "stats":{
                    'armadura':1,
                    'resistencia':0,
                    'evasion':9,
                    'puntos_de_enfoque':4}
            },
            "erudito": {
                "arma_inicial":'tomo_de_aprendiz',
                "habilidad_pasiva": 'reenfocar',
                "atributos":{
                    'vitalidad':65,
                    'fuerza':47,
                    'inteligencia':83,
                    'velocidad':75,
                    'talento':75,
                    'observacion': 71, 
                    'suerte':55},
                "stats":{
                    'armadura':0,
                    'resistencia':1,
                    'evasion':15,
                    'puntos_de_enfoque':5}
            },
            "bardo": {
                "arma_inicial":'laud_roto',
                "habilidad_pasiva":'entretener',
                "atributos":{
                    'vitalidad':73,
                    'fuerza':77,
                    'inteligencia':53,
                    'velocidad':63,
                    'talento':81,
                    'observacion': 59,
                    'suerte':55},
                "stats":{
                    'armadura':0,
                    'resistencia':1,
                    'evasion':13,
                    'puntos_de_enfoque':4}
            },
            "cazador": {
                "arma_inicial":'arco_de_caza',
                "habilidad_pasiva":'tiro_cargado',
                "atributos":{
                    'vitalidad':71,
                    'fuerza':57,
                    'inteligencia':51,
                    'velocidad':83,
                    'talento':69,
                    'observacion': 83,
                    'suerte':55},
                "stats":{
                    'armadura':1,
                    'resistencia':1,
                    'evasion':20,
                    'puntos_de_enfoque':4}
            },
    }
    

class AdministradorDeBaseDeDatos:

    def __init__(self, nombre):
        self.conexion = sql.connect(nombre + ".db")
        self.crear_tabla_jugadores()
        self.crear_tabla_clases()

    def realizar_consulta(self, query):     
        cursor  = self.conexion.cursor()
        consulta = f"{query}" 
        cursor.execute(consulta)
        resultado = cursor.fetchall()[0] 
        self.efectuar_cambios()
        return resultado #type list
    
    def realizar_consulta_de_cambio(self, query):
        cursor  = self.conexion.cursor()
        consulta = f"{query}" 
        cursor.execute(consulta)
        self.efectuar_cambios()


    def efectuar_cambios(self):
        self.conexion.commit()
    
    def crear_tabla_jugadores(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS jugadores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()

    def crear_tabla_personajes(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS personajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT, 
                clase TEXT, 
                habilidad_pasiva TEXT, 
                nivel INT, 
                vitalidad INT, 
                fuerza INT, 
                inteligencia INT, 
                velocidad INT, 
                talento INT, 
                observacion INT, 
                suerte INT,  
                armadura INT, 
                resistencia INT, 
                evasion INT, 
                vida_base INT,
                puntos_de_enfoque INT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()
    
    def crear_tabla_items(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    dano_base INT,     
                    afinidad TEXT, 
                    bonus_armadura INT,
                    bonus_resistencia INT,
                    bonus_vitalidad INT,
                    bonus_fuerza INT,
                    bonus_inteligencia INT,
                    bonus_velocidad INT,
                    bonus_talento INT,
                    bonus_observacion INT,
                    bonus_concentracion INT,
                    bonus_suerte INT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()
    
    def crear_tabla_habilidades_de_armas(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS habilidades_de_armas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT, 
                    efecto TEXT,
                    dano_en_area TINYINT,
                    multiplicador_de_dano REAL,
                    rolls INT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()
    
    def insertar_jugador(self, jugador):#en ejecucion
        query = f"INSERT INTO jugadores VALUES (NULL, '{jugador.nombre}')"
        self.realizar_consulta_de_cambio(query)
    
    def guardar_personaje_en_BD(self, personaje):#en ejecucion
        pass

    
    def insertar_clase(self, clase):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO personajes VALUES (
                    NULL,
                    '{clases[clase]['arma_inicial']}',                    
                    '{clases[clase]['habilidad_pasiva']}',   
                    '{clases[clase]['atributos']['vitalidad']}',                         
                    '{clases[clase]['atributos']['fuerza']}',             
                    '{clases[clase]['atributos']['inteligencia']}',             
                    '{clases[clase]['atributos']['velocidad']}',             
                    '{clases[clase]['atributos']['talento']}',             
                    '{clases[clase]['atributos']['observacion']}',             
                    '{clases[clase]['atributos']['suerte']}',             
                    '{clases[clase]['stats']['armadura']}',             
                    '{clases[clase]['stats']['resistencia']}',             
                    '{clases[clase]['stats']['evasion']}',             
                    '{clases[clase]['stats']['puntos_de_enfoque']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    
    def insertar_item(self, item):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO personajes VALUES (
                    NULL,
                    '{items[item]['tipo']}',
                    '{items[item]['dano_base']}',
                    '{items[item]['afinidad']}',
                    '{items[item]['bonus_armadura']}',
                    '{items[item]['bonus_resistencia']}',
                    '{items[item]['bonus_vitalidad']}',
                    '{items[item]['bonus_fuerza']}',
                    '{items[item]['bonus_inteligencia']}',
                    '{items[item]['bonus_velocidad']}',
                    '{items[item]['bonus_talento']}',
                    '{items[item]['bonus_observacion']}',
                    '{items[item]['bonus_concentracion']}',,
                    '{items[item]['bonus_suerte']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    
    def insertar_habilidad_de_arma(self, arma):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO habilidades_de_armas VALUES (
                    NULL,
                    '{habilidades_de_armas[arma]['nombre']}',
                    '{habilidades_de_armas[arma]['efecto']}',
                    '{habilidades_de_armas[arma]['dano_en_area']}',
                    '{habilidades_de_armas[arma]['multiplicador_de_dano']}',
                    '{habilidades_de_armas[arma]['rolls']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()



    

administradorDeBaseDeDatos = AdministradorDeBaseDeDatos("For_The_Queen")



