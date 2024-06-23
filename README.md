I. Overview:
  KOTASTU is an innovative device that helps people with hand disabilities control home appliances and computers with their feet. 
  The system includes a foot-controlled mouse and a chair that integrates advanced functions such as voice control and facial recognition.
II. Source code include 2 parts:
  Part 1: App voice recording 
    This app will recieve voice from user and enter words into computer or control device by voice via the internet (sever Blynk).
    App is coded by Python programming language. Code on Visual Studio Code then export by command on terminal, this command is "pyinstaller --onefile --noconsole --icon=[file name icon] [file name program].py".
    After export .exe file. Compressed file .zip by RAR and add to NSIS app export to file installer.
  Part 2: Web control device
    This web used to control device, set time auto on or off and call to optional phone number, the data will send to sever Blynk.
    Web is coded by HTML, CSS and JavaScript. Code on Visual Studio Code. Web can run local host or public on Github. 
III. Owned:
  This source code is owned and written by SevKan (Khuu Trieu Minh Khang)
