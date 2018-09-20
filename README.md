# school_of_ai_KaggleTeam_GS-Salt-Identification-Challenge

Hi Team, the competition in which we will participate is this one https://www.kaggle.com/c/tgs-salt-identification-challenge.

We will mainly use convolutional neural networks. The programming language I think is the best for us is python (but you are in any case free to use the language you prefer)
In this competition we have to identify if a subsurface target is salt or not, in particular the goal of the competition is to segment regions that contain salt. 

The training data is composed of images(101 x 101 pixels ) similar to X-ray with associated masks (they are binary images that indicate the presence of salt), 
and in addition to the seismic images, it is provided for each image the depth of the imaged location. <a href="https://www.kaggle.com/meaninglesslives/data-exploration">Here</a> you can find an explorative notebook.

****
The most used network topology in this competition is the U-net, it's like an encoder-decoder network. 
For this reason these are the steps we must take:
<ol>
  <li> Become a member of <a href="https://www.kaggle.com/c/tgs-salt-identification-challenge/team">school_of_AI</a> Kaggle's team </li>
  <li> Try to optimize the hyperparameters of the U-net network. Share your scores and your tips/hyperparameters on the slack channel or on the school_of_AI Kaggle's team (share your kernels) </li>
  <li> Once we reach good scores we can create other networks other than U-NET </li>
</ol>
  
****
