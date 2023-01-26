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
            },
            "morder": {
                "nombre":"morder",
                "efecto":'sangrado',
                "dano_en_area":False,
                "multiplicador_de_dano":0.9,
                'rolls':2
            },
            "rebanar": {
                "nombre":"rebanar",
                "efecto":'',
                "dano_en_area":False,
                "multiplicador_de_dano":1,
                'rolls':3
            },
            "estocada": {
                "nombre":"estocada",
                "efecto":'',
                "dano_en_area":False,
                "multiplicador_de_dano":1.2,
                'rolls':4
            }
}

armas = {  
            "lanza": {
                "nombre":"lanza",
                "habilidades": "perforar desgarrar",
                "calidad":1,
                "stats":{
                    'dano_base':9,
                    'tipo_de_dano':'fisico',
                    'afinidad':'fuerza', 
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_evasion':1,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "arco_de_caza": {
                "nombre":"arco_de_caza",
                "habilidades": "tiro tiro_de_francotirador",
                "calidad":1,
                "stats":{
                    'dano_base':6,
                    'tipo_de_dano':'fisico', 
                    'afinidad':'observacion',
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "laud_roto": {
                "nombre":"laud_roto",
                "habilidades": "sinfonia ritardando",
                "calidad":1,
                "stats":{
                    'dano_base':6,
                    'tipo_de_dano':'magico',
                    'afinidad':'talento', 
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "tomo_de_aprendiz": {
                "nombre":"tomo_de_aprendiz",
                "habilidades": "maldecir explosion",
                "calidad":1,
                "stats":{
                    'dano_base':7,    
                    'tipo_de_dano':'magico', 
                    'afinidad':'inteligencia', 
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "espada_corta": {
                "nombre":"espada_corta",
                "habilidades": "rebanar estocada",
                "calidad":1,
                "stats":{
                    'dano_base':7,    
                    'tipo_de_dano':'fisico', 
                    'afinidad':'fuerza', 
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "colmillos": {
                "nombre":"colmillos",
                "habilidades": "morder",
                "calidad":1,
                "stats":{
                    'dano_base':7,    
                    'tipo_de_dano':'fisico', 
                    'afinidad':'fuerza', 
                    'bonus_armadura':0,
                    'bonus_resistencia':0,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    }
}
armaduras = {
            "botas_viejas": {
                "nombre":"botas_viejas",
                "habilidad_pasiva":'',
                "calidad":1,
                "stats":{ 
                    'bonus_armadura':1,
                    'bonus_resistencia':0,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "casco_roto": {
                "nombre":"casco_roto",
                "habilidad_pasiva":'',
                "calidad":1,
                "stats":{ 
                    'bonus_armadura':1,
                    'bonus_resistencia':1,
                    'bonus_evasion':0,
                    'bonus_vitalidad':1,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "chaleco_de_cuero": {
                "nombre":"chaleco_de_cuero",
                "habilidad_pasiva":'',
                "calidad":1,
                "stats":{ 
                    'bonus_armadura':2,
                    'bonus_resistencia':1,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "tunica": {
                "nombre":"tunica",
                "habilidad_pasiva":'',
                "calidad":2,
                "stats":{ 
                    'bonus_armadura':1,
                    'bonus_resistencia':2,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':3,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':1,
                    'bonus_suerte':0}
                    },
            "cota_de_mallas": {
                "nombre":"cota_de_mallas",
                "habilidad_pasiva":'',
                "calidad":2,
                "stats":{ 
                    'bonus_armadura':7,
                    'bonus_resistencia':3,
                    'bonus_evasion':0,
                    'bonus_vitalidad':2,
                    'bonus_fuerza':2,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':0,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "traje_lujoso": {
                "nombre":"traje_lujoso",
                "habilidad_pasiva":'',
                "calidad":2,
                "stats":{ 
                    'bonus_armadura':4,
                    'bonus_resistencia':4,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':0,
                    'bonus_talento':6,
                    'bonus_observacion': 0,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    },
            "chaleco_de_asesino": {
                "nombre":"chaleco_de_asesino",
                "habilidad_pasiva":'',
                "calidad":2,
                "stats":{ 
                    'bonus_armadura':4,
                    'bonus_resistencia':4,
                    'bonus_evasion':0,
                    'bonus_vitalidad':0,
                    'bonus_fuerza':0,
                    'bonus_inteligencia':0,
                    'bonus_velocidad':2,
                    'bonus_talento':6,
                    'bonus_observacion': 7,
                    'bonus_enfoque':0,
                    'bonus_suerte':0}
                    }
}
consumibles = {   
            "barba_de_dios": {
                "nombre":"barba_de_dios",
                "stats":{
                    'dano_base':'',      
                    'efecto_en_tablero':'curacion',
                    'efecto_en_combate':'curacion',
                    'curacion_base': 18}
                    },
            "raiz_dorada": {
                "nombre":"raiz_dorada",
                "stats":{
                    'dano_base':'',      
                    'efecto_en_tablero':'concentrarse',
                    'efecto_en_combate':'concentrarse',
                    'curacion_base': 0,}
                    },
            "hiedra_bailarina": {
                "nombre":"hiedra_bailiarina",
                "stats":{
                    'dano_base':'',      
                    'efecto_en_tablero':'movilidad',
                    'efecto_en_combate':'aumentar_velocidad',
                    'curacion_base': 0}
                    },
            "panax": {
                "nombre":"panax",
                "stats":{
                    'dano_base':'',      
                    'efecto_en_tablero':'curar_veneno',
                    'efecto_en_combate':'curar_veneno',
                    'curacion_base': 0}
                    },
            "hierba_del_erudito": {
                "nombre":"hierba_del_erudito",
                "stats":{
                    'dano_base':'',      
                    'efecto_en_tablero':'ganar_xp',
                    'efecto_en_combate':'ganar_xp',
                    'curacion_base': 0}
                    }
}


clases = {  "herrero": {
                "nombre":"herrero",
                "arma_inicial":'lanza',
                "habilidad_pasiva":'firmeza',
                "sprite_path":r'C:\Users\54115\Desktop\python\For The Queen\assets\dc-mon\holy\paladin.png',
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
                "nombre":"erudito",
                "arma_inicial":'tomo_de_aprendiz',
                "habilidad_pasiva": 'reenfocar',
                "sprite_path":r'C:\Users\54115\Desktop\python\For The Queen\assets\dc-mon\wizard.png',
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
                "nombre":"bardo",
                "arma_inicial":'laud_roto',
                "habilidad_pasiva":'entretener',
                "sprite_path":r'C:\Users\54115\Desktop\python\For The Queen\assets\dc-mon\unique\mnoleg.png',
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
                "nombre":"cazador",
                "arma_inicial":'arco_de_caza',
                "habilidad_pasiva":'tiro_cargado',
                "sprite_path":r'C:\Users\54115\Desktop\python\For The Queen\assets\dc-mon\deep_elf_master_archer.png',
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
    
criaturas = { "esqueleto":{
                    'nombre':'esqueleto',
                    'arma':'espada_corta',
                    'nivel':0,
                    'puntos_de_vida':17,
                    'dano_de_ataque':4,
                    'armadura':1,
                    'resistencia':0,
                    'evasion':0,
                    'sprite_path':r'C:\Users\54115\Desktop\python\For The Queen\assets\UNUSED\monsters\skeleton_small.png'
            },
            "lobo":{
                    'nombre':'lobo',
                    'arma':'colmillos',
                    'nivel':1,
                    'puntos_de_vida':16,
                    'dano_de_ataque':6,
                    'armadura':0,
                    'resistencia':0,
                    'velocidad':85,
                    'evasion':5,
                    'sprite_path':r'C:\Users\54115\Desktop\python\For The Queen\assets\dc-mon\animals\wolf.png'
            },
            "murcielago":{
                    'nombre':'murcielago',
                    'arma':'colmillos',
                    'nivel':1,
                    'puntos_de_vida':15,
                    'dano_de_ataque':5,
                    'armadura':0,
                    'resistencia':1,
                    'velocidad':90,
                    'evasion':10,
                    'sprite_path':r'C:\Users\54115\Desktop\python\For The Queen\assets\UNUSED\monsters\quasit.png'
            },      
            "serpiente":{
                    'nombre':'serpiente',
                    'arma':'colmillos',
                    'nivel':1,
                    'puntos_de_vida':30,
                    'dano_de_ataque':1,
                    'armadura':0,
                    'resistencia':1,
                    'velocidad':90,
                    'evasion':10,
                    'sprite_path':r'C:\Users\54115\Desktop\python\For The Queen\assets\UNUSED\monsters\yellow_snake.png'
            }
}



class AdministradorDeBaseDeDatos:
    def __init__(self, nombre):
        self.conexion = sql.connect(nombre + ".db")
        #tablas a llenar en ejecucion
        self.crear_tabla_jugadores() 
        self.crear_tabla_aventureros()

        #tablas que se llenan al iniciar el programa
        self.crear_tabla_clases()
        self.crear_tabla_criaturas()
        self.crear_tabla_armas()
        self.crear_tabla_armaduras()
        self.crear_tabla_consumibles()
        self.crear_tabla_habilidades_de_armas()

        #inserts iniciales
        self.insertar_clases()
        self.insertar_criaturas()
        self.insertar_armas()
        self.insertar_armaduras()
        self.insertar_consumibles()
        self.insertar_habilidades_de_armas()

        '''
        inserts en ejecucion, no van a ir en este constructor sino en el de Jugador y Aventurero respectivamente
        self.insertar_jugador()
        self.insertar_aventurero()
        '''

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
    

    def crear_tabla_clases(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS clases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT,
                    arma_inicial TEXT,
                    habilidad_pasiva TEXT,
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
                    puntos_de_enfoque INT,
                    sprite_path TEXT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()


    def crear_tabla_aventureros(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS aventureros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                arma INT, 
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
    

    def crear_tabla_criaturas(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS criaturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT,
                    arma TEXT,
                    nivel INT,
                    puntos_de_vida INT,
                    dano_de_ataque INT,
                    armadura INT,
                    resistencia INT,
                    evasion INT,
                    sprite_path TEXT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()
    
    
    def crear_tabla_armas(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS armas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT,
                    habilidades TEXT,
                    calidad INT, 
                    dano_base INT,
                    tipo_de_dano TEXT,     
                    afinidad TEXT,
                    bonus_vitalidad INT,
                    bonus_fuerza INT,
                    bonus_inteligencia INT,
                    bonus_velocidad INT,
                    bonus_talento INT,
                    bonus_observacion INT,
                    bonus_suerte INT, 
                    bonus_armadura INT,
                    bonus_resistencia INT,
                    bonus_evasion INT,
                    bonus_enfoque INT
                    )'''
        cursor.execute(consulta)
        self.efectuar_cambios()


    def crear_tabla_armaduras(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS armaduras (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT,
                    habilidad_pasiva TEXT,
                    calidad INT,   
                    bonus_vitalidad INT,
                    bonus_fuerza INT,
                    bonus_inteligencia INT,
                    bonus_velocidad INT,
                    bonus_talento INT,
                    bonus_observacion INT,
                    bonus_suerte INT, 
                    bonus_armadura INT,
                    bonus_resistencia INT,
                    bonus_evasion INT,
                    bonus_enfoque INT )'''
        cursor.execute(consulta)
        self.efectuar_cambios()


    def crear_tabla_consumibles(self):
        cursor = self.conexion.cursor()
        consulta = f'''CREATE TABLE IF NOT EXISTS consumibles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT,
                    dano_base TEXT,
                    curacion_base INT,
                    efecto_en_tablero TEXT,
                    efecto_en_combate TEXT )'''
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


    def insertar_clase(self, clase):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO clases VALUES (
                    NULL,
                    '{clases[clase]['nombre']}',                    
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
                    '{clases[clase]['stats']['puntos_de_enfoque']}',
                    '{clases[clase]['sprite_path']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    

    def insertar_clases(self):
        for clase in clases:
            self.insertar_clase(clase)


    def insertar_criatura(self, criatura):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO criaturas VALUES (
                    NULL,
                    '{criaturas[criatura]['nombre']}',                    
                    '{criaturas[criatura]['arma']}',                    
                    '{criaturas[criatura]['nivel']}',                    
                    '{criaturas[criatura]['puntos_de_vida']}',                    
                    '{criaturas[criatura]['dano_de_ataque']}',                    
                    '{criaturas[criatura]['armadura']}',                    
                    '{criaturas[criatura]['resistencia']}',                    
                    '{criaturas[criatura]['evasion']}',
                    '{criaturas[criatura]['sprite_path']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    

    def insertar_criaturas(self):
        for criatura in criaturas:
            self.insertar_criatura(criatura)
    

    def insertar_arma(self, arma):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO armas VALUES (
                    NULL,
                    '{armas[arma]['nombre']}',                   
                    '{armas[arma]['habilidades']}',                    
                    '{armas[arma]['calidad']}',   
                    '{armas[arma]['stats']['dano_base']}',                         
                    '{armas[arma]['stats']['tipo_de_dano']}',                         
                    '{armas[arma]['stats']['afinidad']}',                         
                    '{armas[arma]['stats']['bonus_vitalidad']}',                         
                    '{armas[arma]['stats']['bonus_fuerza']}',             
                    '{armas[arma]['stats']['bonus_inteligencia']}',             
                    '{armas[arma]['stats']['bonus_velocidad']}',             
                    '{armas[arma]['stats']['bonus_talento']}',             
                    '{armas[arma]['stats']['bonus_observacion']}',             
                    '{armas[arma]['stats']['bonus_suerte']}',             
                    '{armas[arma]['stats']['bonus_armadura']}',             
                    '{armas[arma]['stats']['bonus_resistencia']}',             
                    '{armas[arma]['stats']['bonus_evasion']}',             
                    '{armas[arma]['stats']['bonus_enfoque']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    

    def insertar_armas(self):
        for arma in armas:
            self.insertar_arma(arma)
    

    def insertar_armadura(self, armadura):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO armaduras VALUES (
                    NULL,
                    '{armaduras[armadura]['nombre']}',                   
                    '{armaduras[armadura]['habilidad_pasiva']}',                    
                    '{armaduras[armadura]['calidad']}',   
                    '{armaduras[armadura]['stats']['bonus_vitalidad']}',                         
                    '{armaduras[armadura]['stats']['bonus_fuerza']}',                         
                    '{armaduras[armadura]['stats']['bonus_inteligencia']}',                         
                    '{armaduras[armadura]['stats']['bonus_velocidad']}',                                                            
                    '{armaduras[armadura]['stats']['bonus_talento']}',             
                    '{armaduras[armadura]['stats']['bonus_observacion']}',             
                    '{armaduras[armadura]['stats']['bonus_suerte']}',             
                    '{armaduras[armadura]['stats']['bonus_armadura']}',             
                    '{armaduras[armadura]['stats']['bonus_resistencia']}',             
                    '{armaduras[armadura]['stats']['bonus_evasion']}',             
                    '{armaduras[armadura]['stats']['bonus_enfoque']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    

    def insertar_armaduras(self):
        for armadura in armaduras:
            self.insertar_armadura(armadura)
    

    def insertar_consumible(self, consumible):
        cursor  = self.conexion.cursor()
        insert = f'''INSERT INTO consumibles VALUES (
                    NULL,
                    '{consumibles[consumible]['nombre']}',
                    '{consumibles[consumible]['stats']['dano_base']}',
                    '{consumibles[consumible]['stats']['curacion_base']}',
                    '{consumibles[consumible]['stats']['efecto_en_tablero']}',
                    '{consumibles[consumible]['stats']['efecto_en_combate']}' )'''
        cursor.execute(insert)
        self.efectuar_cambios()
    

    def insertar_consumibles(self):
        for consumible in consumibles:
            self.insertar_consumible(consumible)
    

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
    

    def insertar_habilidades_de_armas(self):
        for habilidad in habilidades_de_armas:
            self.insertar_habilidad_de_arma(habilidad)


administradorDeBaseDeDatos = AdministradorDeBaseDeDatos("For_The_Queen")


