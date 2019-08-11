# wow-addon-updater

This utility provides an alternative to the Twitch/Curse client for management and updating of addons for World of Warcraft. The Twitch/Curse client is rather bloated and buggy, and comes with many features that most users will not ever use in the first place. This utility, however, is lightweight and makes it very easy to manage which addons are being updated, and to update them just by running a python script.

## First-time setup

This utility has two dependencies:

* A version of [Python](https://www.python.org/) 3.6+
* The [requests](http://docs.python-requests.org/en/master/) module

The install should be managed by [`pipenv`](https://github.com/pypa/pipenv). All you need to do is run the following:

```bash
cd wow-addon-updater/
pip install pipenv
pipenv install
```

## Running the utility

After performing the setup steps, `pipenv run` is used to execute the utility. To run from the command line, use:
```bash
pipenv run updater/WoWAddonUpdater.py
```

## Configuring the utility

The `config.ini` file is used by the utility to find where to install the addons to, and where to get the list of mods from.

The default location in Windows to install the addons to is `C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns`. If this is not the location where you have World of Warcraft installed, you will need to edit "config.ini" to point to your addons folder.

The standard addon location on macOS is `/Applications/World of Warcraft/Interface/AddOns`

The default location of the addon list file is simply `in.txt`, but this file will not exist on your PC, so you should either create "in.txt" in the same location as the utility, or name the file something else and edit "config.ini" to point to the new file.

The `config.ini` file also has two other properties that you may not need to change. `Installed Versions File` determines where to store the file that keeps track of the current versions of your addons, and I don't recommend changing that.

The `Close Automatically When Completed` property determines whether the window automatically closes when the process completes (both successfully and unsuccessfully). It defaults to "False" so that you can see if any errors occurred. If you run this utility as a scheduled job (e.g. upon startup, every x hours, etc), we recommend changing this to "True".

## Input file format

Whatever file you use for your list of mods needs to be formatted in a particular way. Each line corresponds to a mod, and the line just needs to contain the link to the Curse or WoWInterface page for the mod. For example:

```
https://www.curseforge.com/wow/addons/world-quest-tracker
https://www.curseforge.com/wow/addons/deadly-boss-mods
https://www.curseforge.com/wow/addons/auctionator
http://www.wowinterface.com/downloads/info24005-RavenousMounts.html
```
    
Each link needs to be the main page for the addon, as shown above.

If you want to extract a subfolder from the default downloaded folder (typically needed with Tukui addons), add a pipe character (`|`) and the name of the subfolder at the end of the line. For example, the ElvUI addon can be added as follows:

```
https://git.tukui.org/elvui/elvui|ElvUI
```

because the downloadable zip from this website contains a subfolder called "ElvUI" containing the actual mod.

## Contributing
Bring up the dev `pipenv` with:
```bash
pipenv install --dev
```

Run tests with:
```bash
pipenv run coverage run --source=updater -m unittest -v
```

See code coverage with:
```bash
pipenv run coverage report
```

1. Submit Issues, PR's, or make general comments
1. ????
1. Profit

## Thanks
Shout out to GitHub user [`kuhnertdm`](https://github.com/kuhnertdm) for establishing the base of this utility, and giving people an alternative to the wasteland of mainstream clients.
