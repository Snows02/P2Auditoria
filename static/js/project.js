function changeState(id_lig, id_project) {
  val = $(`#${id_lig}`).val().replace('%', '');
  url = `/api/project/update/${id_project}/${id_lig}/${val}/`

  $.ajax({
    type: "POST",
    url: url,
    data: {},
    success: () => {}
  });
}

function uploadFile(idForm) {
  $(`#form-lig-${idForm}`).submit();
}
