export ZSH="$HOME/.oh-my-zsh"
export EDITOR="nvim"

ZSH_THEME="ys"
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

alias mutt="neomutt"
alias news="newsboat"
alias ls="eza -b -l -g -a -h --icons=always --group-directories-first"
alias du="ncdu -r -e --show-mtime --show-percent --color dark-bg --group-directories-first --sort name-asc"

