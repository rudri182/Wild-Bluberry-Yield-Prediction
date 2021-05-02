# Wild Blueberry Yield Prediction

## Problem definition :

The principal objective of this project is to assess the general significance of honey bee species arrangement and climate factors in managing wild blueberry agroecosystems in order to predict the yield of blueberry production. In particular, it will try to uncover what honey bee species structure and climate affect the yield and to foresee ideal honey bee species arrangement and climate conditions that accomplish the best yield. The requirement for this project arose as the production of blueberries required unique cross-pollination of bees with a proper environment.

### Team #Shiva's project :
#### Team members: Rudri Jani, Riya Shah, Vatsal Suthar, Yashil Depani, Harshil Mehta

The project trying to maximize the wild blueberry yield given the parameters

#### How the data is coming around???

The data is taken from [kaggle](https://www.kaggle.com/saurabhshahane/wild-blueberry-yield-prediction). The dataset can be found in ```/Dataset``` folder.

The dataset of 777 records with 18 different features like clonesize(the avg blueberry clone size in the field), honeybee(honeybee density in the field), bumbles(bumblebee density), fruitset(process in which flowers become fruit and potential fruit size is determined), fruitmass, seeds etc.

#### Yield Prediction Using Machine Learning

First the data is extracted using kaggle dataset. After some EDA and data cleaning and preprocessing, the feature selection is done. Using those features linear regression and XGBoost models are applied.

The code can be found in ```/Code``` folder.

The public URL for the code can be found [here](https://colab.research.google.com/drive/15dGil4ZugXXxC2OmvZFSSeNxSQaL1eKj?usp=sharing)

#### Model Deployment

The trained model is deployed on the IBM cloud. It returns the predictions.

#### Yield Prediction Using Reinforcement Learning

The idea is to maximize the yield by providing state and taking actions and find which actions are appropriate and maximize the reward *i.e* yield.

+ State: Fruitmass, Seeds
+ Action: Fruitset
+ Agent: Algorithm
+ Environment: Whole table which is our environment
+ Rewards: Maximizing the yield performing different actions on states

#### Code Flow

The highly correlated columns are selected as states and actions. Initially, there are 3 states and 6 actions. From the states, the new actions are predicted using DNN. These actions are merged to predict yield with given states using ANN.

The public of the code URL can be found [here](https://colab.research.google.com/drive/1XRMvYINMaqZTI9thFBsy5iFgJe2emJRq?usp=sharing).

#### Deployment on Heroku - User-Friendly website

A user-friendly yield prediction website is deployed on heroku and can be found [here](https://yield-prediction-rl.herokuapp.com/)

Feel free to fork this repository and create an environment and RL agent which maximizes the yield using a typical RL problem!
