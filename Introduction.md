# JAVA

###install the PPA update source

```
sudo gedit /etc/apt/sources.list.d/webupd8team-java-trusty.list
append>>deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
        deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
save & quit
```

###add the key to the apt system

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <key>
```
The signature key can be found on the PPA:
https://launchpad.net/~webupd8team/+archive/ubuntu/java

###install the PPA update source

```
sudo gedit /etc/apt/sources.list.d/webupd8team-java-trusty.list
```
