function download_csv(csv, filename) {
    var csvFile;var downloadLink;
    csvFile = new Blob([csv], {type: "text/csv"});
    downloadLink = document.createElement("a");
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);downloadLink.click();
}
function export_table_to_csv(html, filename) {
   var csv = [];var rows = document.querySelectorAll("table tr");
    for (var i = 0; i < rows.length; i++) {
      var row = [], cols = rows[i].querySelectorAll("td, th");
        for (var j = 0; j < cols.length; j++)
            row.push(cols[j].innerText);
      csv.push(row.join(","));
   }
    download_csv(csv.join("\n"), filename);
}
document.getElementById("csvdata").addEventListener("click", function () {
   var html = document.getElementById("table").outerHTML;
   export_table_to_csv(html, "table.csv");
});
function download_xls(xls, filename) {
    var excelFile;var downloadLink;
    excelFile = new Blob([xls], {type: "text/xls"});
    downloadLink = document.createElement("a");
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(excelFile);
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
    downloadLink.click();
}
function export_table_to_xls(html, filename) {
   var xls = [];var rows = document.querySelectorAll("table tr");
    for (var i = 0; i < rows.length; i++) {
      var row = [], cols = rows[i].querySelectorAll("td, th");
        for (var j = 0; j < cols.length; j++)
            row.push(cols[j].innerText);
      xls.push(row.join(","));
   }
    download_csv(xls.join("\n"), filename);
}
document.getElementById("btnexcel").addEventListener("click", function () {
    var html = document.getElementById("table").outerHTML;export_table_to_xls(html, "table.xls");
});
document.getElementById('pdfdata').addEventListener('click',exportPDF);

var specialElementHandlers = {
  '.no-export': function(element, renderer) {return true;}
};
function exportPDF() {
  var doc = new jsPDF('p', 'pt', 'a4');
  var source = document.getElementById('table').outerHTML;
  var margins = {top: 10,bottom: 10,left: 10,width: 595};
  doc.fromHTML(
    source,
    margins.left,
    margins.top, {
      'width': margins.width,
      'elementHandlers': specialElementHandlers
    },
    function(dispose) {
      doc.save('table.pdf');
    }, margins);
}
function printData()
{
   var divToPrint=document.getElementById("table");
   newWin= window.open("");
   newWin.document.write(divToPrint.outerHTML);
   newWin.print();newWin.close();
}
$('#btnprint').on('click',function(){printData();})