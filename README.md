# Charlie's Grillhouse

![Charlie's Grillhouse]()

Charlie’s Grillhouse is an imagined restaurant in New York.
The restaurant website is built for portfolio project 4 for Code Institute. The assignment is to build a full stack website using HTML, CSS, JAVASCRIPT, PYTHON and DJANGO with relational database MySQL or Postgres. Some features to include are; a date/time based bookingsystem and avoid double bookings. A multiple table occupancies and an option for cacellation.

You can visit the deployed website [here]().

---

## 1. Contents
1.	UX
    -	User Stories
    -	Wireframes
    -	Surface
2.	Features
    -	Existing Features
    -	Features left to Implement
3.	Technologies Used
4.	Testing
    -	Browsers
    -	Responsiveness / Mobile friendly
    -	W3C Validation
    -	User Story Testing
5.	Deployment
6.	Credits
    -	Content
    -	Code
    -	Media
    -	Acknowledgements

---

## 1. UX
The goal of this website is:
-	Provide potential customers with important information about the restaurant
-	Increase the awareness around the restaurant
-	Provide a possibility for customers to book a table online or by phone
-	Provide a possibility for customers to  organize an event at the restaurant 
-	Give visitors a possibility to see the menu online and have an impression of the restaurant

### User Stories
-	As a new/ returning customer I want to make a reservation online or by phone
-	As a customer I want the possibility to cancel my reservation
-	As a new customer I want to know about the restaurant concept, history, chef and food
-	As a new customer I want to see the restaurant’s social presence and what to expect
-	As a new/ returning customer I want to contact the restaurant about booking an event there
-	As a new customer I want to know where to find the restaurant
-	As an owner I want to avoid double bookings
-	As an owner I want to control the online bookings of the restaurant

### Wireframes
The wireframes were designed using [Balsamiq](https://balsamiq.com/).Layouts were created for mobile and desktop to assist the design decisions before coding. They're accessible in the following links:

**Desktop**

* [Home Page]()
* [Menu Page]()
* [Events Page]()
* [Chefs Page]()
* [Contact Page]()
* [Book a table Page]()

**Mobile**

* [Home Page]()
* [Menu Page]()
* [Events Page]()
* [Chefs Page]()
* [Contact Page]()
* [Book a table Page]()

### Surface
The colour palette that was used for this website was the green colour of the Brazilian flag with a medium dark shade of gray.
The medium shade of grey colour blends very good with a bright colour like the green that i used because it relates good to the restaurant which is a Brazilian Grillhouse.

Fonts used are:
* [Poppins] - for the body
* [Lobster] - for the headings
- Poppins is a geometric sans-serif typeface published by Indian Type Foundry in 2014. It was released as open-source and is available for free on Google Fonts.
- Lobster Font is the great script typeface that is considered as the bold and thick typeface that was released by the famous font foundry namely Impallari Type.This font comprised many different ligatures and alternates that are used to highlight the content and make the content more prominent ad this available for free.

---

## 2. Features
### Existing Features:
* **Navigation** - The navbar contains a topbar with the restaurants telephone number and opening times, and a header where the logo and the menu bar is with six links. They are all anchored to the homepage.
* **Hero section** - The Hero section contains a carousel with three slide images, with a welcome, a every saturday program and a every friday program. This to provide the user a quick program view that comes back every week.
*  **Home** - On the homepage you can read about the history of the restaurant and a why choose us section with also a link to a youtube video for the visitor to get an impression of the restaurant. There is a gallery with images of the restaurant and a testimonials section of people saying about their experience in the restaurant.
*  **Menu List** - Three menus have been provided covering all dishes available at the restaurant - Steaks, Desserts and Specials. The items include a description of the dish and pricing. The specials are showed with a image of the dish.
*  **Events** - There is a page where you can see which events to book at the restaurant with the details. There are three types of events to book, birthday parties, private parties and a dinner and movie night. There is also an Event Reservation Form that you can fill in to book a partie. You need to know fill in your name, email and phonenumber, the number of people, date and type of event. You will be contacted by the manager to discuss further details.
*  **Chefs** - There is a page where you can see who the grillchef, chef and restaurant manager are of Charlie's Grillhouse. They provide an image, title and social media of the team.
*  **Contact Form** - Visitors can contact the restaurant via the contact page using the contact form for any further information or queries. There is also a google map image where the restaurant is.
* **Online Booking Form** - Reservations can be made online.
*  **Footer** - The footer dislays links to the restaurants social media accounts, the restaurant logo and slogan.

### Features Left to Implement
There are no feautures left to implement.

---

## 3. Technologies Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * For structuring the site pages.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  * For styling the content of each page.

* [Bootstrap 4](https://getbootstrap.com/)
  * A restaurant template.

* [Javascript]()
  * Adding interactive behavior to web pages.

* [GitHub](https://github.com/)
  * Used for managing and storing my code.

* [Django]()
  * Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.

* [Heroku]() 
  * Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps.

* [Google Fonts](https://fonts.google.com/)
  * For linking fonts for use on the site.

* [Unsplash](https://unsplash.com/images)
  * For the images on the website

*  [Balsamiq](https://balsamiq.com/) 
  * used to create the project's wireframes.

*  [Gitpod](https://gitpod.io/) 
  * used to develop the website.

*  [Favicon](https://www.favicon-generator.org//)
  * used to create the icon from the design made with Canva.

*  [Am I Responsive?](http://ami.responsivedesign.is/)
  * used to show in a quick visual way the responsiveness of the site.

---

## 4. Testing
### Browsers
The site was tested across multiple browsers - Chrome, Safari, Firefox and Opera to ensure each page displayed correctly.
Browser compatibility was also tested using the Lambdatest App.

***Notes:***
* 

### Responsiveness / Mobile-Friendly
The site's reponsiveness was continuously monitored during the development stage using Chromes *Dev Tools*. Further testing was done using [Lighthouse]() which allowed for testing on additional devices - no errors were recorded.

### W3C Validation
All html pages were checked using [W3C Markup Validation](https://validator.w3.org/) and passed with no errors.

The CSS file was checked using [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) and passed with no errors.

### JavaScript Validation
All html pages were checked using []() and passed with no errors.

### User Story Testing

* As a new/ returning customer I want to make a reservation online or by phone
    * "Book A Table" link is immediately accesible on the home page via the navbar and call to action button. This button links to the booking section on the home page which holds a booking form will all necessary inputs to make a reservation.

* As a new customer I want to know about the restaurant concept, history, chef and food.
    * On the homepage you find a section about the history. The Chefs and menu pages are on separate pages when clicking on the navbar links.

* As a new customer I want to see the restaurant's social presence.
    * Social media icons are located on the site footer which is featured on every page. On the homepage you will find a gallery with images of the restaurant

* -	As a new/ returning customer I want to contact the restaurant 
    * A contact form is located on the contact page which is accessible from the navbar. 

* -	As a customer I want the possibility to cancel my reservation
    * 

* As a new customer I want to know about upcoming events held at the restaurant.
   * An event slide show is showing on the events page with all the information for customers to view. Each event has its own dedicated information. You can fill in the event reservation form to book an event with the restaurant manager.

* -	As a new customer I want to know where to find the restaurant.
    * On the contact page you can find a google map and telephone and email to contact the restaurant.

* -	As an owner I want to avoid double bookings.
    * 

* -	As an owner I want to control the online bookings, events, chefs section and menu list of the restaurant
    * There is an admin site at the backend with a login that gives you the oppertunity to make necessary changes.

---

## 5. Deployment

---

## 6. Credits
### Content
### Code
### Media
### Acknowledgements
