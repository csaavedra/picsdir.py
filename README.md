# picsdir.py
A python script to sort pictures by date creation

This is a very simple script that will read the exif creation date
from all pictures in a directory and sort them into different
directories using the date as directory name. It can also 
add a suffix to each directory.

## Why?

I use this script to sort pictures straight from my
camera onto my photo archive. I like to have a directory
per day. I started using this in 2008, go figure if it 
makes any sense anymore, but I still use it to this day.

## How?

Say you have a directory `photos/` with pictures from
your christmas holiday and you want to sort them and store
them in your `/media/disc/photos/` folder. Just do:

```
  $ picsdir.py photos/ /media/disc/photos/ christmas
```

to have the script do its magic. The pictures will
be moved to directories like:

```
   /media/disc/photos/2021-12-24-christmas
   /media/disc/photos/2021-12-25-christmas
   /media/disc/photos/2021-12-26-christmas
   /media/disc/photos/2021-12-27-christmas
```

and so on.

## Disclaimer

Last but no least, use at your own risk! I only put this 
on github so as not to have copies of the script lying 
around in my computers.
