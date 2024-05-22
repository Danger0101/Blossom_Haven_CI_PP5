# Blossom Haven

Welcome to Burger Blast, where flavor meets delight! We're a culinary haven dedicated to crafting unforgettable experiences through sensational bites and impeccable service. This is a theoretical burger restaurant based in London, UK.

The site allows users:

- 
- 


---

## Table of contents

- [User Stories & Sprints](#user-stories)

|        **[Features](#features)**        |                **[Testing](#testing)**                |      **[Lighthouse](#lighthouse)**      |
| :-------------------------------------: | :---------------------------------------------------: | :-------------------------------------: |
|            [Navbar](#navbar)            |          - [Manual Testing](#manual-testing)          |          [Index LH](#index-lh)          |
|             [Index](#index)             |    [Automated Testing](#automated-testing-scripts)    |          [About LH](#about-lh)          |
|          [About Us](#about-us)          | [Bugs & Issues Encounterd](#bugs--issues-encountered) |          [Admin LH](#admin-lh)          |
|           [Sign Up](#signup)            |                                                       |   [Reservations LH](#reservations-lh)   |
|           [Sign in](#sign-in)           |                                                       |           [Menu LH](#menu-lh)           |
|    [Change Details](#change-details)    |                                                       |         [Signup LH](#signup-lh)         |
|   [My Reservations](#my-reservations)   |                                                       |        [Sign in LH](#sign-in-lh)        |
| [Make Reservations](#make-reservations) |                                                       | [Change Details LH](#change-details-lh) |
| [Edit Reservations](#edit-reservations) |                                                       | [Contact Us LH](#contact-us-details-lh) |
|              [Menu](#menu)              |                                                       |                                         |
|       [Contact Use](#contact-us)        |                                                       |                                         |
|            [Footer](#footer)            |                                                       |                                         |
|       [Error Pages](#error-pages)       |                                                       |                                         |
|      [Django Admin](#django-admin)      |                                                       |                                         |

| **[Validation Testing](#validation-testing)** |    **[Setup](#setup)**    |                 **More**                 |
| :-------------------------------------------: | :-----------------------: | :--------------------------------------: |
|               [Python](#python)               |   [Database](#database)   |        [Wireframes](#wireframes)         |
|           [JavaScript](#javascript)           | [Cloudinary](#cloudinary) |           [Credits](#credits)            |
|                  [CSS](#css)                  | [Deployment](#deployment) | [Future Features](#future-feature-ideas) |
|                 [HTML](#html)                 |                           |                                          |
|             [Contrast](#contrast)             |                           |                                          |

## User Stories

- User stories were stored in "Burger Blast User Stories" project of my git hub. I was a little delayed in moving them around to completion so times are a bit off although stucture of sprints were followed throughout development.

** Sprint One**

- [Setup and Basic Functionality](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/1?closed=1)

| **User Stories** | **Needed for MVP** | Completed |
| ------------------------------------------------------------------------------------------------------------ | :----------------: | :-------: |
| As a user, I can visit the website and see a homepage with navigation to different sections. |        Yes         |    Yes    |
| As a user I can browse different arrangements of flowers | Yes | Yes |
| As a user I can view details of a specific flower bouquet so that I can make informed buying decisions. |     Yes     | Yes |

** Sprint Two**

- [Shopping Cart and Checkout](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/2?closed=1)

| **User Stories** | **Needed for MVP** | Completed |
| ---------------- | :----------------: | :-------: |
| As a user I can add items to my shopping cart so that I can purchase them later. |        Yes         |    Yes    |
| As a user I can view my shopping cart so that proceeded to check out or edit my order |        Yes         |    Yes    |
| As a User or Admin I can provide my shipping and payment information to complete the purchase. |        Yes         |    Yes    |


**Sprint Three**

- [Admin Panel and Product Management](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/3?closed=1)

| **User Stories** | **Needed for MVP** | Completed |
| ---------------  | :----------------: | :-------: |
| As an Admin, when I add, or edit a product to where it has no product image it will show a default no image |        Yes         |    Yes    |
| As a User, when a product has no image I want to see a default no image so that I know there are no images available for this product |        Yes         |    Yes    |
| As a Admin I can view and edit existing products so that it updates and users can see the changes |        Yes         |    Yes    |
| As a admin I can Add products so that users can see and purchase them |        Yes         |    Yes    |
| As a Admin I can Login to admin panel so that I can view admin panel |        Yes         |    Yes    |


**Sprint Four**

- [Inventory Management and Stock Tracking](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/4?closed=1)

| **User Stories**   | **Needed for MVP** | Completed |
| ------------------ | :----------------: | :-------: |
| As a user, I want to see if products are available before adding them to the cart. |         Yes         |    Yes     | 
| As an admin, I want to manage the inventory of flowers to ensure availability. |         Yes         |    Yes     | 

**Sprint Five**

- [Add-Ons and Reviews](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/5?closed=1)

| **User Stories**   | **Needed for MVP** | Completed |
| ------------------ | :----------------: | :-------: |
| As a Admin, I want to be able to delete inappropriate reviews to maintain integrity of the site. |         No         |    Yes     | 
| As a User, I want to see all reviews and be able to leave a review on products I have purchased so that myself and other users can make educated purchases. |         No         |    Yes     | 
| As an Admin, I want to manage the availability and pricing of add-on items so that they can only be added if they are in stock. |         No         |    Yes     | 
| As a user, I want to add additional items to compliment my purchase. |         No         |    Yes     | 


**Sprint Six**

- [User Account and Order History](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/6?closed=1)

| **User Stories**   | **Needed for MVP** | Completed |
| ------------------ | :----------------: | :-------: |
| As an admin, I want to view a summary of orders and manage order statuses so that I can ensure the smooth operation and get the jump on any issues that arise. |         Yes         |    Yes     | 
| As a user, I want to create an account to track my orders and save my shipping information for future purchases. |         Yes         |    Yes     | 

**Sprint Seven**

- [The Social Media and SEO](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/7?closed=1)

| **User Story or Action**   | **Needed for MVP** | Completed |
| ------------------ | :----------------: | :-------: |
| As a User or Admin, when i visit the site there is a footer with links to social media and any other relevant footer links. So that I can follow them accordingly. |         Yes         |    Yes     |
| robots.txt file. and sitemap.xm |         Yes         |    Yes     |
| Newsletter Signup |         Yes         |    Yes     |
| Create Products in live database |         Yes         |    Yes     |
| HTML SEO |         Yes         |    Yes     |
| Instagram page |         No         |    Yes     |
| Facebook Bussiness page |         Yes         |    Yes     |

(MVP = Minimal Viable Product)

**Sprint Eight**

- [Testing, fixing and refactoring, Extras](https://github.com/Danger0101/Blossom_Haven_CI_PP5/milestone/8?closed=1)

## Features

### Navbar

- 

![Navbar]()

---
### Index

- 

![Index Page]()

---

### Register

- Allows Users to signup/register for an account

![Signup Page]()

**Signup Email Customer**

![Signup Email Image]()

**Signup Email Restaurant**

![Signup Email Image]()

---

### Forgot Password

- 

![Forgot Password]()

**Forgot Password Email**

![Forgot Password Email Image)

---

### Chnage Password

-

![Change Password Page]()

**Change Password Email**

![Change Password Email]()

---

### Sign In

- Allows Users to sign into their accounts using username/Email and password.

![Sign In Page]()

---

### Profiles

- 

![Profile Page]()

**Change Details Email**

![Change shipping email image]()

---

### Reviews

- 

![Reviews Page]()

**Review Confirmation Email**

![Review confirmation email image]()

**Review Edit Confirmation Email**

![Change review email image]()

---

### Products List

- 

![Product List Page]()

---

### Products Details

- 

![Product Detail Page]()

---

### Add or Edit Products

**Add Product**

- 

![Add Product Page]()

**Edit Product**

- 

![Edit Product Page]()

---

### Facebook Page

-

![Facebook Screenshot]()

---

### Instagram Page

-

![Instagram Screenshot]()

---

### footer

- Links to Social Sites, Legal, and Newsletter signup

![Image of footer]()

---

### Error Pages

**400**

![400 html error]()

**403**

![403 html error](./staticfiles/images/feature_images/403_msg.png)

**404**

![404 html error](./staticfiles/images/feature_images/404_page.png)

**500**

![500 html error](./staticfiles/images/feature_images/500_page.png)

### Django Admin

- Django admin is a powerful tool designed to make managing a website easier for staff members. It provides a user-friendly interface where staff can easily add, edit, or delete content without needing technical skills. Staff members can log in and access a dashboard that gives them control over various aspects of the website, such as managing user accounts, updating product listings, posting articles, and more. The admin panel organizes information neatly, allowing staff to navigate through different sections effortlessly. It's like having a control center for the website, making it simple for staff members to keep everything running smoothly and up-to-date.

![Admin login image](./staticfiles/images/feature_images/admin/admin_login_page.png)

![Admin site logged in image](./staticfiles/images/feature_images/admin/admin_main_page.png)

**Django admin_interface and colorfield**

- Lightly experimented but setteled quickly with the current theme this was a pip package I found that so far I really like.

![Theme main page](./staticfiles/images/feature_images/admin/admin_theme_page.png)

![Theme edit page](./staticfiles/images/feature_images/admin/admin_theme_edit_page.png)

**Meals**

- Allows admins to view, create, edit, and delete meals as needed.

![Main admin meals](./staticfiles/images/feature_images/admin/admin_meals_page.png)

![Make or edit admin meals](./staticfiles/images/feature_images/admin/admin_meals_edit_page.png)

**Reservations**

- Allows admins to view, create, edit, and delete reservations as needed.

![Main admin reservations](./staticfiles/images/feature_images/admin/admin_reservation_page.png)

![Make or edit admin reservations](./staticfiles/images/feature_images/admin/admin_reservation_edit_page.png)

![Action Email Sending](./staticfiles/images/feature_images/admin_reservation_send_emails.png)

**Accounts User**

- Allows admins to view, create accounts, and/or edit account details as needed.

![Main user accounts](./staticfiles/images/feature_images/admin/admin_user_page.png)

![Make user accounts](./staticfiles/images/feature_images/admin/admin_user_make_page.png)

![Edit user accounts](./staticfiles/images/feature_images/admin/admin_user_edit_page.png)

![Action Email Sending](./staticfiles/images/feature_images/admin_user_send_emails.png)

**Accounts Group**

- Allows admin's to view, create, or deltete group catigories. Used to set a permissions easily to certian accounts and change them as needed based on whats set by superusers or users with permissions.

![Accounts main group page](./staticfiles/images/feature_images/admin/admin_group_page.png)

![Accounts edit group page](./staticfiles/images/feature_images/admin/admin_group_edit_page.png)

---

## Testing

### Manual Testing

|                 What test was completed                  | Passed? |           Other information            |
| :------------------------------------------------------: | :-----: | :------------------------------------: |
|               Make a super user (Manager)                |   Yes   |                                        |
|                  Make a staff member ()                  |   Yes   |                                        |
| Sign up as a customer/user (Jane.Doe, John.Doe, Jon.Doe) |   Yes   |                                        |
|               Login to site as a superuser               |   Yes   |                                        |
|                 Login to site as a staff                 |   Yes   |                                        |
|             Login to site as a customer/user             |   Yes   |                                        |
|              Log out of site as a superuser              |   Yes   |                                        |
|                Log out of site as a staff                |   Yes   |                                        |
|            Log out of site as a customer/user            |   Yes   |                                        |
|          Login to Django admin as customer/user          |   Yes   |   Only staff can log in successfully   |
|            Login to Django admin as superuser            |   Yes   |   Only staff can log in successfully   |
|              Login to Django admin as staff              |   Yes   |   Only staff can log in successfully   |
|           Log out of Django admin as superuser           |   Yes   |                                        |
|             Log out of Django admin as staff             |   Yes   |                                        |
|     Successfully change any users data on main site      |   Yes   |                                        |
|     Successfully change any users data on admin site     |   Yes   |   Can only be done as a satff member   |
|           Make reservation as a customer/user            |   Yes   |                                        |
|             Make reservation as a superuser              |   Yes   |                                        |
|                Make reservation as staff                 |   Yes   |                                        |
|           Edit reservation as a customer/user            |   Yes   |                                        |
|             Edit reservation as a superuser              |   Yes   |                                        |
|                Edit reservation as staff                 |   Yes   |                                        |
|          Delete reservation as a customer/user           |   Yes   |                                        |
|            Delete reservation as a superuser             |   Yes   |                                        |
|               Delete reservation as staff                |   Yes   |                                        |
|      Edit reservation as a superuser on admin site       |   Yes   |                                        |
|         Edit reservation as staff on admin site          |   Yes   |                                        |
|     Delete reservation as a superuser on admin site      |   Yes   |                                        |
|        Delete reservation as staff on admin site         |   Yes   |                                        |
|     Check no more then 14 day's into future booking      |   Yes   | Unable to book outside of constraints  |
|      Check booking time frame ends 2h befor closing      |   Yes   | Unable to book outside of constraints  |
|        Multiple users can book same day and time         |   Yes   |                                        |
|     Cant book over 20 people in a single reservation     |   Yes   | Added contraint to reduce cancelations |
|      Booking 20 or less returns value of 20 or less      |   Yes   |                                        |
|      Booking 21 or more returns value of 20 no more      |   Yes   |                                        |
|        Admin Action send_reservation_confirmation        |   Yes   |             Email Recieved             |
|           Admin Action send_reservation_update           |   Yes   |             Email Recieved             |
|          Admin Action send_cancel_email_to_user          |   Yes   |             Email Recieved             |
|             Admin Action send_welcome_email              |   Yes   |             Email Recieved             |
|           Admin Action send_admin_notification           |   Yes   |             Email Recieved             |
|           Admin Action send_edit_notification            |   Yes   |             Email Recieved             |
|          Admin Action send_delete_notification           |   Yes   |             Email Recieved             |

### Automated Testing Scripts

- Must use local Django database for the django tests

|             Script             | Passed? |  Other information  |
| :----------------------------: | :-----: | :-----------------: |
|         email_test.py          |   Yes   |   Email Recieved    |
|        test_menu_add.py        |   Yes   | No redirect testing |
|      test_menu_remove.py       |   Yes   | No redirect testing |
| tests_authentication_basics.py |   Yes   |        None         |

|             Script             |                          Terminal line                           |
| :----------------------------: | :--------------------------------------------------------------: |
|         email_test.py          |                       Ran as a python file                       |
|        test_menu_add.py        |            python manage.py test meals.test_menu_add             |
|      test_menu_remove.py       |           python manage.py test meals.test_menu_remove           |
| tests_authentication_basics.py | python manage.py test authentication.tests_authentication_basics |

### Bugs & Issues Encountered

| Bugs/Issues Encountered                                                                    |                        How problem was fixed or ammended                         | Fixed? |
| ------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------: | :----: |
| Enabling user sign-up with email verification due to email sending issues.                 |                 Removed the verification prior to making it live                 |  Yes   |
| Getting images to load into the menu items                                                 |              Removed due to time constraint may add back in future               |  Yes   |
| Getting static files to work as intended                                                   |         Tried different code variations, settled on one store location.          |  Yes   |
| Getting static file js to load for menu selection                                          |              added it in script tags instead as its a small script               |  Yes   |
| Users could set any date or time in making reservation whether future or past              | JS and Python ensure bookings within opening hours, No same-day online bookings. |  Yes   |
| If a user attempts to book two reservations for the same date and time, it won't be saved. |                  Removed the section of code causing the issue                   |  Yes   |
| Show password disapearing on certian browsers such as chrome                               |                               Not fixed currently                                |   No   |
| Edit reservation not populating the time due to the way field is set up                    |              <p> fields added to alert user to original reservation              |   No   |

---

## Validation Testing

### Python

All Scripts checked with [PEP8 Code institute](https://pep8ci.herokuapp.com/)

|                   **File**                    | **Line** | **Errors or Warnings** |
| :-------------------------------------------: | :------: | :--------------------: |
|                 about\apps.py                 |   All    |          None          |
|                about\forms.py                 |   All    |          None          |
|                 about\urls.py                 |   All    |          None          |
|                about\views.py                 |   All    |          None          |
|            authentication\apps.py             |   All    |          None          |
|            authentication\forms.py            |   All    |          None          |
| authentication\tests_authentication_basics.py |   All    |          None          |
|            authentication\urls.py             |   All    |          None          |
|            authentication\views.py            |   All    |          None          |
|             burger_blast\asgi.py              |   All    |          None          |
|           burger_blast\settings.py            |   All    |          None          |
|             burger_blast\urls.py              |   All    |          None          |
|             burger_blast\wsgi.py              |   All    |          None          |
|                 email_test.py                 |   All    |          None          |
|                   manage.py                   |   All    |          None          |
|                meals\admin.py                 |   All    |          None          |
|                 meals\apps.py                 |   All    |          None          |
|                meals\models.py                |   All    |          None          |
|            meals\test_menu_add.py             |   All    |          None          |
|           meals\test_menu_remove.py           |   All    |          None          |
|                 meals\urls.py                 |   All    |          None          |
|                meals\views.py                 |   All    |          None          |
|             reservation\admin.py              |   All    |          None          |
|              reservation\apps.py              |   All    |          None          |
|             reservation\forms.py              |   All    |          None          |
|             reservation\models.py             |   All    |          None          |
|              reservation\urls.py              |   All    |          None          |
|             reservation\views.py              |   All    |          None          |

## Javascript

- All my custom js scripts were run though [jshint](https://jshint.com/).

**reservation_checks.js**

![reservation_checks.js; js check](./staticfiles/images/js_checks/reservation_script_check.png)

**meals.js**

![meals.js; js check](./staticfiles/images/js_checks/menu_script_check.png)

**arrows.js**

![arrows.js; js check](./staticfiles/images/js_checks/arrows_script_check.png)

### CSS

- checked my custom css with [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) direct input; completed with no issues found.

![css verification img](./staticfiles/images/css_verification_img.png)

### HTML

- checked all non logged in pages as html urls and logged in pages as raw html with [W3 HTML Validator](https://validator.w3.org/) on all pages with no errors or warnings.

**Index**

![Index HTML w3 Validation Image](./staticfiles/images/html_checks/index_html_check.png)

**About**

![About Us HTML w3 Validation Image](./staticfiles/images/html_checks/about_html_check.png)

**Menu**

![Menu HTML w3 Validation Image](./staticfiles/images/html_checks/menu_html_check.png)

**Contact Us**

![Contact Us HTML w3 Validation Image](./staticfiles/images/html_checks/contact_us_html_check.png)

**Login**

![Login HTML w3 Validation Image](./staticfiles/images/html_checks/login_html_check.png)

**Sign Up**

![Signup HTML w3 Validation Image](./staticfiles/images/html_checks/sign_up_html_check.png)

**My Reservation**

![My Reservation HTML w3 Validation Imag](./staticfiles/images/html_checks/my_reservations_html_check.png)

**Edit Reservatoin**

![Edit Reservation HTML w3 Validation Imag](./staticfiles/images/html_checks/edit_reservations_html_check.png)

**Make Reservatoin**

![Make Reservation HTML w3 Validation Imag](./staticfiles/images/html_checks/make_reservations_html_check.png)

**Change Details**

![Change details HTML w3 Validation Imag](./staticfiles/images/html_checks/change_details_html_check.png)

### Contrast

- Checked all non logged in pages with [A11Y contrast checker](https://color.a11y.com/) Cameback with no issues.

**Index**

![Contrast checker index Image](./staticfiles/images/contrast_checks/index_page.png)

**About Us**

![Contrast checker about us Image](./staticfiles/images/contrast_checks/about_page.png)

**Menu**

![Contrast checker menu Image](./staticfiles/images/contrast_checks/menu_page.png)

**Contact Us**

![Contrast checker contact us Image](./staticfiles/images/contrast_checks/contact_us_page.png)

**Login**

![Contrast checker login Image](./staticfiles/images/contrast_checks/login_page.png)

**Sign Up**

![Contrast checker sign up Image](./staticfiles/images/contrast_checks/sign_up_page.png)

## Lighthouse

### Index LH

**Chrome lighthouse desktop**

![Screencap index lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/Index_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap index lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/Index_lh_mobile.png)

### About LH

**Chrome lighthouse desktop**

![Screencap about lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/aboutus_lh_desktop.png)

**Chrome mobile lighthouse**

![Screencap about lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/aboutus_lh_mobile.png)

### Admin LH

**Admin Login lighthouse desktop**

![Screencap admin login lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/admin_signin_lh_desktop.png)

**Admin Login mobile lighthouse**

![Screencap admin login lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/admin_signin_lh_mobile.png)

**Admin site lighthouse desktop**

![Screencap admin site lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/admin_lh_desktop.png)

**Admin site mobile lighthouse**

![Screencap admin site lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/admin_lh_mobile.png)

### Reservations LH

**Edit Reservation lighthouse desktop**

![Screencap edit reservationt lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/edit_reservations_lh_desktop.png)

**Edit Reservation mobile lighthouse**

![Screencap edit reservation lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/edit_reservations_lh_mobile.png)

**Make Reservation lighthouse desktop**

![Screencap make reservation lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/make_reservations_lh_desktop.png)

**Make Reservation mobile lighthouse**

![Screencap make reservation lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/make_reservations_lh_mobile.png)

**My Reservation lighthouse desktop**

![Screencap my reservation lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/my_reservations_lh_desktop.png)

**My Reservation mobile lighthouse**

![Screencap my reservation lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/my_reservations_lh_mobile.png)

### Menu LH

**Lighthouse desktop**

![Screencap menu lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/menu_lh_desktop.png)

**Lighthouse mobile**

![Screencap menu lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/menu_lh_mobile.png)

### Signup LH

**Lighthouse desktop**

![Screencap signup lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/signup_lh_desktop.png)

**Lighthouse mobile**

![Screencap singup lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/signup_lh_mobile.png)

### Sign In LH

**ighthouse desktop**

![Screencap sign in lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/signin_lh_desktop.png)

**Lighthouse mobile**

![Screencap sign in lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/signin_lh_mobile.png)

### Change Details LH

**lighthouse desktop**

![Screencap change details lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/update_details_lh_desktop.png)

**Lighthouse mobile**

![Screencap change details lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/update_details_lh_mobile.png)

### Contact Us Details LH

**lighthouse desktop**

![Screencap contact us lighthouse desktop](./staticfiles/images/burger_blast_lighthouse/contact_lh_desktop.png)

**Lighthouse mobile**

![Screencap contact us lighthouse mobile](./staticfiles/images/burger_blast_lighthouse/contact_lh_mobile.png)

---

## Setup

### Database

**Seting Up Database**

1. Go to [elephantsql](https://customer.elephantsql.com/login)
2. Make an account or sign in (I used my GitHub account)
3. Once logged in hit the "+ Create New Instance"

![elephantsql loggedin page](./staticfiles/images/esql_img/esql_loggedin_page.png)

4. Set up a name for the plan.
5. Select version for the plan.
6. **Optional** Add any tags if you wish
7. Hit "select region" button

![elephantsql Setup Paln page](./staticfiles/images/esql_img/esql_plan_setup_page.png)

8. Select a Data Center.
9. Once chosen hit the "Review" button

![elephantsql Data Center page](./staticfiles/images/esql_img/esql_select_region_page.png)

10. If all looks correct hit "Create Instance"

![elephantsql Conrifm page](./staticfiles/images/esql_img/esql_confirm_page.png)

11. Now you have your database set up all that is left is linking it to django project.
12. URL has a copy button hit this to copy your URL

![elephantsql Data Base page](./staticfiles/images/esql_img/esql_db_page.png)

12. Now you need to put this in your env file for the project or in your heroku config variables

**Heroku Cofig Variables**
| Key | Value |
|:---:|:-----:|
| DATABASE_URL | postgres database url |

- In the .env put it as "DATABASE_URL=your.database.url.HERE"

13. Now its linked to your project make sure to run the command to migrate all the models into your database as it is currently empty.

- Make migrations if you made any recent changes to the database models.

python manage.py makemigrations

- Migrate to move all the changes into your database.

python manage.py migrate

- There are more and other varriatons with diffrent useses [Click here to learn more (Django 5.0)](https://docs.djangoproject.com/en/5.0/topics/migrations/)

14. Now that migration is completed you are all set.
15. If you recieved an error please sort this out and then try again.

**Visualization of Databae**

![Data Base Visiualization](./staticfiles/images/database_models_visualization.png)

- I was able to make this using [django-extensions](https://pypi.org/project/django-extensions/) and [graphviz](https://django-extensions.readthedocs.io/en/latest/graph_models.html)

**Broken apart visuals**

![Main Data Visiualization](./staticfiles/images/db_visualization/main_data.png)

![Admin Interface Data Visiualization](./staticfiles/images/db_visualization/admin_interface.png)

![Meals Data Visiualization](./staticfiles/images/db_visualization/meals_data.png)

![Session Data Visiualization](./staticfiles/images/db_visualization/session_data.png)

---

### Cloudinary

**Creating a Cloudinary Account**

1. **Sign Up for Cloudinary:** Go to [Cloudinary's website](https://cloudinary.com/) and sign up for a new account.
2. **Verify Your Email:** Follow the instructions in the email sent to you to verify your email address.

**Integrating Cloudinary with Django**

1. **Install Cloudinary Library:** Run the following command in your terminal to install the Cloudinary Python library:

   |    run in terminal     |
   | :--------------------: |
   | pip install cloudinary |

2. **Configure Settings:** In your Django project's settings.py file, add the following configurations:

   **.env**

|              Line to enter               |
| :--------------------------------------: |
|    CLOUDINARY_API_KEY = Api key value    |
| CLOUDINARY_API_SECRET = Api secret value |
| CLOUDINARY_CLOUD_NAME = Cloudinary Name  |

(Replace all after **"="** with your information)

**Heroku Cofig Variables**

|          Key          |      Value       |
| :-------------------: | :--------------: |
|  CLOUDINARY_API_KEY   |  Api key value   |
| CLOUDINARY_API_SECRET | Api secret value |
| CLOUDINARY_CLOUD_NAME | Cloudinary Name  |

(Replace all **Values** with your information)

3. **Set Up Cloudinary Storage Backend:** Add the following line to settings.py to use Cloudinary as the storage backend for media files:

|                             Add to settings.py                             |
| :------------------------------------------------------------------------: |
| DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage' |

4. **Accessing Cloudinary URLs:** Whenever you upload media files in your Django application, they will automatically be stored in Cloudinary. You can access the URLs of these files to display them in your application.

5. **Optional: Resize and Manipulate Images:** Cloudinary provides various transformation options for images. You can resize, crop, and apply filters to images using Cloudinary's URL-based transformations.

6. **Testing Integration:** Upload a sample media file through your Django application and verify that it gets stored in Cloudinary.

7. **Further Customizations:** Explore [Cloudinary's documentation](https://cloudinary.com/documentation) for more advanced features and customizations, such as video processing, secure URLs, and transformation options.

8. **Congradulations you should be all set up**

---

### Deployment

Used Heroku to deploy the website. You can [Visit Live Site by clicking here](https://burger-blast-ci-2024-63403f4a3896.herokuapp.com/)

#### How to deploy to heroku:

1. **Run Migrations:** Once your project is deployed, you'll need to run any pending database migrations. You can do this using Heroku's web-based console or by running commands in your local terminal.
2. **Create a Superuser:** If your project uses Django's admin interface, you may want to create a superuser account on Heroku. You can do this by accessing your app's shell through the Heroku dashboard and running the createsuperuser command.
3. **Create a Heroku Account:** If you haven't already, sign up for a Heroku account at heroku.com.
4. **Prepare Your Django Project:** Ensure your Django project is properly configured for deployment. This includes setting up a requirements.txt file listing all dependencies and a Procfile specifying the command to start your application.
5. **Install Gunicorn:** Gunicorn is a WSGI HTTP server for Python. You'll need to install it via pip: "pip install gunicorn"
6. **Create a Procfile:** In the root directory of your project, create a file named Procfile (without any file extension) and add the following line: web: "web: gunicorn burger_blast.wsgi:application"
7. **Update Django Settings:** Ensure your Django settings.py file is configured to work in a production environment. This includes setting DEBUG = False and adding Heroku's domain to the ALLOWED_HOSTS list.
8. **Create a requirements.txt File:** Generate a requirements.txt file listing all Python dependencies your project needs. You can create it by running: "pip freeze > requirements.txt"
9. **Create a Heroku App:** Go to the Heroku dashboard and create a new app. Choose a unique name for your app.
10. **Link GitHub Repo:** Under deploy tab in the settings link your GitHub repository.
11. **Set Up Environment Variables:** Now under settings tab set any necessary environment variables for this django project. See chart below for needed key and values.

**Heroku Cofig Variables**

|          Key          |               Value               |
| :-------------------: | :-------------------------------: |
| DISABLE_COLLECTSTATIC |                 1                 |
|     DATABASE_URL      |       postgres database url       |
|   DJANGO_SECRET_KEY   | Django secret key for the project |
|   SENDGRID_API_KEY    |         sendgrid api key          |
|  CLOUDINARY_API_KEY   |           Api key value           |
| CLOUDINARY_API_SECRET |         Api secret value          |
| CLOUDINARY_CLOUD_NAME |          Cloudinary Name          |

(Replace all **Values** with your information)

12. **Deploy Your Project:** Back under deploy tab on Heroku scroll down to manual deploy and choose the branch you wish to deploy and hit button "Deploy Branch" wait for the success and trouble shoot if needed.

## Technology used

- HTML
- CSS
- Fontawesome
- Google Fonts
- Visual Studios Code (VSCode)
- Github
- Git
- Gyzo
- mspaint
- Github Desktop App
- Cloudinary
- Python
- Django
- Django-extensions
- fotor (AI Image generator)
- Logo designed by [app logo site](https://app.logo.com/login)

## Wireframes

### Admin Page

- Ended up going with a pre built one from ![django-admin-interface](https://pypi.org/project/django-admin-interface/0.6.0/) "pip install django-admin-interface"

![Image for admin page wireframe](staticfiles/images/wireframes/admin_page.png)

### Landing Page

![Image for admin page wireframe](staticfiles/images/wireframes/landing_page.png)

### Menu

![Image for admin page wireframe](staticfiles/images/wireframes/menu_page.png)

### Make/Edit Reservations

![Image for admin page wireframe](staticfiles/images/wireframes/reservation_and_edit_reservastion_page.png)

## Credits

**Images**

![websitebackground Actual Image](./staticfiles/images/background_burger_two.jpg)

- Website Background Image by [fotor:](https://www.fotor.com/)

- Logo designed by [app logo](https://app.logo.com/)

**More Credits**

- My wife who’s been supper supportive of this change in career for me and just being out right amazing we will get her into this one way or another I am sure.

- Code Institute for providing an excellent accelerated learning platform worth every penny.

---

## Future feature ideas

|              Feature Ideas               |    Why Not Implimented    |
| :--------------------------------------: | :-----------------------: |
|               Reviews page               |       Nice to have        |
|            Email verification            |       Nice to have        |
|          Users Delete accounts           |       Nice to have        |
|          Reset/Forgot Password           |       Nice to have        |
|        Online Ordering/Deliveries        |       Nice to have        |
|          Better looking emails           |       Nice to have        |
|  Auto admin site emails upon task save   |       Nice to have        |
| Link socials to restaurant (if launched) | Needed if real restaurant |
