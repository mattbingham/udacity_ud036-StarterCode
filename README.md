## ud036_StarterCode
___
Source code for a Movie Trailer website.

### Instructions to run program
___
This guide assumes you have saved all files to your computer and have Python IDLE installed.

- Open `entertainment_center.py` in Python IDLE
- Goto **Run** > **Run Module**

### Changes to original code
___
I've tried very hard to get the website looking as nice as possible by adding additional features I thought would complement the website whilst adhering to the project specification. I've noted some of the changes to the original requirements for the project below.

#### Classes

`class Movie(Shared):`

- Added length of movie
- Added year of production
- Class is now a child of Shared

`class Shared():`

- Added this new parent class with reusable attributes for Movies. It can be used in the future to easily add future classes (for example TV series)

#### House keeping

New files and folders have been added for assets. References to the locations of these files have been changed in the `fresh_tomatoes.py` file. A new parent class has been created and references within the child class changed. A new stylesheet has been created to give the website a refined look.

`fresh_tomatoes.py`

- **Added** `main.css` and referenced links to `css` folder
- **Added** local images and referenced links to `img` folder
- **Added** logo and spin styles
- **Added** Lato font (Google font link in `fresh_tomatoes.py` and changed text styles for body, headings and span classes)
- **Added** `#bootstrap-override` to body tag to over-ride font-family styles in the bootstrap stylesheet (priority now higher - here's an interesting article on Stack Overflow about [Bootstrap prioritisation](https://stackoverflow.com/questions/20721248/best-way-to-override-bootstrap-css))
- **Changed** poster image sizes for better display
- **Moved** Javascript to `js` folder
- **Moved** links in `fresh_tomatoes.py` to load after body (inserted just before closing body tag)
- **Moved** `main.css` link in `fresh_tomatoes.py` to load after bootstrap stylesheets
- **Removed** references to YouTube in case of future use of a service other than YouTube

### Versioning / Future proofing
___
For future project code that requires marking by Udacity tutors, the [Udacity GitHub folder](https://github.com/mattbingham/udacity) will allow easy access to these files. The [README.md](https://github.com/mattbingham/udacity/blob/master/README.md) file at the link will be updated to list all projects.