var array_header = new Array();
array_header = ('Task', 'Summary', 'Start Date', 'Status', 'Help Needed');
var x = 0;
var list1 = [];
var list2 = [];
var list3 = [];
var list4 = [];
var list5 = [];
var list6 = [];

list1[x] = document.getElementById("title1").value;
list2[x] = document.getElementById("summary").value;
list3[x] = document.getElementById("start_date").value;
list4[x] = document.getElementById("status").value;
list5[x] = document.getElementById("help").value;

function create_table() {
	var emp_table = document.createElement('table');
	emp_table.setAttribute('id', 'emp_table');

	var tr = emp_table.insertRow(-1);
	for(var i = 0; i<array_header.length; i++){
		var th = document.createElement('th');
		th.innerHTML = array_header[i];
		tr.appendChild(th);

	}
	
	var div = document.getElementById('cont');
	div.appendChild(emp_table);

}


function add_new_row() {
	$("#exampleModal").modal("hide");	
	
	var n=1;
	var x=0;

	var emp_table = document.getElementById('table1');
	var row_count = emp_table.rows.length;
	var tr;
	tr = emp_table.insertRow(row_count);
			
	for(var i = 0; i < 6; i++){
		var td = document.createElement('td');
		td = tr.insertCell(i);
		if (i == 3){
			var status = ['Work in Progress', 'Completed', 'Pending','Cancel'];
			var selection = document.createElement('select');
			td.appendChild(selection);

			for(var j=0; j< status.length; j++){
				var option = document.createElement('option');
				option.value = status[j];
				option.text = status[j];
				selection.appendChild(option);
			}
		}
		else{
			var ele = document.createElement('textarea');
			ele.readOnly = true;
			ele.setAttribute('id', 'cell'+row_count+i);
			ele.setAttribute('name', 'text'+row_count+i);
			td.appendChild(ele);
			add_text_to_cell(i,ele);
		}
	
	}
	n++;
	x++;
}

function add_text_to_cell(num,element) {

	var x=0;
	var list1 = [];
	var list2 = [];
	var list3 = [];
	var list4 = [];
	var list5 = [];
	var list6 = [];
	
	list1[x] = document.getElementById("title1").value;
	list2[x] = document.getElementById("summary").value;
	list3[x] = document.getElementById("start_date").value;
	list4[x] = document.getElementById("status").value;
	list5[x] = document.getElementById("help").value;
	list6[x] = document.getElementById("remark").value;

	if (num == 0){
		element.innerHTML = list1[x];
	}
	else if (num == 1){
		element.innerHTML = list2[x];
	}
	else if (num==2){
		element.innerHTML = list3[x];
	}
	else if (num == 4){
		element.innerHTML = list5[x];
	}
	else if (num == 5){
		element.innerHTML = list6[x];
	}
}
