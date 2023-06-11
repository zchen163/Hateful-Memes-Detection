# Hateful-Memes-Detection

This project works on Facebook Hateful Memes Challenges and aims at improving classification of memes through AI modeling technologies including ensembled algorithms, NLP transformer modeling and multimodal VisualBERT model. Our final model pre-trained on visualBERT and augmented data with single averaging ensemble shows the ROC-AUC is 0.7675 and Accuracy is 0.7111, which is slightly higher than an award winning model.

<img width="411" alt="image" src="https://github.com/zchen163/Hateful-Memes-Detection/assets/48006055/91b09ad0-c246-4f7e-8b26-acc742200df6">
Figure 1. Examples of Hateful Memes Dataset[2]

## Introduction

Memes have gained huge popularity over the past years. Although memes are oftentimes harmless and generated especially for humorous purposes, they have also been used to produce and disseminate hate speech to make communities more toxic, such as direct attacks on people based on race, ethnicity, national origin, religious affiliation, sexual orientation, sex, gender, and serious disease or disability. Recently it becomes a growing problem in modern society on social media platforms like Facebook, Twitter and Instagram. Due to the surge of the amount of malicious content it cannot be addressed by human inspection of every sample. In 2020, Facebook AI initiated a competition with focus on hateful memes classification.

![image](https://github.com/zchen163/Hateful-Memes-Detection/assets/48006055/d24ae16a-b152-4d8b-aed8-17249c820518)

Representation of Multimodal VisualBERT Model taken from reference paper[9]

## Experiment

Vairous multimodal framework (MMF) pre-trained models for vision and language research are compared. VisualBERT pre-trained on Conceptual Captions (CC) achievs hte best score among all models. Thus, VisualBERT is selected as our benchmark model for further fine-tuning. 

The following technologies are applied to the VisualBERT model: 

- Data Augmentation: 

Data augmentation are widely-used technologies in data expansion as state-of-the-art deep learning models typically have parameters in the order of millions, especially in image processing. In this project we carry out two data augmentation experiments and compare the result with established
model. The approaches are image modification including flipping and blurring, and addition of Memotion Dataset which contains 7k annotated memes with labels. 

<img width="444" alt="image" src="https://github.com/zchen163/Hateful-Memes-Detection/assets/48006055/0057911d-54a1-432c-abd6-e3f71e3b7ce4">

- Hyper




## References

[1] Kaiming He, Georgia Gkioxari, Piotr Doll´ar, and Ross Girshick. Mask r-cnn. In Proceedings of the IEEE international conference on computer vision, pages 2961–2969, 2017.
[2] https://www.drivendata.org/competitions/64/hateful memes/. Hateful memes: Phase 1. Facebook AI, 2020.
[3] https://www.drivendata.org/competitions/70/hateful-memesphase 2/leaderboard/. Hateful memes: Phase 2 leaderboard. Facebook AI, 2020. 
[4] https://www.facebook.com/communitystandards/hate speech. Community standards. Facebook, 2020.
[5] Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj Goswami, Amanpreet Singh, Pratik Ringshia, and Davide Testuggine. The hateful memes challenge: Detecting hate speech in multimodal memes. arXiv preprint arXiv:2005.04790, 2020. 
[6] Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh, and Kai-Wei Chang. Visualbert: A simple and performant baseline for vision and https://www.overleaf.com/project/6053c78eb5a9aa2d9f842a20language. arXiv preprint arXiv:1908.03557, 2019.
[7] Chhavi Sharma, William Paka, Scott, Deepesh Bhageria, Amitava Das, Soujanya Poria, Tanmoy Chakraborty, and Bj¨orn Gamb¨ack. Task Report: Memotion Analysis 1.0 @SemEval 2020: The Visuo-Lingual Metaphor! In Proceedings of the 14th International Workshop on Semantic Evaluation (SemEval-2020), Barcelona, Spain, Sep 2020. Association for Computational Linguistics.
[8] Amanpreet Singh, Vedanuj Goswami, Vivek Natarajan, Yu Jiang, Xinlei Chen, Meet Shah, Marcus Rohrbach, Dhruv Batra, and Devi Parikh. Mmf: A multimodal framework for vision and language research. https://github.com/ facebookresearch/mmf, 2020.
[9] Riza Velioglu and Jewgeni Rose. Detecting hate speech in memes using multimodal deep learning approaches: Prizewinning solution to hateful memes challenge. arXiv preprint arXiv:2012.12975, 2020. 
