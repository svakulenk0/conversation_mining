# Pattern composition 


## Input

File with traces where every event is encoded with a single symbol (do not use numbers for encoding, they are reserved to detect loops!), e.g., scs/original_scs.stringenc.txt:

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


## Output

Sample output is a list of sequence patterns ranked by their support values:

```
208 Initial information request -> Confirms -> Scanning document without modification -> Information request within document -> Within-Document search result
163 Initial information request -> Query refinement offer -> Confirms -> SERP without modification
...
18 Initial information request -> Confirms -> Scanning document without modification -> (Information request within document -> Within-Document search result) -> Scanning document without modification
...
```

where (XY) is a loop, i.e., a sequence repeated more than once, e.g., XYX or XYXYX
