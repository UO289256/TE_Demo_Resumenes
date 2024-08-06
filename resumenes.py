# EN ESTE ARCHIVO ESTA LA FUNCIÓN CON TODOS LOS RESUMENES, PARA LLAMARLA DESDE LA DEMO

import random

def resumenes(enfoque, BOE):
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
    
    if enfoque == "tradicional":
        if BOE == "BOE-A-2015-6119":
            resumen1 = """
            Enagás Transporte, S. A., concesión administrativa para la conducción y suministro de gasoducto en Otero, en la provincia de Asturias de Asturias, se concedió la licencia administrativa para el uso industrial de energía natural en el término municipal de Otero en 2013 y Energía y Turismo, en 2013 de 2013, en el plazo de 3 meses a partir de la entrada en vigor de la autorización de cierre de la estación de regulación de la Estación de Regulación ER 8072 bar Sigue en EL PAÍS VÍDEO el extracto de sus artículos sobre la actualidad política y la actualidad de la actualidad sobre el tema de su vida política y su actualidad de actualidad en la actualidad del tema de sus últimos artículos sobre su vida en el libro The New York Times
            """
            
            resumen2 = """
            La empresa en la línea de regulación en Otero se hizo con la posición de válvulas Otero en 2013 y Medio y Turismo, en 2013, en fin de desmantelamiento de la estación de regulación de la Estación de Regulación ER 8072 bar, en Asturias, y Energía y Turismo ( En Magún de 2013 ), en el País Vasco, en Madrid, y Turismo y Turismo ) ( en 2013 ) en 2013 (, en España ), se concedió la licencia administrativa para la construcción y comercialización de los servicios de suministro de gas natural a favor de En Magás, en la provincia de Asturias, pero el Gobierno de Industria, Industria ), Industria (, Industria y Turismo. El Gobierno de la compañía en 2013 de la empresa en el término municipal de 2013, Industria,, Industria e Industria, en Industria ) ( Industria ) ) en en 2013 o Medio y Energía ( ( Industria y Energía ) se concedió a En Mag Magún, en 2014, y Gas y Energía, en Medio y Gas Gas, en Gas y Turismo o Turismo y ) Medio y turismo ) ) ( y Turismo e e Industria ) en Turismo ), En Magagás Transporte, en País Vasco ), y Industria ( ( Energía y y Turismo!, en especial Turismo ) ) El plazo máximo de tres meses de febrero, el año pasado, termina con el cierre de las plantas de Otero y Enagás Transporte, en Otero e instalaciones asociadas de gas natural, se aprobó en febrero de 2001 y febrero febrero de febrero de 2012 y febrero de marzo de 2013. El cierre de de las instalaciones, que se aprobó por el Gobierno en 2001 y marzo de 2002, se realizó en febrero, en febrero febrero, febrero de 2013, y el último año de 2002 y febrero 2013, se inició en febrero 2013 y febrero, se abrió en febrero. El Gobierno de febrero febrero febrero en febrero y febrero en marzo de febrero. La medida se aprobó el año de marzo, febrero febrero 2013 2013, con el año máximo de marzo del cierre de los campos de la Estación de Cerre, en diciembre de 2012, se ha realizado en febrero en 2013 de 2013 y marzo. El año pasado se aprobó con la autorización del de la Ley de Régimen Jurídico de las Administraciones Públicas y febrero 27 de 2013 de 2001, y la autorización de 2013 2013 y 2012 de marzo 2013 2013 de febrero 2013. Se aprobó en 2013, pero se llegó a cabo cabo cabo de febrero en 2012 y diciembre de febrero 2. El fin de febrero del año pasado El periodista de EL PAÍS Rubén Amón analiza las claves de la publicación de los resultados de la elección del presidente de EE UU en el plazo de un mes de mayo de 2015, el día siguiente de su publicación publicado en The New York Times. El Gobierno en asturiano dejará en español, dejará de ser parte del sistema Gasista de las consejería de la Comunidad General de Agricultura y Energía, desde febrero de 2014, dejará sin efecto retributivo de las empresas públicas y de de otros organismos públicos y de del sistema de las compañías públicas, y el Gobierno en febrero de febrero de 2013, el Gobierno, desde el momento en la declaración inexacta de las autorizaciones, licencias o permisos de competencia de las sociedades públicas y licencias o licencias o permiso de competencia municipal, y del procedimiento administrativo. La Administración se reserva el derecho a dejar de percibir alguna alguna reconocida, licencias y permiso de competencias de las multinacionales públicas y permisos de Competencia y de los otros organismos de de competencia y de otras empresas de de de empresas públicas. El Ejecutivo en el caso en caso de que se demuestre el incumplimiento de las condiciones de competencia, no tendrán la consideración de licencias o licencia de competencia en las compañías de de los grandes organismos públicos, y la actualidad de los datos
            """
            
            resumen3 = """
            En Otero la empresa de regulación se hizo con la posición de válvulas Otero en 2013, en 2013, en fin de desmantelamiento de la estación de regulación de la Estación de Regulación ER 8072 bar, en Asturias, y Energía y Turismo ( En Magún de 2013 ), en el País Vasco, en Madrid, y Turismo y Turismo ) ( en 2013 ) en 2013 (, en España ), se concedió la licencia administrativa para la construcción y comercialización de los servicios de suministro de gas natural a favor de En Magás, en la provincia de Asturias, pero el Gobierno de Industria, Industria ), Industria (, Industria y Turismo. El Gobierno de la compañía en 2013 de la empresa en el término municipal de 2013, Industria,, Industria e Industria, en Industria ) ( Industria ) ) en en 2013 o Medio y Energía ( ( Industria y Energía ) se concedió a En Mag Magún, en 2014, y Gas y Energía, en Medio y Gas Gas, en Gas y Turismo o Turismo y ) Medio y turismo ) ) ( y Turismo e e Industria ) en Turismo ), En Magagás Transporte, en País Vasco ), y Industria ( ( Energía y y Turismo!, en especial Turismo ) ) El plazo máximo de tres meses de febrero, el año pasado, termina con el cierre de las plantas de Otero y Enagás Transporte, en Otero e instalaciones asociadas de gas natural, se aprobó en febrero de 2001 y febrero febrero de febrero de 2012 y febrero de marzo de 2013. El cierre de de las instalaciones, que se aprobó por el Gobierno en 2001 y marzo de 2002, se realizó en febrero, en febrero febrero, febrero de 2013, y el último año de 2002 y febrero 2013, se inició en febrero 2013 y febrero, se abrió en febrero. El Gobierno de febrero febrero febrero en febrero y febrero en marzo de febrero. La medida se aprobó el año de marzo, febrero febrero 2013 2013, con el año máximo de marzo del cierre de los campos de la Estación de Cerre, en diciembre de 2012, se ha realizado en febrero en 2013 de 2013 y marzo. El año pasado se aprobó con la autorización del de la Ley de Régimen Jurídico de las Administraciones Públicas y febrero 27 de 2013 de 2001, y la autorización de 2013 2013 y 2012 de marzo 2013 2013 de febrero 2013. Se aprobó en 2013, pero se llegó a cabo cabo cabo de febrero en 2012 y diciembre de febrero 2. El fin de febrero del año pasado El periodista de EL PAÍS Rubén Amón analiza las claves de la publicación de los resultados de la elección del presidente de EE UU en el plazo de un mes de mayo de 2015, el día siguiente de su publicación publicado en The New York Times. El Gobierno en asturiano dejará en español, dejará de ser parte del sistema Gasista de las consejería de la Comunidad General de Agricultura y Energía, desde febrero de 2014, dejará sin efecto retributivo de las empresas públicas y de de otros organismos públicos y de del sistema de las compañías públicas, y el Gobierno en febrero de febrero de 2013, el Gobierno, desde el momento en la declaración inexacta de las autorizaciones, licencias o permisos de competencia de las sociedades públicas y licencias o licencias o permiso de competencia municipal, y del procedimiento administrativo. La Administración se reserva el derecho a dejar de percibir alguna alguna reconocida, licencias y permiso de competencias de las multinacionales públicas y permisos de Competencia y de los otros organismos de de competencia y de otras empresas de de de empresas públicas. El Ejecutivo en el caso en caso de que se demuestre el incumplimiento de las condiciones de competencia, no tendrán la consideración de licencias o licencia de competencia en las compañías de de los grandes organismos públicos, y la actualidad de los datos
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2019-2031":
            resumen1 = """
            El recurso de inconstitucionalidad en relación con las expropiaciones de uso de casas desocupadas es una modificación del régimen de ejecución hipotetexa de la Ley de buenas prácticas para la reestructuración de deudas con garantía hipotecaria de carácter social, pobreza energética y acceso a la vivienda. El Gobierno en funciones de la vivienda no puede recurrir a las extralimitaciones competenciales que hay en la Ley del Parlamento Vasco 32015, de enero de 2017, se declara nulo, en caso La Ley de Propiedad de 19797 es una transferencia coactiva y temporal de la titularidad de las casas en todo el territorio nacional. El Estado de la propiedad de las viviendas es el Estado de acuerdo con el artículo 150. 1. 000 %. El decretoley autonómico perjudica también el valor de reserva de ley para regular las manifestaciones de la función social del derecho de propiedad de la vivienda y las sociedades financieras bajo el control y las entidades financieras bajo la gestión del inmobili inmobiliaria El plazo de 15 días es suficiente para que se declare nulo el recurso de la Letrada de la Comunidad Autónoma de Aragón EAArgabilidad que no se puede ser tachada de inconstitucional por vulnerar los artíts de las entidades de crédito y otras de similar naturaleza en en sus balances de los balances. El plazo para formalizar el recurso del recurso de alegaciones de la letrada de la comunidad de sus resultados. El Gobierno de Aragón informó a El recurso de la Letrada de las Cortes de Aragón, del de Aragón y Cataluña, no se sustenta en el principio de conservación del derecho de propiedad de determinados sectores de la sociedad en riesgo de exclusión social, sino en la doctrina del Tribunal Supremo de Aragón. El Gobierno de Rajoy a la personalidad de de cada propiedad es un límite a la regulación del derecho que ha de respetar el legislador estatal a decidir sobre el derecho de la propiedad de determinadas casas, y la competencia estatal del derecho El artículo de la ley aragonesa establece un plazo para que los poderes públicos puedan imponer límites al derecho de propiedad de la vivienda y la delimitación del derecho a la propiedad de las preferentes en materia de vivienda y vivienda, función para la libertad de las personas en favor de las entidades financieras o sociedades inmobiliarias a las que elijan los compradores de las casas en pro de las empresas inmobiliarias bajo el control de las sociedades inmobili inmobiliras bajo su control o en la que elija los compradores El abogado del Estado, en nombre y representación de la presidenta del Gobierno en funciones, afirma que la petición de desistimiento parcial es un acuerdo alcanzado en la comisión bilateral de cooperación AragónEstado en Aragón y Cataluña, el Gobierno y las Cortes de Aragón, Aragón y País Vasco. El recurso de incons en contra de la Ley de Propiedad Inte Inte Intelectual de Aragón EAAAr no se prejucida en el derecho aragonés en conexión con la ley de ayudas El recurso de inconstitucionalidad no afectaba a la viabilidad y subsistencia del recurso de impugnación de la Ley de Propiedad del Pueblo de 2017, que ha sido parcialmente impugnado en el recurso de los recurrentes, por lo que la norma no puede ser impugnada y se ha impugnado y sobre las de las comunidades autónomas de las distintas comunidades del derecho sustantivo, no se cumplen en el presente caso ninguna en el caso ninguna es suficiente para la resolución del presente recurso de la ley impugnadas La ley estatal y la autonómica atienden a la misma situación lanzamientos de viviendas en supuestos de personas o a un tercero en caso de persona o a una persona en casos de persona y un tercero por otro por otro, o un tercero, en caso con persona, a un o por otro. La norma o un tercer por otro es el derecho de las comunidades a decidir si las autonomías en situación de persona, o en caso, se encuentran en el mismo presupuesto fáctico que la El recurso de inconstitucionalidad se limita a plasmar con modulaciones que acaban de ser recurrida por la ley estatal de la Ley de Propiedad del Pueblo. El recurso no puede ser compatible con el plazo de suspensión del lanzamiento de la norma de la ley de la propiedad del Pueblo, sin alterar la competencia del de las Administraciones estatales de la Comunidad Autónoma de Aragón y otras Administraciones públicas aragonesas, ni alterar la normativa procesal de la Administración de la la Comunidad Valenciana de Aragón, El recurso de inconstitucionalidad no es inconstitucional, sino que no son inconstitucionales interpretados en el sentido expuesto el escrito de Juan José González Trevijano Sánchez Rivas Rivas, que ha recurrido el recurso de la Sala del Estado de Madrid de la Audiencia de Madrid, que en el caso de la mediación hipotecaria de la ley de en el Código de buenas prácticas, que fue dictada al amparo de los apartados 6 y 8 del Códigoley 6222
            """
            
            resumen2 = """
            El Ejecutivo en funciones de Aragón, que ha recurrido el fallo de 17 de enero de 2019, se encuentra en contra de los artículos 1, 9, 12 y 3 del decretoley del Gobierno de Aragón 32015, de la Ley de buenas prácticas para la reestructuración viable de deudas con garantías hipotecarias de carácter social, pobreza energética y acceso a la vivienda en Navarra 320151515, que establece la ley de las buenas prácticas, no podrá ser recurrido en el plazo de las Cortes Generales y el Gobierno vasco en materia de ayudas públicas y de las normas de la ley hipotecaria sobre la vivienda y el recurso de las nuevas leyes del Gobierno central de Aragón 3211515. El recurso de emergencia para la reforma de las ayudas públicas, de las que ha sido interpuesto por el Ejecutivo de Aragón 31815, es suficiente para que haya que recurrir de contencioso contencioso contencioso de la Generalitat y el Ejecutivo vasco nulidad de las leyes de las públicas y del recurso de los bancos vasco, que han sido impugnadas por el Gobierno de la Comunidad Valenciana 32015 151515 15, pero no puede ser recurrir de emergencia social, no puede recurrir de las hipotecas de de las entidades públicas y las normas del Gobierno catalán. El plazo de gracia del Ejecutivo de Euskadi El recurso de la Junta andaluza se ha interpuesto en el caso de la pobreza energética y de la reforma de la ley de alquiler de casas y alquiler social o de la rehabilitación del convenio social de 2013 2013 201320161616, en la Ley de Andal Andaluzidad Andaluz, se ha detractores del decretoley 621222, que permite a las personas que pueden acceder a ellas sin recurrir a las extralimitaciones competenciales que fundamentan el presente recurso. El plazo de aplicación de los Ley de Andalucía 32015 en el convenio social o la modificación de los convenios de 2013, de 201320202012, que se han adoptado por el Estado de alquiler social de vivienda y la reforma del convenio del convenio de alquiler del colectivo colectivo de alquiler sociales o el colectivo colectivo colectivo que haya recurrido por el Gobierno andaluz, se limita a la posibilidad de que haya sido recurrida por el Ejecutivo de 2013 y la modificación del convenio y las leyes de 2013. El recurso del Estado de de pisos sociales o a la reforma urbana y la revisión de la deuda y la renovación urbana y de las pensiones públicas, en en los juzgados y administrativos, de de las prestaciones públicas de 2013 en la ley estatal de servicios sociales o la revisión del del convenio colectivo El recurso de los bienes recurre ante el Tribunal Supremo de las Autonomía La STC 932015 en caso de que se declara que no se expresan en la Ley del Estado de los últimos lanzamientos de desahucio de las que, al amparo del artículo 150, el Estado de la Ley en materia procesal o en los recursos de los contenciosos de la ley estatal o en las particularidades del derecho sustantivo aragonés no tiene conexión con la libertad de las competencias y el recurso contencioso contencioso contencioso, no hay conexión con el derecho sustantivo Aragonés. El Tribunal Supremo lo considera constitucional o constitucional o en el contencioso contencioso de los delitos de prevaricación y en los tribunales y en el plazo de la norma estatal y en en los casos de los recursos contenciosos. El Supremo considera que es constitucional o no hay relación alguna con el Derecho de las expropiaciones de viviendas desocupadas en todo el territorio nacional, sino en los los contencioso contencioso. El recurso del Estado a decidir si es legal o no puede ser recurso recurso retroactivo en la ley de los tribunales o en en el caso de los Contenciosos de los interpuestos de las comunidades. El Constitucional considera que no hay que ser ser ser constitucional o formalmente estatal o no en el recurso de las Supremo El recurso de inconstitucionalidad es suficiente para que se fije la ley de reserva del Estado a la comunidad vasca y temporalidad. El Gobierno autonómico puede imponer la obligación de reserva de ley para regular las manifestaciones de la función social del derecho de propiedad de la vivienda en todo el territorio nacional STC 61 de de de forma temporal de la propiedad de las propiedades desocupadas y temporales, y no puede ser válida de la Ley de expropiación forzosa de las hipotecas desocupada y temporal de las casas desocupados y temporales. El Estado de la ley que establece el derecho de los desahuciamiento de las viviendas en todos el ámbito nacional de disponer de una propiedad desocupado y temporal, pero no se puede, a partir de una orden de un consejero autonómico, a la comunidades vasca o temporalidad, y sin que se pueda ser válida en el caso de las decisiones de la la Administración estatal de expropiación de las propiedad de viviendas desocupaciones. La ley de la ejecución hipotecario en caso de desahuciar las hipoteca hipotecas. El recurso es (....)
            """
            
            resumen3 = """
            El Ejecutivo en funciones de Aragón, que ha recurrido el fallo de 17 de enero de 2019, se encuentra en contra de los artículos 1, 9, 12 y 3 del decretoley del Gobierno de Aragón 32015, de la Ley de buenas prácticas para la reestructuración viable de deudas con garantías hipotecarias de carácter social, pobreza energética y acceso a la vivienda en Navarra 320151515, que establece la ley de las buenas prácticas, no podrá ser recurrido en el plazo de las Cortes Generales y el Gobierno vasco en materia de ayudas públicas y de las normas de la ley hipotecaria sobre la vivienda y el recurso de las nuevas leyes del Gobierno central de Aragón 3211515. El recurso de emergencia para la reforma de las ayudas públicas, de las que ha sido interpuesto por el Ejecutivo de Aragón 31815, es suficiente para que haya que recurrir de contencioso contencioso contencioso de la Generalitat y el Ejecutivo vasco nulidad de las leyes de las públicas y del recurso de los bancos vasco, que han sido impugnadas por el Gobierno de la Comunidad Valenciana 32015 151515 15, pero no puede ser recurrir de emergencia social, no puede recurrir de las hipotecas de de las entidades públicas y las normas del Gobierno catalán. El plazo de gracia del Ejecutivo de Euskadi El recurso de la Junta andaluza se ha interpuesto en el caso de la pobreza energética y de la reforma de la ley de alquiler de casas y alquiler social o de la rehabilitación del convenio social de 2013 2013 201320161616, en la Ley de Andal Andaluzidad Andaluz, se ha detractores del decretoley 621222, que permite a las personas que pueden acceder a ellas sin recurrir a las extralimitaciones competenciales que fundamentan el presente recurso. El plazo de aplicación de los Ley de Andalucía 32015 en el convenio social o la modificación de los convenios de 2013, de 201320202012, que se han adoptado por el Estado de alquiler social de vivienda y la reforma del convenio del convenio de alquiler del colectivo colectivo de alquiler sociales o el colectivo colectivo colectivo que haya recurrido por el Gobierno andaluz, se limita a la posibilidad de que haya sido recurrida por el Ejecutivo de 2013 y la modificación del convenio y las leyes de 2013. El recurso del Estado de de pisos sociales o a la reforma urbana y la revisión de la deuda y la renovación urbana y de las pensiones públicas, en en los juzgados y administrativos, de de las prestaciones públicas de 2013 en la ley estatal de servicios sociales o la revisión del del convenio colectivo El recurso de los bienes recurre ante el Tribunal Supremo de las Autonomía La STC 932015 en caso de que se declara que no se expresan en la Ley del Estado de los últimos lanzamientos de desahucio de las que, al amparo del artículo 150, el Estado de la Ley en materia procesal o en los recursos de los contenciosos de la ley estatal o en las particularidades del derecho sustantivo aragonés no tiene conexión con la libertad de las competencias y el recurso contencioso contencioso contencioso, no hay conexión con el derecho sustantivo Aragonés. El Tribunal Supremo lo considera constitucional o constitucional o en el contencioso contencioso de los delitos de prevaricación y en los tribunales y en el plazo de la norma estatal y en en los casos de los recursos contenciosos. El Supremo considera que es constitucional o no hay relación alguna con el Derecho de las expropiaciones de viviendas desocupadas en todo el territorio nacional, sino en los los contencioso contencioso. El recurso del Estado a decidir si es legal o no puede ser recurso recurso retroactivo en la ley de los tribunales o en en el caso de los Contenciosos de los interpuestos de las comunidades. El Constitucional considera que no hay que ser ser ser constitucional o formalmente estatal o no en el recurso de las Supremo El recurso de inconstitucionalidad es suficiente para que se fije la ley de reserva del Estado a la comunidad vasca y temporalidad. El Gobierno autonómico puede imponer la obligación de reserva de ley para regular las manifestaciones de la función social del derecho de propiedad de la vivienda en todo el territorio nacional STC 61 de de de forma temporal de la propiedad de las propiedades desocupadas y temporales, y no puede ser válida de la Ley de expropiación forzosa de las hipotecas desocupada y temporal de las casas desocupados y temporales. El Estado de la ley que establece el derecho de los desahuciamiento de las viviendas en todos el ámbito nacional de disponer de una propiedad desocupado y temporal, pero no se puede, a partir de una orden de un consejero autonómico, a la comunidades vasca o temporalidad, y sin que se pueda ser válida en el caso de las decisiones de la la Administración estatal de expropiación de las propiedad de viviendas desocupaciones. La ley de la ejecución hipotecario en caso de desahuciar las hipoteca hipotecas. El recurso es suficiente de la libertad de propiedad del colectivo de disposición que establece la ley del artículo 150. 1. La medida es suficiente, pero es suficiente en la libertad del Estado para que haya una norma con rango de orden El recurso de inconstitucionalidad, que vulnera el principio de proporcionalidad, no se aprecia en el marco del derecho de las comunidades de gestión de activos, menoscabado la política comercial del Estado por la empresa de gestión y entidades financieras bajo en el control del yihadismo y la inmobili inmobili inmobili de gestión del sector bancario bajo en la gestión y las sociedades financieras bajo el control y la sociedad de gestión. El recurso no se puede ser compatible con los objetivos objetivos de las empresas financieras bajo del control y las entidades financieras Bajo el control de las entidades financiera bajo la gestión del sistema de meditación inmobiliaria bajo la tutela del y de la sociedad del Estado, menoscabando la libertad del del Estado en ejercicio de la gestión de entidades financieras sobre las sociedades públicas bajo en su control y con las sociedades financiera bajo de la propiedad del sector financiero en el que se ha ejercido en el sobre sobre las las entidades y entidades entidades financieras y las empresas de gestión privada bajo en manos del control control del de las sociedades de gestión, pero menoscabada en la política económica y en en el sistema de de mediática bajo en un control y en la sociedad y las inmobili inmobiliarias bajo bajo de control y de las las sociedades y financieras bajo la control del del y la empresa El plazo de 15 días es suficiente para que se declare nulo los preceptos impugnados desde la fecha de intepotencia y el empeoramiento de las condiciones en el mercado de la concesión de créditos hipotecarios y las titulizaciones en las cuentas de los vencimientos de eudulas y tarjetas tarjetas. El recurso de los bancos de crédito a las personas de crédito hipotecario y tarjetas hipotecario, según el decretoley, puede ser solventar la solvencia de las entidades. El Gobierno debe ser solvente en el plazo de quince días, a la Diputación General de Aragón, al margen de las empresas de crédito y tarjetas, según la ley de la Comunidad Autónoma de Aragón y a las Cortes de Aragón. El plazo para formalizar el recurso de la Letrada de Castilla - La Rioja, a las entidades de crédito, puede suspender la vigencia del plazo para presentar alegaciones en los últimos balances de los préstamos hipotecario. El Ejecutivo debe garantizar su solvencia y con el endurecimiento de los requisitos de contratación de los créditos hipotecario de las tarjetas y tarjetas de tarjetas. La petición de la letrada de las prefer preferentes y tarjetas. Los bancos de credi credirio y las tarjetas de los tipos hipotecario se declara necesario para el buen funcionamiento del mercado de tarjetas hipotecarias El plazo para solicitar la prórroga de un plazo para los tres días de la solicitud de prórroga del recurso de alegaciones en la contra de los terceros y en el plazo que presentó la Sala de la impugnación del plazo de tres semanas de plazo para la formalización de la denuncia de los tres meses de noviembre de 2016 de 2016, en la que aparece publicada en el recurso del recurso. La declaración de inembargabilidad es procesal derivado de las particularidades del derecho sustantivo de las competencias de alegaciones de la Comunidad de Aragón EAAr, en el marco de distribución del competencias de las comunidades de Aragón e IAA en ejercicio del sus competencias en la ley de Aragón y el derecho a la acción social y con un carácter puramente instrumental de la legislación autonómica. El recurso de la Ley de las personas del que se presentó la denuncia presentada en la recurso de de los meses de la petición de de la comunidad de Aragón a la petición del de las rentas económicas de Cataluña y el el derecho de la actuación social y del derecho de las las comunidades del País Vasco, en ejercicio de sus competencias, debe ser la que se asuma por por el titular de la competencia, y no puede imponerse en el ámbito de distribución de competencias en el el sus competencias de la Generalitat El recurso de la ley estatal de libertad de las personas que carecen de medios económicos suficientes para justificar que no hay ninguna posibilidad habitacional de lanzamiento de las entidades de entidades de crédito de las empresas de crédito y creación de un fondo social de las casas de crédito o creación de bancos de crédito no podrá imponerse en en el reglamento del decretoley, sino un límite que debe ser respetado por el legislador que resulte competente para regular el uso de la propiedad de las viviendas de las compañías de crédito, sino una limitación de la utilidad económica del derecho a decidir sobre el derecho de propiedad de la vivienda de las sociedades de crédito. No puede ser considerado que no se interfiere en el normal desenvivivimiento y de creación de las casetas de entidades financieras de las grandes entidades de préstamo de las nuevas entidades de créditos de las bancos de las las casas. El recurso no puede ser interpretado que no más intenso al mercado hipotecario, sino en el sistema de suspensión y no en absoluto el normal del derecho de Propiedad, sino que no puede prosperar en el marco de la Ley de ley de ley 2720121212. La ley estatal no es suficiente para que haya un recurso recurso de inconstitucionalidad por parte de la Administración anticipa la reducción del plazo de las operaciones de crédito La Comunidad Autónoma de Aragón ostenta competencia exclusiva en materia de vivienda, y la competencia estatal del derecho de propiedad de determinados sectores de la sociedad en riesgo de exclusión social, ni para limitar el plazo de la Ley de Autoterminación de las casas, y el límite a las competencias de la ley de reserva de de las propiedades a la Comunidad Autónoma es un límite a la regulación del derecho que ha de respetar el legislador estatal, sin perjuicio de quien ostente la propiedad del de la propiedad de determinadas casas, ni puede ser ser excluyente a la intervención de las comunidades. El límite de la libertad de propiedad del alquiler o título de arrendamiento o títulos de alquiler o titulaciones de las viviendas en el caso de las desocupaciones, ni a limitar la posibilidad de las nuevas viviendas, ni se restringe el derecho a decidir sobre el recurso de las competencias Rechaza también la intervención del de una función social en una urgencia de expropiación forzosa, y no es un vaciamiento de la posibilidad posibilidad de que acota el derecho de reserva reserva de las las propiedades en en caso de que las comunidades de de la Propiedad del de las algunas casas en en peligro de exclusión, ni en el marco de la competencia de algunas casas, o para limitar limitar la aplicación de las desahucia El recurso de la Letrada de las Cortes de Aragón, del de Aragón y Cataluña, no se sustenta en el principio de conservación de la norma de las autonomías sobre la posibilidad de que no innove en la ley estatal de las comunidades de crédito y de los inmuebles adjudicados a las entidades de crédito de crédito o en la práctica de las garantías hipotecarias sobre la vida económica general de cada tipo de propiedad privada del Estado es genérico y constituyen meras hipótesis, no puede pronunciarse sobre el derecho a decidir sobre la constitucionalidad de las entidades, y debe ser competente para que se limite a lo establecido en la Ley de las personas, y puede ser competencia del Estado, que legitima dicha en la vía judicial de la Ley sectorial que vela el derecho de propiedad de los deudores del Estado y en la actividad económica general del Estado. El Gobierno de Rajoy es competente para la aplicación del derecho de la propiedad de las empresas de entidades de entidades. El recurso contra una disposición con rango de ley autonómica encierra una dosis de discrecionalidad que refleja la orientación política del Gobierno en funciones. El Supremo puede ser competente en la materia del del sistema público. La ley sectorial es competencia de la ley de buenas prácticas. La norma sectorial, que vela la ley sectorial, es competencia del del Estado La falta de legitimación de la actuación de un mediador no es suficiente para que haya que prosperar o no se pueda suspender la eficacia de las medidas de crédito en el caso de las empresas afectadas, y que no puede ser el criterio de conservación del de conservación de la vivienda y la delimitación del derecho de derechos de la comunidad con los que se circunscribe el ámbito material de actuación del del Gobierno en funciones, consistentes en la implantación de las comunidades del Derecho propio Aragonés de la intervención del de Rajoy en funciones. El Gobierno de Aragón, en la ley de justicia, no puede suspender la aplicación de las normas especiales en materia del derecho a la propiedad de las preferentes en materia de acción social, no debe suspender el uso de las competencias especiales de la ley aragonés. El plazo para que los poderes públicos no sean suficientes de eventuales procesos de las diversas comunidades del ámbito ámbito de actuación de la Comunidad Autónoma a las entidades del Estado de Aragón y el Estado de de Aragón a las personas afectadas de la norma arañés de las las entidades de crédito a los bancos de crédito y la declaración del del derecho al de las personas personas afectadas, pero no debe ser la excepción de de conservación, y no deben ser excluidas de eventuales procedimientos de desprotección social El recurso de inconstitucionalidad, en relación con el derecho a decidir sobre el derecho de las personas, es el límite de la actuación de los funcionarios públicos de las rentas de propiedad y en cada caso histórico, no puede ser recognoscibles de todos los ciudadanos de cualquier comunidad del Estado de la propiedad del de la vivienda al amparo de una razón social, ni puede imponer una identidad de los deudores hipotecarios y de sus competencias, ni para imponer una discriminación de las comunidades del Estado. El Gobierno central, en caso de que se ampare en un título competencial, es legitimado a la ley de propiedad del Estado y de las autonomías exclusivas en cada uno de los ciudadanos en cualquier parte del territorio del derecho de propiedad de las casas y el resto de los poderes de las competencias, en cada momento histórico, carecen de la competencia estatal del artículo de la Ley de Propiedad de la Comunidad Autónoma. El artículo 9 no permite a las personas que pueden acceder a las viviendas que la Administración pone a su disposición se cumple en la legislación de las las competencias de la Generalitat, y que no puede imponerse en cualquier caso histórico histórico. El Estado no puede actuar en el ámbito ámbito de las facultades de las autonómicas exclusivas de las familias de de la comunidad del La Comunidad Autónoma no ha vulnerado una competencia no ejercida y unas condiciones estatales no existen, sino que se ha limitado a ejercitar su competencia en materia de vivienda para tratar de garantizar su disfrute por personas o entidades inmobiliarias bajo su control o en la libertad de los propietarios de o las entidades hipotecarias bajo en favor de las entidades o sociedades inmobiliarias o o sociedades o sociedades hipotecarias o sociedades y entidades hipotecaras bajo su derecho de propiedad de empresas o empresas inmobiliarias. Las entidades o entidades hipotecaarias bajo la tutela de las casas o sociedades. Las empresas o sociedades, en caso de personas o sociedades con entidades inmobililares bajo su libertad de decidir sobre la propiedad de las viviendas o sociedades que elijan los alquiler de las personas o empresas o entidades inmobiliariorias bajo el control de las empresas o en las sociedades o en sociedades inmobiliras bajo el derecho a decidir sobre el derecho de las o empresas hipotecaras o o en entidades inmobiliras o en el caso de sociedades o entidades entidades inmobilirias o o o las sociedades inmobililares (...)
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-10584":
            resumen1 = """
            El aumento de los precios de la electricidad y de los contratos de suministro de electricidad amenaza con convertirse en estructural si se atiende al comportamiento de los mercados a plazo plazo plazo, acaban por trasladándose también a sus contratos cuando se revisen los datos de precios de los hogares con menos renta, lo que amenaza con ser de forma inmediatos en el corto plazo ya que se han superado ya los años de la factura eléctrica y de las emisiones de electricidad en el marco de la transición ecológica en el escenario post El nuevo marco de ordenación del espacio marino prevé que se beneficien de la misma un gran número de trabajadores autónomos en todo el mercado mayorista en el anterior a la UE y las fuentes de energía de los países europeos o de la Gustera Marina y las energías renovables en países de la UE o los países de de la Samoa Europea, o en los países emergentes o de las Gustera, o por los países del mar territorial en países extranjeros o de los Estados europeos o países europeos, o de La nueva ley de modificación del régimen de deducción de 5, 4 millones de euros establece la obligación de aprobar los cánones y tarifas antes del inicio del ejercicio aoo en el que se aúpa la economía espaola de lugares en los que se da una excelente combinación de energía y electricidad de origen renovable en materia fiscalidad, en cuestión fiscalidad y fiscalidad. La nueva Ley de Investigación de Energía es una actividad liberalizada, no sometida a planificación vinculante y sujeta a un régimen regla La nueva ley de ordenación del espacio matinal debe servir para garantizar la protección de la seguridad, salud y orden público en nuestro país mientras se consolida la salida de la crisis sanitaria y la recuperación económica de las rentas más altas de la UE y la reducción de las primas de gas y las ayudas a las familias de la red de transporte y distribución en la red red de tren y distribución de las líneas de transporte o las ayudas de las redes de transporte de las energías renovables de las centrales de transporte La modificación de la Ley de Propiedad de la Constitución de 1978 es un ejercicio abusivo o arbitrario de las instituciones básicas del Estado, a los derechos, deberes y libertades de los ciudadanos en el siglo XXI y el Derecho electoral general. El Gobierno de Rajoy no puede imponer la ley de de las autonomías ni al Tribunal de las Comunidades Autónomas ni el Tribunal de la Carta Magna ni al el Tribunal electoral general de la República, ni a el Tribunal Electoral general ni El nuevo decretoley, de 17 de diciembre, se aplicará desde el día de la entrada en vigor de este real decretoley hasta el 31 de diciembre en el que se regula la figura del consumidor vulnerable, el bono social y otras medidas de protección para los consumidores domésticos de electricidad en el mar territorial del mar en barra de central central, o en parte, admitida a negociación en un mercado secundario espaol y concesión de recursos y reserva de energía renovable. El Gobierno de Rajoy, La Ley de Aguas, de junio de 2017, se aprobó en febrero de 2013, de 27 de noviembre, de modificado el régimen de Ley Americana de Libre Comercio y de los derechos de voto del capital social de la Unión Europea y de la Asociación Europea de libre Comercio de Comercio, de 6 de julio para la implantación de energía yo almacenamiento en la zona, regional y comunitaria, se podrá ver en distintas zonas en el mapa de Zonificación ambiental y foto en las zonas en las que El BOE oficial del Reino Unido publica en español el decreto deley Westwwn, que entrará en vigor el próximo día siguiente a partir de la Ley de Propiedad del Pueblo del Gobierno en el ámbito de las Administraciones. El decretoley puede aplicarse hasta el próximo mes siguiente a aquellos en el marco de de las administraciones sigue en vigor en la forma prevista en la Ley 392015, de 1 de octubre, en la que continúa en vigor vigor el mismo día siguiente de la ley
            """
            
            resumen2 = """
            El aumento de los precios de la electricidad y los contratos de suministro de electricidad puede convertirse en algo estructural si se observa el comportamiento de los mercados a plazo plazo plazo. Estos aumentos acabarán trasladándose también a los contratos cuando se revisen los datos de precios de los hogares con menos renta, lo que amenaza con ser inmediato inmediato en el corto plazo. Los años de la factura eléctrica y las emisiones de electricidad han sido superados superados en el marco de la transición ecológica en el nuevo escenario. El nuevo marco de ordenación del espacio marino prevé que un gran número de trabajadores autónomos se beneficien en todo el mercado mayorista, en la UE y en las fuentes de energía de los países europeos, o la Gustera Marina y las energías renovables en países de la UE o Samoa Europea, o en países emergentes o en la Gustera, o por los países del mar territorial en países extranjeros o Estados europeos. La nueva ley de modificación del régimen de deducción de 5.4 millones de euros establece la obligación de aprobar los cánones y tarifas antes del inicio del ejercicio aoo en el que se aúpa la economía española en lugares con excelente combinación de energía y electricidad renovable en materia de fiscalidad, fiscalidad y fiscalidad. La nueva Ley de Investigación de Energía es una actividad liberalizada, no sometida a planificación vinculante y sujeta a un régimen específico. La ley de ordenación del espacio matinal debe garantizar la protección de la seguridad, salud y orden público mientras se consolida la salida de la crisis sanitaria y la recuperación económica de las rentas más altas de la UE y la reducción de las primas de gas y las ayudas a las familias en la red de transporte y distribución en la red red de tren y distribución de las líneas de transporte o las ayudas de las redes de transporte de las energías renovables. La modificación de la Ley de Propiedad de la Constitución de 1978 es un ejercicio abusivo y arbitrario de las instituciones básicas del Estado y los derechos y libertades de los ciudadanos del siglo XXI. El Gobierno de Rajoy no puede imponer la ley de las autonomías ni al Tribunal de las Comunidades Autónomas ni al Tribunal de la Carta Magna ni al Tribunal Electoral General ni al Tribunal Electoral General ni El nuevo decreto-ley de 17 de diciembre se aplicará desde el día siguiente a la entrada en vigor hasta el 31 de diciembre, regulando la figura del consumidor vulnerable, el bono social y otras medidas de protección para los consumidores domésticos de electricidad en el mar territorial del mar en barra de central central o en parte, admitida a negociación en un mercado secundario español y concesión de recursos y reserva de energía renovable.
            """
            
            resumen3 = """
            El incremento de los precios de la electricidad y los contratos de suministro de electricidad puede llegar a ser estructural si consideramos el comportamiento de los mercados a plazo plazo plazo. Estos precios altos eventualmente se trasladarán también a los contratos cuando se revisen los datos de precios de los hogares con menos menos renta, lo que amenaza con ser de forma inmediata en el corto corto plazo. Se han superado ya los años de la factura eléctrica y las emisiones de electricidad dentro del marco de la transición ecológica en el nuevo nuevo escenario. El nuevo marco de ordenación del espacio marino prevé que un gran número de trabajadores autónomos se beneficien en todo el mercado mayorista y en la UE, las fuentes de energía de los países europeos o la Gustera Marina y las energías renovables en países de la UE o Samoa Europea, o en países emergentes o de la Gustera, o en los países del mar territorial, en países extranjeros o en Estados europeos. La nueva ley de modificación del régimen de deducción de 5.4 millones de euros establece la obligación de aprobar los cánones y tarifas antes del inicio del ejercicio aoo, en el que se mejora la economía española en lugares con excelente combinación de energía y electricidad renovable en materia de fiscalidad, fiscalidad y fiscalidad. La nueva Ley de Investigación de Energía es una actividad liberalizada, no sujeta a planificación vinculante y con un régimen específico. La nueva ley de ordenación del espacio matinal debe garantizar la protección de la seguridad, salud y orden público mientras se consolida la salida de la crisis sanitaria y la recuperación económica de las rentas más altas de la UE, y la reducción de las primas de gas y ayudas a las familias en la red red de transporte y distribución en la red de tren y distribución de las líneas de transporte o las ayudas de las redes de transporte de energías renovables. La modificación de la Ley de Propiedad de 1978 se considera un ejercicio abusivo y arbitrario de las instituciones básicas del Estado, los derechos y libertades de los ciudadanos en el siglo XXI. El Gobierno de Rajoy no puede imponer la ley de las autonomías ni al Tribunal de las Comunidades Autónomas ni al Tribunal de la Carta Magna ni al Tribunal Electoral General ni al Tribunal Electoral General ni al Tribunal Electoral General. El nuevo decreto-ley de 17 de diciembre se aplicará desde el día siguiente a la entrada en vigor hasta el 31 de diciembre, regulando la figura del consumidor vulnerable, el bono social y otras medidas de protección para los consumidores domésticos de electricidad en el mar territorial del mar en barra de central central o en parte, admitida a negociación en un mercado secundario español y concesión de recursos y reserva de energía renovable.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-11043":
            resumen1 = """
            El Real Decretoley1, de 24 de junio de 2021, se aprobó en junio de 2007, por el que se adoptado medidas urgentes en el ámbito de la fiscalidad energética y de la energía de fuentes renovables, y sobre gestión del agua de electricidad y de electricidad de electricidad, y de energía de de fuentes limpias, y en la gestión del suministro del agua, y del agua del, y la tarifa de fuentes fuentes renovables. En materia de generación del agua y de energías de fuentes
            """
            
            resumen2 = """
            El Real Decreto-ley 1, de 24 de junio de 2021, fue aprobado en junio de 2007, por el que se han adoptado medidas urgentes urgentes en el ámbito de la fiscalidad energética y la energía de fuentes renovables, y sobre la gestión de agua de electricidad y de electricidad de electricidad, y de energía de fuentes limpias, y en la gestión del suministro de agua, y del agua del, y la tarifa de fuentes fuentes renovables. En materia de generación del agua y de energías de fuentes de fuentes limpias y renovables, se han establecido nuevas normativas para la gestión y administración de estos recursos.
            """
            
            resumen3 = """
            El Real Decreto-ley 1, de 24 de junio de 2021, fue aprobado en junio de 2007, y se refiere a la adopción de medidas urgentes urgentes en el ámbito de la fiscalidad energética y de la energía de fuentes renovables, y sobre la gestión del agua de electricidad y de electricidad de electricidad, y energía de fuentes limpias, y en la gestión del suministro de agua y del agua del, y la tarifa de fuentes fuentes renovables. En cuanto a la generación del agua y energías de fuentes de fuentes renovables, se han creado normativas para regular la gestión y administración de estos recursos y sus respectivos suministros.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-12603":
            resumen1 = """
            El Congreso aprobó el Acuerdo de convalidación del Real Decretoley 122021, de 24 de junio, por el que se adoptado medidas urgentes en el ámbito de la fiscalidad energética y de la tarifa de utilización del de la energía de uso público del agua, publicado en el BOE oficial del Estado número 158 en 2021, publicada en el Boletín Oficial del Estado. El texto se aprobó en un BOE Oficial del del Estado de 158. 0000. 000021. 0000ce, en el País
            """
            
            resumen2 = """
            El Congreso aprobó el Acuerdo de convalidación del Real Decreto-ley 12/2021, de 24 de junio, por el que se adoptaron medidas urgentes urgentes en el ámbito de la fiscalidad energética y de la tarifa de utilización del agua de la energía de uso público, publicado en el BOE Oficial del Estado número 158 en 2021, publicada en el Boletín Oficial del Estado. El texto se aprobó en un BOE Oficial del Estado 158. 0000. 000021. 0000ce, en el País País.
            """
            
            resumen3 = """
            El Congreso aprobó el Acuerdo de convalidación del Real Decreto-ley 12/2021, de 24 de junio, por el que se han adoptado medidas urgentes urgentes en el ámbito de la fiscalidad energética y de la tarifa de utilización del de la energía de uso público del agua, publicado en el BOE oficial del Estado número 158 en 2021, publicada en el Boletín Oficial del Estado. El texto fue aprobado en un BOE Oficial del Estado 158. 0000. 000021. 0000ce, en el País País.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-16956":
            resumen1 = """
            La Comisión Bilateral de Cooperación Administración General del EstadoComunidad Autónoma de Canarias ha adoptado el Acuerdo de Cooperación Territorial, que se transcribe como anexo a la resolución del Tribunal Constitucional, a los efectos de la aplicación del decretoley 1221 en el ámbito de la Ley de Estatuto de autonomía de autonomía, de Canarias y en materia fiscalidad energética y de la tarifa de electricidad y de energía energía y de servicios de energía, y de tarifa de energía energética y fiscalidad energético y de electricidad
            """
            
            resumen2 = """
            La Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias ha adoptado el Acuerdo de Cooperación Territorial, que se transcribe como anexo a la resolución del Tribunal Constitucional, a los efectos de la aplicación del decreto-ley 12/21 en el ámbito de la Ley de Estatuto de autonomía de autonomía, de Canarias y en materia de fiscalidad energética y de la tarifa de electricidad y de energía energía, y de servicios de energía, y de tarifa de energía energética y fiscalidad energética y de electricidad
            """
            
            resumen3 = """
            La Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias ha adoptado el Acuerdo de Cooperación Territorial, que se transcribe como anexo a la resolución del Tribunal Constitucional, con el propósito de la aplicación del decreto-ley 12/21 en el ámbito de la Ley de Estatuto de autonomía de autonomía, de Canarias, y en materia de fiscalidad energética y la tarifa de electricidad y de energía de energía, y servicios de energía, y la tarifa de energía energética y fiscalidad energética y de electricidad.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-21214":
            resumen1 = """
            El recurso de inconstitucionalidad contra la disposición final tercera del Real Decretoley 122021, de 24 de junio de 2021, se ha producido en el marco de la fiscalidad energética y en materia de generación de energía, y sobre gestión del agua y la tarifa de utilización del agua, y de gestión de fuentes renovables, se han adoptado medidas urgentes en el ámbito de la generación de electricidad, y en el sistema de riego del agua. De uso del agua o de gestión del recurso de
            """
            
            resumen2 = """
            El recurso de inconstitucionalidad contra la disposición final tercera del Real Decreto-ley 12/2021, de 24 de junio de 2021, se ha producido en el marco de la fiscalidad energética y en materia de generación de energía, y sobre la gestión del agua y la tarifa de utilización del agua, y de gestión de fuentes renovables. Se han adoptado medidas urgentes urgentes en el ámbito de la generación de electricidad, y en el sistema de riego del agua. De uso del agua o de gestión del recurso de agua.
            """
            
            resumen3 = """
            El recurso de inconstitucionalidad contra la disposición final tercera del Real Decreto-ley 12/2021, de 24 de junio de 2021, ha surgido en el marco de la fiscalidad energética y en materia de generación de energía, así como sobre la gestión del agua y la tarifa de utilización del agua, y la gestión de fuentes renovables. Se han adoptado medidas urgentes urgentes en el ámbito de la generación de electricidad, y en el sistema de riego del agua. De uso del agua o de gestión del recurso del agua.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-12754":
            resumen1 = """
            El recurso de inconstitucionalidad de la Xunta de Galicia contra el artículo 20 y la disposición derogatoria única de la Ley 72021 debe dar lugar a una revisión de oficio de las prórrogas extraordinarias concedidas antes de que la Ley de costas y el Estatuto de Autonomía para gallegas o de de las prorros en la Ley J2021 no hayan sido derogadas, o en el plazo de prórroga de las concesiones o de prórrogas en el año de costas, ni en El abogado del Estado afirma que la Ley 72021 no puede ser retroactiva y que el plazo de setenta y cinco aos de la Ley K2021 debe solventarse conforme a los criterios hermenéuticos, según la Ley del Mar y a los requisitos de prórrogas anteriores o de la ley de Costa, que se prorrogó en ocho días más el plazo máximo legal para presentar alegaciones, según el plazo concedido por la Ley de Costa. El recurso de la X El letrado de la Xunta de Galicia entiende que la Ley 72021 ha omitido deliberadamente el régimen del art. 2 de la Ley K2021, pero no puede imponerse en el plazo de prórroga de los títulos de ocupación y uso sostenible del espacio público. El recurso de la defensa del Estado de ocupación no puede ser suficiente para saber si el régimen de las concesiones del dominio público terrestre y sus prórrogas se ha derogado, o no, para saber cuál la regulación del dominio El recurso de inconstitucionalidad a la Ley 7202021 es razonable que se pueda desvirtuarse sin un mínimo de argumentación y no caben impugnaciones globales y car car de argumentaciones y car Las alegaciones de la Xunta se concretan exclusivamente en la incertidumbre que ha supuesto la entrada en en vigor en vigor de la Ley de costas, que es totalmente ajeno a la duración de concesiones y prórrogas de los títulos de ocupación del dominio del dominio público de la propiedad del La Ley 72021 impugnados, que no es más que una norma de reenvío, se extrae la suficiencia e inteligibilidad de la remisión que, en relación con el régimen de gestión de los títeres y los intereses de la defensa del Estado de las La imprecisa línea que de interpretación aplicable en Derecho, puede ser determinante para la aplicación del ordenamiento jurídico en Derecho y no en el ámbito de lo jurídico y en los intereses del Estado, pueden ser determinantes en El Tribunal Constitucional desestima el recurso de inconstitucionalidad interpuesto por la defensa de la Xunta de Galicia contra la Ley de Costamiento de la Ley 72021, de que el plazo máximo de ocupación del dominio público terrestreterrestre se acota a setenta y de mayo, no se ajusta a lo fijado en en la Ley J20212, pero no puede ser objeto de interpretación de los operadores jurídicos en el siglo X2021. El plazo máximo, no prorrogó a lo establecido en
            """
            
            resumen2 = """
            El recurso de inconstitucionalidad de la Xunta de Galicia contra el artículo 20 y la disposición derogatoria única de la Ley 7/2021 debe dar lugar a una revisión de oficio de las prórrogas extraordinarias concedidas antes de que la Ley de Costas y el Estatuto de Autonomía para gallegas o de de las prórrogas en la Ley J/2021 hayan sido derogadas, o en el plazo de prórroga de las concesiones o de prórrogas en el año de costas, ni en. El abogado del Estado afirma que la Ley 7/2021 no puede ser retroactiva y que el plazo de setenta y cinco años de la Ley K/2021 debe solventarse conforme a los criterios hermenéuticos, según la Ley del Mar y a los requisitos de prórrogas anteriores o de la Ley de Costas, que se prorrogó en ocho días más el plazo máximo legal para presentar alegaciones, según el plazo concedido por la Ley de Costas. El recurso de la X. El letrado de la Xunta de Galicia entiende que la Ley 7/2021 ha omitido deliberadamente el régimen del art. 2 de la Ley K/2021, pero no puede imponerse en el plazo de prórroga de los títulos de ocupación y uso sostenible del espacio público. El recurso de la defensa del Estado de ocupación no puede ser suficiente para saber si el régimen de las concesiones del dominio público terrestre y sus prórrogas se ha derogado o no, para saber cuál es la regulación del dominio. El recurso de inconstitucionalidad a la Ley 7/2021 es razonable que se pueda desvirtuar sin un mínimo de argumentación y no caben impugnaciones globales y car car de argumentaciones y car. Las alegaciones de la Xunta se concretan exclusivamente en la incertidumbre que ha supuesto la entrada en en vigor en vigor de la Ley de Costas, que es totalmente ajeno a la duración de concesiones y prórrogas de los títulos de ocupación del dominio del dominio público de la propiedad del. La Ley 7/2021 impugnada, que no es más que una norma de reenvío, se extrae la suficiencia e inteligibilidad de la remisión que, en relación con el régimen de gestión de los títulos y los intereses de la defensa del Estado de las. La imprecisa línea que de interpretación aplicable en Derecho puede ser determinante para la aplicación del ordenamiento jurídico en Derecho y no en el ámbito de lo jurídico y en los intereses del Estado, pueden ser determinantes en. El Tribunal Constitucional desestima el recurso de inconstitucionalidad interpuesto por la defensa de la Xunta de Galicia contra la Ley de Costas de la Ley 7/2021, de que el plazo máximo de ocupación del dominio público terrestre se acota a setenta y mayo, no se ajusta a lo fijado en la Ley J/2021, pero no puede ser objeto de interpretación de los operadores jurídicos en el siglo X/2021. El plazo máximo, no prorrogó a lo establecido en.
            """
            
            resumen3 = """
            El recurso de inconstitucionalidad de la Xunta de Galicia contra el artículo 20 y la disposición derogatoria única de la Ley 7/2021 debe llevar a una revisión de oficio de las prórrogas extraordinarias concedidas antes de que la Ley de Costas y el Estatuto de Autonomía para gallegas o de de las prórrogas en la Ley J/2021 hayan sido derogadas, o en el plazo de prórroga de las concesiones o de prórrogas en el año de costas, ni en. El abogado del Estado afirma que la Ley 7/2021 no puede ser retroactiva y que el plazo de setenta y cinco años de la Ley K/2021 debe solventarse conforme a los criterios hermenéuticos, según la Ley del Mar y a los requisitos de prórrogas anteriores o de la Ley de Costas, que se prorrogó en ocho días más el plazo máximo legal para presentar alegaciones, según el plazo concedido por la Ley de Costas. El recurso de la X. El letrado de la Xunta de Galicia entiende que la Ley 7/2021 ha omitido deliberadamente el régimen del art. 2 de la Ley K/2021, pero no puede imponerse en el plazo de prórroga de los títulos de ocupación y uso sostenible del espacio público. El recurso de la defensa del Estado de ocupación no puede ser suficiente para saber si el régimen de las concesiones del dominio público terrestre y sus prórrogas se ha derogado o no, para saber cuál la regulación del dominio. El recurso de inconstitucionalidad a la Ley 7/2021 es razonable que se pueda desvirtuar sin un mínimo de argumentación y no caben impugnaciones globales y car car de argumentaciones y car. Las alegaciones de la Xunta se concretan exclusivamente en la incertidumbre que ha supuesto la entrada en en vigor en vigor de la Ley de Costas, que es totalmente ajeno a la duración de concesiones y prórrogas de los títulos de ocupación del dominio del dominio público de la propiedad del. La Ley 7/2021 impugnada, que no es más que una norma de reenvío, se extrae la suficiencia e inteligibilidad de la remisión que, en relación con el régimen de gestión de los títulos y los intereses de la defensa del Estado de las. La imprecisa línea que de interpretación aplicable en Derecho puede ser determinante para la aplicación del ordenamiento jurídico en Derecho y no en el ámbito de lo jurídico y en los intereses del Estado, pueden ser determinantes en. El Tribunal Constitucional desestima el recurso de inconstitucionalidad interpuesto por la defensa de la Xunta de Galicia contra la Ley de Costas de la Ley 7/2021, de que el plazo máximo de ocupación del dominio público terrestre se acota a setenta y mayo, no se ajusta a lo fijado en la Ley J/2021, pero no puede ser objeto de interpretación de los operadores jurídicos en el siglo X/2021. El plazo máximo, no prorrogó a lo establecido en.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-2707":
            resumen1 = """
            Las partidas de ayudas del fondo europeo Next Generation NGEU tienen por objetivo modificar el Código Civil de Catalua respecto a los aspectos relativos a la eficiencia energética y la instalación de equipos de energías renovables en los edificios públicos de uso común en los años de uso compartido en los sectores de energía y energía de energía renovable en los elementos de uso compartida en los últimos últimos apartados de las comunidades de uso público en los otros sectores de usos públicos de usos de uso uso compartido compartido en en los El acuerdo de la junta para instalar infraestructuras y sistemas de energía renovable es compatible con las instalaciones existentes en las ciudades de la UE y del Consejo Europeo y el Consejo Europeo de noviembre de 2013 de 2014 de 2013 2013 de 2013, año de enero de 2013 y 2013 de febrero de 2013. El decretoley amplía de 2013 se aprobó en diciembre de 2013 del año de febrero a 2013 de, febrero de diciembre, y el año de 2013 2012, en 2013 de de febrero febrero de 2012 de 2013 El Gobierno tiene que recurrir a la Ley 132008 para que se vuelvan más sostenibles en el conjunto de las comunidades de autoconsumo en los elementos comunes de la construcción y de elementos comunes en los que se ha instalado en la construcción o de los estatutos de la autonomía y los estatutos del Código Civil de Cataluña de Cataluña y de sus estatutos de los años de la Constitución y de los Estatutos del Código civil de la Comunidad y del los estatutos, el Código Civil del Código de la comunidad y de Las cuatro quintas partes de los apartados anteriores, a la hora de aplicarlos, no se han opuesto ninguno de los propietarios de las nuevas instalaciones o los nuevos servicios, que tienen un uso común por un plazo superior de quince a 10 a diez a los que conviven con sus familias con los mayores de setenta de setenta aos, y sus familiares con con sus padres con sus familiares y con sus familia con sus hijos con sus sus familias, con su familia con con derecho a voto común, Los propietarios de elementos comunes asumen todos los gastos de conservación y mantenimiento del inmueble, de manera que cumpla las condiciones básicas, de accesibilidad, de seguridad y de eficiencia energética o de higiene y eficiencia energética, de brindar servicios esenciales a todos los que se benefician de la instalación de infraestructuras o equipos de servicios públicos de energía renovable o en mal estado de casa o en malos estado de casas o en otros elementos comunes de uso uso exclusivo de de uso público o de mal estado, así así lo tienen
            """
            
            resumen2 = """
            Las partidas de ayudas del fondo europeo Next Generation NGEU tienen por objetivo modificar el Código Civil de Cataluña respecto a los aspectos relativos a la eficiencia energética y la instalación de equipos de energías renovables en los edificios públicos de uso común en los años de uso compartido en los sectores de energía y energía de energía renovable en los elementos de uso compartido en los últimos últimos apartados de las comunidades de uso público en los otros sectores de usos públicos de usos de uso uso compartido compartido en en los. El acuerdo de la junta para instalar infraestructuras y sistemas de energía renovable es compatible con las instalaciones existentes en las ciudades de la UE y del Consejo Europeo y el Consejo Europeo de noviembre de 2013 de 2014 de 2013 2013 de 2013, año de enero de 2013 y 2013 de febrero de 2013. El decreto-ley amplía de 2013 se aprobó en diciembre de 2013 del año de febrero a 2013 de, febrero de diciembre, y el año de 2013 2012, en 2013 de de febrero febrero de 2012 de 2013. El Gobierno tiene que recurrir a la Ley 13/2008 para que se vuelvan más sostenibles en el conjunto de las comunidades de autoconsumo en los elementos comunes de la construcción y de elementos comunes en los que se ha instalado en la construcción o de los estatutos de la autonomía y los estatutos del Código Civil de Cataluña de Cataluña y de sus estatutos de los años de la Constitución y de los Estatutos del Código Civil de la Comunidad y del los estatutos, el Código Civil del Código de la comunidad y de. Las cuatro quintas partes de los apartados anteriores, a la hora de aplicarlos, no se han opuesto ninguno de los propietarios de las nuevas instalaciones o los nuevos servicios, que tienen un uso común por un plazo superior de quince a 10 a diez a los que conviven con sus familias con los mayores de setenta de setenta años, y sus familiares con con sus padres con sus familiares y con sus familia con sus hijos con sus sus familias, con su familia con con derecho a voto común. Los propietarios de elementos comunes asumen todos los gastos de conservación y mantenimiento del inmueble, de manera que cumpla las condiciones básicas, de accesibilidad, de seguridad y de eficiencia energética o de higiene y eficiencia energética, de brindar servicios esenciales a todos los que se benefician de la instalación de infraestructuras o equipos de servicios públicos de energía renovable o en mal estado de casa o en malos estado de casas o en otros elementos comunes de uso uso exclusivo de de uso público o de mal estado, así así lo tienen.
            """
            
            resumen3 = """
            Las partidas de ayudas del fondo europeo Next Generation NGEU tienen como objetivo modificar el Código Civil de Cataluña en cuanto a los aspectos relacionados con la eficiencia energética y la instalación de equipos de energías renovables en los edificios públicos de uso común en los años de uso compartido en los sectores de energía y energía de energía renovable en los elementos de uso compartido en los últimos últimos apartados de las comunidades de uso público en los otros sectores de usos públicos de usos de uso uso compartido compartido en en los. El acuerdo de la junta para instalar infraestructuras y sistemas de energía renovable es compatible con las instalaciones existentes en las ciudades de la UE y del Consejo Europeo y el Consejo Europeo de noviembre de 2013 de 2014 de 2013 2013 de 2013, año de enero de 2013 y 2013 de febrero de 2013. El decreto-ley amplía de 2013 se aprobó en diciembre de 2013 del año de febrero a 2013 de, febrero de diciembre, y el año de 2013 2012, en 2013 de de febrero febrero de 2012 de 2013. El Gobierno debe recurrir a la Ley 13/2008 para que se vuelvan más sostenibles en el conjunto de las comunidades de autoconsumo en los elementos comunes de la construcción y de elementos comunes en los que se ha instalado en la construcción o de los estatutos de la autonomía y los estatutos del Código Civil de Cataluña de Cataluña y de sus estatutos de los años de la Constitución y de los Estatutos del Código Civil de la Comunidad y del los estatutos, el Código Civil del Código de la comunidad y de. Las cuatro quintas partes de los apartados anteriores, a la hora de aplicarlos, no se han opuesto ninguno de los propietarios de las nuevas instalaciones o los nuevos servicios, que tienen un uso común por un plazo superior de quince a 10 a diez a los que conviven con sus familias con los mayores de setenta de setenta años, y sus familiares con con sus padres con sus familiares y con sus familia con sus hijos con sus sus familias, con su familia con con derecho a voto común. Los propietarios de elementos comunes asumen todos los gastos de conservación y mantenimiento del inmueble, de manera que cumpla las condiciones básicas, de accesibilidad, de seguridad y de eficiencia energética o de higiene y eficiencia energética, de brindar servicios esenciales a todos los que se benefician de la instalación de infraestructuras o equipos de servicios públicos de energía renovable o en mal estado de casa o en malos estado de casas o en otros elementos comunes de uso uso exclusivo de de uso público o de mal estado, así así lo tienen.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-2982":
            resumen1 = """
            El artículo 55342 de la ley de adopción de acuerdos, el año 55 de todos los años, es el que más se ha modificado en seis artículos de uso exclusivo y disfrute disfrute disfrute del resto de elementos comunes, el de las sociedades renovables en los años de propiedad horizontal y de disfrute de la propiedad horizontal de de de las personas jurídicas de derecho civil catalán y los sistemas de energías renovables en todos los edificios públicos de propiedad vertical en los últimos años, los de las familias jurídicas de los edificios
            """
            
            resumen2 = """
            El artículo 55342 de la ley de adopción de acuerdos, el año 55 de todos los años, es el que más se ha modificado en seis artículos de uso exclusivo y disfrute disfrute disfrute del resto de elementos comunes, el de las sociedades renovables en los años de propiedad horizontal y de disfrute de la propiedad horizontal de de de las personas jurídicas de derecho civil catalán y los sistemas de energías renovables en todos los edificios públicos de propiedad vertical en los últimos años, los de las familias jurídicas de los edificios.
            """
            
            resumen3 = """
            El artículo 55342 de la ley de adopción de acuerdos, del año 55 de todos los años, es el que más se ha modificado en seis artículos de uso exclusivo y disfrute disfrute del resto de elementos comunes, el de las sociedades renovables en los años de propiedad horizontal y de disfrute de la propiedad horizontal de de de las personas jurídicas de derecho civil catalán y los sistemas de energías renovables en todos los edificios públicos de propiedad vertical en los últimos años, los de las familias jurídicas de los edificios.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2023-26461":
            resumen1 = """
            El Real Decreto 6912021, dotado con el carácter de base reguladora, se adapta a la inversión C2. de las comunidades y ciudades de Ceuta y Melilla y las ciudades del País Vasco, en ejecución del Plan más Seguridad Ener de la UE n. 651201. 000 millones de euros de 2013, se ajusta a los planes de ayudas públicas de la Unión Europea, según la Comisión Europea y otras ciudades de País Vasco y Ceuta, y en las ciudades de de la El Realley 36202020, de 3 de agos, no se vio afectado por las modificaciones en el reglamento de ayudas y las mejoras en la documentación a las comunidades de Ceuta y Melilla. El nuevo presupuesto de ayudas se aprobó en febrero de 2023, pero no se ha visto afectado por de los beneficiarios últimos de los programas de ayuda, y el año pasado, y del Consejo Europeo y el Consejo Europeo de junio de 2014, ni para los destinatarios últimos de la Ley de El Gobierno de Rajoy de los incentivos para las comunidades autónomas y ciudades de Ceuta y Melilla en sus listas de convocatorias, sin que pueda exceder de 18 meses desde la fecha de notificación de la concesión de la ayuda será el que se establezca en cada una de las convocatorias de las comunidades. El plan de de recuperación y reto demográfico del Plan de Recuperación, Transformación y Resiliencia Energética, Trans transformación y Resformación, Trans transformado y Resificación, Transforma y Res El informe de la Autoridad Europea de la Energía Europea de 2020 revela el impacto en el empleo local y en la cadena de valor industrial del 70 % de los residuos de Ceuta y Melilla, según la UE 202020. El Gobierno de Rajoy y Rajoy tendrán que deducciones en 2013 y de 2013 y 8. 8. 000 millones de euros en tres meses de la convocatoria de las adjudicaciones en cada uno de las convocatorias públicas, según el documento de la Unión Europea 2020 Las comunidades de Ceuta y Melilla podrán solicitar el reintegro anticipado del presupuesto de 2013, antes del 31 de octubre de 2024, en caso de no facilitarse ningún informe ni ninguna información a que se refiere el anexo V. 3. 3, de la UE N - 1407202 de la de la Unión Europea N - 1 n. 140222 de Bruselas N. 1407222, de Bruselas Europea N N, 1402, en 2013, se refiere a los La medida se realizará en los supuestos que determine la UE Europea y los sistemas de control de la UE y el Consejo de febrero de 2021 y ciudades de Ceuta y Melilla. El organismo de cada autonomía y ciudades deberá someterse a cualesquiera otras actuaciones de comprobación y control financiero que puedan realizar los órganos de control del organismo de las comunidades y ciudades del país, según el informe de la Intervención General de la Administración del Estado, el Tribunal de la Competencia Ecológica y del Consejo del Pueblo de febrero El plazo para la justificación de la concesión de ayudas se completará con la información aportada en el formulario de La Ley 382003, el reglamento europeo de 18 años de Bruselas Europe20202080, el año 2020202088. En el reglamento de la UE Europe208080, Bruselas Europea202081, el documento de la Unión Europea Europea208081, la ley de Bruselas Europea Europea8080... en el reglamento Europeo 202020802080. en Las comunidades autónomas y ciudades de Ceuta y Melilla se beneficiarán de los incentivos para autoconsumo existentes en el sector servicios y otros sectores productivos 10 kWh Cap 5. 000 kWI, el doble de lo que exige el Gobierno de EE UUhAyu de la empresa aplicable sobre el de los planes de ayuda a la protección del medio ambiente y otras ciudades de la comunidad autónoma y ciudades a las comunidades de la comunidades y ciudades españolas de las regiones españolas y las ciudades españolas El ministro de Cultura y del Reto Demográfico analiza el estado de la situación política de España y la situación de Cataluña en el país sudamericano de la crisis económica y el estado del Estado de las finanzas públicas en el último año, el año en el que se ha reunido con el ministro de del Cultura de Cultura
            """
            
            resumen2 = """
            El Real Decreto 6912021, dotado con el carácter de base reguladora, se adapta a la inversión C2. de las comunidades y ciudades de Ceuta y Melilla y las ciudades del País Vasco, en ejecución del Plan más Seguridad Ener de la UE n. 651201. 000 millones de euros de 2013, se ajusta a los planes de ayudas públicas de la Unión Europea, según la Comisión Europea y otras ciudades de País Vasco y Ceuta, y en las ciudades de de la El Realley 36202020, de 3 de agos, no se vio afectado por las modificaciones en el reglamento de ayudas y las mejoras en la documentación a las comunidades de Ceuta y Melilla. El nuevo presupuesto de ayudas se aprobó en febrero de 2023, pero no se ha visto afectado por de los beneficiarios últimos de los programas de ayuda, y el año pasado, y del Consejo Europeo y el Consejo Europeo de junio de 2014, ni para los destinatarios últimos de la Ley de El Gobierno de Rajoy de los incentivos para las comunidades autónomas y ciudades de Ceuta y Melilla en sus listas de convocatorias, sin que pueda exceder de 18 meses desde la fecha de notificación de la concesión de la ayuda será el que se establezca en cada una de las convocatorias de las comunidades. El plan de de recuperación y reto demográfico del Plan de Recuperación, Transformación y Resiliencia Energética, Trans transformación y Resformación, Trans transformado y Resificación, Transforma y Res El informe de la Autoridad Europea de la Energía Europea de 2020 revela el impacto en el empleo local y en la cadena de valor industrial del 70 % de los residuos de Ceuta y Melilla, según la UE 202020. El Gobierno de Rajoy y Rajoy tendrán que deducciones en 2013 y de 2013 y 8. 8. 000 millones de euros en tres meses de la convocatoria de las adjudicaciones en cada uno de las convocatorias públicas, según el documento de la Unión Europea 2020 Las comunidades de Ceuta y Melilla podrán solicitar el reintegro anticipado del presupuesto de 2013, antes del 31 de octubre de 2024, en caso de no facilitarse ningún informe ni ninguna información a que se refiere el anexo V. 3. 3, de la UE N - 1407202 de la de la Unión Europea N - 1 n. 140222 de Bruselas N. 1407222, de Bruselas Europea N N, 1402, en 2013, se refiere a los La medida se realizará en los supuestos que determine la UE Europea y los sistemas de control de la UE y el Consejo de febrero de 2021 y ciudades de Ceuta y Melilla. El organismo de cada autonomía y ciudades deberá someterse a cualesquiera otras actuaciones de comprobación y control financiero que puedan realizar los órganos de control del organismo de las comunidades y ciudades del país, según el informe de la Intervención General de la Administración del Estado, el Tribunal de la Competencia Ecológica y del Consejo del Pueblo de febrero El plazo para la justificación de la concesión de ayudas se completará con la información aportada en el formulario de La Ley 382003, el reglamento europeo de 18 años de Bruselas Europe20202080, el año 2020202088. En el reglamento de la UE Europe208080, Bruselas Europea202081, el documento de la Unión Europea Europea208081, la ley de Bruselas Europea Europea8080... en el reglamento Europeo 202020802080. en Las comunidades autónomas y ciudades de Ceuta y Melilla se beneficiarán de los incentivos para autoconsumo existentes en el sector servicios y otros sectores productivos 10 kWh Cap 5. 000 kWI, el doble de lo que exige el Gobierno de EE UUhAyu de la empresa aplicable sobre el de los planes de ayuda a la protección del medio ambiente y otras ciudades de la comunidad autónoma y ciudades a las comunidades de la comunidades y ciudades españolas de las regiones españolas y las ciudades españolas El ministro de Cultura y del Reto Demográfico analiza el estado de la situación política de España y la situación de Cataluña en el país sudamericano de la crisis económica y el estado del Estado de las finanzas públicas en el último año, el año en el que se ha reunido con el ministro de del Cultura de Cultura.
            """
            
            resumen3 = """
            El Real Decreto 6912021, dotado con el carácter de base reguladora, se adapta a la inversión C2. de las comunidades y ciudades de Ceuta y Melilla y las ciudades del País Vasco, en ejecución del Plan más Seguridad Ener de la UE n. 651201. 000 millones de euros de 2013, se ajusta a los planes de ayudas públicas de la Unión Europea, según la Comisión Europea y otras ciudades de País Vasco y Ceuta, y en las ciudades de de la El Realley 36202020, de 3 de agos, no se vio afectado por las modificaciones en el reglamento de ayudas y las mejoras en la documentación a las comunidades de Ceuta y Melilla. El nuevo presupuesto de ayudas se aprobó en febrero de 2023, pero no se ha visto afectado por de los beneficiarios últimos de los programas de ayuda, y el año pasado, y del Consejo Europeo y el Consejo Europeo de junio de 2014, ni para los destinatarios últimos de la Ley de El Gobierno de Rajoy de los incentivos para las comunidades autónomas y ciudades de Ceuta y Melilla en sus listas de convocatorias, sin que pueda exceder de 18 meses desde la fecha de notificación de la concesión de la ayuda será el que se establezca en cada una de las convocatorias de las comunidades. El plan de de recuperación y reto demográfico del Plan de Recuperación, Transformación y Resiliencia Energética, Trans transformación y Resformación, Trans transformado y Resificación, Transforma y Res El informe de la Autoridad Europea de la Energía Europea de 2020 revela el impacto en el empleo local y en la cadena de valor industrial del 70 % de los residuos de Ceuta y Melilla, según la UE 202020. El Gobierno de Rajoy y Rajoy tendrán que deducciones en 2013 y de 2013 y 8. 8. 000 millones de euros en tres meses de la convocatoria de las adjudicaciones en cada uno de las convocatorias públicas, según el documento de la Unión Europea 2020 Las comunidades de Ceuta y Melilla podrán solicitar el reintegro anticipado del presupuesto de 2013, antes del 31 de octubre de 2024, en caso de no facilitarse ningún informe ni ninguna información a que se refiere el anexo V. 3. 3, de la UE N - 1407202 de la de la Unión Europea N - 1 n. 140222 de Bruselas N. 1407222, de Bruselas Europea N N, 1402, en 2013, se refiere a los La medida se realizará en los supuestos que determine la UE Europea y los sistemas de control de la UE y el Consejo de febrero de 2021 y ciudades de Ceuta y Melilla. El organismo de cada autonomía y ciudades deberá someterse a cualesquiera otras actuaciones de comprobación y control financiero que puedan realizar los órganos de control del organismo de las comunidades y ciudades del país, según el informe de la Intervención General de la Administración del Estado, el Tribunal de la Competencia Ecológica y del Consejo del Pueblo de febrero El plazo para la justificación de la concesión de ayudas se completará con la información aportada en el formulario de La Ley 382003, el reglamento europeo de 18 años de Bruselas Europe20202080, el año 2020202088. En el reglamento de la UE Europe208080, Bruselas Europea202081, el documento de la Unión Europea Europea208081, la ley de Bruselas Europea Europea8080... en el reglamento Europeo 202020802080. en Las comunidades autónomas y ciudades de Ceuta y Melilla se beneficiarán de los incentivos para autoconsumo existentes en el sector servicios y otros sectores productivos 10 kWh Cap 5. 000 kWI, el doble de lo que exige el Gobierno de EE UUhAyu de la empresa aplicable sobre el de los planes de ayuda a la protección del medio ambiente y otras ciudades de la comunidad autónoma y ciudades a las comunidades de la comunidades y ciudades españolas de las regiones españolas y las ciudades españolas El ministro de Cultura y del Reto Demográfico analiza el estado de la situación política de España y la situación de Cataluña en el país sudamericano de la crisis económica y el estado del Estado de las finanzas públicas en el último año, el año en el que se ha reunido con el ministro de del Cultura de Cultura.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2023-9215":
            resumen1 = """
            El recurso de inconstitucionalidad de la disposición final tercera del Real Decretoley 122021, de 24 de junio, se ha interpuesto en el marco de los decretos leyes y régimen fiscal y fiscalidad y de las renovables y de suministro del agua de uso público del agua y energía del agua del suministro del de electricidad del agua se ha recurrido por el Gobierno de Canarias en el ámbito de la fiscalidad energética y de la tarifa de uso y de electricidad de uso del público de energía y energía de energía, y en la línea de suministro de energía del suministro y energía fiscal y de generación del agua, y el de la energía de electricidad y de energía de de electricidad, y la tarifa del agua ha interpuesto alegaciones de contra la disposición de los Gobiernos de Canarias y el suministro de electricidad en Canarias en la Ley de autonomía y electricidad del siglo XX. El recurso interpuesto por el Tribunal Constitucional no es suficiente para justificar el recurso de la garantía institucional del régimen fiscal fiscal de Balea sobre el canon de regulación y electricidad de de energía natural y de el energía de fuentes del suministro de agua del del agua. La ley de electricidad no es suficientes para justificar su recurso de deducciones en Canarias, pero no hay suficiente para justifica el recurso recurso de EACan sobre las renovables El nuevo art. 36 LIS, de 5 de noviembre, no solo se proyecta en una imposición indirecta singularidad de las deducciones en producciones cinematográficas y musicales y musicales, también en los términos de la ley de la Ley del Estatuto de autonomía de Canarias y de los impuestos impuestos impuestos de sociedades en adelante y en sus extensión ni en su extensión o en sus oportunidades ni en sus oportunidad ni en el plazo de aplicación del régimen fiscal de las sociedades ni en en su posibilidad o en su oportunidad o en en sus perspectivas ni en los detalles de la legislación estatal, sino también en sus proyecciones ni en la extensión o sus extensión o En sus oportunidades u en sus consecuencias ni en las oportunidades ni de en sus posibilidades ni en si si la ley tributaria ni en cuando se cumple o en los datos de la normativa estatal y musicales de las normas que configura la norma estatal y fiscalidad, sino en sus utilidad o en la posibilidad posibilidad de que la ley del impuesto de sociedades no cuestiona la aplicación aplicación aplicación aplicar o afecta a la imposición indirecta de las las de sociedades de de sociedades, sino a que la norma fiscalidad y el fiscal de estas comunidades en Canarias y en su alcance o en cuando la ley fiscal fiscalidad de estas sociedades en Canarias en adelante, en en el caso de la imposición El recurso recuerda la doctrina constitucional sobre la constitucionalidad de la ley de Canarias91, la deducción por inversiones en producciones cinematográficas y musicales en Canarias sin informes preceptivo y previo previo previo del Gobierno de Canarias y el de Canarias no cuestionó la modificación del régimen fiscal de la Ley de modificado del régimen de las en Canarias. El informe del Parlamento de Canarias recuerda que el sistema fiscal y fiscalidad es necesario y de constituirse antes, y que debe ser previo, previo o de constitución del trámite de la norma no puede ser previo y de constitución de un trámite de un procedimiento de participación en el procedimiento de consultas de las películas de artes, proyecciones audiovisuales y espectáculo en concierto de artes y espectáculos en conciertos de artes de artes escénicas o musicales de artes musicales en reci recital de artes en Canarias, y no se ha modificado uno de los elementos esenciales de los estatuto de las cintas audiovisuales de artes o musicales en el registro de los datos preceptivo de un informe previo previo y previo o previo o en el caso de creación de un plazo de participación y espectáculo de artes. El Gobierno de la un trámite previo previo, previa y de de constituir un trámite para que no se puede tener que ser antes, por lo que no hay que ser previo antes ...
            """
            
            resumen2 = """
            El recurso de inconstitucionalidad de la disposición final tercera del Real Decretoley 122021, de 24 de junio, se ha interpuesto en el marco de los decretos leyes y régimen fiscal y fiscalidad y de las renovables y de suministro del agua de uso público del agua y energía del agua del suministro del de electricidad del agua se ha recurrido por el Gobierno de Canarias en el ámbito de la fiscalidad energética y de la tarifa de uso y de electricidad de uso del público de energía y energía de energía, y en la línea de suministro de energía del suministro y energía fiscal y de generación del agua, y el de la energía de electricidad y de energía de de electricidad, y la tarifa del agua ha interpuesto alegaciones de contra la disposición de los Gobiernos de Canarias y el suministro de electricidad en Canarias en la Ley de autonomía y electricidad del siglo XX. El recurso interpuesto por el Tribunal Constitucional no es suficiente para justificar el recurso de la garantía institucional del régimen fiscal fiscal de Balea sobre el canon de regulación y electricidad de de energía natural y de el energía de fuentes del suministro de agua del del agua. La ley de electricidad no es suficientes para justificar su recurso de deducciones en Canarias, pero no hay suficiente para justifica el recurso recurso de EACan sobre las renovables El nuevo art. 36 LIS, de 5 de noviembre, no solo se proyecta en una imposición indirecta singularidad de las deducciones en producciones cinematográficas y musicales y musicales, también en los términos de la ley de la Ley del Estatuto de autonomía de Canarias y de los impuestos impuestos impuestos de sociedades en adelante y en sus extensión ni en su extensión o en sus oportunidades ni en sus oportunidad ni en el plazo de aplicación del régimen fiscal de las sociedades ni en en su posibilidad o en su oportunidad o en en sus perspectivas ni en los detalles de la legislación estatal, sino también en sus proyecciones ni en la extensión o sus extensión o En sus oportunidades u en sus consecuencias ni en las oportunidades ni de en sus posibilidades ni en si si la ley tributaria ni en cuando se cumple o en los datos de la normativa estatal y musicales de las normas que configura la norma estatal y fiscalidad, sino en sus utilidad o en la posibilidad posibilidad de que la ley del impuesto de sociedades no cuestiona la aplicación aplicación aplicación aplicar o afecta a la imposición indirecta de las las de sociedades de de sociedades, sino a que la norma fiscalidad y el fiscal de estas comunidades en Canarias y en su alcance o en cuando la ley fiscal fiscalidad de estas sociedades en Canarias en adelante, en en el caso de la imposición El recurso recuerda la doctrina constitucional sobre la constitucionalidad de la ley de Canarias91, la deducción por inversiones en producciones cinematográficas y musicales en Canarias sin informes preceptivo y previo previo previo del Gobierno de Canarias y el de Canarias no cuestionó la modificación del régimen fiscal de la Ley de modificado del régimen de las en Canarias. El informe del Parlamento de Canarias recuerda que el sistema fiscal y fiscalidad es necesario y de constituirse antes, y que debe ser previo, previo o de constitución del trámite de la norma no puede ser previo y de constitución de un trámite de un procedimiento de participación en el procedimiento de consultas de las películas de artes, proyecciones audiovisuales y espectáculo en concierto de artes y espectáculos en conciertos de artes de artes escénicas o musicales de artes musicales en reci recital de artes en Canarias, y no se ha modificado uno de los elementos esenciales de los estatuto de las cintas audiovisuales de artes o musicales en el registro de los datos preceptivo de un informe previo previo y previo o previo o en el caso de creación de un plazo de participación y espectáculo de artes. El Gobierno de la un trámite previo previo, previa y de de constituir un trámite para que no se puede tener que ser antes, por lo que no hay que ser previo antes ...
            """
            
            resumen3 = """
            El recurso de inconstitucionalidad de la disposición final tercera del Real Decretoley 122021, de 24 de junio, se ha interpuesto en el marco de los decretos leyes y régimen fiscal y fiscalidad y de las renovables y de suministro del agua de uso público del agua y energía del agua del suministro del de electricidad del agua se ha recurrido por el Gobierno de Canarias en el ámbito de la fiscalidad energética y de la tarifa de uso y de electricidad de uso del público de energía y energía de energía, y en la línea de suministro de energía del suministro y energía fiscal y de generación del agua, y el de la energía de electricidad y de energía de de electricidad, y la tarifa del agua ha interpuesto alegaciones de contra la disposición de los Gobiernos de Canarias y el suministro de electricidad en Canarias en la Ley de autonomía y electricidad del siglo XX. El recurso interpuesto por el Tribunal Constitucional no es suficiente para justificar el recurso de la garantía institucional del régimen fiscal fiscal de Balea sobre el canon de regulación y electricidad de de energía natural y de el energía de fuentes del suministro de agua del del agua. La ley de electricidad no es suficientes para justificar su recurso de deducciones en Canarias, pero no hay suficiente para justifica el recurso recurso de EACan sobre las renovables El nuevo art. 36 LIS, de 5 de noviembre, no solo se proyecta en una imposición indirecta singularidad de las deducciones en producciones cinematográficas y musicales y musicales, también en los términos de la ley de la Ley del Estatuto de autonomía de Canarias y de los impuestos impuestos impuestos de sociedades en adelante y en sus extensión ni en su extensión o en sus oportunidades ni en sus oportunidad ni en el plazo de aplicación del régimen fiscal de las sociedades ni en en su posibilidad o en su oportunidad o en en sus perspectivas ni en los detalles de la legislación estatal, sino también en sus proyecciones ni en la extensión o sus extensión o En sus oportunidades u en sus consecuencias ni en las oportunidades ni de en sus posibilidades ni en si si la ley tributaria ni en cuando se cumple o en los datos de la normativa estatal y musicales de las normas que configura la norma estatal y fiscalidad, sino en sus utilidad o en la posibilidad posibilidad de que la ley del impuesto de sociedades no cuestiona la aplicación aplicación aplicación aplicar o afecta a la imposición indirecta de las las de sociedades de de sociedades, sino a que la norma fiscalidad y el fiscal de estas comunidades en Canarias y en su alcance o en cuando la ley fiscal fiscalidad de estas sociedades en Canarias en adelante, en en el caso de la imposición El recurso recuerda la doctrina constitucional sobre la constitucionalidad de la ley de Canarias91, la deducción por inversiones en producciones cinematográficas y musicales en Canarias sin informes preceptivo y previo previo previo del Gobierno de Canarias y el de Canarias no cuestionó la modificación del régimen fiscal de la Ley de modificado del régimen de las en Canarias. El informe del Parlamento de Canarias recuerda que el sistema fiscal y fiscalidad es necesario y de constituirse antes, y que debe ser previo, previo o de constitución del trámite de la norma no puede ser previo y de constitución de un trámite de un procedimiento de participación en el procedimiento de consultas de las películas de artes, proyecciones audiovisuales y espectáculo en concierto de artes y espectáculos en conciertos de artes de artes escénicas o musicales de artes musicales en reci recital de artes en Canarias, y no se ha modificado uno de los elementos esenciales de los estatuto de las cintas audiovisuales de artes o musicales en el registro de los datos preceptivo de un informe previo previo y previo o previo o en el caso de creación de un plazo de participación y espectáculo de artes. El Gobierno de la un trámite previo previo, previa y de de constituir un trámite para que no se puede tener que ser antes, por lo que no hay que ser previo antes ...
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-B-2018-54744":
            resumen1 = """
            El Ayuntamiento de la única ciudad adjudicada a Organismo Ayuntamientos de Marina de Cudeo tiene un contrato de servicios para la construcción y suministro de servicios públicos en la zona de la adjudicación de servicio a Organismo Municipales de Marina. El Ayuntamiento se niega a declararse en contra de una empresa concesionaria del de servicio, pero la empresa no se ha formalizado en la adjudicación del contrato a Organismo consist consistoriaria del servicio de servicio de transporte público, pero el gobierno municipal se negó a declarararse en contra contra de de la empresa pública de servicios de servicio público de servicio y servicios públicos de Marina, pero no se encuentra en contra contrario de la compañía pública del servicio, que se adjudicó en junio de 2018, pese no de la concesión del servicio a organismos públicos de la ciudad de la adjudicataria del servicio en la que se ha adjudicado el servicio a un instituto público de servicios, y la empresa municipal se ha quedado en manos de un contrato mixto, pero su empresa municipal no ha logrado adjudicar la concesión de servicios a Organismo, aunque no no de las adjudicar el contrato de servicio en el servicio público, no de 2013. El Gobierno municipal se niega en manos del sector público, que ya ha recurrido el concurso de la licitación del servicio público
            """
            
            resumen2 = """
            
            El Ayuntamiento de la única ciudad adjudicada a Organismo Ayuntamientos de Marina de Cudeo tiene un contrato de servicios para la construcción y suministro de servicios públicos en la zona de la adjudicación de servicio a Organismo Municipales de Marina. El Ayuntamiento se niega a declararse en contra de una empresa concesionaria del de servicio, pero la empresa no se ha formalizado en la adjudicación del contrato a Organismo consist consistoriaria del servicio de servicio de transporte público, pero el gobierno municipal se negó a declarararse en contra contra de de la empresa pública de servicios de servicio público de servicio y servicios públicos de Marina, pero no se encuentra en contra contrario de la compañía pública del servicio, que se adjudicó en junio de 2018, pese no de la concesión del servicio a organismos públicos de la ciudad de la adjudicataria del servicio en la que se ha adjudicado el servicio a un instituto público de servicios, y la empresa municipal se ha quedado en manos de un contrato mixto, pero su empresa municipal no ha logrado adjudicar la concesión de servicios a Organismo, aunque no no de las adjudicar el contrato de servicio en el servicio público, no de 2013. El Gobierno municipal se niega en manos del sector público, que ya ha recurrido el concurso de la licitación del servicio público
            """
            
            resumen3 = """
            El Ayuntamiento de la única ciudad, que está adjudicada a Organismo Ayuntamientos de Marina de Cudeo, tiene un contrato para servicios en la construcción y el suministro de servicios públicos en la zona adjudicada a Organismo Municipales de Marina. El Ayuntamiento no quiere declararse en contra de una empresa concesionaria del servicio, aunque la empresa no se ha formalizado en la adjudicación del contrato a Organismo consistoriaria del servicio de transporte público. El gobierno municipal se niega a declararse en contra de la empresa pública de servicios de servicio y servicios públicos de Marina. A pesar de que la compañía pública del servicio fue adjudicada en junio de 2018, la concesión del servicio a organismos públicos de la ciudad de la adjudicataria del servicio no se ha concretado. La empresa municipal se ha quedado con un contrato mixto, pero no ha logrado adjudicar la concesión de servicios a Organismo, aunque no se ha adjudicado el contrato de servicio en el servicio público desde 2013. El Gobierno municipal sigue en manos del sector público, que ya ha recurrido el concurso de la licitación del servicio público.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

        elif BOE == "BOE-B-2019-52073":
            resumen1 = """
            El ganador de la serie MasterChef, de Netflix, es el ganador de un concurso de acreedores de la empresa de EE UU, que tiene más de 1. 800. 000 empleos en España de todo el país sudamericano. Te mostramos las mejores ofertas de la última semana en España y el Banco Mundial de Desarrollo Humanos, según la estadística de ventas de este tipo de ofertas más altas del año pasado. Cada día en España. Te explicamos los mejores ofertas en España, España, Reino Unido, México, Chile, Chile y América Latina, donde te mostramos la lista de las ofertas más alta de esta semana. Te contamos las mejor ofertas de este año
            """
            
            resumen2 = """
            El ganador de la serie MasterChef, que se emite en Netflix, es el ganador de un concurso de acreedores de una empresa en EE.UU., que cuenta con más de 1.800.000 empleos en España y en todo el país sudamericano. Te mostramos las mejores ofertas de la última semana en España y el Banco Mundial de Desarrollo Humanos, según la estadística de ventas de este tipo de ofertas más altas del año pasado. Cada día en España, te explicamos las mejores ofertas en España, en España, Reino Unido, México, Chile, Chile y América Latina. Te mostramos la lista de las ofertas más altas de esta semana. Además, te contamos las mejor ofertas de este año.
            """
            
            resumen3 = """
            El ganador de la serie MasterChef en Netflix, que es el ganador de un concurso de acreedores de la empresa de EE.UU., tiene más de 1.800.000 empleos en España y en todo el país sudamericano. Te mostramos las mejores ofertas de la última semana en España y el Banco Mundial de Desarrollo Humanos, basado en la estadística de ventas de ofertas más altas del año pasado. Cada día en España, te explicamos las mejores ofertas en España, España, Reino Unido, México, Chile, Chile y América Latina. Aquí tienes la lista de las ofertas más altas de esta semana. También te contamos las mejores ofertas de este año.
            """
            resumenes = [resumen1, resumen2, resumen3]
            return random.choice(resumenes)

    elif enfoque == "summaryindex":
        if BOE == "BOE-A-2015-6119":  #1
            
            resumen1 = """
            Este documento oficial del gobierno español, emitido por el Ministerio de Industria, Energía y Turismo, autoriza a Enagás Transporte, S.A.U. a cerrar y desmantelar una estación de regulación de gas (ER) en Otero, Asturias, y sus instalaciones asociadas. La resolución especifica que la empresa debe obtener un Acta de Cierre de la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias dentro de los tres meses posteriores a la entrada en vigor de la resolución, cumpliendo así con todas las condiciones establecidas para el cierre y desmantelamiento.
            """
            
            resumen2 = """
            Este conjunto de texto parece ser un documento oficial del gobierno, específicamente una resolución emitida por el Ministerio de Industria, Energía y Turismo. La resolución autoriza a Enagás Transporte SAU a cerrar y desmantelar una estación de regulación de gas (ER) ubicada en Otero, Asturias. El cierre está sujeto a ciertas condiciones, incluyendo la presentación de un plan para el cierre y desmantelamiento de la estación, la eliminación de materiales peligrosos, y la notificación del destino final y la reutilización o reciclaje del equipo retirado.
            """
            
            resumen3 = """
            Este conjunto de texto parece ser un documento gubernamental, específicamente una resolución que autoriza el cierre y desmantelamiento de una estación de regulación (ER) en Otero, España. La ER es propiedad de Enagás Transporte, S.A.U., y la autorización se concede después de varios informes de distintas agencias y una revisión de las regulaciones pertinentes. La resolución detalla los términos de la autorización, incluyendo el plazo para la finalización, los procedimientos para la eliminación de materiales y cualquier ingreso o beneficio potencial derivado del cierre.
            """
            
            resumen4 = """
            Este conjunto de textos parece ser una resolución gubernamental que autoriza el cierre y desmantelamiento de una estación de regulación de energía en Otero, España. La resolución fue emitida por el Ministerio de Industria, Energía y Turismo el 22 de mayo de 2015, y publicada en el Boletín Oficial del Estado (BOE) el 2 de junio de 2015. La resolución detalla los términos y condiciones para el cierre y desmantelamiento de la estación, incluyendo los requisitos para obtener un Acta de Cierre de las autoridades competentes y la eliminación de materiales.
            """
            
            resumen5 = """
            Este conjunto de textos parece ser un documento formal del gobierno, específicamente una resolución emitida por el Ministerio de Industria, Energía y Turismo, que autoriza a Enagás Transporte SAU a cerrar y desmantelar una instalación conocida como la Estación de Regulación (ER) en Otero. La resolución detalla los términos y condiciones para el cierre y desmantelamiento, incluyendo el requisito de obtener un Acta de Cierre de la Dirección del Área de Industria y Energía de la Delegación del Gobierno en Asturias dentro de un plazo determinado.
            """
            
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2019-2031":  #2
            resumen1 = """
            Este resumen trata sobre una disputa relacionada con un decreto-ley emitido por el Gobierno de Aragón, que busca resolver problemas sociales vinculados a la vivienda y a la reestructuración del sector bancario. El decreto-ley incluye medidas como la suspensión de procedimientos de desalojo para personas vulnerables, la provisión de asistencia financiera y la asignación de viviendas vacías para asegurar que todos tengan acceso a condiciones de vida dignas.
            """
            
            resumen2 = """
            Este conjunto de textos parece ser un caso legal que involucra una queja constitucional contra ciertas disposiciones de un decreto-ley aprobado por la Comunidad Autónoma de Aragón. El demandante argumenta que estas disposiciones infringen varios artículos constitucionales, incluidos aquellos relacionados con los derechos de propiedad, el principio de reserva de ley y las competencias asignadas al Estado.
            """
            
            resumen3 = """
            Este conjunto de textos parece ser una serie de documentos legales relacionados con impugnaciones constitucionales en España. Los principales temas tratados incluyen disputas sobre la constitucionalidad de decretos-leyes aprobados por los gobiernos regionales, particularmente aquellos relacionados con cuestiones de vivienda y bienestar social. La colección también aborda preguntas sobre la competencia entre el gobierno central y las autoridades regionales, así como la aplicación de principios constitucionales como la proporcionalidad y la protección del derecho a una vivienda digna.
            """
            
            resumen4 = """
            Un resumen de este conjunto de textos parece ser un documento legal o una decisión judicial relacionada con un decreto-ley aprobado por el Gobierno de Aragón en España. El documento discute varios aspectos del decreto-ley, incluyendo su constitucionalidad y su cumplimiento con las leyes nacionales.
            """
            
            resumen5 = """
            Este conjunto de textos parece ser una serie de documentos legales que discuten la constitucionalidad de un decreto-ley aprobado por el Gobierno de Aragón en España. Los documentos analizan varios aspectos del decreto-ley, incluyendo su compatibilidad con la Constitución Española y las leyes existentes, así como impugnaciones a su constitucionalidad en relación con los derechos de propiedad, la política de vivienda, las medidas de bienestar social y la autonomía regional.
            """
            
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)
            

        elif BOE == "BOE-A-2021-10584": #3
            resumen1 = """
            Esta colección de textos es un conjunto integral de documentos oficiales relacionados con la política energética, la fiscalidad y las medidas económicas en España. Los textos tratan temas como:

            -   Medidas para enfrentar el aumento de los precios de la electricidad.

            -   Promoción de fuentes de energía renovable.
            
            -   Reducción de impuestos sobre la electricidad.
            
            -   Apoyo a consumidores vulnerables.
            
            -   Mitigación del impacto económico de la pandemia de COVID-19.
            """
            
            resumen2 = """
            Este conjunto de textos parece ser una publicación gubernamental que describe medidas para abordar el aumento de los precios de la electricidad en España. Discute la situación actual, incluyendo el impacto de la pandemia de COVID-19, y propone soluciones como la reducción de las tasas del Impuesto sobre el Valor Añadido (IVA) y la minimización del "dividendo de CO2" recibido por las plantas de energía no emisoras más antiguas. El texto también toca otros temas, incluyendo la pobreza y vulnerabilidad entre los consumidores, las energías renovables y el desarrollo económico en España.
            """
            
            resumen3 = """
            La situación en España, donde el precio de la electricidad ha aumentado significativamente, especialmente desde diciembre de 2020, debido a diversos factores como el aumento de los costos del gas y las emisiones de CO2. Este aumento ha dado lugar a un incremento sustancial en los precios de la electricidad, afectando a los hogares, especialmente a aquellos con menores ingresos. El gobierno ha propuesto medidas para reducir el impacto de estos costos incrementados en los consumidores, incluyendo una reducción temporal en la tasa del impuesto sobre el valor añadido (IVA) aplicable a ciertos suministros de energía.
            """
            
            resumen4 = """
            Este conjunto de textos parece ser una recopilación de varios decretos, leyes y regulaciones relacionadas con la energía, la economía y las finanzas en España. Los temas principales discutidos incluyen medidas destinadas a abordar el impacto del aumento de los precios de la electricidad en los consumidores, promover fuentes de energía renovable y apoyar los objetivos del gobierno de reducir las emisiones de carbono.
            """
            
            resumen5 = """
            Este conjunto de textos parece ser una recopilación de diversas leyes, decretos y regulaciones emitidos por el gobierno español. Los temas principales discutidos incluyen medidas para abordar el aumento de los precios de la electricidad, promover fuentes de energía renovable, apoyar a las empresas afectadas por la pandemia de COVID-19 y regular el sector energético.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-11043": #4
            resumen1 = """
            Corrección de errores en un Real Decreto-ley sobre medidas urgentes en materia tributaria y de generación de energía.
            """
            
            resumen2 = """
            Se ha realizado una corrección a un decreto-ley anterior. El error estaba en un artículo referente a los contratos de suministro de electricidad, donde se especificaba "inferior a 10 kW" en lugar de "inferior o igual a 10 kW"
            """
            
            resumen3 = """
            Se ha realizado una corrección a un real decreto-ley sobre fiscalidad energética y generación de energía. El cambio afecta a un artículo en el documento original que trataba sobre contratos de suministro de energía eléctrica.
            """
            
            resumen4 = """
            Se está realizando una corrección a un decreto existente debido a un error. La corrección implica cambiar una frase específica en el Artículo 1, Punto a) en la página 76283 para que sea más precisa.
            """
            
            resumen5 = """
            Se ha realizado una corrección a un Real Decreto-ley sobre medidas en fiscalidad y generación de energía. La corrección afecta a un artículo que establece la potencia mínima contratada para los contratos de suministro de electricidad.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-12603": #5
            resumen1 = """
            Esta resolución confirma la convalidación de un decreto-ley por el Congreso de los Diputados, que incluye medidas sobre la fiscalidad energética, la generación de energía y la gestión del agua. Además, ordena su publicación para conocimiento público.
            """
            
            resumen2 = """
            Esta resolución confirma la validación de un real decreto-ley por parte del Congreso de los Diputados el 21 de julio de 2021. El decreto-ley introdujo medidas relacionadas con la fiscalidad energética, la generación de energía y la regulación del uso del agua, con el objetivo de hacer públicas estas modificaciones.
            """
            
            resumen3 = """
            El Real Decreto-ley 12/2021 fue convalidado por el Congreso de los Diputados el 21 de julio de 2021. El decreto-ley adopta medidas en el ámbito de la fiscalidad energética y la generación de energía, así como en la gestión de tasas de regulación y tarifas de uso del agua.
            """
            
            resumen4 = """
            Se acordó una resolución por parte del Congreso de los Diputados el 21 de julio de 2021, respecto a la validación de un Real Decreto-ley y su publicación en el Boletín Oficial del Estado. La resolución concierne medidas urgentes relacionadas con la fiscalidad energética, la generación de energía y la gestión del agua.
            """
            
            resumen5 = """
            Se aprobó una resolución por parte del Congreso de los Diputados el 21 de julio de 2021, para validar un Real Decreto-ley que adoptó medidas urgentes en las áreas de fiscalidad energética y generación de energía, así como en la regulación y uso del agua. La resolución también ordenó la publicación de esta decisión para el conocimiento general.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)
            
        elif BOE == "BOE-A-2021-16956": #6
            resumen1 = """
            El 17 de septiembre de 2021, la Secretaría General de Coordinación Territorial publicó una resolución sobre un acuerdo entre el Gobierno de España y la Comunidad Autónoma de Canarias. Este acuerdo busca resolver discrepancias relacionadas con un decreto-ley sobre fiscalidad energética, generación de energía y gestión del agua. La resolución especifica los términos del acuerdo, que incluyen negociaciones con el Tribunal Constitucional, la publicación en el Boletín Oficial del Estado y el Boletín Oficial de Canarias, y la notificación a las Cortes Generales y al Parlamento de Canarias.
            """
            
            resumen2 = """
            Se publicó una resolución por parte de la Secretaría General de Coordinación Territorial el 17 de septiembre de 2021, relativa a un acuerdo entre la Administración General del Estado y la Comunidad Autónoma de Canarias. El acuerdo tiene como objetivo resolver discrepancias relacionadas con un real decreto-ley que introdujo medidas urgentes en los campos de la fiscalidad energética, la generación de energía y la gestión del agua. La resolución incluye los términos del acuerdo y las acciones a llevar a cabo, como negociar con las partes relevantes, establecer un grupo de trabajo, comunicar el resultado a diversas instituciones y publicarlo en los diarios oficiales.
            """
            
            resumen3 = """
            Una resolución publicada en el Boletín Oficial del Estado (BOE) por la Secretaría General de Coordinación Territorial el 17 de septiembre de 2021. La resolución publica un acuerdo entre la Administración General del Estado y la Comunidad Autónoma de Canarias respecto a las medidas urgentes adoptadas en el ámbito de la fiscalidad y generación de energía, así como la gestión de tasas de regulación y tarifas de uso del agua.
            """
            
            resumen4 = """
            Una resolución de la Secretaría General de Coordinación Territorial del 17 de septiembre de 2021 publica un acuerdo entre la Administración General del Estado y la Comunidad Autónoma de Canarias respecto a medidas urgentes en el campo de la fiscalidad energética y la generación de energía. El acuerdo tiene como objetivo resolver discrepancias y propone una solución para la Comisión Bilateral de Cooperación. También requiere comunicación con el Tribunal Constitucional, las Cortes Generales y el Parlamento de Canarias.
            """
            
            resumen5 = """
            Se ha publicado una resolución por parte de la Secretaría General de Coordinación Territorial sobre un acuerdo entre la Administración General del Estado y la Comunidad Autónoma de Canarias. El acuerdo tiene como objetivo resolver discrepancias en relación con un real decreto-ley que introdujo medidas urgentes en la fiscalidad energética, la generación de energía y la gestión del uso del agua.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-21214":  #7
            resumen1 = """
            Una decisión del Tribunal Constitucional sobre una ley que establece medidas urgentes en la fiscalidad y generación de energía, así como en la regulación del agua.
            """
            
            resumen2 = """
            Se ha tomado una decisión por parte del Tribunal Constitucional para revisar la constitucionalidad de una disposición específica en un Real Decreto-ley. La disposición en cuestión es parte de un decreto que aborda medidas urgentes en los campos de la fiscalidad energética y la generación de energía, así como la regulación y utilización del agua. La decisión se tomó después de que se presentara una petición del Parlamento de Canarias contra esta disposición.
            """
            
            resumen3 = """
            Una sentencia del Tribunal Constitucional ha sido aceptada respecto a una disposición en un decreto-ley que introdujo medidas urgentes en los campos de la fiscalidad energética y la generación de energía.
            """
            
            resumen4 = """
            Se ha admitido una decisión del Tribunal Constitucional para proceder con un recurso de inconstitucionalidad contra una disposición en un real decreto-ley. El recurso fue interpuesto por el Parlamento de Canarias y concierne a medidas para la fiscalidad energética, la generación de energía y la gestión del uso del agua.
            """
            
            resumen5 = """
            Una decisión del Tribunal Constitucional respecto a una impugnación de una disposición en un real decreto-ley relacionado con la fiscalidad energética y la gestión del agua.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-12754":  #8
            resumen1  = """
            Esta colección de textos es una recopilación de documentos legales y procedimientos judiciales relacionados con una controversia sobre la aplicación de leyes que rigen las zonas costeras en España. El problema específico se centra en la interpretación de ciertos artículos y disposiciones de la Ley 7/2021, que han sido impugnados por la Xunta de Galicia.
            """
            
            resumen2 = """
            Esta colección de textos parece ser un documento legal relacionado con la constitucionalidad de ciertas disposiciones en la Ley 7/2021, una ley sobre cambio climático y transición energética. Los puntos principales discutidos son el principio de seguridad jurídica, el concepto de dominio público marítimo-terrestre, y el impacto de la Ley 7/2021 en las concesiones y permisos existentes relacionados con este dominio
            """
            
            resumen3 = """
            Esta colección de textos parece ser un documento legal, específicamente una decisión del Tribunal Constitucional español respecto a la constitucionalidad de ciertas disposiciones en la Ley 7/2021 sobre cambio climático y transición energética. El documento aborda diversos aspectos de la ley, incluyendo su impacto en el principio de certeza jurídica y la reserva de ley en asuntos relacionados con el dominio público.
            """
            resumen4 = """
            Esta colección de textos parece ser un documento legal relacionado con un caso constitucional en España. Involucra una impugnación a ciertas disposiciones de una ley sobre cambio climático y transición energética. El principal problema en cuestión es el principio de certeza jurídica y la reserva de poder legislativo en asuntos relacionados con la propiedad del dominio público.
            """
            
            resumen5 = """
            Una colección de textos parece ser un documento legal que discute una disputa en torno a la Ley 7/2021, ley relacionada con el cambio climático y la transición energética en España. Los principales puntos de controversia giran en torno a la duración de las concesiones para áreas de dominio público marítimo-terrestre, la posible retroactividad de ciertas disposiciones, la aplicabilidad de nuevas regulaciones y la interpretación de leyes existentes.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-2707":  #9
            resumen1  = """
            Este decreto-ley introduce modificaciones en varios artículos del Código Civil de Cataluña en materia de propiedad y gestión de bienes. Su objetivo es facilitar acuerdos para proyectos de eficiencia energética, promover el desarrollo sostenible y asegurar el buen funcionamiento de la comunidad.
            """
            
            resumen2 = """
            Una serie de decretos-leyes emitidos por el Gobierno de Cataluña tienen como objetivo modificar ciertos artículos del Código Civil Catalán en relación con la propiedad y la convivencia comunitaria. Los decretos se centran principalmente en promover fuentes de energía renovable, particularmente la energía solar, en viviendas de varias familias, mientras que también abordan la necesidad de tomar medidas urgentes durante la pandemia de COVID-19.
            """
            
            resumen3 = """
            Esta colección de textos parece ser un decreto oficial emitido por el Gobierno de Cataluña que modifica varios artículos del Código Civil de Cataluña. El decreto tiene como objetivo promover la eficiencia energética, la sostenibilidad y la accesibilidad en las propiedades, particularmente para los regímenes de propiedad comunitaria. Introduce nuevas disposiciones para los procesos de toma de decisiones, establece reglas para la instalación y mantenimiento de elementos comunes, y establece procedimientos para reparaciones y mejoras.
            """
            
            resumen4 = """
            Este decreto-ley modifica las regulaciones existentes para promover las energías renovables y la eficiencia energética en Cataluña. Tiene como objetivo mejorar la sostenibilidad y la eficiencia energética en los edificios residenciales sujetos a regímenes de propiedad horizontal mediante la instalación de sistemas de energía renovable y equipos de alta eficiencia energética. El decreto-ley establece reglas específicas para la ejecución de obras, la generación compartida de energía renovable, y la conservación y mantenimiento de las instalaciones.
            """
            
            resumen5 = """"
            Esta colección de textos parece ser modificaciones al Código Civil Catalán, específicamente al Libro Quinto, destinadas a promover la eficiencia energética y las energías renovables en edificios sujetos al régimen de propiedad horizontal. Los decretos buscan facilitar la instalación de paneles solares en techos, proporcionar continuidad en la regulación de entidades privadas, y abordar el impacto de la pandemia de COVID-19.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-2982":  #10
            resumen1 = """
            Este documento corrige errores en un decreto-ley que modifica el Código Civil de Cataluña. Las correcciones se centran en problemas con el título y la exposición de motivos, en particular en lo que respecta a la instalación de sistemas de energía eficiente o renovable en edificios sometidos al régimen de propiedad horizontal.
            """
            
            resumen2 = """
            Este documento es una corrección de errores en un decreto-ley sobre la modificación del Libro Quinto del Código Civil de Cataluña. Las correcciones tienen como objetivo incorporar regulaciones para la eficiencia energética y del agua, así como sistemas de energías renovables, en edificios sujetos al régimen de propiedad horizontal. Además, modifica otro decreto-ley para abordar el impacto de la COVID-19 en las entidades privadas bajo la legislación civil catalana.
            """
            
            resumen3 = """
            Esta colección de textos parece ser un aviso de corrección para un decreto-ley (Decreto-Ley) publicado en el Diario Oficial de Cataluña (Diari Oficial de la Generalitat de Catalunya). El aviso corrige errores en el decreto-ley original, específicamente dos instancias donde se reemplaza "sujetos" en singular por "sujetas" en plural, y también actualiza una sección sobre el alcance de la reforma.
            """
            
            resumen4 = """
            Corrección de errores en el Decreto-ley 28/2021, que modifica el Libro Quinto del Código Civil de Cataluña y el Decreto-ley 10/2020, para incorporar regulaciones sobre eficiencia energética o hídrica y sistemas de energías renovables en edificios sujetos al régimen de propiedad horizontal.
            """
            
            resumen5 = """
            Este documento corrige errores en el Decreto-ley 28/2021, que modifica el Código Civil de Cataluña en relación con la eficiencia energética y los sistemas de energías renovables en edificios sujetos a las regulaciones de propiedad horizontal. La corrección incluye cambios en el título y en la exposición de motivos en el texto original.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2023-26461": #11
            resumen1 = """
            Esta colección de textos constituye un conjunto de regulaciones, modificaciones y directrices relacionadas con ayudas financieras, subvenciones y programas diseñados para fomentar la eficiencia energética, las energías renovables y el desarrollo sostenible en España. Los documentos tratan sobre las reformas a programas vigentes, la simplificación de procedimientos, la introducción de nuevos principios, y establecen requisitos para garantizar la transparencia y la rendición de cuentas.
            """
            
            resumen2 = """
            Esta colección de textos parece ser modificaciones a las regulaciones gubernamentales relacionadas con políticas ambientales y energías renovables en España. Los documentos detallan procedimientos para implementar diversos programas, proporcionar asistencia financiera y gestionar fondos. También abordan los requisitos para la presentación de informes, auditorías y contabilidad, así como modificaciones a las regulaciones existentes y plazos para la presentación de solicitudes.
            """
            
            resumen3 = """
            Esta colección de textos parece ser una recopilación de documentos oficiales del gobierno relacionados con la recuperación económica, la transformación y la resiliencia en España. Los principales temas tratados incluyen la modificación de regulaciones para programas de ayuda destinados a promover las energías renovables y reducir la dependencia de los combustibles fósiles, la extensión del período de validez de ciertos programas hasta el 31 de julio de 2024, la simplificación de procesos administrativos y la adaptación de las regulaciones para cumplir con las directrices de la Unión Europea.
            """
            
            resumen4 = """
            Un decreto o regulación gubernamental destinado a promover las energías renovables y reducir la dependencia de los combustibles fósiles, proporcionando un marco para la implementación de programas relacionados y especificando roles y responsabilidades.
            """
            
            resumen5 = """
            Esta colección de textos parece ser una recopilación de documentos oficiales y regulaciones relacionadas con las políticas y programas gubernamentales destinados a promover la energía renovable, reducir la dependencia de los combustibles fósiles y aumentar la eficiencia energética. Los principales temas cubiertos incluyen modificaciones a las regulaciones existentes, cambios en el tratamiento del almacenamiento detrás del medidor, provisión de seguridad y certeza para los participantes en el programa, y establecimiento de reglas y procedimientos claros.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2023-9215":  #12
            resumen1 = """
            Esta colección de textos parece ser una recopilación de documentos oficiales y decisiones judiciales relacionadas con las políticas fiscales y regulaciones en España. Los textos discuten las medidas tomadas por el gobierno para abordar la crisis económica causada por la COVID-19, específicamente en las Islas Canarias. Los documentos detallan los cambios en las leyes y regulaciones fiscales destinados a mantener la competitividad de la región y apoyar a la industria cinematográfica.
            """
            
            resumen2 = """
            Esta colección de textos parece ser una recopilación de documentos legales y análisis relacionados con los desafíos constitucionales a los reales decretos-leyes sobre la modificación del régimen fiscal en las Islas Canarias. Los textos abordan varias cuestiones constitucionales, incluyendo el principio de estabilidad constitucional, la aprobación previa del Parlamento de Canarias, y la justificación para usar reales decretos-leyes en lugar de leyes ordinarias. Los temas principales incluyen la constitucionalidad del Real Decreto-Ley 12/2021, su relación con el régimen fiscal en las Islas Canarias y el compromiso del gobierno de apoyar a la región mediante medidas económicas.
            """
            
            resumen3 = """
            Esta colección de textos parece estar relacionada con un caso del tribunal constitucional en España sobre la modificación del régimen económico y fiscal de las Islas Canarias. La principal cuestión es si se cumplió con el informe previo requerido del Parlamento de Canarias antes de que la modificación entrara en vigor. El texto discute varias disposiciones constitucionales, incluyendo la disposición adicional tercera de la Constitución Española, que exige un informe previo del Parlamento de Canarias antes de cualquier modificación al régimen económico y fiscal de las Islas Canarias.
            """
            
            resumen4 = """
            Esta colección de textos parece ser una decisión judicial, específicamente una sentencia emitida por el Tribunal Constitucional en España sobre la constitucionalidad del Real Decreto-ley 12/2021. La ley introdujo medidas para abordar problemas relacionados con la energía y el agua, pero su disposición final tercera fue impugnada por el Parlamento de Canarias. Los puntos principales de contención se refieren a la supuesta violación de la garantía institucional del régimen económico y fiscal de Canarias, la falta de consulta previa con el Parlamento de Canarias y la falta de conexión entre el contenido de la reforma y la situación de urgencia que supuestamente la justificaba.
            """
            
            resumen5 = """
            Esta colección de textos parece estar relacionada con un caso del tribunal constitucional en España sobre la constitucionalidad de ciertas disposiciones en un Real Decreto-Ley y su impacto en el régimen económico y fiscal de las Islas Canarias. El Real Decreto-Ley modifica la Ley 19/1994, que regula el sistema económico y fiscal de las Islas Canarias, sin consulta previa con el Parlamento de Canarias.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

        elif BOE == "BOE-B-2018-54744": #13
            resumen1 = """
            Aviso público sobre un contrato mixto (de obra y suministro) celebrado entre el Ayuntamiento de Marina de Cudeyo e Imesapi, S.A. para llevar a cabo la rehabilitación, reforma y mejora de la eficiencia energética de la iluminación pública municipal. El presupuesto asignado para este proyecto es de 1.101.860,18 euros.
            """
            
            resumen2 = """
            Este documento formaliza el contrato para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. El contrato fue adjudicado a Imesapi, S.A. con un valor neto de 841.602,63 € y un valor total de 1.018.339,18 €
            """
            
            resumen3 = """
            El Ayuntamiento de Marina de Cudeyo ha formalizado un contrato mixto (obra y suministro) para la rehabilitación, reforma y mejora de la eficiencia energética de su alumbrado público municipal. El contrato fue adjudicado a Imesapi, S.A. con un valor neto de 841.602,63 € y un valor total de 1.018.339,18 €.
            """
            
            resumen4 = """
            El Ayuntamiento de Marina de Cudeyo formalizó un contrato mixto (obra y suministro) para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público municipal. El contratista es Imesapi, S.A. y el presupuesto base de licitación es de 1.101.860 euros.
            """
            
            resumen5 = """
            Este anuncio formaliza un contrato mixto (obra y suministro) sujeto a regulación armonizada para la rehabilitación, reforma y mejora de la eficiencia energética del alumbrado público en Marina de Cudeyo. El contrato fue adjudicado a Imesapi, S.A. con un valor neto de 841.602,63 € y un valor total de 1.018.339,18 €.
            """
            
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)
            

        elif BOE == "BOE-B-2019-52073":  #14
            resumen1 = """
            Este documento es un anuncio oficial del Boletín Oficial del Estado (BOE) que detalla el proceso de adjudicación para un proyecto destinado a mejorar la eficiencia energética y adaptar los sistemas de aire acondicionado a las normativas anti-legionella en el centro penitenciario Evaristo Martín Nieto, ubicado en Málaga. El contrato ha sido concedido a VIVENDIO SOSTENIBILIDAD ENERGÉTICA, S.L., una PYME, con un valor cercano a los 93.000 euros.
            """
            
            resumen2 = """
            Este documento es un anuncio oficial del Boletín Oficial del Estado (BOE) del gobierno español respecto a un proceso de contratación pública. El contrato específico es para la mejora de la eficiencia energética y la adaptación de los sistemas de aire acondicionado a los requisitos normativos contra la legionella en el Centro Penitenciario Evaristo Martín Nieto en Málaga, España. El anuncio proporciona detalles sobre la entidad contratante, el proceso de licitación, el adjudicatario ganador y los aspectos financieros del contrato.
            """
            
            resumen3 = """
            Este documento es un anuncio para un proceso de contratación pública por parte de la Subdirección General de Servicios Penitenciarios dentro del Ministerio del Interior. El proyecto implica la actualización de la eficiencia energética y la adaptación del sistema de aire acondicionado en el C.I.S. Evaristo Martín Nieto en Málaga para cumplir con la normativa sobre legionella.
            """
            
            resumen4 = """
            Este documento es un anuncio oficial de la Subdirección General de Servicios Penitenciarios del Ministerio del Interior sobre la formalización de contratos para un proyecto de mejora de la eficiencia energética y adaptación del sistema de aire acondicionado en el C.I.S. Evaristo Martín Nieto en Málaga, España. El contrato fue adjudicado a Vivendio Sostenibilidad Energética, S.L. con un valor de 93.158,91 euros.
            """
            
            resumen5 = """
            Este documento es un anuncio oficial de la Subdirección General de Servicios Penitenciarios del Ministerio del Interior respecto a la formalización de contratos para la mejora de la eficiencia energética y adaptación a la normativa anti-legionella en el centro penitenciario Evaristo Martín Nieto en Málaga.
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4, resumen5]
            return random.choice(resumenes)

    elif enfoque == "documentsummaryindex":
        if BOE == "BOE-A-2015-6119":
            resumen1 = """
                El texto proporcionado parece ser una publicación gubernamental, específicamente una resolución emitida por la Dirección General de Política Energética y Minas de España.

                Esta resolución autoriza el cierre y desmantelamiento de una antigua estación de regulación de gas ubicada en Otero, Asturias. La estación pertenece a Enagás Transporte, S.A.U., una empresa dedicada al transporte y suministro de gas natural a diversas industrias.
                El documento detalla las condiciones para el cierre de la estación, incluyendo la obtención de un acta de cierre por parte de la Delegación del Gobierno en Asturias, el desmantelamiento de la estación en un plazo de tres meses y la garantía de que cualquier material reutilizable se emplee en otras instalaciones relacionadas con el gas.
                
                Este texto puede responder a preguntas como:
                
                •	¿Cuál es el propósito de esta resolución?
                
                •	¿Quién es el propietario de la estación de regulación de gas que se cierra?
                
                •	¿Cuáles son las condiciones para el cierre de la estación?
               
                •	¿Qué sucede con los materiales desmantelados de la estación?
                
                •	¿Puede alguien impugnar esta resolución?
            """
            
            resumen2 = """
                El texto proporcionado parece ser un documento oficial del gobierno, específicamente una resolución o decreto emitido por el Ministerio de Industria, Energía y Turismo de España. El documento autoriza a Enagás Transporte, S.A.U. a cerrar y desmantelar una estación de regulación (ER) en Otero, Asturias.

                Este texto puede responder a preguntas tales como:

                • ¿Cuál es el propósito del documento?
                
                • ¿Quién es el destinatario de la autorización?
                
                • ¿Cuáles son las condiciones para cerrar y desmantelar la estación ER?
                
                • ¿Cuánto tiempo tiene Enagás Transporte, S.A.U. para completar el proceso de cierre y desmantelamiento?
                
                • ¿Qué sucede con los materiales resultantes del cierre y desmantelamiento?
                
                En general, este texto proporciona información sobre una decisión administrativa específica relacionada con la operación de una instalación vinculada a la energía en España.
                """
                
            resumen3 = """
                El texto proporcionado parece ser un documento oficial del gobierno español, específicamente una resolución del Ministerio de Industria, Energía y Turismo sobre el cierre y desmantelamiento de una estación de regulación de gas.

                Este texto puede responder a varias preguntas relacionadas con el tema, como:

                •   ¿Cuál es el propósito de la resolución?
                
                •   ¿Qué empresa está autorizada para cerrar y desmantelar la estación de regulación de gas?
                
                •   ¿Cuáles son las condiciones para el proceso de cierre y desmantelamiento?
                
                •   ¿Cuáles son las responsabilidades de la empresa involucrada en el proceso?
                
                •   ¿Cuál es el plazo para completar el cierre y desmantelamiento?

                Además, este texto también puede proporcionar información sobre el marco legal que regula el proceso de autorización, el papel de las diferentes agencias gubernamentales y los procedimientos para la supervisión del cumplimiento de la resolución.
                """
                
            resumen4 = """
                Resumen generado para el documento BOE-A-2015-6119.pdf: Basado en el texto proporcionado, parece ser un documento oficial del gobierno, específicamente una resolución del Ministerio de Industria, Energía y Turismo respecto al cierre y desmantelamiento de una estación de regulación de gas.

                Este texto puede responder preguntas como:

                * ¿Cuál es el propósito de la resolución?
                
                * ¿Quiénes son los afectados por esta resolución?
                
                * ¿Cuáles son las condiciones para el cierre y desmantelamiento de la estación de regulación de gas?
                
                * ¿Cómo debe proceder la empresa "Enagás Transporte, S.A.U." con el proceso de cierre y desmantelamiento?
                
                * ¿Cuáles son las consecuencias si la empresa no cumple con las condiciones establecidas en la resolución?

                En general, este texto proporciona información sobre una decisión gubernamental específica respecto al cierre de una estación de regulación de gas, y puede ser utilizado para responder preguntas relacionadas con los detalles de dicha decisión.
                                """
                
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2019-2031":
            resumen1 = """
                El documento proporcionado parece ser un informe formal, posiblemente una decisión judicial o un reporte gubernamental, que examina una impugnación constitucional contra ciertas leyes y regulaciones relativas a la vivienda y los derechos de propiedad en España.

                Este texto puede responder a diversas preguntas sobre el marco legal que rige la vivienda y los derechos de propiedad en España, tales como:

                •	¿Cuáles son las disposiciones clave de las leyes y regulaciones impugnadas?

                •	¿Cómo interactúan estas leyes con la legislación nacional y la Constitución española?

                •	¿Qué implicaciones tienen estas leyes para los derechos de propiedad individuales y la función social de la propiedad?

                •	¿Pueden estas leyes interpretarse como una violación a las competencias estatales o regionales?

                •	¿Cómo se relaciona este caso con decisiones judiciales previas y principios constitucionales?

                De manera más amplia, este texto también puede ofrecer perspectivas sobre los debates legales y de políticas públicas en torno a la vivienda, los derechos de propiedad y el bienestar social en España.
            """
            
            resumen2 = """
                Basado en el contexto proporcionado, parece que el texto es un documento legal relacionado con una decisión del Tribunal Constitucional en España. Específicamente, parece ser una transcripción o un resumen de un fallo del Tribunal Constitucional respecto a la constitucionalidad de ciertas disposiciones en un decreto-ley aprobado por el Gobierno de Aragón.

                Este texto puede responder a preguntas tales como:

                •   ¿Cuáles son las disposiciones clave del decreto-ley que fueron impugnadas ante el Tribunal Constitucional?
                
                •   ¿Cómo falló el tribunal sobre la constitucionalidad de estas disposiciones?
                
                •   ¿Se declararon inconstitucionales algunos artículos o secciones específicos, y si es así, por qué?
                
                •   ¿Tuvo la decisión del tribunal implicaciones para el equilibrio de poder entre el gobierno nacional y la comunidad autónoma de Aragón?
                
                •   ¿Cuáles son los principios constitucionales más amplios en juego en este caso?
                
                En general, es probable que el texto sea de interés para académicos y practicantes del derecho constitucional español, así como para cualquiera que busque información sobre la relación entre el gobierno central y las comunidades autónomas en España.
            """
            
            resumen3 = """
            Basado en el contexto proporcionado, describiría el texto como un documento oficial del gobierno español, específicamente una sentencia del Tribunal Constitucional sobre la constitucionalidad de ciertas disposiciones en un decreto-ley de una Comunidad Autónoma (Aragón). El documento detalla el contexto y los argumentos presentados por las partes involucradas, incluyendo al Gobierno de España y a la Comunidad Autónoma de Aragón.

            Este texto puede responder a preguntas relacionadas con:

            
            1. El marco legal que regula los derechos de propiedad y los procedimientos de ejecución hipotecaria en España.
            
            2. Los límites constitucionales a las competencias de las Comunidades Autónomas (Aragón) respecto a la regulación de asuntos de propiedad e hipotecarios.
            
            3. Las disposiciones específicas del decreto-ley que fueron impugnadas como inconstitucionales por el Gobierno de España.
            
            4. La argumentación detrás de la decisión del Tribunal Constitucional de mantener o anular ciertas disposiciones del decreto-ley.

            Algunas posibles preguntas que este texto puede responder incluyen:

            •   ¿Cuáles son los límites constitucionales a las competencias de las Comunidades Autónomas (Aragón) en relación con los derechos de propiedad y los procedimientos de ejecución hipotecaria?
            
            •   ¿Puede un decreto-ley de una Comunidad Autónoma (Aragón) anular leyes federales que regulan asuntos de propiedad e hipotecarios?
            
            •   ¿Cómo interpreta el Tribunal Constitucional el concepto de "efectos lesivos" sobre el ejercicio de las competencias constitucionales en este caso?
            
            •   ¿Cuáles son las implicaciones de esta decisión para futuras iniciativas legislativas de las Comunidades Autónomas (Aragón) en relación con los derechos de propiedad y los procedimientos de ejecución hipotecaria?
                        """
            
            resumen4 = """
                El texto proporcionado parece ser un documento legal, específicamente una sentencia del Tribunal Constitucional en España. Trata sobre la constitucionalidad de ciertos artículos y disposiciones dentro del Decreto-ley del Gobierno de Aragón 3/2015, una ley-decreto aprobada por el gobierno regional de Aragón.

                Este texto puede responder preguntas relacionadas con:

                * La constitucionalidad de leyes o regulaciones específicas
                
                * La distribución de poderes entre el gobierno central y las autoridades regionales en España
                
                * El alcance de las competencias estatales, particularmente en lo referente a la legislación sobre derechos de propiedad y procedimientos de ejecución
                
                * Las implicaciones de ciertas disposiciones legales sobre los derechos y libertades individuales

                Algunas posibles preguntas de seguimiento que podrían ser respondidas por este texto incluyen:

                * ¿Cuáles son las principales cuestiones constitucionales en juego en este caso?
                
                * ¿Cómo afecta la decisión del Tribunal Constitucional la relación entre el gobierno central y las autoridades regionales en España?
                
                * ¿Se pueden proporcionar ejemplos específicos para ilustrar cómo estas disposiciones legales afectan los derechos o libertades individuales?
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-10584":
            resumen1 = """
                El texto proporcionado parece ser un extracto de un decreto o reglamento gubernamental en España relativo al sector energético. Específicamente, aborda el aumento de los precios de la electricidad y las medidas que se están implementando para abordar esta problemática.
                
                Este texto puede responder a diversas preguntas relacionadas con el tema, tales como:
                
                •	¿Cuáles son las tendencias actuales de los precios de la electricidad en España?
                
                •	¿Cómo afectan estos aumentos de precios a los consumidores y las empresas?
            
                •	¿Qué medidas está adoptando el gobierno para reducir los costos de la electricidad para ciertos grupos, como los hogares vulnerables?
                
                •	¿Se están proponiendo cambios en el sistema de impuestos (IVA) relacionados con el consumo de electricidad?
            
                •	¿Cuál es el impacto de las fuentes de energía renovable en el panorama energético general de España?
            
                En un sentido más amplio, este texto puede ser utilizado para analizar la respuesta del gobierno a los desafíos económicos y ambientales en el sector energético, así como sus esfuerzos para promover el desarrollo sostenible y reducir las emisiones de carbono.
            """
            
            resumen2 = """
                El texto proporcionado parece ser un documento oficial del gobierno de España, específicamente un Real Decreto-ley fechado el 24 de junio de 2021. El texto describe un conjunto de medidas destinadas a abordar los altos precios de la electricidad en España, que se han visto exacerbados por la pandemia de COVID-19 y otros factores.

                El texto discute varios aspectos del problema, incluyendo el impacto en los hogares, el papel de los impuestos y subsidios, y la necesidad de promover el uso de fuentes de energía renovable. También describe una serie de medidas destinadas a reducir el costo de la electricidad para los consumidores, como la reducción del tipo del impuesto sobre el valor añadido (IVA) aplicable a ciertos tipos de consumo de energía.

                Este texto puede responder a preguntas relacionadas con las causas y consecuencias de los altos precios de la electricidad en España, así como la respuesta del gobierno a este problema. Algunas preguntas específicas que este texto podría ayudar a responder incluyen:

                •   ¿Cuáles son los principales factores que impulsan el aumento de los precios de la electricidad en España?
                
                •   ¿Cómo afectarán las medidas propuestas a los hogares y las empresas?
                
                •   ¿Qué papel juegan los impuestos en la determinación del costo de la electricidad en España?
                
                •  ¿Cómo pueden las fuentes de energía renovable ayudar a reducir los costos de la electricidad?
                
                •  ¿Serán efectivas estas medidas para abordar el problema de los altos precios de la electricidad?
            """
            
            resumen3 = """
            El texto proporcionado parece ser una publicación gubernamental o un documento oficial sobre la política energética en España. Específicamente, discute los altos precios de la electricidad en el país y las medidas que se están tomando para abordar este problema.

            Algunos de los temas cubiertos en el texto incluyen:

            * Las causas de los altos precios de la electricidad, como el aumento de la demanda y los costos asociados con las emisiones de carbono.
           
            * Propuestas del gobierno para reducir los precios de la electricidad, como rebajas en los impuestos (IVA) para ciertos consumidores y empresas.
           
            * Cambios en el tipo impositivo del IVA aplicable a los suministros de energía.
           
            * Medidas destinadas a promover el uso de fuentes de energía renovable y reducir las emisiones de gases de efecto invernadero.

            Este texto puede responder a preguntas como:

            * ¿Cuáles son las principales causas de los altos precios de la electricidad en España?
           
            * ¿Cómo está respondiendo el gobierno español al problema de los altos precios de la electricidad?
           
            * ¿Qué medidas se están tomando para promover el uso de fuentes de energía renovable en España?
           
            * ¿Cómo afectarán los cambios en los impuestos del IVA a los consumidores y empresas de electricidad en España?

            En general, este texto parece ser un documento oficial que proporciona información sobre la política energética en España y puede ofrecer respuestas a preguntas relacionadas con este tema.
                        """
            
            resumen4 = """
                El texto proporcionado parece ser un documento gubernamental, específicamente un Real Decreto-ley de España, fechado en junio de 2021. El texto trata sobre el aumento de los precios de la electricidad en España y el impacto que esto tiene en los consumidores, particularmente en aquellos con menores ingresos. También describe las medidas que el gobierno está tomando para abordar este problema, incluyendo la reducción del tipo del Impuesto sobre el Valor Añadido (IVA) aplicable a ciertos contratos de suministro de energía.

                Algunas preguntas que este texto puede responder incluyen:

                * ¿Cuáles son los precios actuales de la electricidad en España?
                
                * ¿Cómo están afectando a los consumidores los aumentos de los precios de la electricidad, especialmente a aquellos con menores ingresos?
                
                * ¿Qué medidas está tomando el gobierno español para abordar estos aumentos de precios y aliviar la carga sobre los consumidores?
                
                * ¿Cómo afectará a los consumidores y las empresas la reducción del tipo del IVA aplicable a ciertos contratos de suministro de energía?
                
                * ¿Cuál es el impacto de estos aumentos de precios en la economía general y el medio ambiente?
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)
            

        elif BOE == "BOE-A-2021-11043":
            resumen1 = """
                El texto proporcionado parece ser una nota de corrección para un decreto oficial (Real Decreto-ley) relacionado con la fiscalidad y la generación de energía. Detalla un error en la publicación original y proporciona la redacción corregida.
                
                Este texto puede responder a preguntas como:

                •	¿Cuál es la redacción correcta respecto a los términos contractuales para el suministro de electricidad?

                •	¿Cuál fue el error original en el Real Decreto-ley 12/2021?

                •	¿Cómo afecta esta corrección a las políticas de fiscalidad y generación de energía?
            """
            
            resumen2 = """
                Este texto parece ser un documento oficial del gobierno, específicamente una corrección publicada en el Boletín Oficial del Estado (BOE). Corrige un error en un real decreto-ley anterior y proporciona el texto corregido.

                Algunas preguntas que este texto puede responder incluyen:

                •   ¿Cuál es la corrección que se está haciendo al real decreto-ley anterior?
               
                •   ¿Cómo cambia el texto original con la corrección?
               
                •   ¿Cuáles son las implicaciones de la corrección para las personas u organizaciones afectadas por la ley original?
            """
            
            resumen3 = """
                El texto proporcionado parece ser una publicación gubernamental, específicamente una nota de corrección para un real decreto-ley relacionado con la fiscalidad y generación de energía.

                Este texto puede responder a preguntas como:

                
                * ¿Cuál era el error original en el Real Decreto-ley 12/2021?
                
                * ¿Cómo afecta la versión corregida del Artículo 1 a los titulares de contratos de suministro eléctrico?
                
                * ¿Cuándo se publicó esta corrección y dónde puede verificarse?

                En general, este documento detalla la corrección de errores en la normativa original y proporciona información sobre cómo estas correcciones impactan a los sujetos afectados y cómo consultar la corrección oficial.
                            """
            
            resumen4 = """
                El texto proporcionado parece ser un documento oficial del gobierno, específicamente una nota de corrección publicada en el Boletín Oficial del Estado (BOE). El documento corrige errores en un Real Decreto-ley anterior relacionado con la política fiscal energética y la generación de electricidad.

                Este texto puede responder preguntas como:

                * ¿Qué correcciones se hicieron a un Real Decreto-ley específico?
                
                * ¿Qué cambios se implementaron en el artículo o disposición original?
                
                * ¿Cómo afectó la corrección al significado o intención original de la ley?
                
                * ¿Cuáles son las implicaciones de esta corrección en las políticas o regulaciones relacionadas?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-12603":
            resumen1 = """
                El documento proporcionado parece ser un anuncio formal sobre la convalidación de un real decreto-ley por parte del Congreso de los Diputados de España. En él se detallan los pormenores del proceso de convalidación y se ofrece información sobre la publicación del decreto-ley en el Boletín Oficial del Estado (BOE).
            
                Este texto puede responder a preguntas como:
                
                •	¿Qué fue convalidado por el Congreso de los Diputados de España?
            
                •	¿Cuándo se publicó el real decreto-ley en el Boletín Oficial del Estado?
                
                •	¿Quién es el presidente del Congreso de los Diputados mencionado en el documento?
                
                •	¿Cuáles son algunas de las medidas clave descritas en el real decreto-ley?
            
                •	¿Cómo se llevó a cabo el proceso de convalidación por el Congreso de los Diputados?

            """
            
            resumen2 = """
            El texto proporcionado parece ser un documento legislativo, específicamente una resolución aprobada por el Congreso de los Diputados el 21 de julio de 2021. El documento confirma la publicación de un Real Decreto-ley y discute su contenido.

            Algunas preguntas que este texto puede responder incluyen:

            •   ¿Cuál es el propósito del Real Decreto-ley 12/2021?
            
            •   ¿Cuáles son las medidas adoptadas por el decreto-ley en el ámbito de la política fiscal energética y la generación de energía?
            
            •   ¿Cuál es el papel del Congreso de los Diputados en la confirmación de la publicación de este documento?
            
            •   ¿Cuándo fue publicado el Real Decreto-ley en el Boletín Oficial del Estado?
            
            •   ¿Quién es responsable de publicar este documento?
            """
            
            resumen3 = """
                El texto proporcionado parece ser un anuncio público o una declaración oficial del Congreso de los Diputados de España sobre la convalidación de un Real Decreto-ley y su posterior publicación en el Boletín Oficial del Estado (BOE).

                Algunas preguntas que este texto puede responder incluyen:

                * ¿Cuál era el tema del Real Decreto-ley que fue convalidado?
                
                * ¿Cuándo se publicó el Real Decreto-ley y cuáles fueron sus principales disposiciones?
                
                * ¿Quién es responsable de ordenar la publicación del anuncio?
                
                * ¿Cuál es el propósito de publicar el anuncio en el Boletín Oficial del Estado?

                En general, el texto parece ser una notificación formal o un comunicado de prensa del gobierno español sobre una acción oficial tomada por el Congreso de los Diputados.
                            """
            
            resumen4 = """
                El texto proporcionado parece ser una resolución aprobada por el Congreso de los Diputados (la cámara baja del parlamento español) el 21 de julio de 2021, respecto a la convalidación de un real decreto-ley y medidas relacionadas en el sector energético.

                Este texto puede responder preguntas como:

                * ¿Cuál es el propósito del Real Decreto-ley 12/2021?
                
                * ¿Cuáles son las medidas urgentes tomadas por el gobierno en el sector energético?
                
                * ¿Quién convalidó el Real Decreto-ley y cuándo fue publicado?
                
                * ¿Cuál es el contexto detrás de la convalidación de este decreto-ley?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-16956":
            resumen1 = """
                El documento proporcionado parece ser una publicación gubernamental, específicamente una resolución y un anexo publicados en el Boletín Oficial del Estado (BOE). Trata sobre un acuerdo bilateral entre la Administración General del Estado y la Comunidad Autónoma de Canarias, referente a medidas urgentes para la fiscalidad y la generación de energía.
                
                Este texto puede responder a preguntas como:
            
                •	¿Cuál es el contenido del acuerdo entre el gobierno español y la Comunidad Autónoma de Canarias?
                
                •	¿Cuáles son los puntos clave del acuerdo, incluyendo su inicio, la designación de un grupo de trabajo, la comunicación con el Tribunal Constitucional y la notificación a las Cortes Generales y al Parlamento de Canarias?
            
                •	¿Cuál es el propósito de publicar esta resolución en el Boletín Oficial del Estado?

            """
            
            resumen2 = """
                El texto proporcionado parece ser una resolución o decreto emitido por el Ministerio de Política Territorial en España, específicamente en relación con la adopción de medidas relacionadas con la fiscalidad y la generación de energía. El texto detalla un acuerdo entre el Gobierno de España y la Comunidad Autónoma de Canarias.

                Este texto puede responder a preguntas tales como:

                •   ¿Cuál es el contenido del Acuerdo de la Comisión Bilateral de Cooperación Administración General del Estado-Comunidad Autónoma de Canarias?
                
                •   ¿Cuáles son las medidas adoptadas por el Ministerio de Política Territorial respecto a la fiscalidad y la generación de energía?
                
                •   ¿Cómo afecta este decreto a la Comunidad Autónoma de Canarias?
                
                •   ¿Cuál es el papel del Tribunal Constitucional en este decreto?
                
                En general, este texto puede proporcionar información sobre las políticas y acuerdos relacionados con la fiscalidad y la generación de energía entre el gobierno español y la comunidad autónoma de Canarias.
                            
            """
            
            resumen3 = """
                El texto proporcionado parece ser un documento gubernamental, específicamente una resolución publicada en el Boletín Oficial del Estado (BOE), el diario oficial del gobierno español. El texto aborda un acuerdo entre el Ministerio de Política Territorial y la Comunidad Autónoma de Canarias sobre la fiscalidad energética y el uso del agua.

                Este texto puede responder a preguntas como:

                
                * ¿Cuál es el propósito del acuerdo entre el Ministerio de Política Territorial y la Comunidad Autónoma de Canarias?
                
                * ¿Qué medidas se están tomando para abordar las discrepancias en la fiscalidad energética y el uso del agua?
                
                * ¿Quién es responsable de comunicar este acuerdo a diversas instituciones, incluyendo el Tribunal Constitucional, las Cortes Generales y el Parlamento de Canarias?
                
                * ¿Cómo se publicará y pondrá a disposición pública este acuerdo?

                En general, el texto proporciona información sobre el acuerdo y su procedimiento de publicación y comunicación a las instituciones relevantes.
            """
            
            resumen4 = """
                El texto proporcionado parece ser una resolución o decreto gubernamental relacionado con la política energética y fiscal en España, específicamente en lo que respecta a las Islas Canarias. Expone un acuerdo entre el gobierno central y la Comunidad Autónoma de Canarias sobre la adopción de medidas urgentes en las áreas de fiscalidad energética y gestión del agua.

                Este texto puede responder preguntas como:

                * ¿Cuál es el contenido del acuerdo alcanzado entre el gobierno central y la Comunidad Autónoma de Canarias?
                
                * ¿Cuáles son los puntos clave del Real Decreto-ley 12/2021 a los que se refiere este acuerdo?
                
                * ¿Quién ha adoptado este acuerdo y cuál es su papel en su implementación?
                
                * ¿Dónde se publicará este acuerdo y cómo se puede verificar?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2021-21214":
            resumen1 = """
                El documento proporcionado parece ser una publicación oficial del gobierno, específicamente una decisión del Tribunal Constitucional junto con la información de contexto relacionada.
            
                Este texto puede responder a preguntas como:
                
                •	¿Cuál fue el resultado de la demanda constitucional presentada contra una ley o regulación específica?
                
                •	¿Qué entidades estuvieron involucradas en la demanda (por ejemplo, qué partes llevaron el caso)?
            
                •	¿Cuál fue la fecha relevante de esta decisión?
            
                •	¿Se puede verificar esta publicación oficial del gobierno en línea?
            
                •	¿Cuál es el propósito y contenido del Real Decreto-ley 12/2021 que fue impugnado?

            """
            
            resumen2 = """
                El texto proporcionado parece ser un documento formal relacionado con la decisión de un tribunal constitucional sobre una ley o decreto específico. Menciona un recurso de inconstitucionalidad, lo que implica que el documento está discutiendo un desafío a la constitucionalidad de una ley en particular.

                Este texto puede responder a preguntas tales como:

                •   ¿Cuál fue el resultado del recurso de inconstitucionalidad presentado contra el Real Decreto-ley 12/2021?
                
                •   ¿Qué institución tomó la decisión respecto al desafío constitucional?
                
                •   ¿Cuáles fueron los motivos del desafío y qué aspecto específico de la ley se cuestionaba?
                
                •   ¿La disposición impugnada fue declarada inconstitucional o fue confirmada por el tribunal?

                El texto también parece proporcionar información sobre los aspectos procedimentales del caso, como la fecha en que el Pleno del Tribunal Constitucional acordó admitir el recurso de inconstitucionalidad y la identidad de la persona que firmó el documento.
                """
                
            resumen3 = """
                El texto proporcionado parece ser un documento oficial del gobierno, específicamente un boletín del Boletín Oficial del Estado (BOE) anunciando una decisión tomada por el Tribunal Constitucional de España.

                Este texto puede responder a preguntas como:

                * ¿Cuál fue la resolución sobre la constitucionalidad de una disposición específica en una ley?
                
                * ¿Quién presentó el caso ante el Tribunal Constitucional?
                
                * ¿Cuándo y cómo se tomó la decisión?
                
                * ¿Cuáles fueron algunos de los puntos clave o medidas destacadas en la ley original que se impugnó?

                En general, el texto proporciona detalles sobre la decisión del Tribunal Constitucional y el contexto en el que se enmarca, así como la información relevante sobre el caso y la ley en cuestión.
                                """
            
            resumen4 = """
                El texto proporcionado parece ser un documento formal relacionado con el derecho constitucional y los procedimientos judiciales en España. Específicamente, describe una decisión del Tribunal Constitucional respecto a una demanda presentada contra un Real Decreto-ley que introdujo ciertas medidas fiscales y relacionadas con la energía.

                Este texto puede responder preguntas como:

                * ¿Cuál fue el resultado de la demanda que impugnaba el Real Decreto-ley 12/2021?
                
                * ¿Qué disposición específica del Real Decreto-ley fue impugnada en el tribunal?
                
                * ¿Quién presentó la demanda contra el Real Decreto-ley?
                
                * ¿Cuándo tomó el Tribunal Constitucional su decisión sobre este caso?
                
                * ¿Cuál es la importancia de esta sentencia judicial en el derecho constitucional español?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-12754":
            resumen1 = """
                El documento proporcionado parece ser una decisión judicial del Tribunal Constitucional en España, específicamente una sentencia plenaria del 30 de junio de 2022, referente a una impugnación constitucional presentada por la Xunta de Galicia contra ciertas disposiciones de la Ley 7/2021. El texto analiza el marco legal relacionado con las concesiones y autorizaciones para propiedades de dominio público en España, destacando la interacción entre la Ley de Costas, la Ley 2/2013 y la Ley 7/2021.
                
                Este texto puede responder a preguntas como:
                
                •	¿Cuáles son las disposiciones clave de la Ley 7/2021 respecto a las concesiones y autorizaciones para propiedades de dominio público en España?
                
                •	¿Cómo se intersectan e interactúan la Ley de Costas, la Ley 2/2013 y la Ley 7/2021?
            
                •	¿Cuál es la importancia constitucional de la impugnación de la Xunta de Galicia a ciertas disposiciones de la Ley 7/2021?
                
                •	¿Cómo afecta el fallo del Tribunal Constitucional sobre este caso el marco legal para concesiones y autorizaciones en España?
            
                •	¿Cuáles son las posibles implicaciones de esta decisión para individuos o entidades que buscan obtener concesiones o autorizaciones para propiedades de dominio público en España?

            """
            
            resumen2 = """
                El texto proporcionado parece ser un documento legal, específicamente una sentencia o fallo del Tribunal Constitucional en España. El texto describe un caso relacionado con la constitucionalidad de ciertas disposiciones de la Ley 7/2021, una ley relacionada con el cambio climático y la transición energética.

                Algunas de las preguntas que este texto puede responder incluyen:

                •  ¿Cuáles son las disposiciones clave de la Ley 7/2021 respecto a las concesiones demaniales y las prórrogas?
                
                •  ¿Cómo afectan estas disposiciones a las concesiones demaniales existentes y los derechos de quienes las han obtenido?
                
                •  ¿Existen problemas constitucionales con la forma en que la Ley 7/2021 ha abordado las concesiones demaniales y las prórrogas?
                
                •  ¿Puede aplicarse el fallo del tribunal retroactivamente a las concesiones demaniales otorgadas antes de que la ley entrara en vigor?
                
                •  ¿Cómo afecta este fallo a la interpretación de leyes existentes, como la Ley de Costas y la Ley 2/2013?

                En general, el texto proporciona un análisis detallado de las implicaciones legales de la Ley 7/2021 y sus efectos sobre las concesiones demaniales y las prórrogas.
            """
            
            resumen3 = """
                Basado en el texto proporcionado, parece ser una decisión o fallo emitido por el Tribunal Constitucional en España. El texto aborda la constitucionalidad de ciertas disposiciones en la Ley 7/2021, de 20 de mayo, de cambio climático y transición energética.

                El principal problema parece ser el tratamiento de las concesiones relacionadas con los bienes de dominio público, especialmente en lo que respecta a su duración y la posibilidad de extensión o renovación. El texto analiza las implicaciones de ciertas disposiciones en la Ley 7/2021 y cómo interactúan con las leyes y regulaciones existentes.

                Este texto puede responder a preguntas como:

                
                * ¿Es constitucional la disposición contenida en el Artículo 20.4 de la Ley 7/2021?
                
                * ¿Cómo afectan las nuevas disposiciones de la Ley 7/2021 a las concesiones existentes relacionadas con bienes de dominio público?
                
                * ¿Pueden revisarse o anularse las concesiones otorgadas antes de la entrada en vigor de la Ley 7/2021 bajo las nuevas normas?
                
                * ¿Introduce la Ley 7/2021 un régimen nuevo para las concesiones que sea incompatible con la legislación anterior, potencialmente causando incertidumbre y desafíos legales?

                En general, este texto ofrece una visión sobre la interpretación y aplicación de leyes y regulaciones específicas relacionadas con los bienes de dominio público en España.
                            """
            
            resumen4 = """
                El texto proporcionado parece ser un documento legal o una decisión judicial sobre la constitucionalidad de ciertas disposiciones de la ley española "Ley 7/2021, de 20 de mayo, de cambio climático y transición energética". El texto discute la interpretación de los Artículos 20 y 2 de esta ley, así como las implicaciones para el régimen de concesiones otorgadas en terrenos de dominio público.

                Este texto puede responder preguntas como:

                * ¿Cuáles son las disposiciones clave en el Artículo 20 de la Ley 7/2021 respecto a la duración de las concesiones en terrenos de dominio público?
                
                * ¿Cómo interactúan estas disposiciones con las del Artículo 2 de la Ley 2/2013, que estableció una duración máxima para ciertos tipos de concesiones?
                
                * ¿Existe un conflicto entre la nueva ley y los derechos o concesiones existentes otorgados antes de su entrada en vigor?
                
                * ¿Cuál es el estado legal de las concesiones otorgadas bajo el antiguo régimen que ahora están por renovarse?
                
                * ¿Cómo puede la administración o los tribunales resolver estas ambigüedades y asegurar el cumplimiento de los principios de legalidad, legitimidad y predictibilidad?

                De manera más general, este texto puede ser utilizado como referencia para entender el marco legal que rige los terrenos de dominio público y las concesiones en España.
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-2707":
            resumen1 = """
                Basado en el texto proporcionado, parece tratarse de un decreto-ley emitido por el Presidente de la Generalitat de Catalunya que regula la modificación del Código Civil de Cataluña en relación con la ejecución de obras para mejorar la eficiencia energética o hídrica y la instalación de sistemas de energías renovables en los elementos comunes de los edificios.
                
                Este decreto-ley puede responder a preguntas como:
               
                •	¿Cuáles son las nuevas regulaciones para las obras de eficiencia energética en los elementos comunes de los edificios?
               
                •	¿Cómo afectan estas regulaciones al proceso de toma de decisiones dentro de las comunidades de propietarios?
               
                •	¿Cuál es el papel de los votos mayoritarios en la aprobación de proyectos de eficiencia energética?
               
                •	¿Pueden los propietarios individuales instalar sistemas de eficiencia energética sin la aprobación previa de la comunidad?
               
                •	¿Cuáles son las responsabilidades de los propietarios respecto al mantenimiento y conservación de las instalaciones existentes?
               
                El texto ofrece información detallada sobre las modificaciones al Código Civil de Cataluña, incluyendo nuevos artículos y subsecciones que establecen las normas y procedimientos para la implementación de proyectos de eficiencia energética. También aborda las posibles discrepancias entre los propietarios individuales y la comunidad en su conjunto.

            """
            
            resumen2 = """
                El texto proporcionado parece ser un decreto-ley emitido por el Presidente de la Generalitat de Catalunya, que modifica ciertos artículos del Código Civil de Cataluña respecto a la ejecución de obras para mejorar la eficiencia energética o hídrica y la instalación de sistemas de energía renovable en edificios sujetos al régimen de propiedad horizontal.

                Este texto puede responder preguntas tales como:

                •   ¿Cuáles son los cambios realizados en el Código Civil de Cataluña respecto a la eficiencia energética y los sistemas de energía renovable?
                
                •   ¿Cómo afectan estos cambios al proceso de toma de decisiones dentro de las comunidades de propietarios?
                
                •   ¿Cuál es el papel de la comunidad en la financiación y ejecución de proyectos para mejorar la eficiencia energética o instalar sistemas de energía renovable?
                
                •   ¿Cómo impactan estas modificaciones en el uso y disfrute de los elementos comunes en los edificios?

                Además, este texto también puede usarse para responder preguntas relacionadas con los cambios de políticas, actualizaciones legislativas y marcos regulatorios que rigen el desarrollo e implementación de iniciativas de energía sostenible en Cataluña.
                            """
                            
            resumen3 = """
                El texto proporcionado parece ser un decreto-ley (Decreto-ley) emitido por la Generalitat de Catalunya (Gobierno de Cataluña), fechado el 21 de febrero de 2022. El decreto-ley tiene como objetivo modificar el Código Civil de Cataluña en relación con la eficiencia energética y los sistemas de energía renovable en los edificios.

                El texto describe las nuevas regulaciones sobre la instalación de equipos eficientes en energía y sistemas de energía renovable en las áreas comunes de los edificios, así como los procedimientos para financiar estas instalaciones. También se delinean las responsabilidades de los propietarios y las comunidades en cuanto al mantenimiento y conservación de estas instalaciones.

                Algunas preguntas que este texto puede responder incluyen:

                -   ¿Cuáles son los requisitos para la instalación de equipos eficientes en energía y sistemas de energía renovable en las áreas comunes de los edificios?
                
                -   ¿Cómo se financiarán los costos de instalación, y cuál es el papel de los propietarios y las comunidades en la cobertura de estos gastos?
                
                -   ¿Cuáles son las responsabilidades de los propietarios y las comunidades en el mantenimiento y conservación de las instalaciones eficientes en energía?
                
                -   ¿Cómo buscan las nuevas regulaciones promover la eficiencia energética y la sostenibilidad en los edificios?
                
                En general, el texto ofrece información detallada sobre las disposiciones y objetivos del decreto-ley, que puede ser útil para propietarios de inmuebles, miembros de comunidades, arquitectos, ingenieros y responsables de políticas interesados en promover prácticas de construcción sostenible.
                            """
                            
            resumen4 = """
                El texto proporcionado parece ser un decreto-ley o reglamento relacionado con la eficiencia energética y las energías renovables en Cataluña, España. Específicamente, parece centrarse en la modificación del Código Civil de Cataluña para facilitar la instalación de medidas de eficiencia energética y sistemas de energías renovables en edificios sujetos al régimen de propiedad horizontal.

                Este texto puede responder preguntas como:

                * ¿Cuáles son las nuevas regulaciones respecto a la eficiencia energética y los sistemas de energías renovables en los edificios?
                
                * ¿Cómo afectarán estas regulaciones a los propietarios y comunidades en Cataluña?
                
                * ¿Cuáles son los beneficios y desafíos asociados con la instalación de medidas de eficiencia energética y sistemas de energías renovables en los edificios?
                
                * ¿Cómo afectará la modificación del Código Civil de Cataluña al desarrollo de proyectos de energía sostenible en la región?

                En general, este texto proporciona información sobre las políticas y regulaciones que rigen la eficiencia energética y las energías renovables en Cataluña, siendo relevante para investigadores, legisladores y profesionales que trabajan en estas áreas.
                            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2022-2982":
            resumen1 = """
                El texto proporcionado parece ser un decreto gubernamental o una enmienda legislativa destinada para corregir errores en un decreto-ley previo relacionado con la eficiencia energética y los sistemas de energías renovables en edificios sujetos a la normativa de propiedad horizontal. Este documento detalla los cambios realizados al decreto-ley original, incluyendo las correcciones a artículos específicos.
                
                Este texto puede responder a preguntas como:
               
                •	¿Cuáles son las modificaciones introducidas al Código Civil de Cataluña en relación con la eficiencia energética y los sistemas de energías renovables?
                
                •	¿Cómo afectan estas modificaciones a los edificios que se rigen por la normativa de propiedad horizontal?
                
                •	¿Cuál es el propósito del decreto-ley corregido y qué problemas busca solucionar?
               
                •	¿Qué cambios específicos se realizaron en ciertos artículos del decreto-ley original?

            """
            
            resumen2 = """
            El texto proporcionado parece ser una versión corregida de un decreto-ley emitido por el Gobierno de Cataluña, España. El decreto-ley tiene como objetivo modificar ciertos aspectos del Código Civil de Cataluña en relación con la ejecución de obras para la eficiencia energética y la instalación de sistemas de energía renovable en edificios sujetos al régimen de propiedad horizontal.

            Este texto puede responder preguntas tales como:

            •   ¿Cuál es el propósito del decreto-ley?
            
            •   ¿Qué artículos específicos del Código Civil de Cataluña están siendo modificados?
            
            •   ¿Qué cambios se están realizando en la normativa existente sobre eficiencia energética y sistemas de energía renovable en los edificios?
            
            •   ¿Por qué se emitió este decreto-ley y cuáles son sus consecuencias previstas?
            """
            
            resumen3 = """
                El texto proporcionado parece ser una publicación gubernamental, específicamente una corrección de errores en un decreto-ley anterior relacionado con las modificaciones al Código Civil de Cataluña en cuanto a la eficiencia energética y los sistemas de energía renovable en edificios sujetos a normas de propiedad.

                Este texto puede responder a varias preguntas, tales como:

                * ¿Cuáles fueron las correcciones realizadas al decreto-ley original?
                
                * ¿Cómo afectan estos cambios a la regulación de la eficiencia energética y los sistemas de energía renovable en los edificios?
                
                * ¿Cuáles son las implicaciones de estos cambios para los propietarios de inmuebles y los desarrolladores en Cataluña?
                
                * ¿Cómo se relaciona este decreto-ley con las leyes y regulaciones existentes sobre propiedad y eficiencia energética?

                En resumen, el texto proporciona información sobre las enmiendas al decreto-ley y sus efectos en la normativa vigente, ofreciendo claridad sobre cómo las correcciones impactan a las partes interesadas en Cataluña.
                            """
                            
            resumen4 = """
                El texto proporcionado parece ser un documento oficial del gobierno, específicamente una nota de corrección publicada en el Boletín Oficial del Estado (BOE), el diario oficial de España. El documento corrige errores en un decreto-ley anterior y modifica ciertas disposiciones relacionadas con la eficiencia energética y las energías renovables en edificios sujetos a propiedad horizontal.

                Este texto puede responder preguntas como:

                * ¿Qué cambios se hicieron al decreto-ley original?
                
                * ¿Cómo afectan estos cambios a la regulación de la eficiencia energética y las energías renovables en los edificios?
                
                * ¿Cuáles son algunos de los artículos o disposiciones específicos que fueron modificados o corregidos?
                
                * ¿Cuál es la base legal para estos cambios y cuál es su fecha de entrada en vigor?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2023-26461":
            resumen1 = """
            En general, este texto ofrece una visión detallada de la política energética de España y las iniciativas destinadas a promover el desarrollo sostenible y reducir las emisiones de carbono.
          
            El texto proporcionado parece ser un decreto gubernamental o una normativa relacionada con la política energética en España. El documento detalla diversos programas e iniciativas diseñados para promover las energías renovables, reducir la dependencia de los combustibles fósiles y mitigar los efectos del cambio climático.
            
            Este texto puede responder a preguntas como:
            
            •	¿Cuáles son los objetivos y metas del Plan de Recuperación, Transformación y Resiliencia?
            
            •	¿Cómo fomentan los programas descritos en este decreto las energías renovables y reducen las emisiones de carbono?
            
            •	¿Qué iniciativas y medidas específicas se han implementado para proteger el medio ambiente y combatir el cambio climático?
           
            •	¿Cómo se relaciona este decreto con las normativas y políticas de la Unión Europea sobre ayudas estatales y asistencia financiera para proyectos de energías renovables?
            
            •	¿Qué implicaciones tienen estos programas para los distintos interesados, como los actores de la industria, los consumidores y los gobiernos?
           
            En resumen, este texto ofrece una visión detallada de la política energética de España y de las iniciativas destinadas a fomentar el desarrollo sostenible y reducir las emisiones de carbono.

            """
            
            resumen2 = """
                El texto proporcionado parece ser un documento gubernamental, específicamente un Real Decreto de España. El texto discute varios programas e iniciativas relacionadas con la transición energética, las energías renovables y el desarrollo sostenible.

                El texto describe las modificaciones realizadas a las regulaciones existentes sobre ayudas estatales para la promoción de fuentes de energía renovable, eficiencia energética y almacenamiento. También detalla los criterios y requisitos para otorgar subvenciones a diferentes sectores, incluidos el sector residencial, la administración pública y las organizaciones del tercer sector.

                Algunas de las preguntas que este texto puede responder incluyen:

                
                •   ¿Cuáles son las nuevas regulaciones que rigen las ayudas estatales para proyectos de energía renovable en España?
                
                •   ¿Cómo afectan estas regulaciones a los programas e iniciativas existentes en el ámbito de la transición energética?
                
                •   ¿Cuáles son los criterios de elegibilidad para que los diferentes sectores reciban subvenciones bajo estos programas?
                
                •   ¿Cómo interactúan estas regulaciones con las leyes y regulaciones de la UE, como el Reglamento (UE) n.º 651/2014?

                En general, este texto proporciona información valiosa sobre las políticas e iniciativas del gobierno español dirigidas a promover el desarrollo sostenible de la energía y reducir las emisiones de carbono.
                            """
            
            resumen3 = """
                El texto proporcionado parece ser parte de un documento o informe oficial relacionado con las políticas y regulaciones gubernamentales en España, específicamente en cuanto a asuntos energéticos y ambientales. El texto discute varios decretos y leyes destinados a promover fuentes de energía renovable, reducir la dependencia de los combustibles fósiles y mejorar la eficiencia energética.

                Algunas de las preguntas que este texto puede responder incluyen:

                
                * ¿Cuáles son los objetivos y metas de la política energética del gobierno español?
                
                * ¿Cómo pretenden los diferentes decretos y regulaciones alcanzar estos objetivos?
                
                * ¿Qué medidas específicas se están tomando para promover fuentes de energía renovable y reducir las emisiones de carbono?
                
                * ¿Cómo afectan estas políticas a diversos sectores, como la industria, las áreas residenciales y comerciales?
                
                * ¿Se están realizando cambios o actualizaciones en las regulaciones o leyes existentes relacionadas con la energía y el medio ambiente?

                En resumen, el texto ofrece una visión detallada de las políticas energéticas y ambientales de España y puede utilizarse para responder a preguntas relacionadas con estos temas.
                            """
                            
            resumen4 = """
                Basado en la información contextual proporcionada, parece tratarse de un documento gubernamental relacionado con la política energética en España. Específicamente, el texto parece detallar medidas y directrices para dos programas destinados a promover las energías renovables y reducir la dependencia de los combustibles fósiles.

                El texto aborda cambios en las regulaciones, modificaciones a las reglas existentes y actualizaciones a planes previamente aprobados. También menciona fechas límite y plazos para la implementación de estos cambios.

                Este documento puede responder preguntas como:

                * ¿Cuáles son los objetivos y metas de los dos programas energéticos mencionados en el texto?
                
                * ¿Cómo pretenden estos programas promover las energías renovables y reducir la dependencia de los combustibles fósiles?
                
                * ¿Qué medidas y directrices específicas se delinean para cada programa?
                
                * ¿Cuáles son las fechas clave y los plazos para implementar estos cambios?
                
                * ¿Cómo se relacionan estas regulaciones con las políticas y directrices de la Unión Europea (UE)?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-A-2023-9215":
            resumen1 = """
            El texto proporcionado parece ser un documento en PDF del Boletín Oficial del Estado (BOE) que contiene una sentencia del Tribunal Constitucional emitida el 7 de marzo de 2023. Esta sentencia aborda un recurso de inconstitucionalidad presentado por el Parlamento de Canarias contra la disposición final tercera del Real Decreto-ley 12/2021.
            
            Este documento puede responder a preguntas como:
            
            •	¿Cuál es el contenido del recurso de inconstitucionalidad presentado por el Parlamento de Canarias?
            
            •	¿Qué establece la disposición final tercera del Real Decreto-ley 12/2021 y por qué ha sido impugnada?
            
            •	¿Cómo fundamenta el Tribunal Constitucional su decisión en este caso?
            
            •	¿Qué disposiciones o leyes específicas están siendo cuestionadas o analizadas en esta sentencia?
           
            •	¿Cuáles son las consecuencias de esta sentencia para los poderes del gobierno y para la relación entre el gobierno nacional y la comunidad autónoma de Canarias?

            """
            
            resumen2 = """
                El texto proporcionado parece ser un documento legal, específicamente una decisión o fallo del tribunal constitucional, sobre la inconstitucionalidad de un Real Decreto-ley y su impacto en el régimen económico y fiscal de las Islas Canarias.

                Este texto puede responder a preguntas tales como:

                •   ¿Cuáles son las implicaciones del Real Decreto-ley 12/2021 para la economía y la política fiscal de las Islas Canarias?
                
                •   ¿Es la modificación del régimen económico y fiscal de las Islas Canarias constitucional o inconstitucional?
                
                •   ¿Viola el Real Decreto-ley 12/2021 el procedimiento establecido en la Constitución y en el Estatuto de Autonomía de las Islas Canarias?
                
                •   ¿Puede el Gobierno aprobar leyes sin la consulta previa con el Parlamento de las Islas Canarias, como se hizo en este caso?

                El texto ofrece un análisis detallado de los problemas constitucionales en torno al Real Decreto-ley 12/2021, incluyendo argumentos sobre la violación de derechos procedimentales y la falta de justificación válida para la modificación del régimen económico y fiscal.
                            """
                            
            resumen3 = """
                Basado en el contexto proporcionado, parece ser un documento formal, probablemente una decisión o fallo judicial, relacionado con el derecho constitucional y la política fiscal en España. El texto discute la modificación de ciertas regulaciones respecto al régimen económico y fiscal de las Islas Canarias, específicamente los límites a las deducciones por inversiones en producciones.

                Este texto puede responder a preguntas tales como:

                
                * ¿Cuáles son las modificaciones específicas realizadas al régimen económico y fiscal de las Islas Canarias?
                
                * ¿Cómo afectan estos cambios a la deducibilidad de las inversiones en producciones, como películas o espectáculos?
                
                * ¿Cuál es la base constitucional para estos cambios y cómo se relacionan con los derechos y competencias del Parlamento de Canarias?
                
                * ¿Existen requisitos procedimentales específicos que deben cumplirse antes de que estos cambios puedan entrar en vigor?

                En general, el texto parece ser un documento legal formal con implicaciones significativas para la política económica y fiscal en España.
            """
            
            resumen4 = """
                El texto proporcionado parece ser una decisión o sentencia constitucional emitida por el Tribunal Constitucional en España. Específicamente, parece tratarse de una resolución sobre un caso constitucional que involucra una disputa entre el gobierno español y el Parlamento de Canarias respecto a la modificación del régimen económico y fiscal de Canarias.

                El texto aborda varios puntos clave, incluyendo:

                1. La supuesta violación de la garantía institucional del régimen económico y fiscal de Canarias, que requiere la consulta previa con el Parlamento de Canarias.
                
                2. La falta de una justificación válida por parte del gobierno para modificar el régimen económico y fiscal sin consultar primero al Parlamento de Canarias.

                Este texto puede responder preguntas como:

                * ¿Cuáles son las implicaciones constitucionales de modificar el régimen económico y fiscal de Canarias?
                
                * ¿Es constitucional que el gobierno español realice cambios en el régimen económico y fiscal de las Islas Canarias sin consultar previamente al Parlamento de Canarias?
                
                * ¿Cómo afecta esta sentencia a la relación entre el gobierno central y la Comunidad Autónoma de Canarias?
                
                * ¿Cuáles son las posibles consecuencias de violar la garantía institucional del régimen económico y fiscal de Canarias?
            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-B-2018-54744":
            resumen1 = """
            El texto proporcionado parece ser un anuncio formal sobre la adjudicación de un contrato público, específicamente un contrato mixto (obra y suministro) destinado a la rehabilitación y mejora del alumbrado público municipal en Marina de Cudeyo. El documento detalla la entidad contratante, el objeto del contrato, el presupuesto asignado y la empresa adjudicataria.
            
            Este texto puede responder a preguntas como:
           
            •	¿Cuál fue el objetivo del contrato público adjudicado a Imesapi, S.A.?
            
            •	¿Quién fue la entidad encargada de la contratación para este proyecto?
           
            •	¿Cuál fue el presupuesto destinado a la rehabilitación y mejora del alumbrado público en Marina de Cudeyo?
           
            •	¿Cuándo se formalizó el contrato?
           
            •	¿Qué empresa resultó adjudicataria del contrato?

            """
            
            resumen2 = """
                El texto proporcionado parece ser un anuncio oficial o boletín del gobierno español, específicamente un aviso de contratación pública para un proyecto de construcción. El texto describe un contrato adjudicado por el Ayuntamiento de Marina de Cudeyo (el consejo local de Marina de Cudeyo) para la rehabilitación, reforma y mejora del sistema de alumbrado público municipal.

                Este texto puede responder a varias preguntas, tales como:

                •   ¿Quién es la autoridad contratante?
                
                •   ¿Cuál es el objetivo del contrato?
                
                •   ¿Cuáles son los detalles del contrato, incluyendo el alcance, el presupuesto y el plazo?
                
                •   ¿Qué empresa fue adjudicataria del contrato?
                
                •   ¿Cuándo se publicaron los documentos del contrato y cuándo se formalizó el contrato?
            """
            
            resumen3 = """
                El texto proporcionado parece ser un anuncio oficial o una notificación pública relacionada con un contrato gubernamental para un proyecto de alumbrado municipal en Marina de Cudeyo. El texto detalla los términos y condiciones del contrato, incluyendo la entidad contratante, el objeto del contrato, el presupuesto y la formalización del acuerdo.

                Este texto puede responder a preguntas como:

                
                * ¿Cuál es el propósito del contrato?
                
                * ¿Quién es responsable de la implementación del proyecto?
                
                * ¿Cuál es el alcance del trabajo involucrado en el proyecto?
                
                * ¿Cuánto costó el proyecto?
                
                * ¿Cuándo se adjudicó el contrato y cuándo se formalizó?
                
                * ¿Quiénes son los principales interesados involucrados en el proyecto?
            """
            
            resumen4  = """
                El texto proporcionado parece ser un anuncio público del Boletín Oficial del Estado (BOE) del gobierno español, específicamente una notificación sobre un contrato adjudicado por el Ayuntamiento de Marina de Cudeyo para la rehabilitación, reforma y mejora de la iluminación pública del municipio.

                Este texto puede responder preguntas como:

                * ¿Quién es la entidad que adjudicó el contrato?
                
                * ¿Cuál es el propósito del contrato?
                
                * ¿Qué empresa fue adjudicataria del contrato?
                
                * ¿Cuándo se formalizó el contrato y cuál fue el importe total gastado?
                
                * ¿Cuál era el precio base para licitar en el contrato?

                En general, este texto proporciona información sobre un proceso de contratación pública en España, incluyendo detalles sobre la entidad contratante, el objeto del contrato, los licitadores y los términos del contrato.
                            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)

        elif BOE == "BOE-B-2019-52073":
            resumen1 = """
            El texto proporcionado parece ser una publicación gubernamental, específicamente un boletín oficial del Estado (BOE) en España. Detalla el proceso de contratación para un proyecto de construcción enfocado en la mejora de la eficiencia energética y la adaptación de los sistemas de aire acondicionado en un centro penitenciario.
           
            Este texto puede responder a preguntas como:
            
            •	¿Cuál era el objetivo del proyecto de construcción?
            
            •	¿Quién fue la autoridad adjudicadora del proyecto?
            
            •	¿Qué empresa fue adjudicataria del contrato?
           
            •	¿Cuáles fueron los costes estimados de la oferta ganadora, así como las ofertas más alta y baja recibidas?
           
            •	¿Cuándo comenzó el proceso de contratación y cuándo se adjudicó el contrato?
            
            •	¿Qué tipo de procedimiento se utilizó para adjudicar el contrato?

            """
            
            resumen2 = """
                El texto proporcionado parece ser una publicación gubernamental, específicamente un aviso de contratación pública, que detalla la formalización de un contrato por parte de la Subdirección General de Servicios Penitenciarios del Ministerio del Interior para una mejora energética y adaptación de los sistemas de aire acondicionado en el C.I.S. Evaristo Martín Nieto en Málaga.

                Este texto puede responder a preguntas tales como:

                •  ¿Quién es el organismo contratante?
                
                •  ¿Cuál es el propósito de la contratación?
                
                •  ¿Cuáles son las especificaciones del contrato?
                
                •  ¿Qué empresa fue adjudicataria del contrato?
                
                •  ¿Cuáles fueron los precios ofrecidos por los diferentes licitadores?
                
                •  ¿Cuándo se publicó el aviso de contratación pública?
                
                •  ¿Cómo se puede verificar la información?
            """
            
            resumen3 = """
            El texto proporcionado parece ser un anuncio gubernamental o una notificación oficial del Boletín Oficial del Estado (BOE) de España, específicamente un anuncio sobre un contrato de contratación pública adjudicado por la Subdirección General de Servicios Penitenciarios del Ministerio del Interior.

            Este texto puede responder a preguntas como:

            
            * ¿Quién fue la entidad contratante del proyecto?
            
            * ¿Cuál era el objetivo del proyecto?
            
            * ¿Qué empresa ganó la licitación y cuál fue el valor de su oferta?
            
            * ¿Cuáles fueron los criterios para adjudicar el contrato?
            
            * ¿Cuándo se anunció el concurso y cuándo se adjudicó?
            
            * ¿Cuál fue el alcance del trabajo involucrado en el proyecto?

            En general, el texto proporciona información sobre un proceso específico de contratación pública y los detalles relacionados con el mismo.
            """
            
            resumen4 = """
                El texto proporcionado parece ser un anuncio oficial del Boletín Oficial del Estado (BOE) del gobierno español, específicamente una notificación sobre un contrato público para servicios de construcción.

                Este texto puede responder diversas preguntas como:

                * ¿Cuál era el propósito del contrato público?
                
                * ¿Quién fue el contratista principal responsable de llevar a cabo el proyecto?
                
                * ¿Cuál fue el presupuesto asignado para el proyecto?
                
                * ¿Cuáles eran los requisitos específicos u objetivos del proyecto?
                
                * ¿Cuándo se adjudicó el contrato y cuándo comenzó el proyecto?

                El texto ofrece información detallada sobre la entidad contratante, el alcance del trabajo, el proceso de licitación y el contratista adjudicatario. Puede ser utilizado como referencia por investigadores, responsables de políticas o individuos interesados en entender cómo se gestionan los contratos públicos en España.
                            
            """
            resumenes = [resumen1, resumen2, resumen3, resumen4]
            return random.choice(resumenes)
