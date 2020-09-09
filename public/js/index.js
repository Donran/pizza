// Creates a date variable with the current date
const dateNow = new Date();

// The map of all of the months with its corresponding number
let listOfMonths = {
    "januari": 1,
    "februari": 2,
    "mars": 3,
    "april": 4,
    "maj": 5,
    "juni": 6,
    "juli": 7,
    "augusti": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "december": 12,
}

// The first function that runs when the page loads
onload = (() => {
    getDaysUntil(document.getElementById("closedDays"));
});

/**
 * The function that gets and reorders the list passed to the function
 * @param {HTMLElement} listElement 
 */
function getDaysUntil(listElement) {
    // The list of all of the child nodes 
    let list = listElement.children;
    for (let index = 0; index < list.length; index++) {
        // The next date from the for loop as a string ex: january 8
        const dateString = list[index].children[0].innerHTML;

        // Initial variables
        let daysBetween = 0;
        let sameDay = false;

        // Splitting the dates into an array with month and year
        let dateSplit = dateString.split(" ");

        // Creates variables with the month/date numbers as value
        let monthNumber = listOfMonths[dateSplit[1]]
        let dateNumber = dateSplit[0];

        // Creates the same variables above but with the current month and date
        let monthNowNumber = dateNow.getMonth() + 1;
        let dayNowNumber = dateNow.getDate();

        let year = 0;
        if (monthNumber < monthNowNumber) {
            // When the number of the month is smaller than the current month number
            // We know that it's next year
            year = dateNow.getFullYear() + 1;
        } else if (monthNumber > monthNowNumber) {
            // When the number of the month is larger than the current month number
            // We know that it's this year
            year = dateNow.getFullYear();
        } else {
            // Same Month
            if (dateNumber < dayNowNumber) {
                // When the date is smaller than the current date
                // We know that it's next year
                year = dateNow.getFullYear() + 1;
            } else if (dateNumber > dayNowNumber) {
                // When the date is larger than the current date
                // We know that it's this year
                year = dateNow.getFullYear();
            } else {
                // Same day
                sameDay = true;
            }
        }
        if (!sameDay) {
            // Calculate the number of days left when the date isn't the current date
            let date = Date.parse(monthNumber + " " + dateNumber + " " + year);
            let deltaTime = new Date(date).getTime() - dateNow.getTime();
            daysBetween = Math.ceil(deltaTime / (1000 * 60 * 60 * 24));
        }
        // Sets the daysLeft attribute for each li element to its correct value
        list[index].setAttribute("daysLeft", daysBetween)
    }
    let childrenList = [];
    // Adds all of the listElements into a new array instead of using the listElement.children which is an HTMLCollection
    for (let index = 0; index < listElement.children.length; index++) {
        childrenList.push(listElement.children[index])
    }
    // Sorts the items by their individual daysLeft value
    childrenList.sort((item1, item2) => {
        return item1.getAttribute("daysLeft") - item2.getAttribute("daysLeft");
    });
    // Appends each element from the array to the HTML li
    childrenList.forEach(element => listElement.appendChild(element));
}