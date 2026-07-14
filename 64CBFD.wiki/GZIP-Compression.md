Official [gzip](https://www.gnu.org/software/gzip/) versions up to (and including) `1.4` will generate matching compression.

As of the `1.5` release, compression does not match. This is due to a bugfix in gzip:

```
2012-03-18  Paul Eggert  <eggert@cs.ucla.edu>

    gzip: fix nondeterministic compression results
    Reported by Jakub Wilk in <http://bugs.debian.org/647522>.
    * deflate.c (fill_window): Don't let garbage pollute the dictionary.
```

and the following line of code:

```c
            /* Don't let garbage pollute the dictionary.  */
            memzero (window + strstart + lookahead, MIN_MATCH - 1);
```

If this line is removed, then we can get matching compression on the latest (1.10) gzip.