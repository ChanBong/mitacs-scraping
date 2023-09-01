# mitacs-project-scraper

-------

This is a utility for extracting projects from [MITACS project page](https://globalink.mitacs.ca/#/student/application/projects) 

If you just need the extracted list, download the latest excel file [here](results)


## Running on local machine

Works fine on linux based system, could be dicey on windows

- Install packages from `requirements.txt`
- Make sure you have google-chrome installed on the machine
```bash
sudo apt-get update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
- run `extract.py`