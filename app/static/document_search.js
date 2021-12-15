// scalić niektóre funkcje (przede wszystkich print...)

function search_parameters_from_url(search_fields) {
    const urlParams = new URLSearchParams(window.location.search);
    function add_components(v, key) {
	if(search_fields.hasOwnProperty(key)) {

	    // podobne do add_searched_id
	    if(!search_fields[key]["ids_list"].has(v)) {
		search_fields[key]["ids_list"].add(v);
		
		get_ajax_fn(endpoint=search_fields[key]["url"],
			    data={"id": v},
			    success_fn=title => search_criterion_component(
				$(search_fields[key]["parent_component_id"]),
				title, on_close_cb=() => search_fields[key][
				    "ids_list"].delete(v)))()
	    }
	}
    }
    urlParams.forEach(add_components);
}

function add_searched_id(set, parent) {
    return event => {
	if(!set.has(event.currentTarget["id"])) {
	    set.add(event.currentTarget["id"]);
	    search_criterion_component(
		parent=parent, event.currentTarget.textContent,
		() => set.delete(event.currentTarget["id"]));
	}
	else {
	    // powiadomienie powinno mieć inną formę
	    alert("Element with a given id is already in the list.");
	}
    }
}

function url_query_for(root) {
    return config_list => {
	let url = new URL(root);
	for(config_item in config_list) {
	    console.log(config_list[config_item]["ids_list"]);
	    config_list[config_item]["ids_list"].forEach(
		id => url.searchParams.append(config_item, id));
	}
	let document_text_search = $("#document-text-fields-search").val()
	if(document_text_search) {
	    url.searchParams.append('document_text_search',
				    document_text_search);
	}
	return url;
    }
}

function print_list(list, drop_down, parent, ids_list) {
    // niech najpierw sprawdza czy cokolwiek tam jest
    drop_down.empty();
    let list_item;
    for(item of list) {
	list_item = $("<div></div>").addClass(
	    "list-group-item list-group-item-action");
	if(item["source"]) {
	    list_item.attr("data-source", item["source"]);
	}
	list_item.attr("id", item["id"]);
	list_item.html(item["text"]);
	list_item.click(add_searched_id(ids_list, parent));
	drop_down.append(list_item);
    }
}

// podobne do print_list - zgeneralizować
function print_search_results(results, dropdown_list, select_multiple_id) {
    // quicksearch results in a selected section/list
    dropdown_list.empty();
    let list_item;
    for(result of results) {
	list_item = $("<div></div>").addClass(
	    "list-group-item list-group-item-action");
	list_item.html(result["text"]);
	list_item.attr("id", result["id"]);

	list_item.click(event => {
	    if(!check_if_in_option_list(
		event.currentTarget.id, select_multiple_id)) {
		let option = $("<option></option>");
		option.attr("value", event.currentTarget.id)
	    	    .text(event.currentTarget.textContent);
		$(`${select_multiple_id}`).append(option);
	    }
	});
	dropdown_list.append(list_item);
    }
}

function add_option_to_multiselect(multisel, option_value, text) {
}

function print_items(results, dropdown_list, select_multiple_id, click_fn) {
    dropdown_list.empty();
    let list_item;
    for(result of results) {
	list_item = $("<div></div>").addClass(
	    "list-group-item list-group-item-action");
	list_item.html(result["text"]);
	list_item.attr("id", result["id"]);
	list_item.click(click_fn);
	dropdown_list.append(list_item);
    }
}

function get_filter_cb(
    input_name, fn_url, drop_down, parent, ids_list) {
    return () => {
	let query = {"query": $(input_name).val()};
	get_ajax_fn(fn_url, query,
	list => print_list(list[0], drop_down, parent, ids_list)
	)()
    };
}

function get_ajax_fn(endpoint, data, success_fn,
		     fail_fn=(jqXHR, status) => alert(
			 `Error while processing the request: ${status}.`)) {
    return () => $.ajax({
	url: endpoint,
	type: "POST",
	data: JSON.stringify(data),
	datatype: "json",
	contentType: "application/json; charset=utf-8",
	success: success_fn,
    }).fail(fail_fn);
}

function get_search_results(endpoint, query, field, root, page=1) {
    let load_next = field + " + div button";
    let spinner = $('<span class="spinner-grow spinner-grow-sm"'
		    + 'role="status"></span>');

    function success_fn(results) {
	spinner.remove();
	print_search_results(results[0], $(field), root);
	$(load_next).off("click");
	if(results[1]) {
	    $(load_next).click(
		get_search_results(endpoint,
				   query, field, root, page=page+1));
	}
	else {
	    $(load_next).attr("disabled", "disabled");
	}
    }
    return () => {
	$(load_next).prepend(spinner);
	let timeout = 400;

	return setTimeout(get_ajax_fn(
	    endpoint=endpoint,
	    data={"query": query, "page": page},
	    success_fn=success_fn), timeout);
    }
}

function set_up_server_callbacks(callbacks) {
    for(callback in callbacks) {
	$(callbacks[callback]["input"]).keyup(get_filter_cb(
	    callbacks[callback]["input"],
	    callbacks[callback]["url"],
	    $(callbacks[callback]["drop_down"]),
	    $(callbacks[callback]["parent_component_id"]),
	    callbacks[callback]["ids_list"]));
    }
}

function check_if_in_option_list(item_id, list_id) {
    // check if a given id is already in a multiple selection list
    for (item of $(list_id).children()) {
	if(item.value == item_id) {
	    return true;
	}
    }
    return false;
}

function search_criterion_component(parent, title, on_close_cb=() => {}) {
    // on_close_cb - callable invoked on component removal
    let main_btn = $("<div></div>").addClass(
	"btn btn-outline-info btn-sm m-1");
    let row = $("<div></div>").addClass("row");
    let label_col = $("<div></div>").addClass("col").html(title);
    let close_bt_col = $("<div></div>").addClass("col-1");
    main_btn.append(row);
    row.append(label_col).append(close_bt_col);
    let close_bt = $("<button></button>").click(
	() => { on_close_cb(); main_btn.remove(); });
    close_bt_col.append(close_bt);
    close_bt.addClass("close");
    close_bt.attr("aria-label", "close").attr(
	"title", "Click to remove").attr("tooltip");
    close_bt.html("&times;");
    row.append(close_bt_col);

    parent.append(main_btn);
}

function unselect_all(multisel_id) {
    // unselect all items from multiple selection field
    $(`#${multisel_id}`).val([]);
}

function select_all_from_multiselect(id) { 
    let values = []; 
    $(id).children().each((id, item) => { 
	values.push(item.value); 
    }); 
    $(id).val(values); 
}

function remove_sel_from_multiselect(id) {
    // remove selected items from a multiple selection list
    $(`${id}` + " option:selected").each(
    	(index, option) => $(option).remove()); 
}

function get_search_function(endpoint, success_fn) {
    return search_field_id => $(`#${search_field_id}`).keyup(() => {
    	let query = {"query": $(`#${search_field_id}`).val()};
    	get_ajax_fn(endpoint, query, success_fn)();
    });
}
