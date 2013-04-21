
# Se insertan a las estados y municipios a tablas de django, ya no debe ser necesario usando fixtures.

# INSERT INTO`app_estado`(estado_id, Nombre, clave, abrev)
# SELECT id, nombre, clave, abrev
# FROM `estados`;

# INSERT INTO`app_municipio`(municipio_id, estado_id_id, Nombre, clave, is_active)
# SELECT id, estado_id, nombre, clave, '1'
# FROM `municipios`;

# UPDATE app_municipio SET `Nombre` = UPPER( `Nombre` );

# UPDATE app_estado SET `Nombre` = UPPER( `Nombre` );

SELECT * FROM app_avaluo WHERE MUNICIPIO = 'GA';

#Encontrar Diferencias entre estados y municipios de la tabla avaluo

SELECT DISTINCT Municipio FROM app_avaluo ORDER BY Municipio;
SELECT DISTINCT Estado FROM app_avaluo ORDER BY Estado;

SELECT DISTINCT * FROM app_avaluo WHERE ESTADO IS NULL ;



#NUEVO LEON
UPDATE app_avaluo SET Municipio='948', Estado='19' WHERE Municipio REGEXP 'ABASOLO';
UPDATE app_avaluo SET Municipio='949', Estado='19' WHERE Municipio REGEXP 'AGUALEGUAS';
UPDATE app_avaluo SET Municipio='951', Estado='19' WHERE Municipio REGEXP 'ALLENDE';
UPDATE app_avaluo SET Municipio='952', Estado='19' WHERE Municipio REGEXP 'ANAHUAC';
UPDATE app_avaluo SET Municipio='956', Estado='19' WHERE Municipio REGEXP 'C.DEREY';
UPDATE app_avaluo SET Municipio='957', Estado='19' WHERE Municipio REGEXP 'CARMEN';
UPDATE app_avaluo SET Municipio='958', Estado='19' WHERE Municipio REGEXP 'CERRALVO';
UPDATE app_avaluo SET Municipio='959', Estado='19' WHERE Municipio REGEXP 'CIENEGA DE ';
UPDATE app_avaluo SET Municipio='961', Estado='19' WHERE Municipio REGEXP 'DOCTOR ARROYO';
UPDATE app_avaluo SET Municipio='968', Estado='19' WHERE Municipio REGEXP 'ESCOBEDO';
UPDATE app_avaluo SET Municipio='993', Estado='19' WHERE Municipio REGEXP 'SAN NICOLAS';
UPDATE app_avaluo SET Municipio='993', Estado='19' WHERE Municipio REGEXP 'SAN  NICOLAS';
UPDATE app_avaluo SET Municipio='966', Estado='19' WHERE Municipio REGEXP 'SAN PEDRO';
UPDATE app_avaluo SET Municipio='953', Estado='19' WHERE Municipio REGEXP 'APODACA';
UPDATE app_avaluo SET Municipio='965', Estado='19' WHERE Municipio REGEXP 'GARCÍA';
UPDATE app_avaluo SET Municipio='965', Estado='19' WHERE Municipio REGEXP 'GA';
UPDATE app_avaluo SET Municipio='969', Estado='19' WHERE Municipio REGEXP 'GENERAL TER';
UPDATE app_avaluo SET Municipio='972', Estado='19' WHERE Municipio REGEXP 'GENERAL ZUA';
UPDATE app_avaluo SET Municipio='972', Estado='19' WHERE Municipio REGEXP 'ZUAZUA';
UPDATE app_avaluo SET Municipio='973', Estado='19' WHERE Municipio REGEXP 'GUADA';
UPDATE app_avaluo SET Municipio='976', Estado='19' WHERE Municipio REGEXP 'HUALAHUI';
UPDATE app_avaluo SET Municipio='978', Estado='19' WHERE Municipio REGEXP 'JUAREZ';
UPDATE app_avaluo SET Municipio='980', Estado='19' WHERE Municipio REGEXP 'LINARES';
UPDATE app_avaluo SET Municipio='981', Estado='19' WHERE Municipio REGEXP 'MARIN';
UPDATE app_avaluo SET Municipio='985', Estado='19' WHERE Municipio REGEXP 'MONTEMORELOS';
UPDATE app_avaluo SET Municipio='986', Estado='19' WHERE Municipio REGEXP 'MONTER';
UPDATE app_avaluo SET Municipio='988', Estado='19' WHERE Municipio REGEXP 'PESQUERI';
UPDATE app_avaluo SET Municipio='991', Estado='19' WHERE Municipio REGEXP 'HIDALGO';
UPDATE app_avaluo SET Municipio='992', Estado='19' WHERE Municipio REGEXP 'SALIANAS VI';
UPDATE app_avaluo SET Municipio='992', Estado='19' WHERE Municipio REGEXP 'SALINAS VI';
UPDATE app_avaluo SET Municipio='992', Estado='19' WHERE Municipio REGEXP 'SALINA VI';
UPDATE app_avaluo SET Municipio='995', Estado='19' WHERE Municipio REGEXP 'SANTA CAT';
UPDATE app_avaluo SET Municipio='996', Estado='19' WHERE Municipio REGEXP 'SANTIAGO';
UPDATE app_avaluo SET Municipio='998', Estado='19' WHERE Municipio REGEXP 'VILLALDAMA';

