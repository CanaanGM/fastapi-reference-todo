# this is meant to be an example

> this repo is a reference as well as a experiment to try developing **inside** docker-compose via VSC container thingy.
it is terrible, developing on the machine itself is faster, unless the language is shitty and refuses to work, like ruby.

---

> future me [check](./alembic-example/Alembic.md)

### pros and cons of using this methos:

#### pros:
1. you don't need to install the language on ur machine, i thought this would replace pyenv but nope
2. scince u're using docker, the env is the same across machines.

#### cons:
1. you need to keep installing the extensions u're using, like the language server.
2. files created in the container **cannot** be modified from the parent VSC instance if u opened it from WSL2.
	-  i had to `chown <user>:<user> README.md` to be able to edit it from arch WSL2 xD
3. environment is ephemeral; meaning u'd need to install all the deps everytime u spin it up, thankfully docker caches things.

---

### do better next time:
- make *docker-compose* run alembic DB creation on ***creation***, cause i couldn't make the `initdb.sh` script work.
- develop locally unless it's either a completly new language or a big ass ***self contained*** project.

---
this is a reference repo (again), anything that should be ignored in git is ***not***, cause i wanna be able to quickly reference it.
