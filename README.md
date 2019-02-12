# FSMtextSimplified

## Prerequisite
   a) Docker should have been installed and working
   
   b) git should have been installed and working
## 1) compile docker image using following command
```
docker build github.com/harjindersingh1123/FSMtextSimplified.git -t fsmtextsimplified
```
## 2) Test image in local directory (fsmtextsimplified should have been there)
```
docker run -p 5000:5000 fsmtextsimplified:latest
```

## Image can be run directly from docker as well
```
Not pushed yet
```
## Git clone, build and run the container
```
git clone https://github.com/harjindersingh1123/FSMtextSimplified.git
docker build -t fsmtextsimplified:latest .
docker run -p 5000:5000 fsmtextsimplified:latest
```
## use the following commands to run without container(Have python 3 installed first)
```
git clone https://github.com/harjindersingh1123/FSMtextSimplified.git
pip install -r requirements.txt 
cd FSMtextSimplified/src
python app.py
```