#TAMALULIPAS

UPDATE app_avaluo SET Municipio='2040',Estado='28' WHERE Municipio REGEXP 'LAREDO';
UPDATE app_avaluo SET Municipio='2035',Estado='28' WHERE Municipio REGEXP 'MATAMOROS';
UPDATE app_avaluo SET Municipio='2038',Estado='28' WHERE Municipio REGEXP 'MIGUEL ALEMAN';
UPDATE app_avaluo SET Municipio='2045',Estado='28' WHERE Municipio REGEXP 'REYNOSA';
UPDATE app_avaluo SET Municipio='2046',Estado='28' WHERE Municipio REGEXP 'RIO BRAVO';
UPDATE app_avaluo SET Municipio='2048',Estado='28' WHERE Municipio REGEXP 'SAN FERNANDO';
UPDATE app_avaluo SET Municipio='2053',Estado='28' WHERE Municipio REGEXP 'VALLE HERMOSO';
UPDATE app_avaluo SET Municipio='2054',Estado='28' WHERE Municipio REGEXP 'VICORIA';

#COAHUILA
UPDATE app_avaluo SET Municipio='34',Estado='5' WHERE Municipio REGEXP 'ACUÑA';
UPDATE app_avaluo SET Municipio='50',Estado='5' WHERE Municipio REGEXP 'ARTEAGA';
UPDATE app_avaluo SET Municipio='50',Estado='5' WHERE Municipio REGEXP 'MONCLOVA';
UPDATE app_avaluo SET Municipio='51',Estado='5' WHERE Municipio REGEXP 'MORELOS';
UPDATE app_avaluo SET Municipio='59',Estado='5' WHERE Municipio REGEXP 'RAMOS ARIZPE';
UPDATE app_avaluo SET Municipio='62',Estado='5' WHERE Municipio REGEXP 'SALTILLO';

#YUCATAN
UPDATE app_avaluo SET Municipio='2366',Estado='31' WHERE Municipio REGEXP 'HUNUCMA';
UPDATE app_avaluo SET Municipio='2369',Estado='31' WHERE Municipio REGEXP 'KANASIN';
UPDATE app_avaluo SET Municipio='2378',Estado='31' WHERE Municipio REGEXP 'MERIDA';
UPDATE app_avaluo SET Municipio='2387',Estado='31' WHERE Municipio REGEXP 'PROGRESO';
UPDATE app_avaluo SET Municipio='2407',Estado='31' WHERE Municipio REGEXP 'TEKAX';
UPDATE app_avaluo SET Municipio='2415',Estado='31' WHERE Municipio REGEXP 'TETIZ';
UPDATE app_avaluo SET Municipio='2428',Estado='31' WHERE Municipio REGEXP 'UCU';
UPDATE app_avaluo SET Municipio='2429',Estado='31' WHERE Municipio REGEXP 'UMAN';
UPDATE app_avaluo SET Municipio='2430',Estado='31' WHERE Municipio REGEXP 'VALLADOLID';

#SAN LUIS POTOSI
UPDATE app_avaluo SET Municipio='1868',Estado='24' WHERE Municipio REGEXP 'MATEHUALA';

#AGUASCALIENTES
UPDATE app_avaluo SET Municipio='11',Estado='1' WHERE Municipio REGEXP 'San Francisco de los';

#UPDATES para estados que no son numero
UPDATE app_avaluo SET Municipio='986', Estado='19' WHERE Estado IS NULL;
UPDATE app_avaluo SET Municipio='986', Estado='19' WHERE Estado = 'Nuevo Leon';

#UPDATES para los que no son nada
UPDATE app_avaluo SET Municipio='986', Estado='19' WHERE Municipio IS NULL;
UPDATE app_avaluo SET Municipio='986', Estado='19' WHERE Municipio = '';
UPDATE app_avaluo SET Municipio='986', Estado='19' WHERE Municipio = '-';