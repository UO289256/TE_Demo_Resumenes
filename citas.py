import random

def citas(enfoque, BOE):
    # Lista de BOEs válidos
    boes_validos = [
        "BOE-A-2015-6119", "BOE-A-2019-2031", "BOE-A-2021-10584",
        "BOE-A-2021-11043", "BOE-A-2021-12603", "BOE-A-2021-16956",
        "BOE-A-2021-21214", "BOE-A-2022-12754", "BOE-A-2022-2707",
        "BOE-A-2022-2982", "BOE-A-2023-26461", "BOE-A-2023-9215",
        "BOE-B-2018-54744", "BOE-B-2019-52073"
    ]

    if BOE not in boes_validos:
        raise ValueError("El nombre del BOE no es válido")

    enfoque = enfoque.lower()
    
    if enfoque == "documentsummaryindex":
        if BOE == "BOE-A-2015-6119":  #1
            resumen1 = """
            La Resolución de la Dirección General de Política Energética y Minas concede a Enagás Transporte, S.A.U. la autorización para el cierre y desmantelamiento de la Estación de Regulación (ER) (80/72 bar) en la ubicación O-00, en Otero, Asturias.

            Esta autorización se emite tras la solicitud presentada por la empresa, con el fin de cumplir con los artículos 88 a 91 del Real Decreto 1434/2002. Además, se han emitido informes favorables por parte del Gestor Técnico del Sistema, la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias, y el Consejo de la Comisión Nacional de los Mercados y la Competencia.

            La resolución establece que el cierre y desmantelamiento deben completarse en un plazo máximo de tres meses. El material inservible deberá ser trasladado a un vertedero autorizado, mientras que el material reutilizable se destinará preferentemente a instalaciones del Sistema gasista.
            """
            
            citas1 = """
            Citas:

            -   "Por Resolución de esta Dirección General, de 26 de marzo de 2013 (BOE de 10 de abril de 2013), se autoriza el cambio de titularidad en todas las autorizaciones y concesiones otorgadas a «Enagás, S.A.» a favor de «Enagás Transporte, S.A.U.»" (Pág. 47023)
            
            -   "La empresa «Enagás Transporte, S.A.U.», para cumplir con lo estipulado en la condición decimoquinta, ha solicitado, con fecha 25 de septiembre de 2014, el cierre de la estación de regulación (ER) (80/72 bar) ubicada en la posición de válvulas O-00, en Otero, provincia de Asturias" (Pág. 47023)
            
            -   "El informe previo emitido por el Gestor Técnico del Sistema, con fecha 7 de noviembre de 2014, avala el cierre y desmantelamiento de dicha estación de regulación" (Pág. 47024)
            
            -   "La Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias ha emitido un informe favorable, con fecha 19 de noviembre de 2014, respecto a la solicitud de cierre de la estación de regulación" (Pág. 47024)
            
            -   "El Consejo de la Comisión Nacional de los Mercados y la Competencia ha emitido el informe previsto en el artículo 90 del Real Decreto 1434/2002, de 27 de diciembre, considerando adecuado autorizar el cierre y desmantelamiento" (Pág. 47024)
            
            Entidades:

            -   Enagás Transporte, S.A.U.
            
            -   Estación de Regulación (ER) (80/72 bar)
            
            -   Otero
            
            -   Asturias
            
            -   Dirección General de Política Energética y Minas
            
            -   Ministerio de Industria, Energía y Turismo
            """
            
            resumen2 = """
            La Resolución de la Dirección General de Política Energética y Minas autoriza a Enagás Transporte, S.A.U. a cerrar la Estación de Regulación (ER) (80/72 bar) en la posición O-00, ubicada en Otero, junto con sus instalaciones asociadas.

            Esta autorización se concede tras la emisión de informes favorables por parte del Gestor Técnico del Sistema y la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias. Además, el Consejo de la Comisión Nacional de los Mercados y la Competencia ha emitido el informe previsto en el artículo 90 del Real Decreto 1434/2002.

            La empresa deberá proceder al cierre y desmantelamiento de las instalaciones en un plazo máximo de tres meses a partir de la entrada en vigor de la resolución, bajo riesgo de caducidad. El material inservible resultante del desmantelamiento deberá ser trasladado a un vertedero autorizado para chatarra, mientras que el material reutilizable se destinará preferentemente a otras instalaciones del Sistema gasista.
            """
            
            citas2 = """
            Citas:

            -   "Se otorga a la empresa 'Enagás Transporte, S.A.U.' autorización administrativa de cierre de la Estación de Regulación (ER) (80/72 bar) en la posición de válvulas O-00, en Otero e instalaciones asociadas." (BOE-A-2015-6119, página 47023)
            
            -   "Vistos la Ley 34/1998, de 7 de octubre, del Sector de Hidrocarburos, la Ley 30/1992, de 26 de noviembre, de Régimen Jurídico de las Administraciones Públicas y del Procedimiento Administrativo Común..." (BOE-A-2015-6119, página 47024)
            
            -   "El cierre de las instalaciones que se autoriza por la presente resolución habrá de realizarse de acuerdo con el documento técnico denominado 'Memoria Cierre y Desmantelamiento Estación de Regulación 80/72 en Posición O-00', presentados por la empresa 'Enagás Transporte, S.A.U.'..." (BOE-A-2015-6119, página 47025)
            
            Entidades:

            -   Enagás Transporte, S.A.U.
            
            -   Dirección General de Política Energética y Minas
            
            -   Gestor Técnico del Sistema
            
            -   Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias
            
            -   Comisión Nacional de los Mercados y la Competencia
            """
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2019-2031":  #2
            resumen1 = """
            La colección de textos presenta una serie de argumentaciones y justificaciones sobre la constitucionalidad de diferentes disposiciones y artículos que se encuentran en el Decreto-Ley autonómico aragonés. El análisis se centra en la competencia autonómica exclusiva en materia de vivienda y acción social, y se examinan las limitaciones y deberes inherentes a cada tipo de propiedad.

            Se discuten medidas adoptadas por el Gobierno de Aragón y la Comunidad Autónoma para promover las condiciones necesarias para hacer efectivo el derecho a una vivienda digna. También se analiza la normativa autonómica en materia procesal y se argumenta que los preceptos impugnados no tienen fundamento en el derecho sustantivo autonómico y, por lo tanto, infringen el artículo 149.1.6 CE.
            """
            
            citas1 = """
            Citas:

            * "La competencia autonómica exclusiva en materia de vivienda... es competencia del titular de la tutela de dicho interés señalar las limitaciones y deberes inherentes a cada tipo de propiedad." (página 19, file_path: /teamspace/studios/this_studio/dataset_prueba/2/BOE-A-2019-2031.pdf)
            
            * "La regulación contenida en la Ley 10/2016 ha venido en unos casos a ampliar y en otros a dar nueva redacción a los preceptos impugnados" (página 19)

            Entidades:

            * Decreto-Ley autonómico aragonés
            
            * Comunidad Autónoma
            
            * Estado
            
            * Ley 10/2016
            """
            
            resumen2 = """
            
            La colección de textos ofrece un análisis detallado sobre diversos aspectos relacionados con la vivienda y el derecho a una vivienda digna en España. Se examina cómo la normativa autonómica se vincula con las competencias estatales en materia procesal y de derecho sustantivo, mientras que la normativa estatal aborda específicamente la suspensión de los lanzamientos hipotecarios.

            Se argumenta que la normativa autonómica no cumple con los tres requisitos sucesivos necesarios para aplicar la excepción competencial recogida en el artículo 149.1.6 de la Constitución Española, lo que resulta en una invasión de la competencia estatal en el ámbito de la legislación procesal.

            Por otro lado, se defiende que la normativa estatal es coherente y no contradice las disposiciones establecidas en la legislación autonómica.

            Preguntas potenciales:

            -   ¿Cómo se relaciona la normativa autonómica con la legislación estatal en materia procesal?
            
            -   ¿Qué implican los tres requisitos sucesivos para aplicar la excepción competencial según el artículo 149.1.6 CE?
            
            -   ¿De qué manera se justifica la coherencia entre la normativa estatal y autonómica en la suspensión de lanzamientos hipotecarios?
            """
            
            citas2 = """
            Citas:

            -   "La norma impugnada se refiere a la competencia autonómica en materia procesal y de derecho sustantivo" (Página 14500).
            
            -   "La norma autonómica no cumple con los tres escalones sucesivos para aplicar la salvedad competencial contenida en el artículo 149.1.6 CE" (Página 14500).
            
            -   "La normativa estatal que regula la suspensión de lanzamientos hipotecarios es coherente y no contradice las previstas en la legislación autonómica" (Página 14502).
            
            Entidades:

            -   La Comunidad Autónoma
            
            -   El Estado
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
            

        elif BOE == "BOE-A-2021-10584": #3
            resumen1 = """
            La colección de textos ofrece información sobre diversas cuestiones, incluyendo modificaciones en la tributación efectiva, concursos de capacidad de acceso a redes de transporte y distribución de energía eléctrica, descarbonización y electrificación de la economía, y medidas para abordar situaciones de urgencia, entre otros temas.

            """
            
            citas1 = """
            Citas:

            -   "Se actualiza el término 'servicios de postproducción' por 'servicios de efectos visuales', considerados técnicamente equivalentes según lo establecido por el Instituto de la Cinematografía y de las Artes Audiovisuales (ICAA)." (página 16, BOE-A-2021-10584)
            
            -   "El Real Decreto 1183/2020, sobre acceso y conexión a las redes de transporte y distribución de energía eléctrica, establece como criterio la determinación de las cuantías anuales del canon de regulación y de la tarifa de utilización del agua antes del comienzo del ejercicio correspondiente." (página 16, BOE-A-2021-10584)
            
            -   "La disposición adicional novena, apartado 3, de la Ley 11/2020, de Presupuestos Generales del Estado para 2021 (LPGE), ha modificado el apartado 7 del artículo 114 del Canon de regulación y tarifa de utilización del agua, recogido en el texto refundido de la Ley de Aguas." (página 16, BOE-A-2021-10584)
            
            Entidades:

            -   ICAA (Instituto de la Cinematografía y de las Artes Audiovisuales)
            
            -   Real Decreto 1183/2020
            
            -   Ley 11/2020
            
            -   Presupuestos Generales del Estado para 2021
            """
            
            resumen2 = """
            El conjunto de textos ofrece un análisis sobre la situación actual de los precios de la electricidad en España, las medidas propuestas para mitigar el aumento de dichos precios, y las regulaciones relacionadas con la energía renovable. Asimismo, se aborda la modificación del Reglamento del Dominio Público Hidráulico y el establecimiento de normas para la regulación de los cánones de utilización del agua.
     
            Preguntas potenciales que pueden responderse con la información de los documentos:

            -   ¿Cuál es el tipo impositivo del IVA aplicable a determinadas entregas, importaciones y adquisiciones intracomunitarias de energía eléctrica?
            
            -   ¿Qué ocurre con las solicitudes de reserva de zona para instalaciones de generación eólicas marinas según el procedimiento establecido en el título II del Real Decreto 1028/2007, de 20 de junio?
            
            -   ¿Cómo se regulan los pagos fraccionados del Impuesto sobre el Valor de la Producción de Energía Eléctrica durante el ejercicio 2021?
            
            -   ¿Cuál es el plazo para el cobro de los cánones de regulación y las tarifas de utilización del agua?
            
            -   ¿Quiénes son los responsables de dictar disposiciones y adoptar medidas para el desarrollo y ejecución de lo dispuesto en este real decreto-ley?
            """  
            
            citas2 = """
            Citas:

            -   "Desde finales de 2020 y, más intensamente, a partir de marzo de 2021, el precio del mercado mayorista de la electricidad en España ha registrado valores inusualmente altos..." (Pág. no indicada)
            
            -   "El canon de regulación se pondrá al cobro desde el inicio del año natural en que sea aplicable hasta el último día del primer semestre del año siguiente." (Pág. 76288)
            
            Entidades:

            -   Energía eléctrica
            """    
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
    
        elif BOE == "BOE-A-2021-11043": #4
            resumen1 = """
            Se ha corregido un error en el Real Decreto-ley 12/2021, publicado en el Boletín Oficial del Estado (BOE) número 151, el 25 de junio de 2021. La corrección afecta al artículo 1, apartado a), en la página 76283, donde se modifica la expresión "inferior a" por "inferior o igual a" al referirse a la potencia contratada por los titulares de contratos de suministro de electricidad.

            Preguntas potenciales que se pueden responder con la información de los documentos:

            -   ¿Cuál es el título del Real Decreto-ley que se corrigió?
            
            -   ¿En qué página y apartado del artículo 1 se encontraba el error corregido?
            
            -   ¿Quiénes son los titulares de contratos de suministro de electricidad afectados por la corrección?
            
            -   ¿Cuál es la fecha de publicación original del Real Decreto-ley?
            
            -   ¿Dónde se puede consultar la versión corregida del Real Decreto-ley?
            """
            
            citas1 = """
            Citas:

            -   "En la página 76283, en el artículo 1, apartado a), donde dice: «Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior a 10 kW…», debe decir: «Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior o igual a 10 kW…»" (Sin número de página especificado)
          
            Entidades:

            -   Real Decreto-ley 12/2021
            
            -   Boletín Oficial del Estado (BOE)
            
            -   Titulares de contratos de suministro de electricidad
            """
            
            resumen2 = """
            Se ha corregido un error en el Real Decreto-ley 12/2021, que aborda medidas urgentes en la fiscalidad energética y la generación de energía, publicado en el Boletín Oficial del Estado (BOE) número 151. La corrección afecta a la página 76283, en el artículo 1, apartado a), donde se ha modificado la expresión "inferior a" por "inferior o igual a" en la descripción de la potencia contratada para los titulares de contratos de suministro de electricidad.

            Preguntas potenciales que pueden ser respondidas con la información en los documentos:

            * ¿Cuál es el error corregido en el Real Decreto-ley 12/2021?
            
            * ¿En qué página y apartado del artículo 1 se encuentra el error?
            
            * ¿Qué cambios se realizaron en las condiciones para los titulares de contratos de suministro de electricidad?
            
            * ¿Cuál es la fecha de publicación del Boletín Oficial del Estado número 151?
            """      
            
            citas2 = """
            Citas:

            * "En la página 76283, en el artículo 1, apartado a), donde dice: «Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior a 10 kW…», debe decir: «Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior o igual a 10 kW…»" (página 76283)
            
            Entidades:

            * Real Decreto-ley 12/2021
            
            * Boletín Oficial del Estado (BOE)
            
            * Canon de regulación
            
            * Tarifa de utilización del agua
            
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2021-12603": #5
            resumen1 = """
            La Resolución del 21 de julio de 2021, emitida por el Congreso de los Diputados, ordena la publicación del Acuerdo de convalidación del Real Decreto-ley 12/2021. Este decreto adopta medidas urgentes en el ámbito de la fiscalidad energética y la generación de energía, así como disposiciones sobre la gestión del canon de regulación y la tarifa de utilización del agua.

            Preguntas potenciales que pueden ser respondidas con la información en los documentos:

            -   ¿Qué medidas urgentes adoptó el Real Decreto-ley 12/2021?
            
            -   ¿Cuál es el contenido del Acuerdo de convalidación aprobado por el Congreso de los Diputados?
            
            -   ¿Quién es la Presidenta del Congreso de los Diputados que ordenó la publicación de la Resolución?
            
            -   ¿En qué artículo de la Constitución se basa la decisión del Congreso de los Diputados?
            """
            
            citas1 = """
            Citas:

            -   "Se ordena la publicación para general conocimiento." (Palacio del Congreso de los Diputados, 21 de julio de 2021. – La Presidenta del Congreso de los Diputados, Meritxell Batet Lamaña.)
            
            -   "De conformidad con lo dispuesto en el artículo 86.2 de la Constitución, el Congreso de los Diputados... acordó convalidar el Real Decreto-ley 12/2021..." (I. DISPOSICIONES GENERALES)
            
            -   "Se ordena la publicación para general conocimiento." (Palacio del Congreso de los Diputados, 21 de julio de 2021. – La Presidenta del Congreso de los Diputados, Meritxell Batet Lamaña.)
            
            Entidades:

            -   Congreso de los Diputados
            
            -   Real Decreto-ley 12/2021
            
            -   Meritxell Batet Lamaña (Presidenta del Congreso de los Diputados)
            """
            resumen2 = """
            El Congreso de los Diputados ha ordenado la publicación del Acuerdo de convalidación del Real Decreto-ley 12/2021, el cual adopta medidas urgentes en el ámbito de la fiscalidad energética y la generación de energía. Esta resolución, aprobada en la sesión de hoy, confirma la validez del mencionado real decreto-ley, que fue originalmente publicado en el Boletín Oficial del Estado número 151, el 25 de junio de 2021.

            Preguntas potenciales que pueden ser respondidas con la información en los documentos:

            -   ¿Cuál es el contenido del Acuerdo de convalidación del Real Decreto-ley 12/2021?
            
            -   ¿Quién es la Presidenta del Congreso de los Diputados que ordenó la publicación de la resolución?
            
            -   ¿En qué fecha se aprobó la resolución en la sesión del día de hoy?
            
            -   ¿Dónde fue publicado originalmente el Real Decreto-ley 12/2021?
            """      
            
            citas2 = """
            Citas:

            -   "Se ordena la publicación para general conocimiento" (página 1).
            
            -   "Acordó convalidar el Real Decreto-ley 12/2021, de 24 de junio, por el que se adoptan medidas urgentes en el ámbito de la fiscalidad energética y en materia de generación de energía..." (página 1).
            
            -   "Publicado en el «Boletín Oficial del Estado» número 151, de 25 de junio de 2021" (página 1).
            
            Entidades:

            -   Congreso de los Diputados
            
            -   Real Decreto-ley 12/2021
            
            -   Boletín Oficial del Estado
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
            
        elif BOE == "BOE-A-2021-16956": #6
            resumen1 = """
            La Secretaría General de Coordinación Territorial ha publicado un Acuerdo de la Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias relacionado con el Real Decreto-ley 12/2021. Este Acuerdo tiene como objetivo iniciar negociaciones para resolver las discrepancias surgidas en torno a la disposición final tercera del Real Decreto-ley, designar un grupo de trabajo para proponer una solución y comunicar el Acuerdo a las entidades correspondientes.

            Preguntas potenciales que pueden ser respondidas con la información en los documentos:

            -   ¿Cuál es el objetivo del Acuerdo publicado por la Secretaría General de Coordinación Territorial?
            
            -   ¿Qué cuestiones relativas a la disposición final tercera del Real Decreto-ley 12/2021 se buscan resolver mediante negociaciones?
            
            -   ¿Qué grupo de trabajo se ha designado para proponer una solución al problema?
            
            -   ¿A qué entidades se comunica el Acuerdo y por qué motivo?
            
            -   ¿Cuál es la fecha de publicación del Boletín Oficial del Estado que contiene el Acuerdo?
            """
            
            citas1 = """
            Citas:

            -   "III. OTRAS DISPOSICIONES" (página 1)
            
            -   "Conforme a lo establecido en el artículo 33 de la Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional, modificado por la Ley Orgánica 1/2000, de 7 de enero" (página 2)
            
            -   "La Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias ha adoptado el siguiente Acuerdo:" (página 3)
            
            -   "BOLETÍN OFICIAL DEL ESTADO Núm. 249, Lunes 18 de octubre de 2021, Sec. III, Pág. 127188" (página 5)
            
            Entidades:

            -   Secretaría General de Coordinación Territorial
            
            -   Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias
            
            -   Real Decreto-ley 12/2021
            
            -   Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional
            
            -   Ley Orgánica 1/2000, de 7 de enero
            
            -   Boletín Oficial del Estado
            """
            resumen2 = """
            La resolución de la Secretaría General de Coordinación Territorial publica el Acuerdo de la Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias, relacionado con el Real Decreto-ley 12/2021. Este Acuerdo establece varias medidas, incluyendo la iniciativa de negociaciones para resolver las discrepancias sobre la disposición final tercera del Real Decreto-ley, la creación de un grupo de trabajo, y la comunicación del Acuerdo al Tribunal Constitucional, a las Cortes Generales y al Parlamento de Canarias.

            Preguntas potenciales que se pueden responder con la información en los documentos:

            1. ¿Cuál es el propósito principal del Acuerdo publicado por la Secretaría General de Coordinación Territorial?
            
            2. ¿Qué medidas específicas se establecen en el Acuerdo para resolver las discrepancias relacionadas con la disposición final tercera del Real Decreto-ley 12/2021?
            
            3. ¿A qué entidades se comunicará el Acuerdo, según el punto 4 del mismo?
            
            4. ¿Cómo se relaciona el artículo 33 de la Ley Orgánica 2/1979 con la Ley Orgánica 1/2018 en el contexto del Acuerdo?
            """      
            
            citas2 = """
            Citas:

            * "La Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias ha adoptado el siguiente Acuerdo:" (p. 2)
           
            * "1. Iniciar negociaciones para resolver las discrepancias manifestadas en relación con la disposición final tercera del Real Decreto-ley 12/2021..." (p. 3)
           
            * "4. Comunicar este Acuerdo a las Cortes Generales y al Parlamento de Canarias a los efectos previstos en el artículo 167 de la Ley Orgánica 1/2018, de 5 de noviembre, de reforma del Estatuto de Autonomía de Canarias." (p. 4)

            Entidades:

            * Secretaría General de Coordinación Territorial
            
            * Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias
            
            * Tribunal Constitucional
            
            * Cortes Generales
            
            * Parlamento de Canarias
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2021-21214":  #7
            resumen1 = """
            El Tribunal Constitucional ha admitido a trámite un recurso de inconstitucionalidad presentado por el Parlamento de Canarias contra la disposición final tercera del Real Decreto-ley 12/2021. Esta disposición aborda medidas urgentes relacionadas con la fiscalidad energética, la generación de energía, así como la gestión del canon de regulación y la tarifa de utilización del agua.

            Preguntas potenciales que se pueden responder con la información en los documentos:

            -   ¿Cuál es el contenido específico de la disposición final tercera del Real Decreto-ley 12/2021?
            
            -   ¿Quién presentó el recurso de inconstitucionalidad y cuál es el motivo del mismo?
            
            -   ¿En qué fecha fue admitido a trámite el recurso de inconstitucionalidad?
            
            -   ¿Qué cuestiones aborda la disposición final tercera del Real Decreto-ley 12/2021 en términos de fiscalidad energética y gestión del agua?
            """
            
            citas1 = """
            Citas:

            -   "El Pleno del Tribunal Constitucional, por providencia de 16 de diciembre de 2021, ha acordado admitir a trámite el recurso de inconstitucionalidad número 5935-2021, promovido por el Parlamento de Canarias, contra la disposición final tercera del Real Decreto-ley 12/2021..." (I. DISPOSICIONES GENERALES)
            
            -   "Madrid, 16 de diciembre de 2021.–El Secretario de Justicia del Pleno del Tribunal Constitucional, Alfonso Pérez Camino." (BOLETÍN OFICIAL DEL ESTADO)
            
            Entidades:

            -   Tribunal Constitucional
            
            -   Parlamento de Canarias
            
            -   Real Decreto-ley 12/2021
            
            """
            
            resumen2 = """
            El Tribunal Constitucional ha admitido a trámite un recurso de inconstitucionalidad presentado por el Parlamento de Canarias contra la disposición final tercera del Real Decreto-ley 12/2021, que establece medidas urgentes en materia de fiscalidad energética y generación de energía.

            Preguntas potenciales que se pueden responder con la información en los documentos:

            -   ¿Qué tipo de recurso de inconstitucionalidad fue presentado por el Parlamento de Canarias?
            
            -   ¿Contra qué disposición específica del Real Decreto-ley 12/2021 se dirige el recurso de inconstitucionalidad?
            
            -   ¿Quién es el Secretario de Justicia del Pleno del Tribunal Constitucional que firmó la providencia?
            """      
            
            citas2 = """
            Citas:

            -   "El Pleno del Tribunal Constitucional, por providencia de 16 de diciembre de 2021, ha acordado admitir a trámite el recurso de inconstitucionalidad número 5935-2021, promovido por el Parlamento de Canarias..." (pág. no especificada)
            
            -   "Madrid, 16 de diciembre de 2021.–El Secretario de Justicia del Pleno del Tribunal Constitucional, Alfonso Pérez Camino." (pág. no especificada)
            
            Entidades:

            -   Tribunal Constitucional
            
            -   Parlamento de Canarias
            
            -   Real Decreto-ley 12/2021
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2022-12754":  #8
            resumen1 = """
            El decreto-ley introduce modificaciones en la regulación de la propiedad horizontal en relación con la eficiencia energética y el uso del agua, con el fin de facilitar la instalación de paneles solares fotovoltaicos para autoconsumo en las cubiertas de los edificios plurifamiliares. Esta reforma busca cumplir con lo dispuesto en la disposición final primera del Decreto-ley 24/2021 y establecer un marco regulador que brinde seguridad jurídica.

            Además, la modificación tiene como objetivo promover la integración de fuentes de energía renovable en los edificios y mejorar la eficiencia energética. Se actualizan los artículos 553-25 y 553-26 del libro quinto del Código Civil de Cataluña, que regulan la adopción de acuerdos en comunidades de propietarios.

            Preguntas potenciales que se pueden responder con la información en los documentos:

            1. ¿Cuál es el objetivo principal del decreto-ley en relación con la instalación de placas solares fotovoltaicas?
            
            2. ¿Qué artículos del Código Civil de Cataluña se modifican y qué aspecto regulan?
            
            3. ¿Qué porcentaje de las viviendas de Cataluña se beneficiará de esta reforma según el decreto-ley?
            
            4. ¿Cuál es el mandato de la disposición final primera del Decreto-ley 24/2021 que se busca cumplir con esta modificación?
            """
            
            citas1 = """
            Citas:

            * "El objetivo principal de la iniciativa es facilitar la instalación de placas solares fotovoltaicas para autoconsumo, es decir, para autoproducción de electricidad, en las cubiertas de los edificios plurifamiliares que representan el 74% de las viviendas de Cataluña." (pág. 11, BOE-A-2022-2707)
            
            * "Se modifica el artículo 553-25 del libro quinto del Código Civil de Cataluña, que queda redactado del modo siguiente..." (pág. 21003)

            Entidades:

            * Generalitat de Cataluña
            
            * Código Civil de Cataluña
            """
            resumen2 = """
            El decreto-ley publicado en el BOE-A-2022-2707 modifica el Código Civil de Cataluña para facilitar la instalación de equipos destinados a mejorar la eficiencia energética y la gestión hídrica, así como sistemas de energías renovables en edificios sometidos al régimen de propiedad horizontal. El propósito de esta modificación es reducir el consumo energético y mejorar la habitabilidad de los hogares mediante la rehabilitación energética.

            Preguntas potenciales que se pueden responder con la información en los documentos:

            -   ¿Cuál es el objetivo principal del decreto-ley BOE-A-2022-2707?

                -   Facilitar la instalación de equipos y sistemas para mejorar la eficiencia energética y la gestión hídrica en edificios sometidos al régimen de propiedad horizontal.
            
            
            -   ¿Qué tipo de instalaciones se pretenden impulsar con este decreto-ley?

                    -   Equipos que mejoren la eficiencia energética y sistemas de energías renovables.
            
            
            -   ¿Cuáles son los beneficios esperados de la instalación de equipos y sistemas de energías renovables en edificios sometidos al régimen de propiedad horizontal?

                    -   Reducción del consumo energético y mejora de la habitabilidad de los hogares a través de la rehabilitación energética.
            
           
            -   ¿Cómo se regula el voto para adoptar diferentes acuerdos relacionados con la instalación de infraestructuras o equipos comunes?

                    -   El decreto-ley establece que el criterio de mayoría simple es suficiente para adoptar estos acuerdos.
            
            
            -   ¿Qué ocurre si un acuerdo de junta para instalar infraestructuras o equipos es incompatible con instalaciones o sistemas previamente autorizados?

                    -   No se especifica en el texto proporcionado; se debe consultar el Código Civil de Cataluña para detalles sobre compatibilidad de instalaciones.
            """   
            
            citas2 = """
            Citas:

            -   "La disponibilidad de estos fondos NGEU es, por lo tanto, una oportunidad crucial para adaptar el parque inmobiliario residencial de nuestro país a un consumo energético más sostenible mediante la instalación de equipos que mejoren la eficiencia energética o de sistemas de energías renovables en edificios sometidos al régimen de propiedad horizontal." (pág. 21000)
            
            -   "El criterio de la mayoría simple permite impulsar las instalaciones para la mejora de la eficiencia energética y el establecimiento de sistemas de energías renovables y, al mismo tiempo, genera comportamientos cooperativos entre los propietarios." (pág. 20999)
            
            Entidades:

            -   Cataluña
            
            -   Código Civil de Cataluña
            
            -   Decreto-ley BOE-A-2022-2707
            
            -   NGEU (Next Generation EU)
            
            -   Parque inmobiliario residencial
            
            """   
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2022-2707":  #9
            resumen1 = """
            El Decreto-ley de la Comunidad Autónoma de Cataluña tiene como objetivo modificar el libro quinto del Código Civil de Cataluña para incorporar nuevas regulaciones sobre la instalación de sistemas de energías renovables y mejoras en la eficiencia energética e hídrica en edificios bajo el régimen de propiedad horizontal. Además, el decreto corrige errores en el texto original publicado en el BOE núm. 44.
            """
            
            citas1 = """
            Citas:

            -   "Este Decreto ley tiene por objeto modificar el Código civil de Cataluña respecto a los aspectos relativos a la ejecución de obras para la mejora de la eficiencia energética o hídrica y la instalación de sistemas de energías renovables en los edificios sujetos al régimen de propiedad horizontal..." (página 22412, BOE núm. 48)
            
            -   "La reforma abarca seis artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-42 (uso y disfrute de los elementos comunes), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes)." (página 22412, BOE núm. 48)
            
            Entidades:

            -   Comunidad Autónoma de Cataluña
            
            -   Decreto-ley 28/2021
            
            -   Código Civil de Cataluña
            
            -   Edificios sujetos al régimen de propiedad horizontal
            """
            
            resumen2 = """
            El texto describe la corrección de errores en el Decreto-ley 28/2021, el cual modifica el libro quinto del Código Civil de Cataluña y el Decreto-ley 10/2020. La corrección se refiere a erratas detectadas en el texto originalmente publicado en el BOE núm. 44, de 21 de febrero de 2022.

            
            Preguntas potenciales que pueden responderse con la información en los documentos:

            1. ¿Cuál es el objetivo del Decreto-ley 28/2021?
            
            2. ¿Qué artículos se modifican en el Código Civil de Cataluña según el Decreto-ley 28/2021?
            
            3. ¿Por qué se realizó la corrección de errores en el texto del Decreto-ley 28/2021?
            
            4. ¿Dónde fue publicado originalmente el Decreto-ley 28/2021?
            """     
            
            citas2 = """
            Citas:

            * "COMUNIDAD AUTÓNOMA DE CATALUÑA 2982 Corrección de errores en el Decreto-ley 28/2021..." (página no especificada)
            
            * "En el título, donde dice: «… en el ámbito de las personas jurídicas de derecho privado sujetos a las disposiciones del derecho civil catalán.», debe decir: «… en el ámbito de las personas jurídicas de derecho privado sujetas a las disposiciones del derecho civil catalán.»" (página no especificada)
            
            * "La reforma abarca cinco artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes)." (página no especificada)
            
            * "La reforma abarca seis artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-42 (uso y disfrute de los elementos comunes), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes)." (página no especificada)
            
            * "Publicada en el «Diario Oficial de la Generalitat de Cataluña» número 8569A, de 23 de diciembre de 2021" (página no especificada)

            Entidades:

            * Comunidad Autónoma de Cataluña
            
            * Decreto-ley 28/2021
            
            * Decreto-ley 10/2020
            
            * Código Civil de Cataluña
            
            * BOE núm. 44, de 21 de febrero de 2022
            
            * Diario Oficial de la Generalitat de Cataluña número 8569A
            """ 
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
            

        elif BOE == "BOE-A-2022-2982":  #10
            resumen1 = """
            El conjunto de textos aborda la Ley 7/2021, de cambio climático y transición energética, enfocándose en la disposición derogatoria única y el artículo 20, ambos objeto de un recurso de inconstitucionalidad interpuesto por la Xunta de Galicia. Este recurso sostiene que dichas disposiciones vulneran el principio de seguridad jurídica y la reserva de ley en materia de dominio público marítimo-terrestre. La Xunta expresa dudas sobre la continuidad del régimen del título III de la Ley de Costas y el cómputo de las prórrogas extraordinarias de concesiones.

            La abogacía del Estado argumenta que la Xunta no ha cumplido con la carga argumentativa necesaria respecto de la impugnación de los dos primeros apartados del artículo 20 y de la disposición derogatoria única. Asimismo, destaca la importancia del principio de seguridad jurídica, consagrado en el artículo 9.3 de la Constitución Española (CE), y su aplicación en la gestión del dominio público marítimo-terrestre. La Ley 7/2021 introduce cambios significativos en la gestión de los títulos de ocupación de este dominio, limitando la duración de las concesiones y sus prórrogas a un máximo de setenta y cinco años.

           
            Preguntas potenciales que pueden responderse con la información en los documentos:

            1. ¿Cuáles son los objetivos de la planificación y gestión del medio marino según la Ley 7/2021?
            2. ¿Cómo se aplica el principio de seguridad jurídica en el ámbito del dominio público marítimo-terrestre?
            3. ¿Qué papel juega el legislador en la regulación del dominio público marítimo-terrestre?
            4. ¿Cómo se evalúan las normas que colisionan con derechos subjetivos de cualquier tipo?
            5. ¿Cuáles son los aspectos importantes a considerar al enjuiciar una ley que colisione con el principio de seguridad jurídica?
            """
            
            citas1 = """
            Citas:

            * "El art. 20.4 de la Ley 7/2021 lesionaría el principio de seguridad jurídica, tanto en su vertiente objetiva como en su vertiente subjetiva..." (página no especificada)
            
            * "La disposición derogatoria única de la Ley 7/2021... al no salvar expresamente el régimen del art. 2 de la Ley 2/2013, lo habría derogado..." (página no especificada)

            Entidades:

            * Xunta de Galicia
            
            * Ley 7/2021, de cambio climático y transición energética
            
            * Artículo 20
            
            * Disposición derogatoria única
            
            * Ley 2/2013
            
            * Ley de Costas
            """
                        
            resumen2 = """
            El recurso de inconstitucionalidad presentado por la Xunta de Galicia cuestiona la constitucionalidad del nuevo régimen jurídico sobre los bienes de dominio público marítimo-terrestre y sus prórrogas, establecido por la Ley 7/2021. La Xunta argumenta que esta ley omite un régimen claro y definido sobre la extensión de las concesiones de ocupación del dominio público marítimo y sus prórrogas, lo cual, a su juicio, vulnera el principio de seguridad jurídica, contemplado en el artículo 9.3 de la Constitución Española, y la reserva de ley establecida en el artículo 132.2 de la misma.

            La Ley 7/2021 introduce un régimen jurídico novedoso para las concesiones de ocupación del dominio público marítimo, sin considerar el marco regulador previamente establecido por la Ley 2/2013 y la Ley de Costas. Esta omisión ha generado incertidumbre sobre si las concesiones otorgadas antes de la entrada en vigor de la Ley 7/2021 pueden prorrogarse hasta alcanzar un plazo total de setenta y cinco años, o si están limitadas al plazo máximo establecido por la Ley 2/2013.

            Por otro lado, la abogacía del Estado sostiene que la Xunta de Galicia no ha cumplido con la carga argumentativa necesaria en su impugnación de los primeros apartados del artículo 20 de la Ley 7/2021, ni en su crítica a la disposición derogatoria única de dicha ley.
            """      
            
            citas2 = """
            Citas:

            * "El art. 20 de la Ley 7/2021 ha omitido deliberadamente el régimen del art. 2 de la Ley 2/2013 y la vigencia de la disposición transitoria primera de la Ley de costas, lo cual, unido a la genérica disposición derogatoria única de la Ley 7/2021, hace que actualmente se ignore si las concesiones demaniales anteriores a la Ley de costas pueden, mediante su prórroga, superar el plazo inicial, o si –conforme a la Ley 7/2021– el plazo máximo incluiría las prórrogas." (Pág. 110219)
            * "La disposición derogatoria única de la Ley 7/2021 al no salvar expresamente el régimen del art. 2 de la Ley 2/2013 lo habría derogado, lo cual entrañaría una retroactividad que afectaría a los derechos adquiridos y al principio de confianza legítima." (Pág. ?)

            Entidades:

            * Xunta de Galicia
            * Ley 7/2021, de cambio climático y transición energética
            * Ley 2/2013
            * Ley de Costas
            * Constitución Española (art. 9.3 CE y art. 132.2 CE)
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2023-26461": #11
            resumen1 = """
            La Constitución española establece un Estado complejo en el que las instituciones generales del Estado y las comunidades autónomas comparten el ejercicio de funciones estatales, reconociendo una cierta descentralización mediante los Estatutos de Autonomía. Esta descentralización permite a las comunidades autónomas, como Canarias, tener competencias en diversos ámbitos, incluidos aspectos económicos y fiscales específicos.

            En cuanto al régimen económico y fiscal de Canarias, se destaca su carácter evolutivo, diseñado para adaptarse a las necesidades sociales y económicas de cada momento histórico, y basado en el principio de solidaridad, más que en la existencia de una garantía institucional fija. La disposición adicional tercera de la Constitución española se interpreta dentro de este marco, permitiendo la descentralización y el desarrollo particular de Canarias bajo el Estatuto de Autonomía.

            La exposición de motivos del Real Decreto-Ley 12/2021 justifica la modificación del límite de la deducción por inversiones en producciones cinematográficas en Canarias debido a la urgente necesidad de responder a las exigencias fiscales del ejercicio de 2020. La disposición final tercera del decreto se concibe con un carácter provisional, adaptando temporalmente la normativa a las circunstancias inmediatas.

        
            Preguntas potenciales:

            1. ¿Cómo contribuyen las comunidades autónomas a la estructura del Estado español?
            2. ¿Qué implica la disposición adicional tercera de la Constitución española para el régimen económico y fiscal de Canarias?
            3. ¿De qué manera se considera evolutivo el régimen económico y fiscal canario según la jurisprudencia constitucional?
            4. ¿Cuál es el procedimiento de modificación de un Real Decreto-Ley según la Constitución española?
            5. ¿Cuál es la importancia del informe previo de la comunidad autónoma en la modificación de un Real Decreto-Ley?
            """
            
            citas1 = """
            Citas:

            * "El Estado es unitario, pero admite una cierta descentralización a través del Estatuto de Autonomía" (página 2). [1]
            * "La Constitución ha querido establecer una regulación evolutiva del régimen económico y fiscal canario, que se basa en el principio de solidaridad" (página 5). [2]
            * "El núcleo esencial del art. 46 EACan tiene, en realidad, como hemos destacado, una naturaleza evolutiva, esto es, ajustada a las necesidades sociales y económicas de cada momento histórico" (página 6). [3]

            Entidades:

            * Estado
            * Comunidades autónomas
            * Parlamento de Canarias
            * Real Decreto-Ley 12/2021
            * Boletín Oficial del Estado (BOE)
            * Estatuto de Autonomía
            * Constitución española
            """
            
            resumen2 = """
            La disposición final tercera del Real Decreto-ley 12/2021 tiene como finalidad asegurar la continuidad de la especialidad del régimen económico y fiscal canario en lo que respecta al límite absoluto aplicable a la deducción por inversiones cinematográficas realizadas en Canarias. Esta disposición busca mantener el diferencial fiscal que Canarias tiene respecto al resto del territorio peninsular, alineándose con las modificaciones recientes en la ley reguladora del impuesto de sociedades.

            En concreto, se actualiza la Ley 19/1994, de modificación del régimen económico y fiscal de Canarias, incrementando el límite absoluto de la deducción de 5,4 a 12,4 millones de euros, en consonancia con los cambios realizados a nivel estatal. Esta actualización tiene como objetivo preservar la ventaja fiscal de Canarias, asegurando que siga siendo un lugar atractivo para las inversiones cinematográficas.
            """   
            
            citas2 = """
            Citas:

            * "La razón que justifica la inclusión en el real decreto-ley de la disposición final tercera no es otra que la de preservar la especialidad del régimen económico y fiscal canario en lo relativo al límite absoluto aplicable a la deducción por inversiones cinematográficas que se realicen en Canarias, siguiendo los cambios que se han realizado en la ley reguladora del impuesto de sociedades, con el objetivo de mantener el diferencial previamente existente respecto al límite de deducción aplicable en el territorio peninsular" (página 5).
            
            * "Con la disposición final tercera se modifica la Ley 19/1994, de 5 de julio, de modificación del régimen económico y fiscal de Canarias, para actualizar el límite absoluto de la deducción de 5,4 a 12,4 millones, siguiendo los cambios que se han introducido en el límite a nivel estatal" (página 16).

            Entidades:

            * Real Decreto-ley 12/2021
            
            * Ley reguladora del impuesto de sociedades
            
            * Ley 19/1994
            """   
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2023-9215":  #12
            resumen1 = """
            El conjunto de textos analiza las modificaciones y actualizaciones realizadas en diversos programas de ayudas para la promoción de energías renovables y almacenamiento. Estas modificaciones incluyen cambios en las condiciones y regulaciones, especialmente en relación con la justificación del cumplimiento del principio de no causar daño significativo (DNSH). Además, se ajustan las cuantías de las ayudas y se establecen nuevos valores de referencia y requisitos documentales.

            Por ejemplo, se actualizan las intensidades de las ayudas a aplicar en cada programa, según se indica en el apartado AIII.A3 del anexo III, que detalla los valores de referencia para el cálculo de la ayuda base. Además, se especifica que, para todos los programas que superen los 100 kW de potencia nominal, se deberá aportar un informe detallado, según se menciona en el epígrafe e) del anexo AII.A1.
            """
            citas1 = """
            Citas:

            -   "Se modifican... en su caso, e intensidades de ayuda a aplicar en cada uno de los programas..." (Apartado AIII.A3. Valores de referencia para el cálculo de la Ayuda Base, del anexo III, pág. 172937).
            
            -   "Para todos los programas, siempre que se superen los 100 kW de potencia nominal, se aportará un informe que indique..." (Epígrafe e), apartados i y ii, del anexo AII.A1. Documentación general, pág. 172935).
            
            Entidades:

            -   Comunidades autónomas
            
            -   Ciudades de Ceuta y Melilla
            
            -   IDAE (Instituto para la Diversificación y el Ahorro de la Energía)
            """
            
            resumen2 = """
            El conjunto de textos analiza la modificación del Plan de Recuperación, Transformación y Resiliencia para alinearlo con el marco europeo de ayudas de Estado, según lo establecido en el Real Decreto 1178/2023, de 27 de diciembre. Este ajuste tiene como objetivo principal fomentar la implementación de instalaciones de almacenamiento energético y energías renovables térmicas en distintos sectores económicos.

            Se establece que las nuevas intensidades de ayuda, introducidas en el artículo tercero del real decreto, serán aplicables a las resoluciones de concesión a partir del 1 de enero de 2024. Además, para las solicitudes presentadas y en lista de reserva provisional, el 31 de diciembre de 2023 se mantendrá como la fecha límite para la presentación de solicitudes.

            Finalmente, se detalla que este real decreto entrará en vigor el mismo día de su publicación en el «Boletín Oficial del Estado».
            """
            
            citas2 = """
            Citas:

            -   "Mediante el Real Decreto 1178/2023, de 27 de diciembre, por el que se modifica la normativa reguladora y se adaptan al marco europeo de ayudas de Estado determinados programas de ayudas de rehabilitación energética y energías renovables del Plan de Recuperación, Transformación y Resiliencia." (Pág. 172926)
            
            -   "Las nuevas intensidades de ayuda introducidas por el apartado diez del artículo tercero de este real decreto serán de aplicación a las resoluciones de concesión que se dicten a partir del 1 de enero de 2024." (pág. no especificada)
            
            -   "Este real decreto entrará en vigor el mismo día de su publicación en el «Boletín Oficial del Estado»..." (pág. 172939)
            
            Entidades:

            -   Plan de Recuperación, Transformación y Resiliencia
            
            -   Reglamento (UE) n.º 651/2014 de la Comisión
            """      
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-B-2018-54744": #13
            resumen1 = """
            
            El anuncio del Ayuntamiento de Marina de Cudeyo formaliza un contrato mixto de obra y suministro para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. Este contrato, que fue adjudicado a Imesapi, S.A., está sujeto a regulación armonizada y se gestionó bajo el expediente número 2018/251.

            Preguntas potenciales:

            ¿Cuál es el objeto del contrato? Rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal.
            ¿Quién es la entidad adjudicadora? El Ayuntamiento de Marina de Cudeyo.
            ¿Cuál es el presupuesto base de licitación? (Esta información no se proporciona en el resumen).
            ¿Cuándo fue formalizado el contrato? El 13 de noviembre de 2018.
            ¿Quién es el contratista? Imesapi, S.A.
            """
            
            citas1 = """
            Citas:

            -   "54744 Anuncio del Ayuntamiento de Marina de Cudeyo por el que se formaliza contrato mixto (obra y suministro) sujeto a regulación armonizada para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (página no especificada)
            
            -   "2. Objeto del contrato: a) Tipo: Mixto. b) Descripción: Rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (página no especificada)
            
            -   "6. Formalización del contrato: a) Fecha de adjudicación: 1 de octubre de 2018. b) Fecha de formalización del contrato: 13 de noviembre de 2018. c) Contratista: Imesapi, S.A." (página no especificada)
            
            Entidades:

            -   Ayuntamiento de Marina de Cudeyo
            
            -   Imesapi, S.A.
            
            -   Secretaría
            
            -   2018/251
            """
            
            resumen2 = """
            El Ayuntamiento de Marina de Cudeyo ha formalizado un contrato mixto (obra y suministro) para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. Este contrato fue adjudicado a Imesapi, S.A..

          
            Preguntas potenciales que pueden responderse con la información proporcionada:

            -   ¿Cuál es el objeto del contrato adjudicado por el Ayuntamiento de Marina de Cudeyo? La rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal.
            
            -   ¿Quién es la entidad adjudicadora del contrato? El Ayuntamiento de Marina de Cudeyo.
            
            -   ¿Cuál es el presupuesto base de licitación del contrato? Esta información no se especifica en el resumen.
            
            -   ¿Cuál es la fecha de formalización del contrato? 1 de octubre de 2018.
            
            -   ¿Quién es el contratista adjudicado para el proyecto? Imesapi, S.A.
            """
            
            citas2 = """
            Citas:

            -   "54744 Anuncio del Ayuntamiento de Marina de Cudeyo por el que se formaliza contrato mixto (obra y suministro) sujeto a regulación armonizada para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (Pág. 69785)
            
            -   "1. Entidad adjudicadora: ... Ayuntamiento de Marina de Cudeyo..." (S/D)
            
            -   "2. Objeto del contrato: ... Rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (S/D)
            
            -   "6. Formalización del contrato: ... Fecha de adjudicación: 1 de octubre de 2018..." (S/D)
            
            Entidades:

            -   Ayuntamiento de Marina de Cudeyo
            
            -   Imesapi, S.A.
            
            -   Secretaría
            """      
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
            

        elif BOE == "BOE-B-2019-52073":  #14
            resumen1 = """
            El Ministerio del Interior, específicamente a través de la Subdirección General de Servicios Penitenciarios, ha formalizado un contrato para la obra de mejora energética y adaptación de la instalación de ACS a la normativa contra legionella en el C.I.S. Evaristo Martín Nieto de Málaga.

    
            Preguntas potenciales que pueden responderse con la información proporcionada:

            -   ¿Quién es el poder adjudicador y qué tipo de actividad ejerce? El poder adjudicador es la Subdirección General de Servicios Penitenciarios, que forma parte del Ministerio del Interior y se encarga de la administración general del Estado.

            -   ¿Cuáles son los códigos CPV relacionados con la licitación? Los códigos CPV relacionados incluyen 45332000, que se refiere a trabajos de instalación de calefacción y otros sistemas de climatización.

            -   ¿Qué cantidad se gastó en la obra y quién fue el adjudicatario? El valor de la oferta seleccionada fue de 93.158,91 euros y el adjudicatario fue VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L.

            -   ¿Cuántas ofertas recibió el Ministerio del Interior para esta licitación? El Ministerio del Interior recibió un total de 7 ofertas para esta licitación.
            """
            
            citas1 = """
            Citas:

            -   "52073 Anuncio de formalización de contratos de: Subdirección General de Servicios Penitenciarios." (Pág. 66827)
            
            -   "2.1) Tipo: Administración General del Estado." (Pág. 66827)
            
            -   "4. Códigos CPV: 45332000 (...)" (Pág. 66827)
            
            -   "6. Descripción de la licitación: Obra para la mejora energética y adaptación de la instalación de ACS a la normativa contra legionella en el C.I.S. Evaristo Martín Nieto de Málaga." (Pág. 66827)
            
            -   "11. Ofertas recibidas: 7." (Pág. 66828)
            
            -   "12.1) Nombre: VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L." (Pág. 66828)
            
            -   "13.1) Valor de la oferta seleccionada: 93.158,91 euros." (Pág. 66828)
            
            Entidades:

            -   Ministerio del Interior
            
            -   Subdirección General de Servicios Penitenciarios
            
            -   VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L.
            
            -   C.I.S. Evaristo Martín Nieto de Málaga
            """
            
            resumen2 = """
            El anuncio detalla la formalización de contratos para la obra de mejora energética y adaptación de la instalación de ACS (agua caliente sanitaria) a la normativa contra la legionella en el C.I.S. Evaristo Martín Nieto de Málaga, adjudicada por el Ministerio del Interior, específicamente por la Subdirección General de Servicios Penitenciarios.

            Preguntas potenciales que pueden responderse con la información proporcionada:

            -   ¿Cuál es el objeto del contrato?

                -   El contrato tiene como objeto la obra para la mejora energética y adaptación de la instalación de ACS a la normativa contra legionella en el C.I.S. Evaristo Martín Nieto de Málaga.
            
            -   ¿Quién es el poder adjudicador y qué tipo de organización es?

                -   El poder adjudicador es la Subdirección General de Servicios Penitenciarios, que forma parte del Ministerio del Interior, una Administración General del Estado.
            
            -   ¿Cuáles son los criterios de adjudicación?

                -   La información específica sobre los criterios de adjudicación no se proporciona en el texto, pero normalmente se basan en aspectos como el precio, la calidad técnica, y el cumplimiento de requisitos técnicos.
            
            -   ¿Cuál es el valor de la oferta seleccionada?

                -   El valor de la oferta seleccionada es 93.158,91 euros.
            
            -   ¿Qué empresa fue adjudicataria del contrato?

                -   La empresa adjudicataria es VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L..
            
            -   ¿Cuándo se formalizó el contrato?

                -   La fecha específica de formalización del contrato no se menciona en el texto proporcionado. Para obtener esta información, se debe consultar el documento oficial completo.
                        """    
                        
            citas2 = """
            Citas:

            -   "52073 Anuncio de formalización de contratos de: Subdirección General de Servicios Penitenciarios." (Pág. 66827)
            
            -   "1. Poder adjudicador: ... Tipo: Administración General del Estado." (Pág. 66827)
            
            -   "Descripción de la licitación: Obra para la mejora energética y adaptación de la instalación de ACS a la normativa contra legionella en el C.I.S. Evaristo Martín Nieto de Málaga." (Pág. 66828)
            
            -   "Adjudicatarios: ... VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L." (Pág. 66828)
            
            -   "Valor de las ofertas: ... Valor de la oferta seleccionada: 93.158,91 euros." (Pág. 66829)
            
            Entidades:

            -   Ministerio del Interior
            
            -   Subdirección General de Servicios Penitenciarios
            
            -   C.I.S. Evaristo Martín Nieto de Málaga
            
            -   VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L.
            """  
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
  
  
  
            
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################




    elif enfoque == "summaryindex":
        if BOE == "BOE-A-2015-6119":         #1
            resumen1 = """
            La presente colección de textos se refiere a la autorización administrativa concedida para el cierre y desmantelamiento de la estación de regulación (ER) con presión de 80/72 bar, ubicada en la posición O-00 en Otero, provincia de Asturias. Esta autorización fue solicitada por Enagás Transporte, S.A.U., en virtud del cambio de titularidad de todas las autorizaciones y concesiones anteriormente otorgadas a Enagás, S.A., traspasadas ahora a Enagás Transporte, S.A.U.

            La Dirección General de Política Energética y Minas emitió informes positivos sobre la solicitud, y el Consejo de la Comisión Nacional de los Mercados y la Competencia también proporcionó un informe favorable.

            La autorización administrativa para el cierre y desmantelamiento de las instalaciones se concede bajo ciertas condiciones, que incluyen la obtención del Acta de Cierre emitida por la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias, así como la adecuada disposición de los materiales desmantelados, ya sea mediante su envío a un vertedero autorizado o su reutilización en otras instalaciones del Sistema gasista.
            """
            
            citas1 = """
            Referencias:

            * "La empresa 'Enagás Transporte, S.A.U.' deberá obtener el Acta de Cierre de las instalaciones de la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias." (BOE núm. 131, página 47024)
            * "El cierre de las instalaciones, autorizado por la presente resolución, deberá realizarse conforme al documento técnico denominado 'Memoria Cierre y Desmantelamiento Estación de Regulación 80/72 en Posición O-00', presentado por la empresa 'Enagás Transporte, S.A.U.' tanto a esta Dirección General como a la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias." (BOE núm. 131, página 47025)

            Entidades involucradas:

            * Enagás Transporte, S.A.U.
            * Dirección General de Política Energética y Minas
            * Consejo de la Comisión Nacional de los Mercados y la Competencia
            * Ministerio de Industria, Energía y Turismo
            * Delegación del Gobierno en Asturias
            """
            
            resumen2 = """
            La Resolución de la Dirección General de Política Energética y Minas concede a Enagás Transporte, S.A.U. la autorización administrativa para el cierre de la Estación de Regulación (ER) con presión de 80/72 bar en la posición O-00 en Otero, así como de las instalaciones asociadas. Esta autorización también incluye el desmantelamiento de dichas instalaciones.

            
            """      
            
            citas2 = """
            Referencias:

            * "Se otorga a la empresa ‘Enagás Transporte, S.A.U.’ autorización administrativa para el cierre de la Estación de Regulación (ER) con presión de 80/72 bar en la posición de válvulas O-00, en Otero, junto con las instalaciones asociadas." (BOE-A-2015-6119, página 47024)
            * "La presente autorización comprende también el desmantelamiento de dichas instalaciones, sin perjuicio de lo dispuesto en el apartado séptimo de la presente resolución." (BOE-A-2015-6119, página 47024)

            Entidades involucradas:

            * Enagás Transporte, S.A.U.
            * Estación de Regulación (ER)
            * Otero
            * Dirección General de Política Energética y Minas
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
            
        
        elif BOE == "BOE-A-2019-2031":     #2
            resumen1 = """
            El recurso de inconstitucionalidad impugna varios Decretos-ley y normativas que establecen medidas para proteger a los deudores hipotecarios, regular la vivienda y gestionar la economía. En particular, se cuestionan las competencias estatales en materia de propiedad, legislación procesal y ordenación económica.
            """
            
            citas1 = """
            Referencias:

            * "A continuación se detallan las actuaciones estatales dirigidas a abordar el problema de la vivienda y la reestructuración inmobiliaria y financiera..." (pág. 14488)
            
            * "El Abogado del Estado sostiene que el Decreto-ley impugnado vulnera las competencias estatales establecidas en los artículos 149.1.11 y 13 de la Constitución, al obstaculizar la eficacia de las medidas adoptadas por el Estado en las normas mencionadas..." (pág. 14489)
            
            * "En particular, se cuestionan los artículos 1 y la disposición adicional primera modificada por el Real Decreto-ley 1/2015, de 27 de febrero." (pág. 19, archivo: /teamspace/studios/this_studio/data/BOEs/BOE-A-2019-2031.pdf)
            
            * "La normativa impugnada altera el régimen jurídico establecido por el Estado, al exigir que las medidas del Código de Buenas Prácticas previstas en el Real Decreto-ley 6/2012, de 9 de marzo, se implementen dentro del sistema de mediación hipotecaria creado por la Comunidad Autónoma de Aragón." (pág. 19, archivo: /teamspace/studios/this_studio/data/BOEs/BOE-A-2019-2031.pdf)
            
            * "El artículo 149.1.11 y 13 CE no otorga al Estado la facultad de definir el contenido esencial de los derechos ni de imponer una uniformidad de situaciones jurídicas en todo el territorio nacional, sino de establecer condiciones básicas esenciales para el ejercicio de los poderes autonómicos." (pág. 1)
            
            * "El Abogado del Estado considera que, en términos generales, los preceptos impugnados violan las competencias del Estado según los artículos 149.1.11 y 13 CE, al interferir y afectar negativamente a la política económica del Gobierno dirigida a la reestructuración y estabilidad del sistema bancario y crediticio." (pág. 19)
            
            * "La norma impugnada se encuadra en el ámbito de la legislación procesal, lo que corresponde al artículo 149.1.6 CE." (pág. 22)

            
            Entidades involucradas:

            * Estado
            
            * Comunidad Autónoma de Aragón
            
            * Decreto-ley
            
            * Real Decreto-ley
            
            * Código de Buenas Prácticas
            
            * Tribunal Constitucional
            
            * Gobierno de Aragón
            """
            
            resumen2 = """
            El texto aborda diversos temas relacionados con la legislación autonómica y estatal en materia de vivienda, pobreza energética y acceso a la vivienda. Examina sentencias del Tribunal Constitucional que han declarado inconstitucionales y nulas varias disposiciones del Decreto-ley 3/2015 y otros textos legales.
            """      
            
            citas2 = """
            Referencias:

            * "El derecho dominical y las facultades que le son propias dejarían de ser reconocibles." (página 14494)
            * "La obligación de cesión no vulnera el contenido esencial del derecho de propiedad, sino que se inscribe dentro de la libertad de configuración de la competencia autonómica en materia de vivienda." (página 14496)
            * "La Ley de Enjuiciamiento Civil (art. 606.4) autoriza la enumeración de categorías generales en su legislación, lo cual ha sido implementado por el Decreto-ley aragonés 3/2015." (página 19)
            * "La STC 97/2018, de 19 de septiembre, FJ 2, a la que se debe hacer referencia en este caso, desestimó una alegación formulada en los mismos términos." (página 19)
            * "En el presente caso, no se cumplen ninguna de las tres operaciones procesales necesarias para aplicar la salvedad competencial contenida en el artículo 149.1.6 CE." (página 14501)

            Entidades involucradas:

            * Tribunal Constitucional
            * Decreto-ley del Gobierno de Aragón 3/2015, de 15 de diciembre
            * Comunidad Autónoma de Aragón
            * Estado
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2021-10584":   #3
            resumen1 = """
            El texto proporcionado contiene información sobre medidas urgentes en el ámbito de la fiscalidad energética y generación de energía, así como regulaciones relacionadas con la gestión del canon de regulación y tarifa de utilización del agua. Se establecen objetivos para reducir las emisiones de gases de efecto invernadero y aumentar la penetración de energías renovables hasta el 42% en 2030. Además, se regula el acceso a la red eléctrica y se fomenta la instalación de plantas de generación renovable y almacenamiento.
            """
            
            citas1 = """
            Cites:

            * "Se establece de forma excepcional y transitoria, hasta el 31 de diciembre de 2021, para los contratos de energía eléctrica cuyo término fijo de potencia no supere los 10 kW, una rebaja, desde el 21 al 10 por ciento, en el tipo impositivo del IVA que recae sobre todos los componentes de la factura eléctrica cuando el precio medio mensual del mercado mayorista en el mes anterior al de la facturación haya superado los 45 €/MWh" (pág. 76276).
            * "Se rebaja al 10 por ciento el tipo impositivo del IVA aplicable a la factura eléctrica de los titulares de contratos de suministro de electricidad que sean perceptores del bono social y, además, tengan reconocida la condición de vulnerable severo o vulnerable severo en riesgo de exclusión social" (pág. 76276).
            * "El proceso de descarbonización y electrificación de la economía, previsto en el Plan Nacional Integrado de Energía y Clima 2021-2030 (PNIEC), adoptado por el Acuerdo del Consejo de Ministros de 16 de marzo de 2021..." - BOE-A-2021-10584, página 76279


            Entities:

            * Hogares consumidores finales
            * Trabajadores autónomos
            * Bono social
            * Unión Europea
            * Asociación Europea de Libre Comercio
            * Canarias
            """
            
            resumen2 = """
            El Real Decreto-ley 12/2021 establece medidas urgentes en el ámbito de la fiscalidad energética y la generación de energía, con el objetivo de mitigar los efectos negativos del aumento de los precios de la electricidad en España. Esta problemática se ha intensificado especialmente desde marzo de 2021, cuando el mercado mayorista de electricidad en España registró precios inusualmente altos (pág. 76274).

            El decreto modifica la Ley 19/2003 para ampliar la protección prevista en el artículo 7 bis, extendiéndola a inversiones provenientes de la Unión Europea y de la Asociación Europea de Libre Comercio bajo ciertas condiciones (BOE-A-2021-10584, pág. 76278). Además, se prorroga hasta el 31 de diciembre de 2021 el régimen transitorio que suspende la liberalización de determinadas inversiones extranjeras directas, aplicándose también a las inversiones extranjeras directas en empresas cotizadas en España o en empresas no cotizadas si el valor de la inversión supera los 500 millones de euros (BOE-A-2021-10584, pág. 76278).
            """      
            
            citas2 = """
            Referencias:

            -   "Desde finales de 2020 y, con mayor intensidad, a partir de marzo de 2021, el mercado mayorista de electricidad en España ha mostrado precios inusualmente altos." (pág. 76274)
            
            -   "Esta situación no parece ser un evento aislado, sino que amenaza con convertirse en una tendencia estructural si se considera el comportamiento de los mercados a plazo de electricidad en España para el año 2021." (pág. 76276)
            
            Entidades involucradas:

            -   Real Decreto-ley 12/2021
            
            -   España
            
            -   Mercado mayorista de electricidad
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
            

        elif BOE == "BOE-A-2021-11043":  #4
            resumen1 = """
            Se corrigen errores en el Real Decreto-ley 12/2021, publicado en el Boletín Oficial del Estado número 151, de 25 de junio de 2021. El error se encuentra en la página 76283, artículo 1, apartado a), donde se indicaba que "Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior a 10 kW…". La corrección modifica esta expresión para que diga "inferior o igual a 10 kW…".
            """
            
            citas1 = """
            Referencias:

            * "Advertido error en el Real Decreto-ley 12/2021, de 24 de junio, por el que se adoptan medidas urgentes en el ámbito de la fiscalidad energética y en materia de generación de energía, y sobre gestión del canon de regulación y de la tarifa de utilización del agua..." (página no especificada)
            * "En la página 76283, en el artículo 1, apartado a), donde dice: ‘Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior a 10 kW…’, debe decir: ‘Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior o igual a 10 kW…’." (página 76283)
            * "BOLETÍN OFICIAL DEL ESTADO Núm. 158, Sábado 3 de julio de 2021, Sec. I, pág. 79322" (página 79322)

            Entidades involucradas:

            * Real Decreto-ley 12/2021
            * Boletín Oficial del Estado
            * Estado
            """
            
            resumen2 = """
            Se corrigen errores en el Real Decreto-ley 12/2021, publicado en el Boletín Oficial del Estado (BOE) número 151, de 25 de junio de 2021. Se rectifica un apartado del artículo 1 en la página 76283.
            """      
            
            citas2 = """
            Referencias:

            * "Advertido error en el Real Decreto-ley 12/2021, de 24 de junio, por el que se adoptan medidas urgentes en el ámbito de la fiscalidad energética y en materia de generación de energía, y sobre gestión del canon de regulación y de la tarifa de utilización del agua..." (página 1)
            * "En la página 76283, en el artículo 1, apartado a), donde dice: ‘Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior a 10 kW…’, debe decir: ‘Titulares de contratos de suministro de electricidad, cuya potencia contratada (término fijo de potencia) sea inferior o igual a 10 kW…’." (página 76283)
            * "BOLETÍN OFICIAL DEL ESTADO Núm. 158, Sábado 3 de julio de 2021, Sec. I, pág. 79322" (página 79322)

            Entidades involucradas:

            * Real Decreto-ley 12/2021
            * Boletín Oficial del Estado (BOE)
            * España
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2021-12603":  #5
            resumen1 = """
            El Congreso de los Diputados ha acordado convalidar el Real Decreto-ley 12/2021, de 24 de junio, que establece medidas urgentes en el ámbito de la fiscalidad energética, la generación de energía, y la gestión del canon de regulación y la tarifa de utilización del agua.


            """
            
            citas1 = """
            Referencias:

            * "De conformidad con lo dispuesto en el artículo 86.2 de la Constitución, el Congreso de los Diputados, en su sesión del día de hoy, acordó convalidar el Real Decreto-ley 12/2021..." (página no proporcionada)
            * "Se ordena la publicación para general conocimiento." (página no proporcionada)

            Entidades involucradas:

            * Congreso de los Diputados
            * Real Decreto-ley 12/2021
            * Palacio del Congreso de los Diputados
            * Meritxell Batet Lamaña
            """
            
            resumen2 = """
            La Resolución de 21 de julio de 2021 del Congreso de los Diputados dispone la publicación del Acuerdo de convalidación del Real Decreto-ley 12/2021 para general conocimiento. Este acuerdo aprobó medidas urgentes en fiscalidad energética, generación de energía, gestión del canon de regulación y tarifa de utilización del agua.
            """      
            
            citas2 = """
            Referencias:

            * "De conformidad con lo dispuesto en el artículo 86.2 de la Constitución, el Congreso de los Diputados, en su sesión del día de hoy, acordó convalidar el Real Decreto-ley 12/2021..." (página no especificada)
            * "Se ordena la publicación para general conocimiento." (página no especificada)
            * "BOLETÍN OFICIAL DEL ESTADO Núm. 179, Miércoles 28 de julio de 2021, Sec. I, pág. 90695" (BOE-A-2021-12603)

            Entidades involucradas:

            * Congreso de los Diputados
            * Real Decreto-ley 12/2021
            * Palacio del Congreso de los Diputados
            * Meritxell Batet Lamaña
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2021-16956":  #6
            resumen1 = """
            La Secretaría General de Coordinación Territorial ha publicado una Resolución (BOE-A-2021-16956) que contiene el Acuerdo de la Comisión Bilateral de Cooperación entre la Administración General del Estado y la Comunidad Autónoma de Canarias. Este acuerdo tiene como objetivo resolver las discrepancias surgidas en relación con la disposición final tercera del Real Decreto-ley 12/2021.
            """
            
            citas1 = """
            Referencias:

            * "La Secretaría General dispone la publicación en el ‘Boletín Oficial del Estado’ del Acuerdo que se transcribe como anexo a la presente resolución." (página no especificada)
            * "Iniciar negociaciones para resolver las discrepancias manifestadas en relación con la disposición final tercera del Real Decreto-ley 12/2021..." (página no especificada, Acuerdo de la Comisión Bilateral)

            Entidades involucradas:

            * Secretaría General de Coordinación Territorial
            * Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias
            * Real Decreto-ley 12/2021
            * Tribunal Constitucional
            * Ley Orgánica 2/1979
            * Ley Orgánica 1/2000
            * Parlamento de Canarias
            """
            
            resumen2 = """
            La Secretaría General de Coordinación Territorial ha publicado un Acuerdo de la Comisión Bilateral de Cooperación entre la Administración General del Estado y la Comunidad Autónoma de Canarias, relacionado con medidas urgentes en el ámbito de la fiscalidad energética y la generación de energía. El Acuerdo aborda las negociaciones para resolver discrepancias sobre la disposición final tercera del Real Decreto-ley 12/2021 y la designación de un grupo de trabajo para proponer soluciones.
            """      
            
            citas2 = """
            Referencias:

            * "La Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias ha adoptado el siguiente Acuerdo:" (página no especificada)
            * "Iniciar negociaciones para resolver las discrepancias manifestadas en relación con la disposición final tercera..." (página no especificada)
            * "Designar un grupo de trabajo para proponer a la Comisión Bilateral de Cooperación la solución que proceda." (página no especificada)

            Entidades involucradas:

            * Secretaría General de Coordinación Territorial
            * Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias
            * Real Decreto-ley 12/2021
            * Ley Orgánica 2/1979
            * Tribunal Constitucional
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2021-21214":  #7
            resumen1 = """
            El Tribunal Constitucional ha admitido a trámite un recurso de inconstitucionalidad contra la disposición final tercera del Real Decreto-ley 12/2021, que establece medidas urgentes en fiscalidad energética y generación de energía.

            
            """
            
            citas1 = """
            Referencias:

            * "El Pleno del Tribunal Constitucional, por providencia de 16 de diciembre de 2021, ha acordado admitir a trámite el recurso de inconstitucionalidad número 5935-2021..."
            * "...contra la disposición final tercera del Real Decreto-ley 12/2021, de 24 de junio..."

            Entidades involucradas:

            * Tribunal Constitucional
            * Pleno del Tribunal Constitucional
            * Secretario de Justicia del Pleno del Tribunal Constitucional (Alfonso Pérez Camino)
            * Parlamento de Canarias
            """
            
            resumen2 = """
            El Tribunal Constitucional ha admitido a trámite un recurso de inconstitucionalidad contra la disposición final tercera del Real Decreto-ley 12/2021, que adopta medidas urgentes en el ámbito de la fiscalidad energética y en materia de generación de energía.
            """      
            
            citas2 = """
            Referencias:

            * "El Pleno del Tribunal Constitucional, por providencia de 16 de diciembre de 2021, ha acordado admitir a trámite el recurso de inconstitucionalidad número 5935-2021, promovido por el Parlamento de Canarias, contra la disposición final tercera del Real Decreto-ley 12/2021..." (BOE-A-2021-21214, página 159287)

            Entidades involucradas:

            * Tribunal Constitucional
            * Real Decreto-ley 12/2021
            * Parlamento de Canarias
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2022-12754":  #8
            resumen1 = """
            La Xunta de Galicia ha interpuesto un recurso de inconstitucionalidad contra el artículo 20 y la disposición derogatoria única de la Ley 7/2021, alegando que infringen los artículos 9.3 y 132 de la Constitución Española (CE), relacionados con la seguridad jurídica y la reserva de ley, respectivamente. La Xunta argumenta que la Ley 7/2021 ha omitido deliberadamente el régimen del artículo 2 de la Ley 2/2013, generando inseguridad jurídica sobre la duración de las concesiones demaniales previas a la Ley de Costas y si el plazo máximo legal incluye prórrogas.

            La Abogacía del Estado sostiene que la Xunta ha fallado en la carga argumentativa y que los apartados tercero y cuarto del artículo 20 de la Ley 7/2021 se ajustan a lo dispuesto en el título III de la Ley 22/1988, considerando el artículo 13 ter de dicha ley.

            El Tribunal Constitucional ha desestimado el recurso de inconstitucionalidad, determinando que los preceptos impugnados no vulneran el principio de seguridad jurídica (artículo 9.3 CE) y son interpretables claramente por los operadores jurídicos, administraciones y tribunales.
            """
            
            citas1 = """
            Referencias:

            * "No basta la mera invocación formal de los preceptos en la demanda […] o incluso, como sucede en este caso, la existencia en la misma de una solicitud expresa de su declaración de inconstitucionalidad, para que este tribunal deba pronunciarse sobre todos y cada uno de ellos, sino que es preciso, además, que en el cuerpo del recurso se contenga la argumentación específica o razonamientos que fundamenten la presunta contradicción de estos con la norma fundamental […]" (STC 149/1991, FJ 4 B) h)
            * "Es carga de los recurrentes no solo la de abrir la vía para que el Tribunal pueda pronunciarse, sino también la de colaborar con la justicia del Tribunal en un pormenorizado análisis de las graves cuestiones que se suscitan. Es justo, pues, hablar [...] de una carga del recurrente y en los casos en que aquella no se observe, de una falta de diligencia procesalmente exigible, que es la diligencia de ofrecer la fundamentación que razonablemente es de esperar" (STC 234/2012, FJ 8)
            * "Desde el punto de vista gramatical, el término “seguridad” denota certeza, certidumbre, pero también confianza o previsibilidad. Si tales cualidades se proyectan sobre el ámbito del Derecho, se refiere a la claridad y certeza del Derecho" (STC 150/1990, FJ 8)

            Entidades involucradas:

            * Xunta de Galicia
            * Ley 7/2021, de 20 de mayo, de cambio climático y transición energética
            * Constitución Española (CE)
            * Tribunal Constitucional
            * Artículo 2 de la Ley 2/2013
            * Artículo 9.3 CE
            * Ley de Costas
            """
            
            resumen2 = """
            La recopilación de textos examina la constitucionalidad del artículo 20 y la disposición derogatoria única de la Ley 7/2021, de cambio climático y transición energética, enfocándose en el principio de seguridad jurídica en el dominio público marítimo-terrestre.
            """      
            
            citas2 = """
            Referencias:

            * "Por el contrario, el artículo 20 de la Ley 7/2021 no ofrece ninguna justificación sobre su alcance..." (página desconocida)
            * "Se ignora si el plazo máximo de setenta y cinco años de prórroga previsto en su artículo 20.4 de la Ley 7/2021 debe dar lugar a una revisión de oficio de las prórrogas extraordinarias concedidas antes de su entrada en vigor..." (página desconocida)
            * "La disposición derogatoria única de la Ley 7/2021, al no salvar expresamente el régimen del artículo 2 de la Ley 2/2013, lo habría derogado, lo cual entrañaría una retroactividad que afectaría a los derechos adquiridos y al principio de confianza legítima..." (página desconocida)

            Entidades involucradas:

            * Ley 7/2021, de cambio climático y transición energética
            * Artículo 20
            * Disposición derogatoria única
            * Ley 2/2013
            * Xunta de Galicia
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2022-2707":  #9
            resumen1 = """
            El Decreto-ley 28/2021 de la Generalitat de Cataluña introduce modificaciones en el libro quinto del Código Civil de Cataluña con el objetivo de facilitar la instalación de placas solares fotovoltaicas y mejorar la eficiencia energética en edificios sometidos al régimen de propiedad horizontal. Esta medida busca reducir el consumo de energía y facilitar el acceso a los fondos europeos Next Generation EU (NGEU) destinados a la rehabilitación de viviendas.
           
            """
            
            citas1 = """
            Referencias:

            * "El objetivo principal de la iniciativa es facilitar la instalación de placas solares fotovoltaicas para autoconsumo, es decir, para autoproducción de electricidad, en las cubiertas de los edificios plurifamiliares." (V, página 21002)
            * "No hay ninguna otra herramienta de elaboración de normas ni siquiera el procedimiento de lectura única que pueda satisfacer a tiempo la necesidad de urgencia descrita. Solo con la modificación normativa pretendida a través de decreto-ley se podrán destinar de manera ágil y efectiva las ayudas a la mejora de la eficiencia energética del parque de viviendas catalán." (V, página 21002)

            Entidades involucradas:

            * Generalitat de Cataluña
            * Código Civil de Cataluña
            * Next Generation EU (NGEU)
            * Régimen de propiedad horizontal
            """
            
            resumen2 = """
            El Decreto-ley 28/2021 de la Generalitat de Cataluña introduce modificaciones en el libro quinto del Código Civil de Cataluña para facilitar la instalación de equipos destinados a mejorar la eficiencia energética y sistemas de energías renovables en edificios sometidos al régimen de propiedad horizontal. También amplía la posibilidad de adoptar acuerdos por videoconferencia o sin reunión para las personas jurídicas de derecho privado hasta el 31 de diciembre de 2022. Además, se modifican los artículos 553-25, 553-26 y 553-30 del Código Civil de Cataluña para fomentar la instalación de fuentes de energía renovable y mejorar la eficiencia energética en los inmuebles.
            """      
            
            citas2 = """
            Referencias:

            * "La disponibilidad de estos fondos NGEU es, por lo tanto, una oportunidad crucial para adaptar el parque inmobiliario residencial de nuestro país a un consumo energético más sostenible mediante la instalación de equipos que mejoren la eficiencia energética o de sistemas de energías renovables en edificios sometidos al régimen de propiedad horizontal." (Página 20999, BOE-A-2022-2707)
            * "Se modifica el artículo 553-25 del libro quinto del Código civil de Cataluña, que queda redactado del modo siguiente..." (pág. 21003)
            * "Se modifica el artículo 553-26 del libro quinto del Código civil de Cataluña, que queda redactado del modo siguiente..." (pág. 21005)

            Entidades involucradas:

            * Generalitat de Cataluña
            * Código Civil de Cataluña
            * Fondo Europeo para la Transición Energética (NGEU)
            * Régimen de propiedad horizontal
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2022-2982":  #10
            resumen1 = """
            La Disposición 2982 del Boletín Oficial del Estado corrige errores en el Decreto-ley 28/2021, el cual modifica el libro quinto del Código civil de Cataluña para mejorar la eficiencia energética y facilitar la instalación de sistemas de energías renovables en edificios sometidos al régimen de propiedad horizontal. Las correcciones afectan al título del Decreto-ley y a la exposición de motivos.
            """
            
            citas1 = """
            Referencias:

            * "Habiendo observado varias erratas en el texto del citado Decreto-ley, publicado en el BOE núm. 44, de 21 de febrero de 2022..." (página no especificada)
            * "En el título, donde dice: «… en el ámbito de las personas jurídicas de derecho privado sujetos a las disposiciones del derecho civil catalán.», debe decir: «… en el ámbito de las personas jurídicas de derecho privado sujetas a las disposiciones del derecho civil catalán.»" (página no especificada)
            * "En la exposición de motivos (versión en catalán y castellano), apartado II, párrafo primero, donde dice: 'Este Decreto ley tiene por objeto modificar el Código civil de Cataluña respecto a los aspectos relativos a la ejecución de obras para la mejora de la eficiencia energética o hídrica y la instalación de sistemas de energías renovables en los edificios sujetos al régimen de propiedad horizontal. La reforma abarca cinco artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes).' Debe decir: 'Este Decreto ley tiene por objeto modificar el Código civil de Cataluña respecto a los aspectos relativos a la ejecución de obras para la mejora de la eficiencia energética o hídrica y la instalación de sistemas de energías renovables en los edificios sujetos al régimen de propiedad horizontal. La reforma abarca seis artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-42 (uso y disfrute de los elementos comunes), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes).'"

            Entidades:

            * Decreto-ley 28/2021
            * Boletín Oficial del Estado (BOE)
            * Código civil de Cataluña
            """
            
            resumen2 = """
            El Decreto-ley 28/2021 corrige errores en el libro quinto del Código civil de Cataluña y modifica el Decreto-ley 10/2020. Las correcciones incluyen un cambio en el título, sustituyendo "sujetos" por "sujetas", y una actualización en la exposición de motivos, apartado II, párrafo primero, donde se añade un artículo a la lista de artículos reformados.

      
            """      
            
            citas2 = """
            Las citas relevantes son:

            - En el título: "… en el ámbito de las personas jurídicas de derecho privado sujetos a las disposiciones del derecho civil catalán." (pág. no especificada)
            - En la exposición de motivos, apartado II, párrafo primero: "Este Decreto-ley tiene por objeto modificar el Código civil de Cataluña en relación con la ejecución de obras para mejorar la eficiencia energética o hídrica y la instalación de sistemas de energías renovables en los edificios sujetos al régimen de propiedad horizontal." (pág. no especificada)
            - En la exposición de motivos, apartado II, párrafo primero: "La reforma abarca cinco artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes)." (pág. no especificada)
            - En la exposición de motivos, apartado II, párrafo primero: "Este Decreto-ley tiene por objeto modificar el Código civil de Cataluña en relación con la ejecución de obras para mejorar la eficiencia energética o hídrica y la instalación de sistemas de energías renovables en los edificios sujetos al régimen de propiedad horizontal. La reforma abarca seis artículos: el artículo 553-25 (régimen general de adopción de acuerdos), el artículo 553-26 (adopción de acuerdos por unanimidad y por mayorías cualificadas), el artículo 553-30 (vinculación de los acuerdos), el artículo 553-42 (uso y disfrute de los elementos comunes), el artículo 553-43 (elementos comunes de uso exclusivo) y el artículo 553-44 (conservación y mantenimiento de los elementos comunes)." (pág. no especificada)

            Entidades implicadas:

            - Comunidad Autónoma de Cataluña
            - Decreto-ley 28/2021
            - Decreto-ley 10/2020
            - Código civil de Cataluña
            - BOE (Boletín Oficial del Estado)
            - Generalitat de Cataluña
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2023-26461":     #11
            resumen1 = """
            Los textos revisados tratan sobre modificaciones y ajustes en los programas de ayudas para la rehabilitación energética, la generación y almacenamiento de energía renovable, así como la normativa para la gestión de ayudas cofinanciadas con fondos europeos. Se introducen nuevos límites y niveles de ayuda, se establecen procedimientos para justificar el cumplimiento de las condiciones y se detallan los objetivos a alcanzar.
            """
            
            citas1 = """
            Las citas relevantes son:

            - Ampliación del Plazo de Vigencia: "Dado el interés observado en ambos programas y su creciente demanda, según la información trasladada por las comunidades autónomas y ciudades de Ceuta y Melilla, se considera oportuno ampliar el plazo de vigencia hasta el 31 de julio de 2024." (Página no especificada. Entidades clave: Programas de ayudas, Comunidades autónomas y ciudades de Ceuta y Melilla.)
            
            - Dotación del Programa PREE 5000: "La dotación del programa PREE 5000 se duplica hasta los 200 millones de euros para contribuir a la realización del objetivo CID #117." (Página no especificada. Entidades clave: Programa PREE 5000, Objetivo CID #117.)

            - Vigencia de los Programas de Incentivos: "Los programas de incentivos que se aprueban por este real decreto estarán vigentes desde el día siguiente a la publicación en el 'Boletín Oficial del Estado' hasta el 31 de julio de 2024." (Página no especificada. Entidad clave: Real Decreto.)

            Entidades implicadas:

            - Programas de ayudas
            - Comunidades autónomas y ciudades de Ceuta y Melilla
            - Programa PREE 5000
            - Objetivo CID #117
            """
            
            resumen2 = """
            El conjunto de textos aborda las modificaciones y ajustes realizados a los programas de incentivos destinados a la implementación de instalaciones de autoconsumo basadas en fuentes de energía renovable. Se introducen nuevos valores de referencia para calcular la ayuda base, se actualizan los requisitos documentales para justificar las actuaciones realizadas y se establecen las fechas límite para la presentación de solicitudes.
            """      
            
            citas2 = """
            Citas:

            - "Apartados i y ii, del anexo AII.A1. Documentación general aplicable a los programas de incentivos..." (pág. 172936)
            - "Programas de incentivos 1 y 2: Realización de instalaciones de autoconsumo, con fuentes de energía renovable, en el sector servicios y en otros sectores productivos de la economía..." (pág. 172937)

            Entidad implicada:

            - IDAE (Instituto para la Diversificación y Ahorro Energético)
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-A-2023-9215":  #12
            resumen1 = """
            El recurso de inconstitucionalidad interpuesto por el Parlamento de Canarias tiene como objetivo cuestionar la disposición final tercera del Real Decreto-ley 12/2021, que modifica la Ley 19/1994 sobre el régimen económico y fiscal de Canarias. Esta disposición establece límites a las deducciones por inversiones en producciones cinematográficas, series audiovisuales y espectáculos en vivo de artes escénicas y musicales realizadas en Canarias.
            """
            
            citas1 = """
            Citas:

            - "Modificación de la Ley 19/1994, de 6 de julio, sobre el régimen económico y fiscal de Canarias." (Disposición final tercera del Real Decreto-ley 12/2021)
            - "La disposición adicional decimocuarta de la Ley 19/1994 (según la redacción dada por el artículo 1.42 de la Ley 8/2018, de 5 de noviembre), bajo la rúbrica «Límites de las deducciones por inversiones en producciones cinematográficas, series audiovisuales y espectáculos en vivo de artes escénicas y musicales realizadas en Canarias»" (Antecedentes de la norma cuestionada)
            - "El objeto del recurso y posiciones de las partes." (Fundamentos jurídicos)

            Entidades implicadas:

            - Parlamento de Canarias
            - Real Decreto-ley 12/2021
            - Ley 19/1994
            - Ley 8/2018
            """
            
            resumen2 = """
            El recurso de inconstitucionalidad presentado por el Parlamento de Canarias se enfoca en la disposición final tercera del Real Decreto-ley 12/2021, que modifica la disposición adicional decimocuarta de la Ley 19/1994. La demanda argumenta que esta norma es inconstitucional al considerar que infringe el artículo 86.1 de la Constitución Española (CE) por falta de un presupuesto habilitante adecuado y que vulnera el artículo 9.3 CE al infringir el principio de seguridad jurídica y confianza legítima.

            Por su parte, se defiende que la norma no infringe el artículo 86.1 CE, dado que la justificación de la necesidad extraordinaria y urgente está reflejada en la exposición de motivos del decreto-ley y en el debate parlamentario.
            """      
            
            citas2 = """
            Citas:

            - "La actuación estatal que se impugna no cuestiona la modificación de la Ley del impuesto de sociedades ni en su oportunidad ni en su extensión. Es la actuación estatal objeto del presente recurso la que de facto propende a la equiparación del tratamiento fiscal en cuanto a los límites de las deducciones por inversiones en producciones cinematográficas, series audiovisuales y espectáculos en vivo de artes escénicas y musicales en Canarias..." (página 53446)
            - "La disposición adicional tercera no resulta fácil extraer de este precepto la garantía de un contenido inalterable del régimen económico y fiscal de Canarias" (STC 16/2003, FJ 7).
            - "El objeto de la presente resolución es resolver el recurso de inconstitucionalidad interpuesto por el Parlamento de Canarias en relación con la disposición final tercera del Real Decreto-ley 12/2021." (página no especificada)

            Entidades implicadas:

            - Parlamento de Canarias
            - Real Decreto-ley 12/2021
            - Ley 19/1994
            - Constitución Española (CE)
            - Congreso de los Diputados
            - Gobierno de la Nación
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-B-2018-54744":  #13
            resumen1 = """
            El anuncio del Ayuntamiento de Marina de Cudeyo comunica la formalización de un contrato mixto (obra y suministro) para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. El contrato fue adjudicado a Imesapi, S.A. (C.I.F.: A-28010478) con un presupuesto base de licitación de 1.101.860,18 euros.

            """
            
            citas1 = """
            
            Citas:

            - "54744 Anuncio del Ayuntamiento de Marina de Cudeyo por el que se formaliza contrato mixto (obra y suministro) sujeto a regulación armonizada para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (Núm. 278 Sábado 17 de noviembre de 2018 Sec. V-A. Pág. 69785)
            - "1. Entidad adjudicadora: a) Organismo: Ayuntamiento de Marina de Cudeyo. b) Dependencia que tramita el expediente: Secretaría. c) Número de expediente: 2018/251." (Idem)
            - "2. Objeto del contrato: a) Tipo: Mixto. b) Descripción: Rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. d) CPV (Referencia de Nomenclatura): 31527200-8; 50232000-0; 50232110-4; 50232100-1." (Idem)
            - "5. Presupuesto base de licitación. Importe neto: 910.628,25 euros. Importe total: 1.101.860,18 euros." (Idem)
            - "6. Formalización del contrato: a) Fecha de adjudicación: 1 de octubre de 2018. b) Fecha de formalización del contrato: 13 de noviembre de 2018. c) Contratista: Imesapi, S.A. (C.I.F.: A-28010478)." (Idem)

            Entidades implicadas:

            - Ayuntamiento de Marina de Cudeyo
            - Imesapi, S.A.
            - CPV (Referencia de Nomenclatura)
            - DOUE; BOE; BOC; Plataforma de Contratación del Sector Público
            """
            
            resumen2 = """
            El Ayuntamiento de Marina de Cudeyo ha formalizado un contrato mixto (obra y suministro) para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. El contrato fue adjudicado a Imesapi, S.A. el 1 de octubre de 2018 y formalizado el 13 de noviembre de 2018.

            
            """      
            
            citas2 = """
            Citas:

            - "54744 Anuncio del Ayuntamiento de Marina de Cudeyo por el que se formaliza contrato mixto (obra y suministro) sujeto a regulación armonizada para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (Núm. 278 Sábado 17 de noviembre de 2018 Sec. V-A. Pág. 69785)
            - "1. Entidad adjudicadora: a) Organismo: Ayuntamiento de Marina de Cudeyo. b) Dependencia que tramita el expediente: Secretaría." (Núm. 278 Sábado 17 de noviembre de 2018 Sec. V-A. Pág. 69785)
            - "2. Objeto del contrato: a) Tipo: Mixto. b) Descripción: Rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal." (Núm. 278 Sábado 17 de noviembre de 2018 Sec. V-A. Pág. 69785)
            - "6. Formalización del contrato: a) Fecha de adjudicación: 1 de octubre de 2018. b) Fecha de formalización del contrato: 13 de noviembre de 2018. c) Contratista: Imesapi, S.A." (Núm. 278 Sábado 17 de noviembre de 2018 Sec. V-A. Pág. 69785)

            Entidades implicadas:

            - Ayuntamiento de Marina de Cudeyo
            - Imesapi, S.A.
            - Secretaría
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2

        elif BOE == "BOE-B-2019-52073":  #14
            resumen1 = """
            Se anuncia la formalización de un contrato para la mejora energética y la adaptación de la instalación de agua caliente sanitaria (ACS) a la normativa contra la legionella en el Centro Penitenciario Evaristo Martín Nieto de Málaga. La Subdirección General de Servicios Penitenciarios, que depende del Ministerio del Interior, es el poder adjudicador de este contrato.


            """
            
            citas1 = """
            Citas:

            - "52073 Anuncio de formalización de contratos de: Subdirección General de Servicios Penitenciarios. Objeto: Obra para la mejora energética y adaptación de la instalación de ACS a la normativa contra legionella en el C.I.S. Evaristo Martín Nieto de Málaga." (Pág. 66827)
            - "1. Poder adjudicador: ... Subdirección General de Servicios Penitenciarios." (Pág. 66827)
            - "7. Tipo de procedimiento de adjudicación: Abierto simplificado." (Pág. 66828)
            - "10. Fecha de adjudicación: 14 de junio de 2019." (Pág. 66828)
            - "12.1) Nombre: VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L." (Pág. 66828)


            Entidades implicadas:

            - Subdirección General de Servicios Penitenciarios
            - Ministerio del Interior
            - Centro Penitenciario Evaristo Martín Nieto de Málaga
            - VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L.
            - España
            """
            
            resumen2 = """
            El anuncio de formalización de contratos está a cargo de la Subdirección General de Servicios Penitenciarios, que depende del Ministerio del Interior. El contrato tiene como objetivo llevar a cabo una obra para la mejora energética y adaptación de la instalación de agua caliente sanitaria (ACS) a la normativa contra la legionella en el Centro Penitenciario Evaristo Martín Nieto de Málaga.

            La Subdirección General de Servicios Penitenciarios, con número de identificación fiscal S2813060G y sede en Madrid, es el poder adjudicador. El procedimiento de licitación fue un abierto simplificado, con criterios de adjudicación basados en la ponderación del presupuesto de licitación.

            Se recibieron siete ofertas, siendo adjudicataria la empresa VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L., con una oferta valorada en 93.158,91 euros.

            
            """      
            
            citas2 = """
            Citas:

            - "MINISTERIO DEL INTERIOR" (página 66827)
            - "Subdirección General de Servicios Penitenciarios" (páginas 66827 y 66828)
            - "VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L." (página 66828)


            Entidades implicadas:

            - Ministerio del Interior
            - Subdirección General de Servicios Penitenciarios
            - VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L.
            - Centro Penitenciario Evaristo Martín Nieto de Málaga
            """
            
            resumenes = [resumen1, resumen2]
            resumen = random.choice(resumenes)
            
            if resumen == resumen1:
                return resumen, citas1
            
            elif resumen == resumen2:
                return resumen, citas2
