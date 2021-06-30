<h1>Bear Lang!</h1>
<p>Very simple scripting language, to create scripts, you can either make a .txt file, or .bearL file.
There is an example script in the testingLang.txt file.
I'm still working on this. This is not complete and still needs work.
Thanks,
     BizzyPythonBear
     A.k.a. Michael</p>
     
<h3>Running Scripts</h3>
<p>To run scripts, all you have to do is run the shell, by typing 'python3 shell.py' inside of the directory that contains the shell.py file.
 Then, once the shell has opened you should see text that says, 'Bear Lang > ', this is how you know you're in the shell. Here is where you can type RUN("NameOfYourScriptFile.txt"). Like I said before, this also works with files that have a .bearL extension.</p>

<h3>Features</h3>
<p>This language has a decent amount of features. I don't want to list them cause thats too hard though, but theres functions, for loops, while loops, variables, printing, and more. You can look at the example code as well, I'll try to add as much to it as possible to show all the features. But to sum it up the features this lang has are pretty basic, and this is pretty much as basic as it gets. It's essentially a BASIC dialect.</p>

<h3>Extras</h3>
<p>To see some of the commands, when you run the shell you can type, "Help" to see a brief summary of the basic commands you'll need to use to be able to run your programs. Btw, I'll make it so you can ONLY run .bearL files as soon as I can. But right now its just easiest to just not check if the file has the extension, and just going with any plain text file. The .bearL extension is NOT required, but it's recommended because I haven't tested the shell with using file extensions like .py, .c, .cc, etc. Nevermind, I tested but im not gonna delete the previous text cause its too hard. It works with every file extension, it just has to match the Bear-Lang syntax.</p>
<h4>Disclaimer: This is not a recommended programming language, it's simply a fun project to work on in my spare time. Though, in the future this could become a very useful language once I expand it.</h4>
<h3>Using the Shell outside of the root shell.py directory</h3>
<p>Really quick before I tell you how to use the shell outside of the main, bear-lang directory, you'll need to install Pyinstaller via the ```pip3 install pyinstaller``` command. Or, you can skip to the, "People Without Python Installed" Section. Once you have installed pyinstaller, make sure your in the bear-lang directory, and then run ```pyinstaller bearLangShell.py``` Once it has finished compiling the exe, add an enviornment variable that leads to the /dist/shell folder. For example, ```C:\Users\name\Documents\Bear-Lang\dist\shell\``` Once you have done that, you can open up a command prompt window and type, ```bearLangShell```, and it should open up the shell for you, completely eliminating the hassle of entering the Bear-Lang directory and having to run the bearLangShell file which also requires python to run.</p>
<h5>People Without Python Installed</h5>
<p>If you don't have python installed, I have included the ```/dist/shell``` directory you could just add to the PATH. Make sure to NEVER delete any of the files inside of the /dist/shell directory, this will break the software, and make it unusable. Once again, when you run command prompt or powershell, you can then run, ```bearLangShell``` to open the shell, without having to be in the root Bear-Lang Directory.</p>