$(document).ready(function(){
	if($('#result') != null){
		Read();
	}
	$('#create').on('click',function(){
		$name = $('#name').val();
		$phonenumber = $('#phonenumber').val();
		$email = $('#email').val();
		$image = $('#image').val();
		if($name == "" || $phonenumber == "" || $email == "" || $image == "")
			alert("please complete the required field");
		else{
			$.ajax({
				url:'create/',
				type:'POST',
				data:{
					name: $name,
					phonenumber: $phonenumber,
					email: $email,
					image: $image,
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
				},
				success: function(){
				   Read();
				   $('#name').val('');
				   $('#phonenumber').val('');
				   $('#email').val('');
				   $('#image').val('');
				   alert("NewMember Successfully Added");
				}
			});
		}
	});

	$(document).on('click', '.edit' ,function(){
		$id = $(this).attr('name');
		window.location = "edit/"+ $id;
	});

	$('#update').on('click', function(){
		$name = $('#name').val();
		$phonenumber = $('#phonenumber').val();
		$email = $('#email').val();
		$image = $('#image').val();
		if($name == "" || $phonenumber == "" || $email == "" || $image == "")
			alert("please complete the required field");
		else{
			$id = $('#blue_id').val();
			$.ajax({
				url:'update/' + $id,
				type: 'POST',
				data:{
					name: $name,
					phonenumber: $phonenumber,
					email: $email,
					image: $image,
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
				},
				success: function(){
					window.location = '/';
					alert('updated');
				}
			});
		}
	});
    $(document).on('click', '.delete', function(){
    	$id = $(this).attr('name');
    	$.ajax({
    		url:'delete/' + $id,
    		type: 'POST',
    		data: {
    			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    		},
    		success: function(){
    			Read();
    			alert('deleted');
    		}
    	});
    });
});

function Read(){
	$.ajax({
		url: 'read/',
		type: 'POST',
		async: false,
		data:{
			res:1,
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success:function(response){
			$('#result').html(response);
		}
	});
}