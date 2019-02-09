# FSMtextSimplified

## Prerequisite
   a) Docker should have been installed and working
   
   b) git should have been installed and working
## 1) compile docker image using following command
```
docker build github.com/harjindersingh1123/FSMtextSimpilied.git -t movie-rating
```
## 2) Test image in local directory (movie-rating should have been there)
```
docker image list
```
## 3) Run the image in docker in intractive mode(as user has to given title name in input) 
```
docker run fsmtextsimpilied --title <title>
```
## 4) User needs to enter movie title name
```
$ docker run movie-rating --title batman
Rotten Tomatoes rating for title 'Batman' is : 72%
```
## Image can be run directly from docker as well
```
docker run harry675/movie-rating --title <title>
```


