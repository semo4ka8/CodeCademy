#Places to visit
In this project I built a simple app to track interesting places and organizing locations into 3 categories: 
  - recommended places to visit, 
  - decided places to visit,
  - places that have been visited. 
    
Within each category we have the option to move a location up to the next category and also remove a location. Lastly, there is also the option to add new locations to any of the categories.

The application consists of 7 files:

`/static/styles.css`: Basic css files to give the application some style and show off the benefits of template inheritance.

`/templates/base.html`: Template header file that the main template file inherits from.

`data.csv`: Data that we used to show of the functionality of the application.

`location.py`: A module the application relies on to add, modify and delete location data. Application instantiates a Locations() class from this module. With this instance we rely on 3 methods:

   - `add()`: Add a location to the data
   - `moveup()`: Move the location up one category
   - `delete()`: Delete a location from the data

`app.py`: The Flask application which consists of 3 routes:

- `locations()`: The main route which return content associated with each category of location. This route is also responsible for handling the changing of categories and deletion of locations.
- `add_location()`: A form handling route which processes the add location form and then redirects back to the locations() route.
- `index()`: This route is the same path as the locations() route but without a category variable. It automatically redirects to the recommended page of the locations() route.

`/templates/locations.html`: Template file that displays the tourist attraction's data.

`forms.py`: A module that defines the form used in the application.

To implement this idea I used combined knowledge of Python, Flask and HTML.