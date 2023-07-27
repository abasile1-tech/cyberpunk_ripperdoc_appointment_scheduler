# Cyberpunk Ripperdoc Appointment Scheduler

In the Cyberpunk genre of science fiction, ripperdocs are medical practitioners that can install cybernetic prostheses, called cyberware.

A customer (don’t worry about multiple users just yet, we can pretend this is already within a user being logged in) wants to be able to book an appointment to get chipped with the latest implant on the market. 


## MVP

A customer should be able to create a `Booking` with a name, date, time, and `Treatment`. A customer should be able to see all their scheduled treatments and click through on one to edit it or cancel it. A Treatment can just have a name.

## Extensions:

- Date and time could be handled as date type instead of as strings
- A treatment could have a length of time
- Could you try preventing double booking?