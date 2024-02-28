# Before Start :checkered_flag:

> [!WARNING]
> I'm using python 3.10.11 here :snake:
> [Python Download](https://www.python.org/downloads/).
> *For tutorial install [click](https://www.youtube.com/watch?v=t3jhhAuGygs)*:eyes:
$~$
## Step 1 : Install Virtual Environment
### 1. Make a _*Virtural Environment*_ in your computer
### 2. Open CMD and click <code>pip install venv</code>
        pip install venv

$~$
## Step 2 : Activate Virtual Environment
### 1. Choose your folder 
   ####     Example : 
   ####     <code>C:\ </code> or
   ####     <code>D:\ </code> or 
   ####     <code>E:\ </code> or

### 2. And Then make a folder for virtual environment <code>python -m venv (name_your_folder)</code>
        python -m venv (name_your_folder)
	
### 3. Activate Virtual Environment, *Make sure you have entered the venv folder*
        .\Scripts\activate
###   or
        name_your_folder\Scripts\activate

> [!TIP]
> There issue <code>execution of scripts is disabled on this system</code>

### 1. Press the <code>Windows</code> button and then type <code>PowerShell</code>
### 2. Click <code>Run as Administrator</code>
### 3. **Copy** and **Paste** the following command and hit <code>Enter</code>
		Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
 
### 4. Type <code>Y</code> and hit <code>Enter</code>
### 5. Rerun the command and type <code>A</code> hit <code>Enter</code>
### 6. Close the powershell and try again like number 3 :hourglass:
### 5. If <code>(Name_Folder)C:\>Name_Folder></code>, venv active :rocket:

$~$
## Step 3 : Clonning Program Exist

### 1. Go to [Repositories Camera Vision YOLOv8 Project](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project)
### 2. Open <code>Code</code> on <code>HTTPS</code> ![Like a documentation](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%201.png) and the copy <code>https://github.com/rakhazl/Camera-Vision-YOLOv8-Project.git</code>
	https://github.com/rakhazl/Camera-Vision-YOLOv8-Project.git
 
### 3. Open your venv in cmd earlier <code>(Name_Folder)C:\>Name_Folder></code>, typing <code>git clone</code>
	git clone
 
 ### and then paste <code>https://github.com/rakhazl/Camera-Vision-YOLOv8-Project.git</code>, so it could be...
 	git clone https://github.com/rakhazl/Camera-Vision-YOLOv8-Project.git
  
### 4. Make make sure it looks like... ![the picture](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%202.png)
### 5. And Click <code>Enter</code> :dizzy:

### And then... :sparkles: ![Congrats](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%203.png) 
$~$
## Step 4 : Running Program 
$~~~~~~~~~~~$
### _*There are 3 ways to Open Visual Studio Code*_ In this tutorial, the folder name is <code>clip-roof-toso</code>
$~~~~~~~~~~~$
### *The First Way*
### 1. Please direct to the folder link, like a picture ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%204.png)
### 2. Typing <code>cmd</code>
        cmd
### ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%205.png)
### 3. Then the command prompt will open, and then typing <code>code .</code>
        code .
### ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%206.png)
### 4. Then will open <code>Visual Studio Code</code>
$~~~~~~~~~~~$
### *The Seccond Way*
### 1. From *Step 3 No. 5*, direct typing <code>code .</code>
        (Name_Folder)C:\>Name_Folder>code .
### Like a picture below ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%207.png)
$~~~~~~~~~~~$
### *The Third Way*
### 1. Open <code>Visual Studio Code</code>, Then the display will look like this. Click <code>Open Folder</code> ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%208.png)
### 2. Select the folder that was downloaded from GitHub earlier ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%209.png)
### 3. Yes, Correct... ![](https://github.com/rakhazl/Camera-Vision-YOLOv8-Project/blob/main/doc%20for%20tutor/step%2010.png)
$~~~~~~~~~~~$
### If you want Install Library, Check your connection :signal_strength:
###        Go into the folder <code>cd</code> C:\Name_Folder 
        cd
###        next step 1, if C:\>Name_Folder>
###        next step 2, copy <code> .\Scripts\activate </code> for <code> (Name_Folder)C:\>Name_Folder> </code>
        .\Scripts\activate
###        next step 3, install ultralytics <code> (Name_Folder)C:\>Name_Folder>pip install ultralytics </code>
        pip install ultralytics
###        next step 4, install yolov8 <code> (Name_Folder)C:\>Name_Folder>pip install yolov8 </code>
        pip install yolov8
###        next step 5, install flask <code> (Name_Folder)C:\>Name_Folder>pip install flask </code>
        pip install flask
###        next step 4, install roboflow _(opsional)_ <code> (Name_Folder)C:\>Name_Folder>pip install roboflow </code>
        pip install roboflow

> [!NOTE]
> You completed the first step :dancers: :clap:

