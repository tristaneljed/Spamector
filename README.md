# 📨 Spamector
![Made_with_love_by Tristan](https://img.shields.io/badge/Made_with_love_by-Tristan-orange.svg) ![Last_deployed November](https://img.shields.io/badge/Last_deployed-November-green.svg)
## 📮 A Spam Detector

- **Summary**

Text mining is a wide field which has gained popularity with the huge text data being generated. 
Automation of several applications like sentiment analysis, document classification, topic classification, text summarization, and machine translation has been done using machine learning models.

Spam filtering is an example of document classification task which involves classifying an email as spam or non-spam (a.k.a. ham) mail.

In this project, I will go through the different steps on how to implement this kind of systems in a form of a tutorial using Python, and a publicly available mail corpus.

The output would be an API and a web application allowing the user to enter a message and get a response if it's a spam or ham.


- **Data Source**

Enron Email Dataset

Link: https://www.cs.cmu.edu/~enron/


- **Python Libraries**

For the Flask App:

![nltk 3.2.4](https://img.shields.io/badge/nltk-3.2.4-green.svg)

![flask 0.12.2](https://img.shields.io/badge/flask-0.12.2-green.svg)

For the Jupyter Notebook:

![scikitlearn 0.19.1](https://img.shields.io/badge/scikitlearn-0.19.1-green.svg)

	
- **Structure**

```
Spamector
│	README.md
│	requirements.txt
│	app.py 
│	engine.py
│	Spamector.ipynb 
│	Spamector.html
│	nb_model.sav
│	nb_model.joblib
└───data
└───jupyter_images
└───static
│   └───css
│   └───img
│   └───js  
└───templates
```


- **Instructions - How to run Spamector**

1. Download the tarzip file.  
2. Extract the files.  
3. Start a terminal window and use cd to move to the Spamector folder.  
4. Run: `python app.py`
5. Open a web browser and type `127.0.0.1:5000`
6. Enjoy 😎


- **Instructions - How to run the Jupyter Notebook**

1. From the Spamector folder in the terminal window, start a jupyter notebook session.  
2. From Jupyter notebook, run the Spamector notebook.
3. Enjoy 😉

***
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a>
