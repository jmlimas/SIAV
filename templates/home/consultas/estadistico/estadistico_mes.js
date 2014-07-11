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
