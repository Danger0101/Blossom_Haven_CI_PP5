# Blossom Haven

Welcome to Blossom Haven, where beauty blooms in every petal! We're a floral haven dedicated to crafting unforgettable experiences through exquisite arrangements and impeccable service. Based in London, UK, we bring the charm of fresh flowers to your doorstep.

The site allows users:

- Browse a wide selection of stunning floral arrangements for every occasion
- To easily place orders for delivery.
- To create and manage user profiles for a personalized experience.
- To read and leave reviews on our products and services.
- To follow us on social media for the latest updates and inspirations.
- And more!


---

## Table of contents

- [User Stories & Sprints](#user-stories)
- [Marketing Plan](#Marketing-Plan)

| **[Features](#features)**                      |
| :--------------------------------------------: |
| [Navbar](#navbar)                              |
| [Index](#index)                                |
| [Register](#Register)                          |
| [Sign in/out](#sign-in-and-out)                |
| [Profiles](#Profiles)                          |
| [Reviews](#Reviews)                            |
| [Products List](#Products-List)                |
| [Products Details](#Products-Details)          |
| [Add & Edit Products](#Add-or-Edit-Products) |
| [Facebook Page](#Facebook-Page)                |
| [Instagram Page](#Instagram-Page)              |
| [Footer](#Footer)                              |
| [Error Pages](#error-pages)                    |
| [Django Admin](#django-admin)                  |

|               **[Testing](#testing)**                 |
| :---------------------------------------------------: |
| [Manual Testing](#manual-testing)                     |
| [Bugs & Issues Encounterd](#bugs--issues-encountered) |

| **[Validation Testing](#validation-testing)** | 
| :-------------------------------------------: |
|               [Python](#python)               |
|           [JavaScript](#javascript)           |
|                  [CSS](#css)                  |
|                 [HTML](#html)                 |
|             [Contrast](#contrast)             |

| **[Lighthouse](#Lighthouse)** |
| :---------------------------: |
| [Index LH](#Index-LH) |
| [Products LH](#Products-LH) |
| [Reviews LH](#Reviews-LH) |
| [Cart LH](#Cart-LH) |
| [Checkout LH](#Checkout-LH) |
| [Profiles LH](#Profiles-LH) |
| [Django Alltuh LH](#Django-Alltuh-LH) |

|    **[Setup](#setup)**      |
| :-------------------------: |
|   [Database](#database)     |
| [Cloudinary](#cloudinary)   |
| [Deployment](#deployment)   |
| [Email Setup](#Email-Setup) |

|                 **More**                 |
| :--------------------------------------: |
|        [Wireframes](#wireframes)         |
|           [Credits](#credits)            |
| [Future Features](#future-feature-ideas) |

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

---

[Back to table of contents](#Table-of-contents)

---

## Marketing Plan

### Social Media Marketing

**Facebook**

1. Create Engaging Content
- Post high-quality images of your floral arrangements regularly.
- Share behind-the-scenes content to show the process of creating your arrangements.
- Post customer testimonials and user-generated content.
- Use Facebook Stories to share daily updates and limited-time offers.

2. Leverage Facebook Groups
- Join local community groups and participate in discussions, subtly promoting your business when relevant.

3. Run Contests and Giveaways
- Host contests where participants need to like, share, and comment on your posts for a chance to win a free floral arrangement.

4. Engage with Your Audience
- Respond promptly to comments and messages.
- Ask questions in your posts to encourage interaction.
- Host live Q&A sessions to engage directly with your audience.

**Instagram**

1. Optimize Instagram Profile
- Ensure bio clearly describes your business and includes a link to your website.
- Use a consistent profile picture (logo) for brand recognition.

2. Create Visually Appealing Content
- Post high-quality photos and videos of your floral arrangements.
- Use Instagram Stories to share daily updates and behind-the-scenes content.
- Use Instagram Reels to showcase quick tutorials, floral arrangement ideas, or customer stories.

3. Use Hashtags Strategically
- Use a mix of popular and niche hashtags to increase your reach. Examples include #Florist, #FlowerDelivery, #LondonFlorist, #BlossomHaven, etc.
- Create a branded hashtag (#BlossomHaven) and encourage customers to use it when they post their own photos.

4. Engage with Your Community
- Like and comment on posts from users who use your hashtags or tag you.
- Follow relevant accounts and engage with their content.
- Host Instagram Live sessions for real-time interaction with your audience.

5. Run Contests and Giveaways
- Similar to Facebook, host Instagram contests where participants need to follow your account, like your post, and tag friends to enter.

**Search Engine Optimization (SEO)**

1. Keyword Research
- Identify relevant keywords that potential customers are using to search for florists and floral arrangements in London. Use tools like Google Keyword Planner, Ahrefs, or Ubersuggest.

2. On-Page SEO
- Optimize your website’s content with the identified keywords, ensuring they appear in titles, headers, meta descriptions, and throughout your content.
- Ensure your website is mobile-friendly and has a fast loading speed.

3. Content Marketing
- Start a blog on your website where you can post articles related to flowers, floral arrangements, care tips, and occasion-specific floral advice.
- Create high-quality, informative content that answers common questions and solves problems for your audience.

4. Local SEO
- Create a Google My Business profile and keep it updated with your latest information, including business hours, address, and contact details.
- Encourage satisfied customers to leave positive reviews on your Google My Business profile and other review sites.

5. Backlink Building
- Reach out to local bloggers and websites to write guest posts or get featured.
- Partner with local businesses for cross-promotion and backlinks.

6. Social Signals
- Ensure that your social media activity links back to your website. Share your blog posts, promotions, and important updates on your social media profiles to drive traffic and improve your search engine rankings.

**Other**

If have the £££ look into paid marketing stradegies to get a broader reach look for a good ROI by investigating the target market and plan accordingly.

---

## Features

### Navbar

- Allows users to navigate the site

![Navbar Desktop](./media/pages/nav/desktop-nav.png)

![Navbar Mobile](./media/pages/nav/mobile-nav.png)

![Navbar All Products](./media/pages/nav/all-products-nav.png)

![Navbar Floral Arrangements](./media/pages/nav/floral-arrangements-nav.png)

![Navbar Ocassions](./media/pages/nav/ocassions-nav.png)

![Navbar Register/Signin](./media/pages/nav/rgister-login-nav.png)

![Navbar Staff/Superuser logged in](./media/pages/nav/admin-nav.png)

![Navbar Customer Logged in](./media/pages/nav/user-nav.png)

---
### Index

- The landing page with a call to action and a soothing floral backgorund image.

![Index Page](./media/pages/home/index_page.jpg)

---
### Register

- Django Allauth register page, allows users to make an account.

![Register Page](./media/pages/allauth/register-page.png)

**Email link to confirm account activation and page**

![Confirm Email Example](./media/pages/allauth/verify-email-page.png)

![Confimed Email Page](./media/pages/allauth/confirm-email-page.png)

---

### Forgot Password

- Django allauth page for users who forgot password and want to reset it

![Forgot Password email page](./media/pages/allauth/forgot-password-page.png)

**Forgot Password Emails**

![Forgot Password Email Image](./media/pages/allauth/forgot-password-email.png)

![Forgot Password Email Image](./media/pages/allauth/email-delivery-forgot-pass-no-account.png)

**Forgot Pass Change Pass Page**

![Forgotten password change password form](./media/pages/allauth/change-password-email-direct-page.png)

---

### Chnage Password

- Django Allauth change password page. Allows logged in users to change account password.

![Change Password Page](./media/pages/allauth/change-password-page.png)

**Change Password Email**

![Change Password Email](./media/pages/allauth/change-password-email.png)

---

### Sign In

- Django allauth sign in page, allows Users to sign into their accounts using username/Email and password.

![Sign In Page](./media/pages/allauth/signin-page.png)

![Wrong Email, username, or password](./media/pages/allauth/wrong-user-pass.png)

---

### Sign out

- Django allauth sign out page, allows Users to sign out of their accounts.

![Sign out Page](./media/pages/allauth/signout-page.png)

---

### Profiles

- Allows users to view past orders and their shipping information which can be updated here.

![Profile Page](./media/pages/profiles/profile-page.png)

**Change Shipping Details Email**

![Change shipping email image](./media/pages/profiles/profile-update-email.png)

---

### Reviews

- Allows all visitors to view user left reviews, if logged in can create, edit, and delete their reviews

![Reviews Page](./media/pages/reviews/review-page.png)

**Review Confirmation Email**

![Review confirmation email image](./media/pages/reviews/new-review-email.png)

**Review Edit Confirmation Email**

![Change review email image](./media/pages/reviews/edit-review-email.png)

**Review Delete Confirmation Email**

![Delete review email image](./media/pages/reviews/delete-review-email.png)

---

### Products List

- This page has many versions based on user search's and sort parameters. Users can see availble products sorted here with image, product name, price, and average rating.

![Product List Page](./media/pages/products/products-page.png)

---

### Products Details

- This is where users can view a specific product as well as the addons available. This will give a full indepth view into the product including the name (product and addons), if its availble and how many are available (product and addons), product decription, a quanity selector (product and addons), Add to cart (product and addons), and even the price (product and addons).

![Product Detail Page](./media/pages/products/products-details-page.png)

---

### Add or Edit Products

**Add Product**

- Here staff and super users can add new products and set all elements of the products.

![Add Product Page](./media/pages/products/add-product-page.png)

**Edit Product**

- Here staff and super users can edit products and set all elements of the products.

![Edit Product Page](./media/pages/products/edit-product-page.png)

---

### Facebook Page

- The primary location for social marketing and escentially like a second storefront.

![Facebook Screenshot](./media/pages/socials/facebook-page.png)

---

### Instagram Page

- The secondary more visual only social media marketing.

![Instagram Screenshot](./media/pages/socials/insta-page.png)

---

### Footer

- Links to Social Sites, Legal, and Newsletter signup

![Image desktop footer](./media/pages/footer/footer-desktop.png)

![Image mobile footer](./media/pages/footer/footer-mobile.png)

![Image privacy policy example footer](./media/pages/footer/privacy-policy-pop-up.png)

![Image terms of service footer](./media/pages/footer/tos-pop-up.png)

---

### Error Pages

**400**

![400 html error](./media/pages/errors/400-page.png)

**403**

![403 html error](./media/pages/errors/403-page.png)

**404**

![404 html error](./media/pages/errors/404-page.png)

**500**

![500 html error](./media/pages/errors/500-page.png)

### Django Admin

- This is the default django admin page for more granual control of site elements.

| Login                  |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin login image](./media/pages/admin/admin-login.png) | ![Admin site logged in image](./media/pages/admin/admin-logged-in.png) |

| Groups                  |                                 |
| :---------------------: | :-----------------------------: |
| ![Admin Groups Main](./media/pages/admin/admin-groups-main.png) | ![Admin Groups Sub](./media/pages/admin/admin-groups-sub.png) |

| Users                  |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Users Main](./media/pages/admin/admin-users-main.png) | ![Admin Users Sub](./media/pages/admin/admin-users-sub.png) |

| Orders                 |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Order Main](./media/pages/admin/admin-orders-main.png) | ![Admin Order Sub](./media/pages/admin/admin-orders-sub.png) |

| Inventory              |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Inventory Main](./media/pages/admin/admin-inv-main.png) | ![Admin Inventory Sub](./media/pages/admin/admin-inv-sub.png) |

| Categories             |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Categories Main](./media/pages/admin/admin-cat-main.png) | ![Admin Categories Sub](./media/pages/admin/admin-cat-sub.png) |

| Products               |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Products Main](./media/pages/admin/admin-products-main.png) | ![Admin Products Sub](./media/pages/admin/admin-products-sub.png) |

| Reviews                |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Reviews Main](./media/pages/admin/admin-reviews-main.png) | ![Admin Reviews Sub](./media/pages/admin/admin-reviews-sub.png) |

| Social accounts        |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Social Account Main](./media/pages/admin/admin-soc-acct-main.png) | ![Admin Social  Account Sub](./media/pages/admin/admin-soc-app-sub.png) |

| Social app tokens      |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Social Token Main](./media/pages/admin/admin-soc-app-token-main.png) | ![Admin Social Token Sub](./media/pages/admin/admin-soc-app-token-sub.png) |

| Social applications    |                                 |
| :--------------------: | :-----------------------------: |
| ![Admin Social App Main](./media/pages/admin/admin-soc-app-main.png) | ![Admin Social App Sub](./media/pages/admin/admin-soc-app-sub.png) |

---

[Back to table of contents](#Table-of-contents)

---

## Testing

### Manual Testing

**Accounts/Profiles**

| What test was completed                   | Passed? |           Other information            |
| :---------------------------------------: | :-----: | :------------------------------------: |
| Login to site as a superuser(Admin)       |   Yes   |                                        |
| Log out of site as a superuser            |   Yes   |                                        |
| Login to site as a staff (BB)             |   Yes   |                                        |
| Log out of site as a staff                |   Yes   |                                        |
| Sign up as a customer/user (John.Doe)     |   Yes   |                                        |
| Login to site as a customer/user          |   Yes   |                                        |
| Log out of site as a customer/user        |   Yes   |                                        |
| Email verification Email sent             |   Yes   |                                        |
| Can't progress with out verifying         |   Yes   |                                        |
| Forgot Password Email sent                |   Yes   |                                        |
| Link working and resets password          |   Yes   |                                        |
| Change password form                      |   Yes   | Changes the password after submission  |
| Save details check box (checkout) updates |   Yes   | Changes the form after submission      |
| Profile details page form loads           |   Yes   |                                        |
| Profile page orders made and links work   |   Yes   |                                        |
| Profile update information button works   |   Yes   | Changes the form after submission      |

**Products**

|                 What test was completed                   | Passed? | Other information   |
| :-------------------------------------------------------: | :-----: | ------------------: |
| Can add products and get a prompt confirming add          | Yes     | Staff and superuser |
| Can edit products and get a prompt confirming edit        | Yes     | Staff and superuser |
| Can remove products and get a prompt confirming deletion  | Yes     | Staff and superuser |
| All products are avialable to be viewed by everyone       | Yes     |                     |
| Can designate products as addon and they appear in addons | Yes     |                     |
| To top scroll arrow works                                 | Yes     |                     |
| Sort by A-Z                                               | Yes     |                     |
| Sort by Z-A                                               | Yes     |                     |
| Sort by rating low to high                                | Yes     |                     |
| Sort by rating high to low                                | Yes     |                     |
| Sort by price low to high                                 | Yes     |                     |
| Sort by price high to low                                 | Yes     |                     |
| View catigory nav roses                                   | Yes     |                     |
| View catigory nav vibrant                                 | Yes     |                     |
| View catigory nav Luxurious                               | Yes     |                     |
| View catigory nav all arangements                         | Yes     |                     |
| View catigory nav Valintines                              | Yes     |                     |
| View catigory nav Birthday                                | Yes     |                     |
| View catigory nav Mothers Day                             | Yes     |                     |
| View catigory nav Houswarming                             | Yes     |                     |
| View catigory nav Thank You                               | Yes     |                     |
| View catigory nav Anniversaries                           | Yes     |                     |
| View catigory nav Graduations                             | Yes     |                     |
| View catigory nav Sympathy                                | Yes     |                     |
| View catigory nav all ocassion's                          | Yes     |                     |

**Inventory**

| What test was completed                    | Passed? | Other information                     |
| :----------------------------------------: | :-----: | :-----------------------------------: |
| Can add inventory                          | Yes     | Staff and superuser                   |
| Can edit inventory                         | Yes     | Staff and superuser                   |
| Can remove inventory                       | Yes     | Staff and superuser                   |
| Inventory updates with purchases           | Yes     | Decrease as bought by correct ammount |
| Users can see the stock available          | Yes     |                                       |
| Out of stock shows visibly                 | Yes     |                                       |
| Cant add more then availble to cart        | Yes     |                                       |
| Cant checkout with more then available     | Yes     |                                       |
| Out of stock items display visual messages | Yes     |                                       |

**Cart**

|  What test was completed                   | Passed? | Other information |
| :----------------------------------------: | :-----: | :---------------: |
| Can set quantity of product to add to cart | Yes     |                   |
| Can set quanity of addons to add to cart   | Yes     |                   |
| Cant add more then allowed to cart         | Yes     |                   |
| Get a prompt when adding to cart           | Yes     |                   |
| Can view cart as superuser                 | Yes     |                   |
| Can view cart as staff                     | Yes     |                   |
| Can view cart as customer                  | Yes     |                   |
| Can update product quantity in cart        | Yes     |                   |
| Get prompt for new cart update             | Yes     |                   |
| Can remove product from cart               | Yes     |                   |
| Get prompt for new cart deletions update   | Yes     |                   |
| Cart carries over to checkout              | Yes     |                   |

**Checkout**

| What test was completed                     | Passed? | Other information |
| :-----------------------------------------: | :-----: | :---------------: |
| Cart carries over to checkout               | Yes     |                   |
| Checkout shipping info form loads           | Yes     |                   |
| Checkout strip form loads                   | Yes     |                   |
| Checkout form submits                       | Yes     |                   |
| Checkout loaing blue and white arrows loads | Yes     |                   |
| Checkout successful                         | Yes     |                   |
| Checkout unsuccessful                       | Yes     |                   |
| Checkout mssing needed information error    | Yes     |                   |
| Checkout success confirmation page          | Yes     |                   |
| Checkout success confirmation email         | Yes     |                   |
| Order shows on admin site                   | Yes     |                   |

**Reviews**

| What test was completed          | Passed? | Other information |
| :------------------------------: | :-----: | :---------------: |
| Make review as a customer/user   |   Yes   |                   |
| Make review as a superuser       |   Yes   |                   |
| Make review as staff             |   Yes   |                   |
| Edit review as a customer/user   |   Yes   |                   |
| Edit review as a superuser       |   Yes   |                   |
| Edit review as staff             |   Yes   |                   |
| Delete review as a customer/user |   Yes   |                   |
| Delete review as a superuser     |   Yes   |                   |
| Delete review as staff           |   Yes   |                   |
| Review creation email sends      |   Yes   |                   |
| Review edited email sends        |   Yes   |                   |
| Review deletion email sends      |   Yes   |                   |

**Admin**

| What test was completed                          | Passed? | Other information                  |
| :----------------------------------------------: | :-----: | :--------------------------------: |
| Make a super user (Admin)                        |   Yes   |                                    |
| make staff role and permissions                  |   Yes   |                                    |
| Login to Django admin as customer/user           |   Yes   | Only staff can log in successfully |
| Login to Django admin as superuser               |   Yes   | Only staff can log in successfully |
| Login to Django admin as staff                   |   Yes   | Only staff can log in successfully |
| Log out of Django admin as superuser             |   Yes   |                                    |
| Log out of Django admin as staff                 |   Yes   |                                    |
| Successfully change any users data on admin site |   Yes   |                                    |
| Superuser can visit all links                    |   Yes   |                                    |
| Staff can visit appropriate links only           |   Yes   |                                    |
| Accounts functionality working as intended       |   Yes   |                                    |
| Products functionality working as intended       |   Yes   |                                    |
| Checkout functionality working as intended       |   Yes   |                                    |
| Admin Action send order shiped email             |   Yes   | Email Recieved                     |
| Admin Action send order delivered email          |   Yes   | Email Recieved                     |
| Admin Action send order cancled                  |   Yes   | Email Recieved                     |
| Reviews functionality working as intended        |   Yes   |                                    |

---

### Bugs & Issues Encountered

| Bugs/Issues Encountered link                                                                           | More about the issue                                   | Fixed? |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------: | :----: |
| [Issues loading css from file](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/20)           | Ended up being a issue in settings.py                  | Yes    |
| [Stock going negative](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/35)                   | added checks to any where stock can be effected        | Yes    |
| [Ratings not showing](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/42)                    | Users could set 0 rating leading to no ratings showing | Yes    |
| [Sort by ratings](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/43)                        | Ratings had caused pages not to load                   | Yes    |
| [Sort by ratings](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/43)                        | No Rating shows before ratings in high to low          | No     |
| [Webhook Issue](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/45)                          | Missing env varriable                                  | Yes    |
| [Webhook payment_intent.succeeded Issue](https://github.com/Danger0101/Blossom_Haven_CI_PP5/issues/45) | Missing env varriable                                  | Yes    |

---

[Back to table of contents](#Table-of-contents)

---

## Validation Testing

### Python

All Scripts checked with [PEP8 Code institute](https://pep8ci.herokuapp.com/)

**blossom_haven**

| **File**                  | **Line** | **Image**                                                                              |
| :-----------------------: | :------: | :------------------------------------------------------------------------------------: |
| blossom_haven\settings.py | All      | ![Blossom Haven Settings Pep8 screenshot](./media/pep8/bolossm-haven/main_urls_py.png) |
| blossom_haven\urls.py     | All      | ![Blossom Haven Urls Pep8 screenshot](./media/pep8/bolossm-haven/settings_py.png)      |
| blossom_haven\wsgi.py     | All      | ![Blossom Haven WSGI Pep8 screenshot](./media/pep8/bolossm-haven/wsgi_py.png)          |

**Cart**

| **File**                        | **Line** | **Image**                                                                |
| :-----------------------------: | :------: | :----------------------------------------------------------------------: |
| cart\apps.py                    | All      | ![Cart Apps Pep8 screenshot](./media/pep8/cart/cart_apps_py.png)         |
| cart\contexts.py                | All      | ![Cart Contexts Pep8 screenshot](./media/pep8/cart/cart_contexts_py.png) |
| cart\urls.py                    | All      | ![Cart Urls Pep8 screenshot](./media/pep8/cart/cart_urls_py.png)         |
| cart\views.py                   | All      | ![Cart Views Pep8 screenshot](./media/pep8/cart/cart_views_py.png)       |
| cart\templatetags\cart_tools.py | All      | ![Cart carttools Pep8 screenshot](./media/pep8/cart/cart_tools_py.png)   |

**Checkout**

| **File**                    | **Line** | **Image**                                                                                          |
| :-------------------------: | :------: | :------------------------------------------------------------------------------------------------: |
| checkout\admin.py           | All      | ![Checkout Admin Pep8 screenshot](./media/pep8/checkout/checkout_admin_py.png)                     |
| checkout\apps.py            | All      | ![Checkout Apps Pep8 screenshot](./media/pep8/checkout/checkout_apps_py.png)                       |
| checkout\forms.py           | All      | ![Checkout Forms Pep8 screenshot](./media/pep8/checkout/checkout_forms_py.png)                     |
| checkout\models.py          | All      | ![Checkout Models Pep8 screenshot](./media/pep8/checkout/checkout_models_py.png)                   |
| checkout\signals.py         | All      | ![Checkout Signals Pep8 screenshot](./media/pep8/checkout/checkout_signals_py.png)                 |
| checkout\views.py           | All      | ![Checkout Views Pep8 screenshot](./media/pep8/checkout/checkout_views_py.png)                     |
| checkout\webhook_handler.py | All      | ![Checkout Webhook Handler Pep8 screenshot](./media/pep8/checkout/checkout_webhook_handler_py.png) |
| checkout\webhooks.py        | All      | ![Checkout Webhook Pep8 screenshot](./media/pep8/checkout/checkout_webhooks_py.png)                |

**Home**

| **File**      | **Line** | **Image**                                                          |
| :-----------: | :------: | :----------------------------------------------------------------: |
| home\apps.py  | All      | ![Home Apps Pep8 screenshot](./media/pep8/home/home_apps_py.png)   |
| home\urls.py  | All      | ![Home Urls Pep8 screenshot](./media/pep8/home/home_urls_py.png)   |
| home\views.py | All      | ![Home Views Pep8 screenshot](./media/pep8/home/home_views_py.png) |

**Inventory**

| **File**             | **Line** | **Image**                                                           |
| :------------------: | :------: | :-----------------------------------------------------------------: |
| inventory\admin.py   | All      | ![Pep8 screenshot](./media/pep8/inventory/inventory_admin_py.png)   |
| inventory\apps.py    | All      | ![Pep8 screenshot](./media/pep8/inventory/inventory_apps_py.png)    |
| inventory\models.py  | All      | ![Pep8 screenshot](./media/pep8/inventory/inventory_models_py.png)  |
| inventory\signals.py | All      | ![Pep8 screenshot](./media/pep8/inventory/inventory_signals_py.png) |

**Products**

| **File**            | **Line** | **Image** |
| :-----------------: | :------: | :--------------------------------------------------------------: |
| products\admin.py   | All      | ![Pep8 screenshot](./media/pep8/products/products_admin_py.png)  |
| products\apps.py    | All      | ![Pep8 screenshot](./media/pep8/products/products_apps_py.png)   |
| products\forms.py   | All      | ![Pep8 screenshot](./media/pep8/products/products_forms_py.png)  |
| products\models.py  | All      | ![Pep8 screenshot](./media/pep8/products/products_models_py.png) |
| products\urls.py    | All      | ![Pep8 screenshot](./media/pep8/products/products_views_py.png)  |
| products\views.py   | All      | ![Pep8 screenshot](./media/pep8/products/products_views_py.png)  |
| products\widgets.py | All      | ![Pep8 screenshot](./media/pep8/products/products_widget_py.png) |

**Profiles**

| **File**            | **Line** | **Image**                                                                         |
| :-----------------: | :------: | :-------------------------------------------------------------------------------: |
| profiles\apps.py    | All      | ![Profiles Apps Pep8 screenshot](./media/pep8/profiles/profile_apps_py.png)       |
| profiles\forms.py   | All      | ![Profiles Forms Pep8 screenshot](./media/pep8/profiles/profile_forms_py.png)     |
| profiles\models.py  | All      | ![Profiles Models Pep8 screenshot](./media/pep8/profiles/profile_models_py.png)   |
| profiles\signals.py | All      | ![Profiles Signals Pep8 screenshot](./media/pep8/profiles/profile_signals_py.png) |
| profiles\urls.py    | All      | ![Profiles Urls Pep8 screenshot](./media/pep8/profiles/profile_urls_py.png)       |
| profiles\views.py   | All      | ![Profiles Views Pep8 screenshot](./media/pep8/profiles/profile_views_py.png)     |

**Reviews**

| **File**          | **Line** | **Image**                                                                               |
| :---------------: | :------: | :-------------------------------------------------------------------------------------: |
| reviews\admin.py  | All      | ![Review Admin Pep8 screenshot](./media/pep8/reviews/reviews_admin_py.png)              |
| reviews\apps.py   | All      | ![Review Apps Pep8 screenshotPep8 screenshot](./media/pep8/reviews/reviews_apps_py.png) |
| reviews\forms.py  | All      | ![Review Forms Pep8 screenshot](./media/pep8/reviews/reviews_forms_py.png)              |
| reviews\models.py | All      | ![Review Models Pep8 screenshot](./media/pep8/reviews/reviews_models_py.png)            |
| reviews\urls.py   | All      | ![Review Urls Pep8 screenshot](./media/pep8/reviews/reviews_urls_py.png)                |
| reviews\views.py  | All      | ![Review Views Pep8 screenshot](./media/pep8/reviews/reviews_views_py.png)              |

**Others**
     
| **File**  | **Line** | **Image**                                                      |
| :-------: | :------: | :------------------------------------------------------------: |
| manage.py | All      | ![Manage.py Pep8 screenshot](./media/pep8/other/manage_py.png) |

## Javascript

- All my custom js scripts were run though [jshint](https://jshint.com/).

| **File**                    | **Line** | **Image**                                                                               |
| :-------------------------: | :------: | :-------------------------------------------------------------------------------------: |
| Cart HTML JS                | All      | ![Cart HTMl side js](./media/js-test/cart/cart-html-js.png)                             |
| Stripe js                   | All      | ![Stripe js](./media/js-test/checkout/stripe-js.png)                                    |
| Async loading product image | All      | ![Async product image](./media/js-test/products/async-product-images-js.png)            |
| Scroll button               | All      | ![Scroll button](./media/js-test/products/btt-scroll-js.png)                            |
| Add/Edit product html js    | All      | ![Add/Edit product html side js](./media/js-test/products/edit-add-product-html-js.png) |
| Sortby js                   | All      | ![Sortby js](./media/js-test/products/sort-selector-js.png)                             |
| Country Field js            | All      | ![Country Field js](./media/js-test/profiles/countryfield-js.png)                       |

---

### CSS

- checked my custom base.css with [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) direct input; completed with a few warnings.

**static\css\base.css**

![css verification img](./media/base_css_verification.png)

---

### HTML

- checked all non logged in pages as html urls and logged in pages as raw html with [W3 HTML Validator](https://validator.w3.org/) on all custom pages with no errors or warnings. Django allauth and a few cripsy forms have some errors.

| Page | Image |
| :--: | :---: |
| Home | ![Home page html check](./media/html-check/home-html-check.png) |
| Products list | ![All products](./media/html-check/products-html-check.png) |
| Product Details | ![Product Details](./media/html-check/products-details-html-check.png) |
| Cart | ![Cart](./media/html-check/cart-html-check.png) |
| Checkout | ![Checkout](./media/html-check/checkout-html-check.png) |
| Order view | ![Order View](./media/html-check/checkout-order-success-html-check.png) |
| Profiles | ![Profiles](./media/html-check/profiles-html-check.png) |
| Reviews | ![Reviews](./media/html-check/reviews-html-check.png) |
| Django-allauth Register | ![Django-allauth Register](./media/html-check/django-all-auth-register-html-check.png) |
| Django-allauth Login | ![Django-allauth Login](./media/html-check/django-all-auth-login-html-check.png) |
| Django-allauth Logout | ![Django-allauth Logout](./media/html-check/django-all-auth-logout-html-check.png) |
| Django-allauth Change Password | ![Django-allauth Change Password](./media/html-check/django-all-auth-change-password-html-check.png) |
| Django-allauth Reset Password | ![Django-allauth Reset Password](./media/html-check/django-all-auth-pass-reset-html-check.png) |
| Add Product | ![Add Product](./media/html-check/products-add-html-check.png) |
| Edit Product | ![Edit Product](./media/html-check/products-edit-html-check.png) |
| Add Review | ![Add Review](./media/html-check/reviews-add-html-check.png) |
| Edit Review | ![Edit Review](./media/html-check/reviews-edit-html-check.png) |

### Contrast

- Checked all non logged in pages with [A11Y contrast checker](https://color.a11y.com/) Cameback with no issues.

![Contrast Check](./media/contrast-check.png)

---

[Back to table of contents](#Table-of-contents)

---

## Lighthouse

### Index LH

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap index lighthouse desktop](./media/lighthouse/home/home-lh-desktop.png) | ![Screencap index lighthouse mobile](./media/lighthouse/home/home-lh-mobile.png) |

### Products LH

**Product Add LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap product add lighthouse desktop](./media/lighthouse/products/products-add-lh-desktop.png) | ![Screencap product add lighthouse mobile](./media/lighthouse/products/products-add-lh-mobile.png) |

**Product Edit LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap product edit lighthouse desktop](./media/lighthouse/products/products-edit-lh-desktop.png) | ![Screencap product edit lighthouse mobile](./media/lighthouse/products/products-edit-lh-mobile.png) |

**Products List LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap products list lighthouse desktop](./media/lighthouse/products/products-all-lh-desktop.png) | ![Screencap products list lighthouse mobile](./media/lighthouse/products/products-all-lh-mobile.png) |

**Product Details LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap product details lighthouse desktop](./media/lighthouse/products/products-details-lh-desktop.png) | ![Screencap product details lighthouse mobile](./media/lighthouse/products/products-details-lh-mobile.png) |

### Reviews LH

**Product Reviews LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap reviews lighthouse desktop](./media/lighthouse/reviews/reviews-lh-all-desktop.png) | ![Screencap reviews lighthouse mobile](./media/lighthouse/reviews/reviews-lh-all-mobile.png) |

**Product Reviews Add LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap review add lighthouse desktop](./media/lighthouse/reviews/reviews-add-lh-desktop.png) | ![Screencap review add lighthouse mobile](./media/lighthouse/reviews/reviews-add-lh-mobile.png) |

**Product Reviews Edit LH**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap review edit lighthouse desktop](./media/lighthouse/reviews/reviews-edit-lh-desktop.png) | ![Screencap review edit lighthouse mobile](./media/lighthouse/reviews/reviews-edit-lh-mobile.png) |

### Cart LH

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap cart lighthouse desktop](./media/lighthouse/cart/cart-lh-desktop.png) | ![Screencap cart lighthouse mobile](./media/lighthouse/cart/cart-lh-mobile.png) |

### Checkout LH

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap checkout lighthouse desktop](./media/lighthouse/checkout/checkout-lh-desktop.png) | ![Screencap checkout lighthouse mobile](./media/lighthouse/checkout/checkout-lh-mobile.png) |

### Profiles LH

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap profiles lighthouse desktop](./media/lighthouse/profiles/profile-lh-desktop.png) | ![Screencap profiles lighthouse mobile](./media/lighthouse/profiles/profile-lh-mobile.png) |

### Django Alltuh LH

**Login**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap profiles lighthouse desktop](./media/lighthouse/allauth/login-lh-desktop.png) | ![Screencap profiles lighthouse mobile](./media/lighthouse/allauth/login-lh-mobile.png) |

**Logout**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap profiles lighthouse desktop](./media/lighthouse/allauth/logout-lh-desktop.png) | ![Screencap profiles lighthouse mobile](./media/lighthouse/allauth/logout-lh-mobile.png) |

**Register**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap profiles lighthouse desktop](./media/lighthouse/allauth/register-lh-desktop.png) | ![Screencap profiles lighthouse mobile](./media/lighthouse/allauth/register-lh-mobile.png) |

**Change Password**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap profiles lighthouse desktop](./media/lighthouse/allauth/change-pass-lh-desktop.png) | ![Screencap profiles lighthouse mobile](./media/lighthouse/allauth/change-pass-lh-mobile.png) |

**Forgot Password**

| **Chrome lighthouse desktop** | **Chrome mobile lighthouse** |
| :---------------------------: | :--------------------------: |
| ![Screencap profiles lighthouse desktop](./media/lighthouse/allauth/forgot-pass-lh-desktop.png) | ![Screencap profiles lighthouse mobile](./media/lighthouse/allauth/forgot-pass-lh-mobile.png) |

---

[Back to table of contents](#Table-of-contents)

---

## Setup

### Database

**Seting Up Database**

1. Go to [elephantsql](https://customer.elephantsql.com/login)
2. Make an account or sign in (I used my GitHub account)
3. Once logged in hit the "+ Create New Instance"

![elephantsql loggedin page](./media/esql_img/esql_loggedin_page.png)

4. Set up a name for the plan.
5. Select version for the plan.
6. **Optional** Add any tags if you wish
7. Hit "select region" button

![elephantsql Setup Paln page](./media/esql_img/esql_plan_setup_page.png)

8. Select a Data Center.
9. Once chosen hit the "Review" button

![elephantsql Data Center page](./media/esql_img/esql_select_region_page.png)

10. If all looks correct hit "Create Instance"

![elephantsql Conrifm page](./media/esql_img/esql_confirm_page.png)

11. Now you have your database set up all that is left is linking it to django project.
12. URL has a copy button hit this to copy your URL

![elephantsql Data Base page](./media/esql_img/esql_db_page.png)

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

- I was able to make this using [django-extensions](https://pypi.org/project/django-extensions/) and [pydotplus](https://pypi.org/project/pydotplus/)

![Data Visiualization](./media/database-visual.png)

---

[Back to table of contents](#Table-of-contents)

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

   **.env env.py or equivilent follow correct stucture for local deployment**

|                  Line to enter                  |
| :---------------------------------------------: |
|    CLOUDINARY_API_KEY = Api key value           |
| CLOUDINARY_API_SECRET = Api secret value        |
| CLOUDINARY_CLOUD_NAME = Cloudinary Name         |
| CLOUDINARY_FOLDER_NAME = Cloudinary folder name |

(Replace all after **"="** with your information)

**[Heroku](https://www.heroku.com/) Cofig Variables for live delpoyment**

|          Key           |         Value          |
| :--------------------: | :--------------------: |
|  CLOUDINARY_API_KEY    |     Api key value      |
| CLOUDINARY_API_SECRET  |    Api secret value    |
| CLOUDINARY_CLOUD_NAME  |    Cloudinary Name     |
| CLOUDINARY_FOLDER_NAME | Cloudinary Folder Name |

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

[Back to table of contents](#Table-of-contents)

---

### Stripe for this project

1. Creat a [Stripe](https://stripe.com/gb) account.
2. Once created following Stripes steps click developer at the top.
3. Click API Keys and coppy API keys (Public and Secret) into the env file or on heroku if deployed there:

| Key Name          | Key Value      |
| :---------------: | :------------: |
| STRIPE_PUBLIC_KEY | API_Public_Key |
| STRIPE_SECRET_KEY | API_Secret_Key |

4. Next set up a webhook on stripe and copy its secrect key (Signing secret) to do this Follow step 2 and then hit webhook this time.
| Key Name          | Key Value      |
| :---------------: | :------------: |
| STRIPE_WH_SECRET | WH_Signing_Secret |

---

[Back to table of contents](#Table-of-contents)

---

### Deployment

Used Heroku to deploy the website. You can [Visit Live Site by clicking here](https://blossom-haven-ci-pp5-d8c652557fbc.herokuapp.com/)

#### How to deploy to [Heroku](https://www.heroku.com/):

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

**[Heroku](https://www.heroku.com/) Cofig Variables**

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

---

[Back to table of contents](#Table-of-contents)

---

### Email Setup

**Using Gmail for this site others may varry slightly**

1. Go to [Gmail](https://mail.google.com/):

- If you already have a Gmail account, you can skip this step
- If not, click on "Create account" and follow the instructions to set up a new Gmail account.

2. Sign in to your Gmail account:

- Visit [Gmail](https://mail.google.com/) and log in with your email and password.

3. [Setting up app passowrd follow these instructions](https://support.google.com/accounts/answer/185833?hl=en)

- if you dont see [app passwords](https://myaccount.google.com/apppasswords) click the link
4. Set Up the settings.py File in Django

**Add to your settings.py**

|                      Line to enter                            |
| :-----------------------------------------------------------: |
| import os (if not already imported)                           |
| EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' |
| EMAIL_USE_TLS = True                                          |
| EMAIL_PORT = 587                                              |
| EMAIL_HOST = 'smtp.gmail.com'                                 |
| EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')            |
| EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASS', '')        |
| DEFAULT_FROM_EMAIL = EMAIL_HOST_USER                          |

5. Set Up Configuration Variables for Email Credentials

   **.env env.py or equivilent follow correct stucture for local development**

|    Line to enter in settings.py        |
| :------------------------------------: |
| EMAIL_HOST_USER = your_email@gmail.com |
| EMAIL_HOST_PASS = your_app_password    |

(Replace all after **"="** with your information)

**[Heroku](https://www.heroku.com/) Cofig Variables for live deployments**

|   Key           |         Value           |
| :-------------: | :---------------------: |
| EMAIL_HOST_USER | Your gamil email        |
| EMAIL_HOST_PASS | your_app_password       |

---

[Back to table of contents](#Table-of-contents)

---

## Technology used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Fontawesome](https://fontawesome.com/)
- [Python 3.12](https://docs.python.org/3/)
- [Django 5.2](https://docs.djangoproject.com/en/5.0/)
- [Django-allauth](https://docs.allauth.org/en/latest/)
- [Visual Studios Code (VSCode)](https://code.visualstudio.com/)
- [Github](https://github.com/)
- [Git](https://git-scm.com/doc)
- [Github Desktop App](https://desktop.github.com/)
- [Cloudinary](https://cloudinary.com/documentation)
- [fooocus](https://github.com/lllyasviel/Fooocus?tab=readme-ov-file)
- [Microsoft Paint](https://www.microsoft.com/en-gb/windows/paint)
- [Gyazo](https://gyazo.com/en)
- [Microsoft Snipping tool](https://support.microsoft.com/en-us/windows/use-snipping-tool-to-capture-screenshots-00246869-1843-655f-f220-97299b865f6b)

## Wireframes

**Landing Page**

![Image for admin page wireframe](./media/wireframes/landing_page.png)

**Product Page**

![Image for admin page wireframe](./media/wireframes/product_list_page.png)

**Product detail Page**

![Image for admin page wireframe](./media/wireframes/product_details_page.png)

**Cart Page**

![Image for admin page wireframe](./media/wireframes/cart_page.png)

**Checkout Page**

![Image for admin page wireframe](./media/wireframes/checkout_page.png)

**Reviews Page**

![Image for admin page wireframe](./media/wireframes/reviews_page.png)

## Credits

**Images**

- All images use on the website are made by [fooocus](https://github.com/lllyasviel/Fooocus?tab=readme-ov-file) which at time of writting this is a completely free AI image generator that uses your own hardware to generate images.

**More Credits**

- My wife who’s been super supportive of this change in career for me and just being out right amazing we will get her into this one way or another I am sure.

- Code Institute for providing an excellent accelerated learning platform worth every penny.

- Botique Ado walk through from code instiute as this was the basis of the project. I originally was going to expand on that but I had a spur of the moment idea for a floarist site and I think I have nailed my version of a MVP and even tweaked it some more.

- My farmers market food stall [Bokit'la](https://www.bokitla.com/) they helped insprie the project unknowingly as I told them I had this project coming up and I will possibly be helping them soon impliment shopify to their website. As a side project I want to remake their site in Django and they said do it and send it so next up is theirs. I would have done it for this but they are specifically looking for shoppify and thats possibly out side the grading for this. They got my brain thinking of ideas and Blossom Haven came out of the wood works from that.

---

[Back to table of contents](#Table-of-contents)

---

## Future feature ideas

| Feature Ideas            | Why Not Implimented                                                            |
| :----------------------: | :----------------------------------------------------------------------------: |
| Cuppons/voucher          | Time and it wasn't needed for MVP                                              |
| Blog page                | Decided at time of writing marketing plan                                      |
| Further bug squashing    | Time left till project is due                                                  |
| Better product rendering | Time to complete and needs to be re thought also couldn't find a good CDN free |
| Custom Domain            | Cost                                                                           |
| Rebranding               | Noticed it to late but many Blossom Havens Exist                               |
| Figure out webhook issue | Was unable to debug it in time for submission alternative email method provided leaving webhook in submission as its still mostly working just payment_intent.succeeded keeps giving 500 code all others are working correctly with 200 code |
