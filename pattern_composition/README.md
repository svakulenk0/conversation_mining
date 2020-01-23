# Pattern composition 


## Input

File with traces, e.g., scs/original_scs.stringenc.txt:

```
Vd/&k/&kzvd/dM/&de&
VsHdMK:M%dM/:L%I!~"Mvs%d/!y|&kMv#QsLsHd/y&k&yvsvsH#Hs%d/:%y&klH&%v#%xd]Iu
Vs%d/G%y&y#%yzvw%d/eLylHe&kv#AdM/y&kJkMMkMMz%G%d
VdA#A%_%A"Ad*"h*dfG%o*dh/e u&k
...
```

Vocabulary file (use the same name as the corresponding file with traces), e.g., scs/original_scs.vocabulary.txt:

```
a Within SERP search result
b Query rephrase
c SERP overview without modification
d SERP without modification
...
```

Create a subfolder in /data and place both files there.


## Run

Arguments: (1) file with traces and (2) maximum pattern length:

```
python3 run.py 'scs/original_scs.stringenc.txt' 5
```


## Interpretation

(XY) a loop, i.e., a sequence repeated more than once, e.g., XYX or XYXYX
