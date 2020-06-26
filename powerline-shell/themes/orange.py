# this theme file placed in "~/.config/powerline-shell/themes/soft-era.py"
# this is a powerline shell theme for use with soft-era iTerm2 theme: https://github.com/soft-aesthetic/soft-era-iterm2

# dark colors:
# 0  black
# 1  darker red (salmon)
# 2  green
# 3  light pink
# 4  blue
# 5  violet?
# 6  purple
# 7  light bg color

# light colors:
# 8  deep purple
# 9  lighter read (coral)
# 10 green
# 11 yellow
# 12 blue
# 13 violet?
# 14 purple
# 15 white

from powerline_shell.themes.default import DefaultColor

class Color(DefaultColor):
    RESET = -1

    USERNAME_FG = 15 #hvit
    USERNAME_BG = 166 #dark orange
    USERNAME_ROOT_BG = 2

    # HOSTNAME_BG = 14
    HOSTNAME_FG = 16 #dark gay
    HOSTNAME_BG = 172 #normal orange

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 2  # siiste
    HOME_FG = 236  # white
    PATH_BG = 237  # dark grey
    PATH_FG = 250  # light grey
    CWD_FG = 254  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 124
    READONLY_FG = 254

    SSH_BG = 166  # medium orange
    SSH_FG = 254

    REPO_CLEAN_BG = 166  # a light green color
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 11  # pink/red
    REPO_DIRTY_FG = 16  # white

    JOBS_FG = 202
    JOBS_BG = 238

    CMD_PASSED_BG = 234 #aller siste biten
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 161
    CMD_FAILED_FG = 15

    SVN_CHANGES_FG = REPO_DIRTY_FG
    SVN_CHANGES_BG = REPO_DIRTY_BG

    GIT_AHEAD_BG = 7
    GIT_AHEAD_FG = 4
    GIT_BEHIND_BG = 7
    GIT_BEHIND_FG = 6
    GIT_STAGED_BG = 7
    GIT_STAGED_FG = 2
    GIT_NOTSTAGED_BG = 7
    GIT_NOTSTAGED_FG = 5
    GIT_UNTRACKED_BG = 7
    GIT_UNTRACKED_FG = 5
    GIT_CONFLICTED_BG = 7
    GIT_CONFLICTED_FG = 1
    GIT_STASH_BG = 7
    GIT_STASH_FG = 6

    VIRTUAL_ENV_BG = 7
    VIRTUAL_ENV_FG = 2

    BATTERY_NORMAL_BG = 7
    BATTERY_NORMAL_FG = 2
    BATTERY_LOW_BG = 7
    BATTERY_LOW_FG = 1

    AWS_PROFILE_FG = 15
    AWS_PROFILE_BG = 2

    TIME_FG = 15
    TIME_BG = 10
