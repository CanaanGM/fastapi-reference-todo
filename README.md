# this is meant to be an example

> this repo is a reference as well as a experiment to try developing **inside** docker-compose via VSC container thingy.
it is terrible, developing on the machine itself is faster, unless the language is shitty and refuses to work, like ruby.

---

### pros and cons of using this methos:

#### pros:
i. you don't need to install the language on ur machine, i thought this would replace pyenv but nope
ii. scince u're using docker, the env is the same across machines.

#### cons:
i. you need to keep installing the extensions u're using, like the language server.
ii. files created in the container **cannot** be modified from the parent VSC instance if u opened it from WSL2.
	i. i had to `chown <user>:<user> README.md` to be able to edit it from arch WSL2 xD
iii. environment is ephemeral; meaning u'd need to install all the deps everytime u spin it up, thankfully docker caches things.

