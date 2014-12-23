# MANAGED BY DOTFILES
export EDITOR="nano"
alias lsa='ls -AF'
alias ls='ls -F'
alias lsl='ls -lF'
alias lsal='ls -AlF'
alias sha1='openssl sha1'
alias md4='openssl md4'
alias opena='open -a'
alias size='du -hs'
alias review="git push gerrit HEAD:refs/for/master"
alias rl2="git push gerrit HEAD:refs/for/RL2"
alias gfetch="git fetch origin; git checkout origin/master"
alias gcom="git checkout origin/master"
alias labs="mosh legoktm@tools-login.wmflabs.org"
alias reginald="mosh legoktm@reginald.uncy.org"
alias hhvmsh="exec hhvm --mode debug --debug-host ::1"
alias py2="source ~/python/bin/activate"
alias py3="source ~/python3/bin/activate"

# pip bash completion start
_pip_completion()
{
    COMPREPLY=( $( COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   PIP_AUTO_COMPLETE=1 $1 ) )
}
complete -o default -F _pip_completion pip
# pip bash completion end

if [ -f ~/.bash_profile_os ]; then
    . ~/.bash_profile_os
fi
