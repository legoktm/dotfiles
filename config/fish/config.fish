set -x EDITOR nano
set -x PATH "$HOME/gogs/bin:$HOME/.cargo/bin:$PATH"
set -x DEBEMAIL "legoktm@debian.org"
set -x DEBFULLNAME "Kunal Mehta"
set -x ROCKET_CLI_COLORS false
set -x PHAN_DISABLE_XDEBUG_WARN 1
set -x JENKINS_USERNAME "legoktm"
set -x QUBES_GPG_DOMAIN vault-gpg
set -x USE_PODMAN 1
set -x FPF_USERNAME legoktm
set -x SOPS_USERNAME legoktm
set -x SOPS_GPG_EXEC "qubes-gpg-client"
