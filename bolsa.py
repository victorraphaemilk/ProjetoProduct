import webbrowser
import subprocess

def executar():
    url = 'https://drive.google.com/drive/u/2/folders/17IleJxtRH3kBimYLjIkf0xk6hqEkWV7c'
    webbrowser.open(url)
    
    subprocess.run(['/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=pomodoro io.gitlab.idevecore.Pomodoro'], shell=True)
    