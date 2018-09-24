![alt text](https://github.com/Fede2000/school_of_ai_KaggleTeam_GS-Salt-Identification-Challenge/blob/master/logo.png?raw=true)
# KaggleTeam   GS-Salt-Identification-Challenge


Hi Team, the competition in which we will participate is this one https://www.kaggle.com/c/tgs-salt-identification-challenge.

We will mainly use convolutional neural networks. The programming language I think is the best for us is python (but you are in any case free to use the language you prefer)
In this competition we have to identify if a subsurface target is salt or not, in particular the goal of the competition is to segment regions that contain salt. 

## Getting Started
### Data
The training data is composed of images(101 x 101 pixels ) similar to X-ray with associated masks (they are binary images that indicate the presence of salt), 
and in addition to the seismic images, it is provided for each image the depth of the imaged location. <a href="https://www.kaggle.com/meaninglesslives/data-exploration">Here</a> you can find an explorative notebook.

### Work Enviroment
If you do not have a pc (with a good nvidia video card), I recommend you use <a href="https://colab.sandbox.google.com/">Google colab</a>, or internal kaggle's Kernels. 
We will use this repo as file container

### Resource
<ul>
  <li> https://www.depends-on-the-definition.com/unet-keras-segmenting-images/  </li>
  <li> Medium general explanation:   https://medium.com/@keremturgutlu/semantic-segmentation-u-net-part-1-d8d6f6005066 </li>
  <li> Siraj's video: https://www.youtube.com/watch?v=jm8IBBK   </li>
  <li> Siraj's file: https://github.com/llSourcell/Kaggle_Challenge_LIVE/   </li>
  <li> Data exploration Kaggle kernel: https://www.kaggle.com/meaninglesslives/data-exploration  </li>
  <li> Clean Workflow in Keras Kaggle kernel: https://www.kaggle.com/wrosinski/clean-workflow-in-keras  </li>
  <li> scoring-metric explanation:https://www.kaggle.com/pestipeti/explanation-of-scoring-metric </li>
  
</ul>
  

## Plan
The most used network topology in this competition is the U-net, it's like an encoder-decoder network. 
For this reason these are the steps you must take:
<ol>
  <li> Become a member of <a href="https://www.kaggle.com/schoolofai">school_of_AI</a> Kaggle's team ** </li>
  <li> Try to optimize the hyperparameters of the U-net network and to do data augmentation if necessary. Share your scores and your tips/hyperparameters on the slack channel or on the school_of_AI Kaggle's team (share your kernels). Use "/scoring metric" for model evaluation </li>
  <li> Once we reach good scores we can create other networks other than U-NET </li>
  <li> Try to combine multiple models </li>
</ol>
  
****
****


## Warnings
** <b>KaggleTeam can only perform 5 submissions per day</b>, so if you are a member of the kaggle team pay attention before sending predictions ( ask before sending on the Slack channel ). 
****
If you have a personal kaggle account keep in mind that submissions made with that account outside the KaggleTeam and then used in kaggle team may cause the disqualification of the team
