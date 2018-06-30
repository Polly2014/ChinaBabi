function formValidAndSubmit(){
	var documentID = $('#documentID').val();
	var documentCode = $('#documentCode').val();
	if(!documentID){
		alert('文档ID不能为空!');
		$('#documentID').focus();
		return;
	}
	if(!documentCode){
		alert('文档查验码不能为空!');
		$('#documentCode').focus();
		return;
	}
	var params = {'documentID':documentID, 'documentCode':documentCode}
	$.ajax({
		type: 'post',
		url: 'valid/',
		data: params,
		async: false,
		dataType: 'json',
		success: function(data){
			// console.log("Ajax Data:"+data);
			if(data['code']==0){
				$('#form_search').submit();
			}else{
				alert(data['message']);
			}
		}
	})
	return false;
}