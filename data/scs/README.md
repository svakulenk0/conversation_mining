# Spoken-Conversational-Search dataset

Original dataset: https://github.com/JTrippas/Spoken-Conversational-Search/blob/master/SCSdataset.csv

1,044 utterances annotated with 135 distinct complex labels, e.g. Access source + Information request within document

that consist of 83 original-dataset labels:
```
a Within SERP search result
b Query rephrase
c SERP overview without modification
d SERP without modification
e Scanning document with modification
f Access source (implicit)
g Access source feedback-request
h Performance feedback
i Recommendations
j Automated repetitive search
k Within-Document search result
l Asking what they are looking for
m Creating bigger picture
n between-document navigation
o Enquiry for further information
p Requests more details about information request
q SERP Card
r Scanning document without modification BUT with interpretation of photos
s Query refinement offer
t Provides information about the search engine
u Feedback on what is happening
v Information request
w Repeats the query back
x Previously seen results
y Scanning document without modification
z Relevance judgement
A Query embellishment
B Results?
C Google query expansion suggestion
D Within-Document search result entity lookup request
E Within-Document command response
F Access search engine
G Checks navigational command
H Intent clarification
I Information request within SERP
J Definition lookup or Person
K Info about document
L Rejects
M Interpretation
N Information Request within Document
P Multi-document summary
Q Query repeat
R Offers to spell
S Comparing results against each other
T Image overview on SERP
U Read more from the document
V Initial information request
W Misheard
X Repeats
Y Enough information
Z Info about SERP overview
! Wayfinding
" SERP with modification
# Asks to repeat
$ Utter
% Confirms
& Information request within document
' Asking about usefulness
( Information Request
) Parahprasing from document which is not in front of them
* Asks to repeat first search result
+ Requests spelling
, Is there more information
- Query formulation for info found in document
. Information Request within SERP
/ Access source
: Source information
; Informs user about searching for information found in document
= Request to access Search engine
? Leave document
@ Spells
[ Asks to repeat Nth search result
\ Suggestion to search more
] Interpretation biased towards information request or clarification given by the User
^ Definition explanation
_ Asks if allowed to query embellish
` Within-document command
{ Requests "enough information" judgement
| Interpretation of photos
} Definition clarification
~ Next
```

## Alternative Labels

AB schema:
```
A Seeker
B Assistant
```

QSRA schema:

```
Seeker:

Q question (information request)
E "yes" answer or accept (encouragement)
D "no" answer or reject (discouragement)
S statement (assertion)
O other (filler)

Assistant:

R question (information request)
Y "yes" answer or accept (encouragement)
N "no" answer or reject (discouragement)
A statement (assertion)
F other (filler)
```

QS schema:

```
G greet and bye (conversation frame decorators)
Q question (information request)
S all other utterance type from the QSRA schema
```
