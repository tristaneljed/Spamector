# Imports
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import random
import pickle

class SpamDetector:

	def createWordFeatures(self,words):
		"""
		Function
		--------
		createWordFeatures

		Create a dictionary that returns True for each word.

		Parameters
		----------
		words : list
		The list of words

		Returns
		-------
		resDict : Dict

		Example
		-------
		createWordFeatures(["the", "MIS 5470", "class", "has", "python", "and","R","modules"])
		
		{'MIS 5470': True,
		 'R': True,
		 'and': True,
		 'class': True,
		 'has': True,
		 'modules': True,
		 'python': True,
		 'the': True}
		"""
		resDict = dict( [ (word, True) for word in words] )
		return resDict
		
	def tokenizeCreateWordFeatures(self):
		"""
		Function
		--------
		tokenizeCreateWordFeatures

		Append a "ham" or "spam" at the end of each dictionary created by createWordFeatures function. 
		This is to tell the algorithm that this text is of type ham or spam.
		Merge spam and ham lists.
		Shuffle the result to make it randomised.

		Returns
		-------
		mergedList : list

		Example
		-------
		output = tokenizeCreateWordFeatures()
		print(output[0])
		
		({'Subject': True, ':': True, 'fw': True, 'nice': True, 'mhoter': True, 'fucking': True, 
		'top': True, 'of': True, 'the': True, 'morning': True, 'to': True, 'you': True, '!': True,
		')': True, 'matayaa': True}, 'spam')
		"""
		data_directory = "data"		
		hamList = []
		spamList = []
		for directories, subdirs, files in os.walk(data_directory):
			if (os.path.split(directories)[1]  == 'ham'):
				for fileName in files:      
					with open(os.path.join(directories, fileName), encoding="latin-1") as f:
						message = f.read()					
						words = word_tokenize(message)						
						hamList.append((self.createWordFeatures(words), "ham"))
			
			if (os.path.split(directories)[1]  == 'spam'):
				for fileName in files:
					with open(os.path.join(directories, fileName), encoding="latin-1") as f:
						message = f.read()						
						words = word_tokenize(message)						
						spamList.append((self.createWordFeatures(words), "spam"))
		mergedList = hamList + spamList
		random.shuffle(mergedList)		
		return mergedList

	def createTestTrain(self):
		"""
		Function
		--------
		createTestTrain

		Create test/train splits.

		Returns
		-------
		(trainingData, testData) : tuple
		"""
		mergedList = self.tokenizeCreateWordFeatures()
		trainingPart = int(len(mergedList) * .6)
		trainingData = mergedList[:trainingPart]
		testData =  mergedList[trainingPart:]		
		return (trainingData, testData)


	def createModel(self):
		"""
		Function
		--------
		createModel

		Create the naive Bayes classifier

		Returns
		-------
		classifier : nltk.classify.naivebayes.NaiveBayesClassifier
		"""
		trainingData, testData = self.createTestTrain()		
		classifier = NaiveBayesClassifier.train(trainingData)
		return classifier

	def saveModel(self):
		"""
		Function
		--------
		saveModel

		Save the model to disk

		Returns
		-------
		outputMsg : str
		
		Example
		-------
		saveModel()
		'Model saved successfully !'
		"""
		classifier = self.createModel()
		fileName = 'nb_model.sav'
		outputMsg = ""
		try:
			pickle.dump(classifier, open(fileName, 'wb'))
			outputMsg = "Model saved successfully !"
		except:
			outputMsg = "Error when saving model !"
		return outputMsg

	def predictMessage(self,msg):
		"""
		Function
		--------
		predictMessage

		Classify the message by telling if it is a ham or spam.

		Parameters
		----------
		msg : str
		A message we want to classify
		
		Returns
		-------
		str: 'ham' or 'spam'
		
		Example
		-------
		message = "Hi welcome to this session, please log in using your username and password then click on the start button."
		predictMessage(message)
		
		'ham'
		"""
		fileName = 'nb_model.sav'
		loaded_model = pickle.load(open(fileName, 'rb'))
		output_msg = ""
		words = word_tokenize(msg)
		output_msg = dict( [ (word, True) for word in words] )
		return loaded_model.classify(output_msg)




