// The map of all of the months with its corresponding number
let listOfMonths = [
    "januari",
    "februari",
    "mars",
    "april",
    "maj",
    "juni",
    "juli",
    "augusti",
    "september",
    "oktober",
    "november",
    "december"
];
let listOfZipCodes = [98139, 98140, 98142, 98138]

function isInViewport(node) {
  var rect = node.getBoundingClientRect()
  return (
    (rect.height > 0 || rect.width > 0) &&
    rect.bottom >= 0 &&
    rect.right >= 0 &&
    rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.left <= (window.innerWidth || document.documentElement.clientWidth)
  )
}

// The first function that runs when the page loads
$(document).ready(() => {
    // Sets display: none on elements that should only be visible without js running.
    $(".rm-on-js").css("display", "none");

    // Displays elements that uses js.
    $(".only-js").css("display", "block");


    $("#orderButton").on("click", () => toggleOverlayVisibility(true));

    $("#orderConfirmButton").on("click", () => getZipCodeFromInput());

    $("#orderInput").on("keyup", ev => {
        if(ev.key === "Enter") {
            ev.preventDefault();
            $("#orderConfirmButton").click();
        }
    });

    reorderListByClosestDate(new Date());

    $("body").on("keyup", ev => {
        if((ev.key === "Esc" || ev.key === "Escape") &&
        $("#orderOverlay").attr("data-state") == "visible") {
            ev.preventDefault();
            toggleOverlayVisibility(false);
        }
    });

    $(window).scroll(function() {
        var scrolled = $(window).scrollTop()
        $('.parallax').each(function(index, element) {
            var initY = $(this).offset().top
            var height = $(this).height()
            var endY  = initY + $(this).height()

            // Check if the element is in the viewport.
            var visible = isInViewport(this)
            if(visible) {
              var diff = scrolled - initY
              var ratio = Math.round((diff / height) * 100)
              $(this).css('background-position','center ' + parseInt(-(ratio * 1.5)) + 'px')
            }
        })
    });

});

/**
 * The function that gets and reorders the list passed to the function.
 */
function reorderListByClosestDate(date) {
    let strList = $(".closed-days").children().map((_, val) => val.children[0].innerText);

    let dates = strList.map((_, val) => {
        let dateString = val.split(" ");
        dateString[1] = listOfMonths.indexOf(dateString[1]);
        let newDate = new Date(date.getFullYear(), dateString[1], dateString[0]);
        if(newDate < date)
            newDate.setFullYear(newDate.getFullYear() + 1);

        return newDate;
    }).sort((a, b) => a - b);
  console.log(dates);
    $(".closed-days").html("");
    dates.each((_, val) => {
        let day = val.getDate();
        let month = listOfMonths[val.getMonth()];
        $(".closed-days").append("<li><span class='closed-day'>"+day+" "+month+"</span><span>Stängt</span></li>");
    });
}
/**
 * Toggles the visibility by switching the overlay display property while adding a few click event listeners to hide the overlay when clicking outside of the overlay
 * @param {Boolean} overlayBool If the overlay is visible or not
 */
function toggleOverlayVisibility(status = false) {
    let overlayDiv = $("#orderOverlay");
    overlayDiv.attr("data-state", status ? "visible" : "hidden");
    if (status) {
        $("#orderStatus").text("Skriv in ditt postnummer");
        $("#orderInput").val("");
        $('body').addClass("stop-scrolling");
        $(window).on("mousedown", ev => {
            ev.target == overlayDiv[0] ? toggleOverlayVisibility(false):null;
        });
        $("#orderCloseButton").on("click", (_) => toggleOverlayVisibility(false));
        $("#orderOverlay").css({ "display": "flex", "opacity": 1});
    } else {
        $('body').removeClass("stop-scrolling");
        overlayDiv.css("opacity", 0);
        setTimeout(() => {
            overlayDiv.css("display", "none");
            $("#orderStatus").removeClass();
        }, 150);
    }
}

/**
 * Gets the overlays input value and validates if it's a number and if it's a valid zip-code.
 * The overlay status element then shows if the zip-code is valid or not
 */
function getZipCodeFromInput() {
    let orderStatus = $("#orderStatus");
    orderStatus.removeClass();

    let inputValue = $("#orderInput").val();

    if (listOfZipCodes.indexOf(parseInt(inputValue)) > -1) {
        finalResult = "Vi levererar till dig";
        finalClass = "orderSuccess";
    } else if (inputValue == "") {
        finalResult = "Skriv in ditt postnummer";
        finalClass = "orderInfo";
    } else {
        finalResult = "Tyvärr kör vi inte ut inom detta område";
        finalClass = "orderFail";
    }
    orderStatus.text(finalResult);
    orderStatus.addClass(finalClass);
}

function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

