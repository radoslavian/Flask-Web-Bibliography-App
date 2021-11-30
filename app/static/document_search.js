function search_parameters_from_url(search_fields) {
    const urlParams = new URLSearchParams(window.location.search);
    function add_components(v, key) {
	if(search_fields.hasOwnProperty(key)) {

	    // podobne do add_searched_id
	    if(!search_fields[key]["ids_list"].has(v)) {
		search_fields[key]["ids_list"].add(v);
		$.post(search_fields[key]["url"], {"id": v},
		       title => search_criterion_component(
			   $(search_fields[key]["parent_component_id"]),
			   title, on_close_cb=() => search_fields[key][
			       "ids_list"].delete(v)))
	    }
	}
    }
    urlParams.forEach(add_components);
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
function print_search_results(results, list, root) {
    // quicksearch results in a selected section/list
    let list_item;
    for(result of results) {
	list_item = $("<a></a>").addClass("list-group-item");
	list_item.attr("href", root + 'id=' + result["id"]).attr(
	    "target", "_blank");
	list_item.html(result["text"]);
	list.append(list_item);
    }
}

var get_filter_cb = (
    input_name, fn_url, drop_down,
    parent, ids_list) => get_ajax_fn(
	fn_url,
	{"query": $(input_name).val()},
	list => print_list(
	    list[0], drop_down, parent, ids_list)
    );

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

var get_search_results = (
    endpoint, query, field, root, page=1) => get_ajax_fn(
	endpoint=endpoint,
	data={"query": query, "page": page},
	success_fn=results => {
	    print_search_results(results[0], $(field), root);
	    $(field + " + div a").off("click");
	    if(results[1]) {
		$(field + " + div a").click(
		    get_search_results(endpoint,
				       query, field, root, page=page+1));
	    }
	    else {
		$(field + " + div a").removeAttr("href");
	    }
	}
    );

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
