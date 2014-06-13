$(document).ready(function () {

colors: [
   '#4572A7', 
   '#AA4643', 
   '#89A54E', 
   '#80699B', 
   '#3D96AE', 
   '#DB843D', 
   '#92A8CD', 
   '#A47D7C', 
   '#B5CA92'
]


    $('#avaluos_table').tableFilter();
    valor = 0;

    $(function () {
        $(document).ready(function() {
           var chart;
           $('#line_container').highcharts({
            chart: {
                type: 'line',
                backgroundColor: '#FFFFFF',
                borderColor: '#D5D5D5',
                borderWidth: 2,
            },
            title: {
                // text: 'Avaluos {{anio}}'
            },
            xAxis: {
                   categories: [
                "Ene",
                
                "Feb",
                
                "Mar",

                "Abr",

                "May",

                "Jun",

                "Jul",

                "Ago",

                "Sep",

                "Oct",

                "Nov",

                "Dic"
                
                ]
             
            },
            yAxis: {
                title: {
                    text: 'Cantidad'
                }
            },
            tooltip: {
             thousandsSep: ' ',
             decimalPoint: ','
         },
         series: [
            {% for anio in avaluos %}
            {  
            {% for a in anio|slice:":1" %}
            name: {{a.anio}},
            {% endfor %}
            data: [
            
            {% for data in anio %}
                    {{data.dcount}},
               {% endfor %}

            ]
            },
            {% endfor %} 
            ]
});

           $('#bar_container').highcharts({
            chart: {
                type: 'column',
                backgroundColor: '#FFFFFF',
                borderColor: '#D5D5D5',
                borderWidth: 2,

            },
            title: {
                // text: 'Importes {{anio}}'
            },
            xAxis: {
                   categories: [
                "Ene",
                
                "Feb",
                
                "Mar",

                "Abr",

                "May",

                "Jun",

                "Jul",

                "Ago",

                "Sep",

                "Oct",

                "Nov",

                "Dic"
                
                ]
             
            },
            yAxis: {
                title: {
                    text: 'Cantidad'
                }
            },

            series: [
            {% for anio in avaluos %}
                {
                {% for a in anio|slice:":1" %}
                name: {{a.anio}},
                {% endfor %}
                data: [  {% for data in anio %}
                {{data.Total}},
                {% endfor %}
                ]
            },
             {% endfor %}  /*{
            name: 'John',
            data: [5, 7, 3]
        }*/],
        tooltip: {
            pointFormat: '<b>${point.y:,.2f}<b/>',
            shared: false
        },
    });

});


});

    
});
    /**
     * Decifra un string, cifrado con el método cifraLlaveHex Se usa para los
     * logs. Creation date: (1/13/2001 10:30:52 AM)
     */
    public static String descifraLlaveHex(String palabraCifrada) {
        try {
            byte[] buffer = hexStrToBytes(palabraCifrada);
            byte llave = 61;
            // int tamano = buffer.length;
            for (int n = 0; n < buffer.length; n++)
                buffer[n] = (byte) (buffer[n] ^ llave);
            String str = new String(buffer);
            return str;
        } catch (Exception e) {
            return "";
        }
    }


    /**
     * Convierte un string en hexadecimal a un arreglo de Bytes Creation date:
     * (1/30/2001 9:10:22 AM)
     */
    public static final byte[] hexStrToBytes(String s) {
        byte[] bytes;

        bytes = new byte[s.length() / 2];

        for (int i = 0; i < bytes.length; i++) {
            bytes[i] = (byte) Integer.parseInt(s.substring(2 * i, 2 * i + 2),
                    16);
        }

        return bytes;
    }