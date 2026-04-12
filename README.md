cd MovieBookingSystem

git init

git add .

git commit -m "Initial Movie Booking System"

git branch develop

git checkout develop

git remote add origin https://github.com/Dharika-2006/MovieBookingSystem

git push -u origin develop

git checkout master

git merge develop

git push origin master

pip install mlflow
python mlflow_demo.py
python -m mlflow ui
