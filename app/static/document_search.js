function url_query_for(root) {
    return config_list => {
	let url = new URL(root);
	config_list.forEach(
	item => item["ids_list"].forEach(
	    id => url.searchParams.append(
		item["url_query_parameter"], id)));
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


function get_filter_cb(input_name, fn_url, drop_down,
		       parent, ids_list) {
    return () => $.ajax({
	url: fn_url,
	type: "POST",
	data: JSON.stringify({"query": $(input_name).val()}),
	datatype: "json",
	contentType: "application/json; charset=utf-8",
	success: list => print_list(list, drop_down, parent, ids_list)
    }).fail((jqXHR, status) => alert(
	`Error while processing the request: ${status}.`));
}


function set_up_server_callbacks(callbacks) {
    for(callback of callbacks) {
	$(callback["input"]).keyup(get_filter_cb(
	    callback["input"], callback["url"], $(callback["drop_down"]),
	    $(callback["parent_component_id"]), callback["ids_list"]));
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
