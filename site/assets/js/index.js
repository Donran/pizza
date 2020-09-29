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


    $(".order-confirm-button").on("click", () => getZipCodeFromInput());

    $(".zipcode-field input").on("keyup", ev => {
        if(ev.key === "Enter") {
            ev.preventDefault();
            $(".order-confirm-button").click();
        }
    });

    reorderListByClosestDate(new Date());

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

    $(".closed-days").html("");
    dates.each((_, val) => {
        let day = val.getDate();
        let month = listOfMonths[val.getMonth()];
        $(".closed-days").append("<li><span class='closed-day'>"+day+" "+month+"</span><span>Stängt</span></li>");
    });
}

/**
 * Gets the overlays input value and validates if it's a number and if it's a valid zip-code.
 * The overlay status element then shows if the zip-code is valid or not
 */
function getZipCodeFromInput() {
    let orderStatus = $(".order-status");
    orderStatus.removeClass();

    let inputValue = $(".zipcode-field input").val();

    if (listOfZipCodes.indexOf(parseInt(inputValue)) > -1) {
        finalResult = "Vi levererar till dig";
        finalClass = "order-success";
    } else if (inputValue == "") {
        finalResult = "Skriv in ditt postnummer";
        finalClass = "order-info";
    } else {
        finalResult = "Tyvärr kör vi inte ut inom detta område";
        finalClass = "order-fail";
    }
    orderStatus.text(finalResult);
    $(".zipcode-field span:last-child").addClass("order-status")
    orderStatus.addClass(finalClass);
}

function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

