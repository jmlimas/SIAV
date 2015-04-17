 var grid2 = jQuery('#avaluos_table');
           var options2 = {      
            additionalFilterTriggers: [jQuery('#onlyno'),],
          matchingRow: function(state, tr, textTokens) {
            if (!state || !state.id) {
              return true;
            }
            var child = tr.children('td:eq(4)');
            if (!child) return true;
            var val = child.text();
            switch (state.id) {
            case 'onlyno':
              return state.value !== true || val !== 'PAQUETE INFONAVIT';
            default:
              return true;
            }
          },
           filteringRows: function(filterStates) {
                grid2.addClass('filtering');
              },
              filteredRows: function(filterStates) {
                grid2.removeClass('filtering');
                setRowCountOnGrid2();
              }
            };      
     
            function setRowCountOnGrid2() {
              var rowcount = grid2.find('tbody tr:not(:hidden)').length;
              jQuery('#rowcount').text('' + rowcount + '');
            }



  grid2.tableFilter(options2);
  setRowCountOnGrid2();

  valor = 0;

  var rowCount = { p: jQuery('#avaluos_table tbody tr:visible').length };
  valor = (jQuery('#avaluos_table tbody tr:visible').length);

  jQuery('#cantidad_tabla').html(valor);

