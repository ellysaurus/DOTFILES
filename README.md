# MY LINUX DOTFILES.
In here you will find my config files, themes, custom scrips i use, ascii art and more.

At the moment the window manager i live in, Is [Qtile](https://github.com/qtile). If you want more info info about Qtile. Read about it on their github (that i linked), or at [Qtile.org](http://www.qtile.org/). 

All my wallpapers can be found in my imgur imagegallery at the bottom. in the album there are multiple wallpapers fitting my theme and colorscheme. and i add more there from time to time.



# Custom Browser homepage
I also made a custom homepage. i tried to make it very minimal. with just links to what i use the most on the web. some entertainment, some social media, and some stuff for when i need to look stff up about linux.

There is some javascript/jquery. so if you are a mini Richard Stallman and afraid of javascript. then thats fine. just remove that part. but the clock is also javascript so i guess u would remove that aswell.

Anyhow, the javascript portion is basicly my version of a news feed. its only tech news. Its using the so called "hackernews" api. its kind of a dumb name but a neat little thing. its basicly just a site that collect RSS and links by crawling the web for keywords related to tech. and then list the relevant articles

Its all styled to match the rice and theme. The css is very responsive to sizing. so pretty much any monitor size will look ok. the background image is on the rather larger side. thats because i have the image locally. and i have a lot of storage. if thats an issue for you. just remove the src for it in the .css file. as the static background is also styled to match everything. under is a screenshot, and a link to a _**video**_ showing how it looks in action.
![](https://i.imgur.com/qnSyfwM.png)
[Video](https://i.imgur.com/bJiGTEj.mp4)



# About my setup.

## Dependencies
there are some **dependencies** for my setup. that means that there are some stuff you have to install, if you are going to use my dotfiles. here are the most important.

_this section will be edited if i change stuff_
* **Dmenu** - Run / App launcher  [[Suckless]](https://tools.suckless.org/dmenu) [[AUR]](https://aur.archlinux.org/packages/dmenu-git/)
* **Psutil** - for statusbar net widget  [[pypi]](https://pypi.org/project/psutil/)
* **Picom** - Compisitor for opacity, shaddows & blur  [[github]](https://github.com/yshui/picom) [[AUR]](https://aur.archlinux.org/packages/picom-git/)
_and ofc there are some dependencies for qtile. but thats documented in their manuals and docs._


## My Default apps & more

| Web Browser | File Manager | Media Player | Text editor | Terminal | Image viewer |
|:-----------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| Brave (edge when it comes to linux) | Ranger(terminal) & dolphin(graphical) | Spotify(music) & VLC(video) | Vim | Alacritty | zxiv |

I Use **Manjaro** as my distro. as its fast to install. Thats really only the reason other than its what ive gotten used to now. I also have KDE Plasma installed. As its running games better without configuring stuff. Not that i game much on this setup anyways. but thats that.

| Vim Theme | Alacritty theme | ranger theme |
|:-----------:|:-------------:|:-------------:|
| miramare | slopeiz (my own theme) | jungle (uses terminal theme) |


### My welcome message in the terminal
in my terminal i have a custom message showing up everytime i open a terminal or refresh bash.
i have done this very simple. i just have a ```.txt``` file with the message / ascii art in.

```
  ┌─────────────────────────┐┌──────────────────────────── 降卋神通 ───────────────────────────────────┐
  │ 水善 - 土強 - 火烈 -气和││ Water is Benevolent, Earth is Strong, Fire is Fierce, Air is Harmonious │
  └─────────────────────────┘└─────────────────────────────────────────────────────────────────────────┘
  ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                                                                                                    │
  │ ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ██████╗  █████╗  ██████╗██╗  ██╗ │
  │ ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝ │
  │ ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗      ██████╔╝███████║██║     █████╔╝  │
  │ ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔══██║██║     ██╔═██╗  │
  │ ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    ██████╔╝██║  ██║╚██████╗██║  ██╗ │
  │  ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ │
  │                                                                                                    │
  └─────── walter  walter-manjaro ────────────────────────────────────────────────────────────────────┘
```
then i have an alias in my ```.bashrc``` that uses _cat_ to display it after it clears the screen and then i call that command at the bottom of my .bashrc. that basicly means i made a command that looks like this:
```
alias welcome='clear; cat welcome.txt'
welcome
```
and the result is like shown under.
![](https://i.imgur.com/Ht3IrcY.png)

## Colorscheme
![](https://i.imgur.com/2C9K99a.png)

So..his is my theme. i called it slopeiz. because thats my gamer alias.
not really much of inspiration i think. i mean im sure is more themes out there that kinda looks like this. ive used a lot of themes before. but no one really worked for me. I changed themes all the time. but i always really loved warm tones in my themes. its easier on the eyes. so thats one thing i kept in mind. i also liked some of the kinda matte google themes. they had good contrasts but also never too striking. and so thats really the only inspiration i think.

_i might update this theme and or make a seperate repo for this aswell. I will for sure be making a vim and airline theme for this in the future._
```
colors:
  # Default colors
  primary:
    background: '#1b1519'
    foreground: '#ffead6'

    # Normal colors
  normal:
    black:   '#1b181b'
    red:     '#fc5133'
    green:   '#80ac41'
    yellow:  '#fec72f'
    blue:    '#5f4494'
    magenta: '#3f201a'
    cyan:    '#7e5a5e'
    white:   '#ffead6'

  # Bright colors
  bright:
    black:   '#3a3634'
    red:     '#fc5133'
    green:   '#b4d973'
    yellow:  '#f8fd63'
    blue:    '#7b59c0'
    magenta: '#673225'
    cyan:    '#c3807a'
    white:   '#ffead6'
```


# Rice Screenshots
![](https://i.imgur.com/JHFocL7.png)
![](https://i.imgur.com/BrddZCd.png)
![](https://i.imgur.com/ZjGeULI.png)
![](https://i.imgur.com/EzuChRs.png)



# Wallpapers to fit this theme.
### Im going to be making more to fit the theme.
yes, they are all weeb wallpapers. i might make a seperate repo for these wallpapers to make it faster for people to get them.
_also, a little warning. these images are all 5000x2813 PNG files. therefore they are kinda large files._
[Wallpapers](https://imgur.com/a/CtcinnP)
