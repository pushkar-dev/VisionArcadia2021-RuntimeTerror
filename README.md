# Vision Arcadia
## Team- Runtimeterror
## Members-
1. Vishesh Soni
2. Aditya Prakash
3. Ravneet Kaur
4. Pushkar Patel
5. Ayush Nigam

# Setting Up environment
1. Make sure you have latest (3.8+) python installation, and python and pip are added to path.
2. make a new folder and cd to that folder
   ```bash
   mkdir <dirname>
   cd <dirname>
   ```
3. Clone the repository in you local machine by executing
   ```bash
   git clone https://github.com/pushkar-dev/VisionArcadia2021-RuntimeTerror.git
   ```
4. Make a virtual environment
   ```bash
    virtualenv <name>
   ```
    you may need to install virtualenv first using pip.
5. Activate the environment
   ```bash
   <name>\Scripts\activate.ps1
   ```
   for cmd
   ```bash
   <name>\Scripts\activate
   ```
6. Install all the dependencies.
   ```bash
   pip install -r requirements.txt
   ```
   It may take a while.
9. Run the program 
   ```bash
   python interpreter.py
   ```
   now start showing gestures

# Instructions for Use
1. It will take a few seconds for camera to start, so that user gets ready.
2. Gesture list and gesture language are shown below.

# Gestures
There are 5 gestures<br>
5![image](https://user-images.githubusercontent.com/79650452/135390350-7da512c9-4529-4820-8f7a-d6e3af0de9d1.png)<br>
3![WhatsApp Image 2021-09-30 at 10 21 38 AM](https://user-images.githubusercontent.com/79650452/135390383-43e6b2ae-a09a-4768-847c-9cdf769f5efc.jpeg)<br>
2![WhatsApp Image 2021-09-30 at 10 22 04 AM](https://user-images.githubusercontent.com/79650452/135390398-9dc742e3-e280-4e8d-b1e0-2e7434a390b0.jpeg)<br>
1![WhatsApp Image 2021-09-30 at 10 22 56 AM](https://user-images.githubusercontent.com/79650452/135390418-cd667beb-eec2-448b-9a26-c8d6853b8f56.jpeg)<br>
0![WhatsApp Image 2021-09-30 at 10 25 05 AM](https://user-images.githubusercontent.com/79650452/135390435-988ddeb0-a387-403c-b1f5-bbd7ac56b33e.jpeg)<br>
One auxilary gesture reserved for only noise

# Gesture Language
1. c1 5,1,0 volume up
2. c2 5,2,0 volume down
3. c3 5,3,0 brightness up
4. c4 5,1,2,0 brightness down
5. c5 5,1,3,0 screenshot
6. c6 5,2,1,0 scroll up
7. c7 5,2,3,0 scroll down
8. c8 5,3,1,0 press enter
9. c9 5,3,2,0 press space
10. c10 5,1,2,3,0 zoomin
11. c11 5,2,3,1,0 zoomout
12. c12 5,3,1,2,0 open / close calender

All codes used in training models and making training dataset re present in model_train directory.
