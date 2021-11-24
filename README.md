# Jackie Chan System

Jackie Chan System is a [Ai21](https://www.ai21.com) powered chatbot system, capable of answering all your Jackie Chan related questions. It also features the ability to process English as well as Dutch input sentences, by automatically translating it using a tranformer neural network by [Open NMT](https://opennmt.net). In order to train our network we used a subset of a dataset provided by [OpenSubtitles](http://www.opensubtitles.org/
)

<center style="padding: 40px"><img width="70%" src="https://github.com/chiayinglu/Jackie_Chan_System/blob/main/FlowDiagram.png" /></center>
Before raising an issue, make sure you read the requirements and the documentation examples.


----


Table of Contents
=================
  * [Setup](#setup)


## Setup

Jackie Chan System requirements:

- Python >= 3.6
- PyTorch == 1.6.0
- googletrans == 3.1.0a0
- OpenNMT-py == 2.2.0
- flask == 1.1.2
- PySimpleGUI

Install all requirements 
```bash
pip install googletrans==3.1.0a0
pip install OpenNMT-py == 2.2.0
pip install PySimpleGUI
pip install flask == 1.1.2
```



