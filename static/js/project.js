function changeState(id_lig, id_project) {
  val = $(`#${id_lig}`).val().replace('%', '');
  url = `http://127.0.0.1:8000/api/project/update/${id_project}/${id_lig}/${val}/`

  $.ajax({
    type: "POST",
    url: url,
    data: {},
    success: () => {}
  });
}
