# Todoist to Ticktick CSV converter

Simple script to convert an exported Todoist board of task to be imported on Ticktick app.

## Motivation

I got a checklist to follow, but was exporeted from Todoist, since I get used to Ticktick, 
I do not want to setup a new Todoist account just to use it. As an alternative, Ticktick already
provides a [migration](https://help.ticktick.com/articles/7055781474263367680) to import directly, although I don't want to use it either.

## Usage

> Use Python `v3.10^`, no dependencies.

Run:

```sh
$ python main.py <exported csv from todoist> <list name to add on ticktick>
```

It will generate a file called `ticktick_to_import.csv` at repo root directory.


Import on TickTick.
