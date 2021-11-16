function add_searched_id(set) {
    return event => {
	set.push(event.currentTarget["id"]);
	// powinienem użyć funkcji/met. z jQuery:
	console.log(event.currentTarget.getAttribute("data-source"));
    }
}


function get_person_from_name_variant(variant_id, endpoint) {
    $.post(endpoint,
	   JSON.stringify({"id": variant_id}),
	   function() {})
}


function print_list(list, drop_down) {
    // niech najpierw sprawdza czy cokolwiek tam jest
    $(drop_down).empty();
    let list_item;
    for(item of list) {
	list_item = $("<div></div>").addClass(
	    "list-group-item list-group-item-action");
	if(item["source"]) {
	    list_item.attr("data-source", item["source"]);
	}
	list_item.attr("id", item["id"]);
	list_item.html(item["text"]);
	list_item.click(add_searched_id([]));
	$(drop_down).append(list_item);
    }
}


function get_filter_cb(input_name, fn_url, drop_down) {
    return () => $.ajax({
	url: fn_url,
	type: "POST",
	data: JSON.stringify({"query": $(input_name).val()}),
	datatype: "json",
	contentType: "application/json; charset=utf-8",
	success: list => print_list(list, drop_down)
	// fail: () => alert("Unable to contact server!") // nie działa
    });
}


function set_up_server_callbacks(callbacks) {
    for(callback of callbacks) {
	$(callback["input"]).keyup(get_filter_cb(
	    callback["input"], callback["url"], callback["drop_down"]))
    }
}


function search_criterion_component(parent, title, on_close_cb=() => {}) {
    // on_close_cb - callable invoked on component removal
    let main_btn = $("<div></div>").addClass(
	"btn btn-outline-info btn-sm");
    let row = $("<div></div>").addClass("row");
    let label_col = $("<div></div>").addClass("col").html(title);
    let close_bt_col = $("<div></div>").addClass("col");
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
    console.log(close_bt.parent());

    parent.append(main_btn);
}

// test
search_criterion_component(parent=$('#people-responsibilities-list'),
    title="test", on_close_cb=() => console.log('lbl1'));
