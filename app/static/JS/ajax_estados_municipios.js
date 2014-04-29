//Funcion para llamar a la vista que se encarga de cambiar dinamicamente estados y municipios.

$(function () {
	$("#id_Colonia").autocomplete({
		source: "/api/get_colonias/",
		minLength: 2,
	});

	$("#id_formset_sencilla-Colonia").autocomplete({
		source: "/api/get_colonias/",
		minLength: 2,
	});

	$("#id_Estado").change(function () {
		$.getJSON("/api/get_municipios/", { id: $(this).val(), ajax: 'true' }, function (j) {
			var options = '';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			$("#id_Municipio").html(options);
		})
	})
	// Cambios dinamicos de municipio para paquetes
	$("#id_formset_sencilla-Estado").change(function () {
		$.getJSON("/api/get_municipios/", { id: $(this).val(), ajax: 'true' }, function (j) {
			var options = '';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			$("#id_formset_sencilla-Municipio").html(options);
		})
	})

	$("#id_Cliente").change(function () {
		$.getJSON("/api/get_deptos/", { id: $(this).val(), ajax: 'true' }, function (j) {
			var options = '';
				options += '<option value="' + '' + '">' + "---------" + '</option>';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			$("#id_Depto").html(options);
		})
	})
	// Cambios dinamicos de departamento para paquetes
	$("#id_formset_sencilla-Cliente").change(function () {
		$.getJSON("/api/get_deptos/", { id: $(this).val(), ajax: 'true' }, function (j) {
			var options = '';
				options += '<option value="' + '' + '">' + "---------" + '</option>';
			for (var i = 0; i < j.length; i++) {
				options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
			}
			$("#id_formset_sencilla-Depto").html(options);
		})
	})

});


