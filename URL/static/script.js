// Function to open the pop-up and display the generated URL
function openPopup(url) {
    var popupContainer = document.getElementById("popupContainer");
    var generatedUrlElement = document.getElementById("generatedUrl");
    generatedUrlElement.textContent = url; // Set the generated URL
  
    popupContainer.style.display = "block"; // Display the pop-up
  }
  
  // Function to close the pop-up
  function closePopup() {
    var popupContainer = document.getElementById("popupContainer");
    popupContainer.style.display = "none"; // Hide the pop-up
  }
  
  // Example usage: Replace 'yourGeneratedUrl' with the actual generated URL
  var generatedUrl = '{{shortenurl}}';
  openPopup(generatedUrl);
  