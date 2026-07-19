// GST Calculator & Invoice System
// Created by Thibakkathirravan H

function formatCurrency(value) {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency: "INR",
    minimumFractionDigits: 2
  }).format(value);
}

function calculateGST() {

  // Get values entered by the user
  const amount = parseFloat(document.getElementById("amount").value);
  const gstRate = parseFloat(document.getElementById("gstRate").value);
  const taxType = document.getElementById("taxType").value;

  // Validate taxable amount
  if (isNaN(amount) || amount < 0) {
    alert("Please enter a valid taxable amount.");
    return;
  }

  // Calculate total GST
  const totalGST = amount * (gstRate / 100);

  let cgst = 0;
  let sgst = 0;
  let igst = 0;

  // Intra-State: GST is divided into CGST and SGST
  if (taxType === "intra") {

    cgst = totalGST / 2;
    sgst = totalGST / 2;

    document.getElementById("cgstRow").style.display = "flex";
    document.getElementById("sgstRow").style.display = "flex";
    document.getElementById("igstRow").style.display = "none";

  }

  // Inter-State: Entire GST is IGST
  else {

    igst = totalGST;

    document.getElementById("cgstRow").style.display = "none";
    document.getElementById("sgstRow").style.display = "none";
    document.getElementById("igstRow").style.display = "flex";

  }

  // Calculate final invoice amount
  const grandTotal = amount + totalGST;

  // Display results
  document.getElementById("taxableResult").textContent =
    formatCurrency(amount);

  document.getElementById("cgstResult").textContent =
    formatCurrency(cgst);

  document.getElementById("sgstResult").textContent =
    formatCurrency(sgst);

  document.getElementById("igstResult").textContent =
    formatCurrency(igst);

  document.getElementById("gstResult").textContent =
    formatCurrency(totalGST);

  document.getElementById("totalResult").textContent =
    formatCurrency(grandTotal);
}

// Allow Enter key to calculate GST
document.getElementById("amount").addEventListener("keydown", function(event) {

  if (event.key === "Enter") {
    calculateGST();
  }

});
