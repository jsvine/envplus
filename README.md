# envplus

Combine your [Python virtualenvs](http://www.virtualenv.org/en/latest/virtualenv.html) into unlimited configurations.

Developed at BuzzFeed.

## Why Combine Virtualenvs?

Most of my projects are modular in nature. Yours probably are too. The large bulk of my projects involve some combination of:

- Web-scraping and data-fetching
- Data analysis
- Web development

For each of these tasks, [I've found a set of Python libraries](https://github.com/jsvine/virtualenv-recipes/) that fit my needs well. Rather than download and install SciPy for the nth time, wouldn't it be nice just to build on top of already-installed versions? Enter `envplus`.

## How It Works

`envplus` takes advantage of [Python's .pth file convention](https://docs.python.org/2/library/site.html). It creates (and manipulates) a special file, `_envplus.pth`, in the `site-packages` directory of your current virtualenv.

## Installation

```sh
pip install envplus
```

## Walkthrough

If you're like me, a lot of your projects involve fetching and parsing web pages. So let's build a virtualenv that contains a handy trio of packages for this task.

```sh
mkvirtualenv scraping
pip install requests
pip install lxml
pip install cssselect
```

For a lot of projects, you'll probably also want to store information in some sort of database. Let's make a bare-bones virtualenv for this task, too.

```sh
mkvirtualenv dbstorage
pip install dataset
```

Now let's say you're working on a project to scrape cat GIFs from BuzzFeed and store them in a database. Rather than reinstall all the packages above, you can just do this:

```sh
mkvirtualenv buzzcats
envplus add scraping dbstorage
```

Now you can use `requests`, `lxml`, `cssselect`, and `dataset` in your `buzzcats` virtualenv. The actions you take in the `buzzcats` virtualenv will not harm or alter your other virtualenvs. (Even if you run `pip uninstall`.) And upgrades to `scraping` and other `envplus add`'ed virtualenvs will become immediately available to `buzzcats`.


## Usage

To use `envplus`, [`virtualenvwrapper`](http://virtualenvwrapper.readthedocs.org/en/latest/) must be installed and __your target virtualenv must be currenlty activated__.

---

### envplus add [envs]

Make another virtualenv's packages available to your current virtualenv. Accepts multiple, space-separated virtualenv names.

```sh
envplus add scraping dbstorage
```

---

### envplus rm [envs]

Remove a previously added virtualenv from your current virtualenv. Accepts multiple, space-separated virtualenv names.

```sh
envplus rm scraping dbstorage
```

---

### envplus pause [envs]

"Pauses" previously added virtualenvs, so that they remain in `_envplus.pth` (as commented lines) but do not effect the current virtualenv. If virtualenv names are provided, only those are paused. Otherwise, all previously added virtualenvs are paused.

```sh
# To pause all
envplus pause
# To pause just one
envplus pause dbstorage
```

---

### envplus resume [envs]

Un-pauses previously added virtualenvs. If virtualenv names are provided, only those are resumed. Otherwise, all previously added virtualenvs are resumed.

```sh
# To resume all
envplus resume
# To resume just one
envplus resume dbstorage
```

---

### envplus ls [-p] [-a]

List added virtualenvs. By default, lists only *non-paused* additions. `-p` will list only *paused* additions, and `-a` will list *all* additions.

---

### envplus run [command]

Temporarily adds your virtualenvs' `bin`-paths to your current `PATH` before running `command`. Lets you use other virtualenvs' command-line programs.

```sh
# Create a dummy virtualenv with csvkit
mkvirtualenv csvtest
pip install csvkit

# Create newenv and add csvtest
mkvirtualenv newenv
envplus add csvtest

# While in newenv, run csvkit's csvcut command-line utility
echo "a,b,c" | envplus run csvcut -c 2
```

---

### envplus path

Print the path of the active virtualenv's `_envplus.pth` file.

```sh
envplus path
```

---

### envplus cat

Print the contents of the active virtualenv's `_envplus.pth` file.

```sh
envplus cat
```

---

### envplus edit

Open the active virtualenv's `_envplus.pth` file in your default editor. You probably shouldn't do this. Mostly for debugging purposes.

```sh
envplus edit
```

## Todos

- Add tests.
- Test on wider variety of systems and virtualenv(wrapper) versions.
