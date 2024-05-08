
$('#file-0a').fileinput({
	theme: 'bs5',
	language: 'es',
	showUpload: true,
	showCaption: true,
	uploadAsync: false,
	maxFileSize: 4768,
	allowedFileExtensions: ['jpg', 'png', 'gif', 'mp4', 'svg'],
	uploadUrl: '/thymeleaf-fileinput/subirImagen',
	elErrorContainer: '#kv-error-1'
}).on('filebatchuploadsuccess', function(event, data) {
	let files = data.files;
	let fileList = '';
	$.each(files, function(index, file) {

		console.log('File' + index + ':' + file.name);

		fileList += '<li>' + file.name + '</li>';

		$('#kv-success-1').show();
		$('#kv-success-1').html(fileList);
		$('#kv-success-1').fadeIn('slow');

	});
});