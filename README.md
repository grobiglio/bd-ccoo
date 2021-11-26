# Código para gestión de Comunicaciones Oficiales (CCOO)

La gestión de las CCOO se realiza mediante una base de datos Sqlite.

La intención del proyecto, además de disponer de una herramienta que ayude a la gestión de las CCOO es aprender a usar Bases de Datos, por tal razón dejo estos links de interés:

[Curso de SQL de Píldoras Informáticas](https://youtube.com/playlist?list=PLU8oAlHdN5Bmx-LChV4K3MbHrpZKefNwn)

[Masterclass de Bases de Datos por Álvaro Chirou](https://youtu.be/FZos4jHlEmE)

[Documentacón oficial sqlite3](https://docs.python.org/3.8/library/sqlite3.html)

Secciones 18 a 20 del curso **Master en Python: Aprender Python 3, Django, Flask y Tkinter** de Vícto Robles que se encuentra en [UDEMY](https://www.udemy.com/share/102Ows3@qcBpJMcqMuf3ar2Ibw_GHkhOuDr6Mtq76A6oIcJtg50HZf6K0YTKNC89WMJTJr-WFA==/).

Secciones 24 a 27 del curso **The Complete 2022 Web Development Bootcamp** de Angela Yu que se encuentra en [UDEMY](https://www.udemy.com/share/1013gG3@36y8eorCDTYGGl4_z6Mc1AMaQQ41jGb4Wy91iVo8aCy47_8kJKdfKeBsfKOTFP1xrg==/).

## Campos de la tabla

* ID: Autonumeración y campo clave
* NoCO: Número de Comunicación Oficial -> Texto de 50 caracteres.
* Fecha: Fecha de la Comunicación Oficial en formato DD/MM/AAAA.
* Referencia: Referencia de la Comunicación Oficial -> Tecto de 255 caracteres.
* Proyecto: Proyecto con el que se encuentra relacionada la Comunicación Oficial -> Texto de 255 caracteres
* Carpeta: Carpeta donde se halla la Comunicación Oficial -> Hipervínculo
