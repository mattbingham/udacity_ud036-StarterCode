import webbrowser
import os
import re

# Improved with normalize and moved styles and js to separate files
main_page_head = '''
<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Fresher Tomatoes!</title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">
  <link rel="stylesheet" href="css/main.css">
</head>
'''
# The main page layout and title bar
main_page_content = '''
<body id="bootstrap-override">
  <!-- Trailer Video Modal -->
  <div class="modal" id="trailer">
    <div class="modal-dialog">
      <div class="modal-content">
        <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
          <img src="img/modal_close.png" alt="Close this pop-up box">
        </a>
        <div class="scale-media" id="trailer-video-container"></div>
      </div>
    </div>
  </div>
  <!-- Main Page Content -->
  <div class="top">
    <nav class="navbar navbar-inverse">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#"><img class="spin" src="img/logo_fresher-tomatoes.png" alt="Fresher Tomatoes trailers">
            <span class="fresher">Fresher</span>&nbsp;<span class="tomatoes">Tomatoes!</span>
          </a>
        </div>
      </div>
    </nav>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="container">
          <div class="section-box">
            <h2 class="text-center">Movies</h2>
              {image_tiles_movies}
            </div>
          </div>
        </div>
      </div>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
  </body>
</html>
'''
# A single movie entry html template
tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center video-wrapper" data-trailer-youtube-id="{vid_id}" data-toggle="modal" data-target="#trailer">
  <div class="tiles-container">
    <img src="{image}" width="180" height="270" alt="{title} poster image">
    <h2 class="text-center">{title}</h2>
    <p class="year"><i class="fa fa-calendar" aria-hidden="true"></i> {year}</p>
    <h3 class="text-center length"><i class="fa fa-clock-o" aria-hidden="true"></i> {length}</h3>
  </div>
</div>
'''


def image_tiles(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        vid_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer)
        vid_id_match = vid_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer)
        vid_id = (vid_id_match.group(0) if vid_id_match else None)

        # Append the tile for the movie and with its content filled in
        content += tile_content.format(
            title=movie.title,
            image=movie.image,
            vid_id=vid_id,
            length=movie.length,
            year=movie.year
        )

    return content


def open_website(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie or tv tiles placeholder generated content
    rendered_content = main_page_content.format(
        image_tiles_movies=image_tiles(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


def show_trailer(self):
    webbrowser.open(self.trailer_url)
