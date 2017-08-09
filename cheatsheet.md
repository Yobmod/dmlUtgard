npm install // install packages in the package.json in same folder
npm update
npm outdated
npm install -g newpackage  // installs globally
npm install -save newpackage  // installs locally and adds to package.json
npm install -save-dev newpackage  // installs locally and adds to package.json as dev requirement

PATHS
c:\users\laventin.LANCS\Appdata\Roaming\npm\
c:\users\yobmod\Appdata\Roaming\npm\
c:/path/to/npm/webpack      //  does the local webpack.config.js
c:/path/to/npm/gulp         //  does the local gulp.js



python app.py   // runs the flask app
python manage.py runserver   // runs django app         -Wd   // flag to show deprections
python manage.py runserver_plus   // runs django app (plus extensions & wagtail)
python manage.py colectstatic
python manage.py makemigrations
python manage.py migrate

mkvirtualenv <name>
workon <name>
pip install <xxx> 					-U // upgrade    -h // command help
pip install -r requirements.txt		 -r // use req file order
pip freeze							//show install packages
pip freeze > requirements.txt     	// create (overwrite) reqs



git add --all
git commit -m "xxxxx"
git push origin master
git pull origin master
git fetch
git reset --hard origin/master
git clone
git remote add origin git@github.com:"yourusername"/"projectname".git   //after rename repo


heroku run python....    //use python comands (....) on heroku
