# [100Reads](https://read100-abad619e4cf8.herokuapp.com)

Developer: Radwan Duadu ([RadwanDuadu](https://www.github.com/RadwanDuadu))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RadwanDuadu/100Reads)](https://www.github.com/RadwanDuadu/100Reads/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RadwanDuadu/100Reads)](https://www.github.com/RadwanDuadu/100Reads/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RadwanDuadu/100Reads)](https://www.github.com/RadwanDuadu/100Reads)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://read100-abad619e4cf8.herokuapp.com)

100 Reads is a vibrant and interactive online platform created for book enthusiasts to discover, review, and share their literary experiences. The project aims to bring together readers from all walks of life — from passionate bookworms who devour novels weekly to casual browsers seeking their next great read. By offering a curated collection of books across a wide range of genres, 100 Reads empowers users to explore new authors, dive into fresh literary worlds, and make informed choices through authentic community-driven reviews.

At its core, 100 Reads strives to create a trustworthy and engaging space where readers can not only find books but also express their opinions, contribute reviews, and interact with others who share their love for reading. Registered users can submit their own reviews, rate books, and engage in meaningful discussions. To maintain credibility and quality, all submitted reviews go through a moderation process — ensuring that shared content remains respectful, insightful, and free from spam or inappropriate language. Moderators and administrators play a key role in approving or disapproving reviews, while additional site features such as average star ratings, pagination, and user profiles enhance both functionality and user experience.

This project was inspired by the growing need for authentic, reader-centered recommendation platforms in an era where book discovery is often dominated by algorithms or commercial interests. As an avid reader and developer, I wanted to build a community where the value of honest human opinion could shine through — a digital space that feels both personal and collaborative. The idea for 100 Reads emerged from my own experience of struggling to find genuine book recommendations that matched my interests and values. By developing this platform, I sought to merge my passion for reading with my technical skills, creating a tool that celebrates literature, fosters community interaction, and promotes a culture of thoughtful reading and sharing.

In essence, 100 Reads is more than just a book review website — it’s a digital community designed to inspire discovery, conversation, and connection among readers worldwide.


![screenshot](documentation/100reads-mockup.png)

source: [100Reads amiresponsive](https://ui.dev/amiresponsive?url=https://read100-abad619e4cf8.herokuapp.com)


## UX

### The 5 Planes of UX


#### 1. Strategy

**Purpose**
- ovide book enthusiasts and administrators with tools to create, manage, and moderate engaging book content and community interactions.
- Offer readers and guests an intuitive platform to discover, review, and discuss books across various genres.

**Primary User Needs**
- Site admins and moderators need seamless tools for adding, managing, and moderating books and reviews.
- Registered users need the ability to contribute by submitting reviews, rating books, and engaging with the community.
- Guests need the ability to browse and explore book listings, view ratings, and read reviews without creating an account.

**Business Goals**
- Foster a vibrant online community centered around books, reviews, and reader engagement.
- Build a trusted space for authentic, high-quality book discussions and recommendations.
- Ensure efficient book and review management tools for site administrators and moderators.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Book management tools (create, update, delete, and preview book entries).
- Review moderation and management features for admins and moderators(front-end).
- User account functionality (register, log in, submit/edit/delete reviews).
- Custom 404 error page to guide users back to book listings or the homepage.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Books, Login/Register, about, and Dashboard (for website moderators).
- **Hierarchy**:
  - Book content displayed prominently for easy browsing.
  - Clear call-to-action buttons for account creation and engagement (e.g., review).

**User Flow**
1. Guest users browse book description → read different books and see approved reviews.
2. Guest users register for an account → log in to leave reviewss.
3. Registered users leave reviewss → receive a pending approval notification.
4. 100Reads Admin create, update, and manage books → moderate reviews.
5. Admin and moderators(approved by admin) approve or reject reviews → manage user interactions.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used the below colours for the creation of the website

| Hex Code                | Usage / Context                                                       |
| ----------------------- | --------------------------------------------------------------------- |
| `#F9FAFC`               | Page background (`body`, `.main-bg`)                                  |
| `#4A4A4F`               | Brand text color (`.brand`)                                           |
| `#E84610`               | Accent color (links, buttons, hover states)                           |
| `#fff` / `#ffffff`      | White text, light backgrounds (`.light-bg`, buttons, text)            |
| `#445261`               | Dark background and text (`.dark-bg`, `.masthead-text`, `.book-link`) |
| `#188181`               | Teal highlight (`.image-flash`, `.btn-signup`, `.btn-edit`)           |
| `#23BBBB`               | Teal-blue for hover links and buttons                                 |
| `#8B5E3C`               | Rustic brown (cards, forms, titles)                                   |
| `#2a2a2a`               | Dark border on cards                                                  |
| `#1f1f1f`               | Pagination background                                                 |
| `#333333`               | Pagination hover background, text                                     |
| `#2c2c2c`               | Image container background                                            |
| `#2e2e2e`               | Horizontal rule border color                                          |
| `#1a1a1a`               | Masthead dark background                                              |
| `#f0f0f0`               | Masthead text color                                                   |
| `#b0b0b0`               | Card text (muted gray)                                                |
| `#cccccc`               | Borders, form inputs, light text                                      |
| `#f5f5f5`               | Input background                                                      |
| `#333333`               | Input text color                                                      |
| `#ffb3b3`               | Error text (light red)                                                |
| `#FFD580`               | Soft gold (signup link color)                                         |
| `#e6e6e6`               | Button hover background                                               |
| `#fefefe`               | Review card background (soft white)                                   |
| `#dddddd`               | Review card border                                                    |
| `#f8f9fa`               | Review section background                                             |
| `#e0e0e0`               | Review section border                                                 |
| `#b0b0b0`               | Card text                                                             |


### Typography


- [Lato](https://fonts.google.com/specimen/Lato) Used for the brand logo/title — modern, clean sans-serif font.
- [Roboto](https://fonts.google.com/specimen/Roboto) Used for card titles — professional, easy-to-read sans-serif font.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Add Blog | ![screenshot](documentation/wireframes/mobile-add-blog.png) | ![screenshot](documentation/wireframes/tablet-add-blog.png) | ![screenshot](documentation/wireframes/desktop-add-blog.png) |
| Edit Blog | ![screenshot](documentation/wireframes/mobile-edit-blog.png) | ![screenshot](documentation/wireframes/tablet-edit-blog.png) | ![screenshot](documentation/wireframes/desktop-edit-blog.png) |
| Blog Post | ![screenshot](documentation/wireframes/mobile-blog-post.png) | ![screenshot](documentation/wireframes/tablet-blog-post.png) | ![screenshot](documentation/wireframes/desktop-blog-post.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## User Stories

| **Target**           | **Expectation**                                                                  | **Outcome**                                                                                        |
| -------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| As a site admin      | I would like to add new books with a title, author, cover image, and description | so that I can expand the library’s book collection.                                                |
| As a site admin      | I would like to update existing book details                                     | so that I can correct information or refresh outdated content.                                     |
| As a site admin      | I would like to delete book entries                                              | so that I can remove books that are no longer relevant or appropriate.                             |
| As a site admin      | I would like to view a list of all books in the library                          | so that I can manage and maintain the book catalogue efficiently.                                  |
| As a moderator       | I would like to review user-submitted reviews before they are published          | so that I can ensure the content is appropriate and constructive.                                  |
| As a moderator       | I would like to approve or disapprove user reviews                               | so that I can maintain the quality and tone of the platform.                                       |
| As a moderator       | I would like to manage and delete reviews if needed                              | so that I can remove inappropriate or duplicate content.                                           |
| As a moderator       | I would like to approve or disapprove reviews directly from the front-end        | so that I can moderate efficiently without accessing the admin panel.                              |
| As a registered user | I would like to register for an account                                          | so that I can become part of the community and leave reviews on books.                             |
| As a registered user | I would like to log in to the site                                               | so that I can add, edit, or delete my own reviews.                                                 |
| As a registered user | I would like to leave a star rating and written review on a book                 | so that I can share my thoughts and help other readers make informed choices.                      |
| As a registered user | I would like to see my name and the date on my submitted review                  | so that my feedback feels personalized and authentic.                                              |
| As a registered user | I would like to receive a notification when my review is pending approval        | so that I understand it will appear once approved by a moderator.                                  |
| As a registered user | I would like to edit or delete my own review                                     | so that I can correct or retract my feedback when needed.                                          |
| As a guest user      | I would like to browse and read book listings without registering                | so that I can explore book recommendations easily.                                                 |
| As a guest user      | I would like to view book details, average ratings, and approved reviews         | so that I can make informed decisions about what to read.                                          |
| As a guest user      | I would like to register for an account                                          | so that I can start contributing my own book reviews.                                              |
| As a guest user      | I would like to see the names of reviewers on each book’s detail page            | so that I can sense the authenticity of community feedback.                                        |
| As a user            | I would like to view an **About** page                                           | so that I can learn more about the purpose and mission of 100Reads.                                |
| As a user            | I would like to use a **Contact** form                                           | so that I can send feedback, questions, or inquiries to the site administrators.                   |
| As a user            | I would like to see a **404 error page** if I visit a broken or invalid link     | so that I understand I’ve reached a page that doesn’t exist and can return to the homepage easily. |


## Features

### Existing Features

| **Feature**                     | **Notes**                                                                                                                                     | **Screenshot**                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Register**                    | Authentication is handled by **Allauth**, allowing users to register for a 100Reads account and start submitting reviews.                     | ![screenshot](documentation/features/register.png)        |
| **Login**                       | Authentication is handled by **Allauth**, allowing registered users and moderators to securely log in to their accounts.                      | ![screenshot](documentation/features/login.png)           |
| **Logout**                      | Users can log out of their account securely through Allauth authentication.                                                                   | ![screenshot](documentation/features/logout.png)          |
| **Book List (Home Page)**       | The homepage displays a selection of books, including their cover image, title, author, and a short description.                              | ![screenshot](documentation/features/book-list.png)       |
| **View Book Details**           | Users can view detailed information about each book, including a blurb, average rating, and approved user reviews.                            | ![screenshot](documentation/features/view-book.png)       |
| **Pagination**                  | Books are displayed in paginated lists for better user navigation across the collection of 100 book recommendations.                          | ![screenshot](documentation/features/pagination.png)      |
| **Add Review**                  | Authenticated users can submit a star rating and a written review for any book. Reviews require moderator approval before appearing publicly. | ![screenshot](documentation/features/add-review.png)      |
| **Edit Review**                 | Users can edit their own reviews after submission to correct mistakes or update their opinions.                                               | ![screenshot](documentation/features/edit-review.png)     |
| **Delete Review**               | Users can delete their own reviews if they wish to retract them.                                                                              | ![screenshot](documentation/features/edit-review.png)   |
| **Review Approval (Moderator)** | Moderators can approve, disapprove, or delete reviews directly from the front-end interface to maintain quality control.                      | ![screenshot](documentation/features/review-approval.png) |
| **Add Book (Admin)**            | Admins can add new book entries from the Django admin dashboard, including title, author, cover image, and book summary.                      | ![screenshot](documentation/features/add-book.png)        |
| **Update Book (Admin)**         | Admins can update existing book entries to fix details or update information.                                                                 | ![screenshot](documentation/features/update-book.png)     |
| **Delete Book (Admin)**         | Admins can delete book entries from the admin dashboard if no longer relevant.                                                                | ![screenshot](documentation/features/update-book.png)     |
| **About Page**                  | The About page explains the purpose and inspiration behind 100Reads, introducing the project’s mission to encourage reading.                  | ![screenshot](documentation/features/about.png)           |
| **Contact Form**                | A contact form allows visitors to send inquiries, feedback, or suggestions directly to the site administrators.                               | ![screenshot](documentation/features/contact.png)         |
| **User Feedback Messages**      | Clear Django messages appear after key actions (e.g., submitting a review or logging in) to provide instant user feedback.                    | ![screenshot](documentation/features/messages.png)        |
| **Heroku Deployment**           | The 100Reads site is fully deployed on Heroku, ensuring accessibility online and easy application management.                                 | ![screenshot](documentation/features/heroku.png)          |
| **404 Error Page**              | A custom 404 page guides users back to the homepage when they reach a non-existent or broken link.                                            | ![screenshot](documentation/features/404.png)             |


### Future Features

- **Search Functionality**: AUsers can search for books by title, author, or keyword, making it easy to find specific recommendations.
- **Ranking by Rating**: Books are ranked and displayed based on their average star rating, allowing users to discover the most highly-rated reads..
- **Moderator Notifications**: Moderators receive notifications when new reviews are submitted so that I can quickly take action.
- **Review Sorting Options**: As a reader, I want to sort reviews on the book details page by date or rating so that I can read the most relevant or highest-rated feedback first.
- **Front-end Moderator Dashboard**: Enhanced front-end moderator dashboard so that moderators can manage reviews and books more efficiently. Dosplaying pending approvals by date of submission. 

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |

## Database Design

### Data Model

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    USER {
        int id
        string username
        string email
        string password
    }

    USERPROFILE {
        int id
        bool is_moderator
        int user_id FK
    }

    BOOK {
        int id
        string title
        string slug
        string author_name
        text description
        int published_year
        string blurb
        string cover
    }

    REVIEW {
        int id
        text body
        int rating
        bool approved
        datetime created_on
        int book_id FK
        int author_id FK
    }

    ABOUT {
        int id
        string title
        datetime updated_on
        text content
    }

    CONTACT {
        int id
        string name
        string email
        text message
        bool read
    }

    %% Relationships
    USER ||--|| USERPROFILE : "has one"
    USER ||--o{ REVIEW : "writes"
    BOOK ||--o{ REVIEW : "has many reviews"
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVG1vmzAQ_ivWSf1GoyQkMPjWZqlUdVumtN2kKRJy8A2sgo1s0zRL8t9nyEsDTFXmT_bx3Mvz3HEbiCVDCAHVZ04TRfOFIPY8P07nZLO_V4cLQzh7f2ujuEhIqVEJmmPnA-aUZx1rQbVeSXWIs1uI92Tf57O7-y_Tj3IupcwI11FuK1bUSNWEVrVEnJG7h1b429ns4QIuhpusS0RnZdIx0tKkUkVN5gbfDGGoY8ULw6VoJizKZcZ1iixaI1WdiMusVMuONZavqFps5tMf99OfH_GpC1lKtm5CrGQ2ZktOWhTKJjnzZtSg4TmSWKG9sqjNxPq9nOt8tB9E-VcHbm5nz0__34JTKWXBOqXULGMpDArTSjeZfXu6mVyS8JLZrRPlqDVNsKWeVag9y1dXZI4ZrQZAp7zQZ7_Tdnt9vd02pj0kC0ipJlLgAlpQuTn2ukKtFDeoj6B6pLugKlROxdoW9spxVcPBgURxBqFRJTqQo7L07BNqdRZgUrQaQOXOqHqpXHbWp6Dil5T50U3JMkkh_E0zbV_7fhwWxslqB0A-rkV88kFhf9SJLIWBcDisY0K4gTcIfb838MeuFwTjT0PXGwcOrCEMRj0_GIz7I9_ve54feDsH_tRF9Hv-yA0G7rjvDf1h0A9cB5BxuwO-7tdXvcV2fwEBjmx4)

⚠️ RECOMMENDED ⚠️

Alternatively, or in addition to, a more comprehensive ERD can be auto-generated once you're at the end of your development stages, just before you submit. Follow the steps below to obtain a thorough ERD that you can include. Feel free to leave the steps below in the README for future use to yourself.

⚠️ --- END --- ⚠️

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

⚠️ TIP ⚠️

Consider adding screenshots of your Projects Board(s), Issues (open and closed), and Milestone tasks.

⚠️ --- END ---⚠️

[GitHub Projects](https://www.github.com/RadwanDuadu/100Reads/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/RadwanDuadu/100Reads/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/RadwanDuadu/100Reads?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/RadwanDuadu/100Reads/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/RadwanDuadu/100Reads?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/RadwanDuadu/100Reads/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://read100-abad619e4cf8.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION RadwanDuadu !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️
⚠️ Replace the keys below with your own actual keys used; example: if not using Cloudinary, then remove those keys, or replace with whatever ones you're using. ⚠️

🛑 --- END --- 🛑

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION RadwanDuadu !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️
⚠️ Replace the keys below with your own actual keys used; example: if not using Cloudinary | AWS, then replace those keys with whatever keys you're using. ⚠️

🛑 --- END --- 🛑

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/RadwanDuadu/100Reads).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/RadwanDuadu/100Reads.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/RadwanDuadu/100Reads)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/RadwanDuadu/100Reads).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to reference where you got your content, media, and any extra help. It is common practice to use code from other repositories and tutorials (which is totally acceptable), however, it is important to be very specific about these sources to avoid potential plagiarism.

⚠️ --- END ---⚠️

### Content

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links for any borrowed code snippets, elements, and resources. Ideally, you should provide an actual link to every resource used, not just a generic link to the main site. If you've used multiple components from the same source (such as Bootstrap), then you only need to list it once, but if it's multiple Codepen samples, then you should list each example individually. If you've used AI for some assistance (such as ChatGPT or Perplexity), be sure to mention that as well. A few examples have been provided below to give you some ideas.

Eventually you'll want to learn how to use Git branches. Here's a helpful tutorial called [Learn Git Branching](https://learngitbranching.js.org) to bookmark for later.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
    - [Button Clicks](https://www.zapsplat.com/sound-effect-category/button-clicks)
    - [Lasers & Weapons](https://www.zapsplat.com/sound-effect-category/lasers-and-weapons/page/5)
    - [Puzzle Music](https://soundimage.org/puzzle-music)
    - [Camtasia Audio](https://library.techsmith.com/camtasia/assets/Audio)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [I Think Therefore I Blog](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution and acknowledgement to any supports that helped, encouraged, or supported you throughout the development stages of this project. It's always lovely to appreciate those that help us grow and improve our developer skills. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

