Hi, you in order for everything to work, you need a few dependencies. For windows users, just run the Interfacesetup.bat

After that run the following commands in Anaconda powershell (start as administrator)
LINE BY LINE

pip install googletrans==3.1.0a0
pip install OpenNMT-py
pip install PySimpleGUI
pip install flask

After running this, you can in theory run the GUIToOrchest.py file, and 
talk to the Jackie Chan bot. Only in English, since you have not set up the translation server yet.

To install the server, you need torch.
For this you need to check your CUDA version (very important, we don't want fried pc)
to do that run the following command in anaconda: nvidia-smi
It will show you a lot of stuff, but the CUDA version should be in the top right
If it is 10.2 run this:
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
If it is 11.3 or higher run this:
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch

After installing all the packages, do the following (in the anaconda powershell prompt)

Now type cd and then the path to your JackieChanSystem folder (after having extracted it).
Then type python GUIToOrchest.py (press tab to autocomplete the name, so you are sure that it has the right file)
Then open a new anaconda powershell (you need to have 2 open at this point).
Navigate to the JackieChanSystem folder
Then type: 
python server.py --ip "0.0.0.0" --port 5000 --url_root "/translator" --config "./available_models/conf.json" 
This should open up the translation server.
Once this is open you can also use dutch sentences, which will be automatically translated :D

Enjoy :)