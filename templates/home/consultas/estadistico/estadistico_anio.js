jQuery(document).ready(function ($) {

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


    $(function () {
        $(document).ready(function() {
           var chart;

           $('#line_container').highcharts({
            chart: {
                type: 'line',
                backgroundColor: '#FFFFFF',
                borderColor: '#D5D5D5',
                borderWidth: 0,
                height: 300,
            },
            title: {
                // text: 'Avaluos {{anio}}'
                text: ''
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
                borderWidth: 0,
                height: 300,

            },
            title: {
                text: ''
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
                formatter: function() {
                    return '<b>'+ this.x +'</b><br/>'+
                        this.series.name +': $'+ this.y.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
                }
            },
            series: [
            {% for anio in avaluos %}
                {
                {% for a in anio|slice:":1" %}
                name: {{a.anio}},
                {% endfor %}
                data: [  {% for data in anio %}
                {{data.Total|default_if_none:"0"}},
                {% endfor %}
                ]
            },
             {% endfor %}  /*{
            name: 'John',
            data: [5, 7, 3]
        }*/],

    });

});


});

    
});
