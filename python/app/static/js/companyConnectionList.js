const INVISIBLE_CLASS = "d-none";
const linkAddConnection = document.getElementById("linkAddConnection");
const linkEditConnection = document.getElementById("linkEditConnection");
const buttonCreateConnection = document.getElementById("buttonCreateConnection");
const buttonUpdateConnection = document.getElementById("buttonUpdateConnection");

linkAddConnection.addEventListener("click", function (event) {
  event.preventDefault();
  buttonCreateConnection.classList.remove(INVISIBLE_CLASS);
  buttonUpdateConnection.classList.add(INVISIBLE_CLASS);
});

function onClickLinkEditConnection(event, companyConnectionId) {
  event.preventDefault();
  companyId = document.getElementById("inputCompanyId").value;
  get_company_connection(companyId, companyConnectionId);
  buttonCreateConnection.classList.add(INVISIBLE_CLASS);
  buttonUpdateConnection.classList.remove(INVISIBLE_CLASS);
}

function get_company_connection(company_id, id) {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", `/company/${company_id}/connection/${id}`);
  xhr.send();
  xhr.responseType = "json";
  xhr.onload = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      const data = xhr.response.company_connection_form;
      console.log(data);
      document.getElementById("inputId").value = data.id;
      document.getElementById("inputConnectionDate").value = data.connection_date;
      document.getElementById("inputWay").value = data.way;
      document.getElementById("inputEmployee").value = data.employee;
      document.getElementById("inputContent").value = data.content;
      document.getElementById("inputRoute").value = data.route;
    } else {
      console.log(`Error: ${xhr.status}`);
    }
  };
}

function onClickLinkRemoveConnection(event, companyConnectionId) {
  event.preventDefault();
  companyId = document.getElementById("inputCompanyId").value;
  url = `/company/${companyId}/connection/delete/${companyConnectionId}`;
  document.getElementById("linkDeleteConnection").href = url;
}
