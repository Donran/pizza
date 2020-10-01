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

function handleHamburgerClicked(){
    $(".navbar").toggleClass("nav-bg");
}

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

var parallax_options = {};
var past_keys = [];
// The first function that runs when the page loads
$(document).ready(() => {
    // Sets display: none on elements that should only be visible without js running.
    $(".rm-on-js").css("display", "none");
    $(".nav-bg-no-js").removeClass("nav-bg-no-js");
    // Displays elements that uses js.
    $(".only-js").css("display", "block");

    $(".navbar-toggler-icon").on("click", handleHamburgerClicked);

    $("body").on("keyup", ev => {
        past_keys.push(ev.key);
        let winner = "PIZZATIME";
        if(past_keys.length >= winner.length) {
            if(past_keys.join("").toUpperCase().indexOf(winner) >= 0) {
                $("body").css("cursor", "url(./assets/cur3.png), auto");
                past_keys = [];
            }
        }
    });

    $(".order-confirm-button").on("click", () => getZipCodeFromInput());

    $(".zipcode-field input").on("keyup", ev => {
        if(ev.key === "Enter") {
            ev.preventDefault();
            $(".order-confirm-button").click();
        }
    });

    reorderListByClosestDate(new Date());

    // Remove animations to be added later if JS is enabled
    $("#find-us").find("hr").each(function() {
        $(this).removeClass("trigger-animation");
    });

    $('.parallax').each(function(_, __) {
        let name = Math.random().toString(36).substring(7);
        $(this).attr("data-parallax-id", name);
        let el = $(this);
        let id = el.attr("data-parallax-id");
        parallax_options[id] = {};
        parallax_options[id]["start_y"] = el.css("background-position-y");
        parallax_options[id]["speed_mul"] = parseInt(el.attr("data-parallax-multiplier") ? el.attr("data-parallax-multiplier") : 1);
    });

    $(window).scroll(handleScroll);
    handleScroll();
});

let animation_triggered = false;
function handleScroll(_, __) {
    let navbar = $('.navbar');
    let navbarHeight = navbar.height()
    if($(window).scrollTop() > navbarHeight){
        navbar.addClass("scrolled-1");
    }else{
        navbar.removeClass("scrolled-1");
    }
 
    let headerHeight = $('#header').height();
    if($(window).scrollTop() > headerHeight - navbarHeight){
        navbar.addClass("scrolled-2");
    } else {
        navbar.removeClass("scrolled-2");
    }

    let $findus = $("#find-us");
    if(isInViewport($findus[0]) && !animation_triggered) {
        animation_triggered = true;
        $findus.find("hr").each(function (){
            $(this).addClass("trigger-animation");
            console.log("asd");
        });
    }

    var scrolled = $(window).scrollTop();
    $('.parallax').each(function(_, __) {
        var initY = $(this).offset().top;
        var height = $(this).height();

        // Check if the element is in the viewport.
        var visible = isInViewport(this);
        if(visible) {
            let el = $(this);
            var opt = parallax_options[el.attr("data-parallax-id")];
            var diff = scrolled - initY;
            var ratio = Math.round((diff / height) * 100);
            $(this).css('background-position-y','calc('+opt["start_y"]+' + '+parseInt(-(opt['speed_mul']*ratio * 1.5)) + 'px)');
        }
    });
}

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

