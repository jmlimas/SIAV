//Funcion para llamar a la vista que se encarga de cambiar dinamicamente estados y municipios.

jQuery(function () {
	

	jQuery("#id_Estado").change(function () {
		jQuery.getJSON("/api/get_municipios/", { id: jQuery(this).val(), ajax: 'true' }, function (j) {
			var options = '';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			jQuery("#id_Municipio").html(options);
		})
	})
	// Cambios dinamicos de municipio para paquetes
	jQuery("#id_formset_sencilla-Estado").change(function () {
		jQuery.getJSON("/api/get_municipios/", { id: jQuery(this).val(), ajax: 'true' }, function (j) {
			var options = '';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			jQuery("#id_formset_sencilla-Municipio").html(options);
		})
	})

	jQuery("#id_Cliente").change(function () {
		jQuery.getJSON("/api/get_deptos/", { id: jQuery(this).val(), ajax: 'true' }, function (j) {
			var options = '';
				options += '<option value="' + '' + '">' + "---------" + '</option>';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			jQuery("#id_Depto").html(options);
		})
	})
	// Cambios dinamicos de departamento para paquetes
	jQuery("#id_formset_sencilla-Cliente").change(function () {
		jQuery.getJSON("/api/get_deptos/", { id: jQuery(this).val(), ajax: 'true' }, function (j) {
			var options = '';
				options += '<option value="' + '' + '">' + "---------" + '</option>';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			jQuery("#id_formset_sencilla-Depto").html(options);
		})
	})

});


