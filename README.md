![](https://github.com/purbayankar/YouCure/blob/main/Health_Care_Unit/static/Webp.net-gifmaker.gif)


**YouCure will predict diseases based on your symptoms and will give descriptions so that you get healed fast**

The **Goal** of the project is to create a platform to know your symptoms and inform you about your disease, so that
you can appoint a doctor with proper specialization, and it will also help you find your nearby hospitals.

This app is made using Flask and so you can use it in both mobile and pc.

**So let's help each other.**


                                      😃Hit that ⭐ button to show some ❤️           

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites


```
Any Code Editor (VS Code preferred)
Python version 3.7 or higher
The latest version of Git
A PythonAnywhere Account (for deploying the project on a live system)
```

### Development Environment Setup: Windows


<details><summary>Step 1 : Downloading and Installing the Code Editor</summary>
 
 
| **Code Editor** | **Link** 	|
|-	|-	|
| Visual Studio Code 	| [Download it from here](https://code.visualstudio.com/)	|
| Sublime Text 3 	| [Download it from here](https://www.sublimetext.com/3) |
| Atom 	| [Download it from here](https://atom.io/)	|


</details>


---


<details><summary>Step 2 : Installing Python 3.7</summary>
 
 
* **For Windows** :  Click on [Download Python3.7](https://www.python.org/downloads/release/python-379/).
   * * Download the Windows x86-64 executable installer for the 64-bit version of Windows
   * * Download the Windows x86 executable installer for the 32-bit version of Windows.


   * * Make sure to check "Add Python 3.7 to Path" in the setup window of the Installer.

Verify the installation from the command prompt using the following command :
```
python3.7 --version
```
And the installed version of python will be printed.


</details>


---

<details><summary>Step 3 : Installing Git </summary>

Click on [Download Git](https://git-scm.com/downloads)

</details>


---


<details><summary>Step 4 : Fork the Repository </summary>

Click on ![Fork](https://user-images.githubusercontent.com/63921263/110382285-b07bba80-8080-11eb-8407-d354849c1753.png)
to fork [this Repo](https://github.com/chiraag-kakar/sharenlearn)

</details>


---



<details><summary>Step 5 : Creating Project Directory </summary>


(Note: We are creating a project directory on the desktop for easy and fast access)

```
cd desktop

mkdir myproject

cd myproject
```

</details>


---


<details><summary>Step 6 : Cloning Repository using Git</summary>
 
 
```
$ git clone https://github.com/<your-github-username>/sharenlearn.git
```


</details>


---


<details><summary>Step 7 : Change directory to sharenlearn</summary>
 

```
$ cd sharenlearn
```


</details>


---


<details><summary>Step 8 : Add a reference to the original repository
</summary>
 

```
$ git remote add upstream https://github.com/chiraag-kakar/sharenlearn.git
```


</details>


---


<details><summary>Step 9 : Creating Virtual Environment</summary>

Install virtualenv 
```
$ pip3 install virtualenv
```
Creating Virtual Environment named "myvenv" :
```
$ virtualenv myvenv -p python3.7
```
Activating "myvenv" :
* For **Windows cmd** :
   ```
   > myvenv\Scripts\activate
   ```
Command to deactivate "myvenv" :
```
deactivate
```


</details>


---


<details><summary>Step 10 : Installing Requirements</summary>


Note: Virtual Environment should be activated.

Installing requirements :
```
pip install -r requirements.txt
```


</details>


---


<details><summary>Step 11 : Creating Superuser and making database migrations to access the default Admin Panel</summary>
 
 
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


</details>


---


<details><summary>Step 12 : Running the Project in local server</summary>


Note: Virtual Environment should be activated.


Run the following command in the terminal :
```
python manage.py run server
```


</details>


---


### 💡️ **Pro Tip!** 
  * Always keep your master branch in sync with the main repository (by running `$ git pull upstream master` on your local master branch). 
  * Always create a new branch before making any changes (`$ git checkout -b <new-branch-name>`), never ever make any changes directly on the master branch.


## Congratulations on setting up the project locally.


---

# Engage in the [Discussions](https://github.com/purbayankar/YouCure/discussions) for more questions.

### Contributing
Please see the [Code of Conduct](https://github.com/purbayankar/YouCure/blob/main/CODE_OF_CONTACT.md) before contributing.

## 🌟 Contributors 

Thanks to these wonderful people ✨✨:

<table>
	<tr>
		<td>
			<a href="https://github.com/purbayankar/YouCure/graphs/contributors">
  				<img src="https://contrib.rocks/image?repo=purbayankar/YouCure" />
			</a>
		</td>
	</tr>
</table>

## AUTHOR : [Purbayan Kar](https://github.com/purbayankar) [Anik Chatterjee](https://github.com/starboi2000) [Sagnik Basu](https://github.com/Swagnick99)


