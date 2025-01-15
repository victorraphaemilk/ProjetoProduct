import subprocess
import webbrowser

def estudos():
    url = 'https://www.udemy.com/home/my-courses/learning/'
    webbrowser.open(url)
    url = 'https://asoftmurmur.com/'
    webbrowser.open(url)

    subprocess.run(['/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=obsidian.sh --file-forwarding md.obsidian.Obsidian @@u %U @@ & /usr/bin/flatpak run --branch=stable --arch=x86_64 --command=pomodoro io.gitlab.idevecore.Pomodoro & /usr/share/code/code'], shell=True)
    