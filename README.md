#Fuzzopress

Fuzzopress is a simple blogging app developed with Django.

After installing the requirements (Gunicorn is not really a requirement to run it) and initializing a database, you should be able to start blogging.

I do actually use it for my own blog! [Fuzzing the Web](http://fuzzingtheweb.com "fuzzingtheweb")
Disclaimer: most of it is in spanish

###You can add Navbar items easily (from the admin, title + url)
![fuzzopress](http://lh3.googleusercontent.com/-4Tf--qaF8Ek/UBI2Dcw3-HI/AAAAAAAABn4/kfB5YAeFCLk/s720/fuzzopress.png "fuzzopress")

###It also has a night-mode!
![night-mode](http://lh3.googleusercontent.com/-_e29XNpqNnE/UBI69BqsekI/AAAAAAAABoU/NF06p2SKAQk/s800/fuzzopress2.png "night-mode")

###And a customizable sidebar with simple widgets (from the admin, title + html-body)
![sidebar](https://s3-eu-west-1.amazonaws.com/fuzzingtheweb/images/sidebar.png "sidebar")

##Theming

I am working on the possibility of adding custom themes to Fuzzopress. For now, it's just adding a .css for your theme and override colors/sizes of elements, but I'm thinking on how could it be easy. It is still in early development.

There are currently two themes: default and bright. You can choose the theme that you want for the blog by changing this option in the settings.py file, at the bottom of it (in the "theme" option).

Here is a pic of the bright theme:
![bright theme](https://s3-eu-west-1.amazonaws.com/fuzzingtheweb/images/bright-theme.png "bright theme")