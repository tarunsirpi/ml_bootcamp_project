# create virtual env & activate

```
conda create -p env_name python=3.8 -y
```

```
source activate ./env_name
```

# setup git repo

```
git init
git add .
git commit -m "commit messsage"
git branch -M main
git remote add origin <repo url>
git push -u origin main
```

# install requirements

```
python setup.py install
```

or

```
pip install -r requirements.txt
```

```
add secrets to Github actions

```
