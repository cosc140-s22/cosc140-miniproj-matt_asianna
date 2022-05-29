# COSC140 miniproject

## Team members

Matthew Rojas and Asianna Sample

## Miniproject descripton

Our project seeks to collect the Magic the Gathering cards for users and organize them alphabetically. The create a deck capability does not work yet. If you need cards for reference use the website EDHrec. Also, I have made an account that already has some cards to save you some time. There is also a theme to it. Let me know if you find the theme:  
 username: prof_sommers
 password: cardiff13

## Feedback

3.6/4.0

The model setup and relationships look good.  Overall site functions pretty well.  Grid layout looks great!

The main rough edge I think is the handling of the `addCard` functionality.  I think you should have either added a message to let the user know _what_ card got added to their collection, or to give them some other information about that in order to make it clear what happened.  I just typed the (random) word "stuff" and got `Stuffed Bear` but I feel like some more information for the user would be better.  Either that, or some slightly different process where the list of matching cards get shown and the user can select from those which one(s) to add to the collection.  Template inheritance wasn't used in your templates and, for best Django practices, should be.

Styling was quite spectacular -- really nice job on that!

