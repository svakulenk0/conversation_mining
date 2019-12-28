# Conversation mining resources


## Conversational data

Publicly available datasets with conversation transcripts annotated with dialog (speech) acts:

[Dialog State Tracking Challenge Series](https://www.microsoft.com/en-us/research/event/dialog-state-tracking-challenge) provided several datasets with annotated information-seeking dialog transcripts for traveling and restaurant domains. Some of them are freely available. These datasets were created to evaluate and compare performance of dialog state trackers, systems able to interpret the user's action. They also include ontologies describing the domain, which consists of attributes (slots) with a set of possible values for each of the attributes. The transcripts are annotated with the dialog acts, user goals, methods, attributes, time-stamps as well as the user feedback.

* [DSTC1](https://www.microsoft.com/en-us/research/event/dialog-state-tracking-challenge/) The domain is route information for buses in Pittsburgh. [Codebook](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Dialog20state20tracking20challenge20handbook20V21.pdf) License: MSR-LA

* [DSTC2](http://camdial.org/~mh521/dstc/) labeled human-computer dialogs in restaurant information domain. JSON format. The domain of a dataset is described by an ontology object, also distributed in JSON. Phoenix grammar. The dialog-act notation closely matches that used in DSTC1.

<!-- * [DSTC3](http://camdial.org/~mh521/dstc/) small amount of labelled data in the tourist information domain. Tourist information subsumes restaurant information, including bars, cafes etc. 10 labelled dialogs -->

* [The Switchboard Dialog Act Corpus (SwDA)](https://github.com/cgpotts/swda) extends the Switchboard-1 Telephone Speech Corpus, Release 2 with turn/utterance-level dialog-act tags. The dataset contains conversation transcripts of telephone conversations annotated with 43 dialog-act tags, part-of-speech tags, lemmas and parse trees. [Description](http://compprag.christopherpotts.net/swda.html) [Codebook](https://web.stanford.edu/~jurafsky/ws97/manual.august1.html) License: GNU GPL v2.0.

<!-- * [Switchboard CMU](https://github.com/snakeztc/NeuralDialog-CVAE/blob/master/data/json_data/valid.jsonl) conversational dataset based on Switchboard (SW) 1 Release 2 Corpus (Godfrey and Holliman, 1997), which contains 2400 phone conversations annotated with 42 types of dialog acts, 70 available topics. License: Apache-2.0. -->

* [Spoken Conversational Search](https://github.com/JTrippas/Spoken-Conversational-Search) (SCS) Data Set provides conversational transcripts collected for the pre-defined search tasks performed in a conversational speech-only setting. The transcripts are annotated with the timestamps, the corresponding search queries and dialog acts for each of the roles. [Codebook](https://github.com/JTrippas/Spoken-Conversational-Search/blob/master/CodeBook_CHIIR.pdf)

* [Open Data Exploration dataset](https://github.com/vendi12/ODExploration_data) for the conversational browsing task contains 26 transcripts annotated with dialog acts and entity spans. [Codebook](https://github.com/vendi12/ODExploration_data#annotations) License: MIT.

## Conversation Logs

Format CSV for importing into ProM. One message/dialog act per row.

Basic columns:

* case ID - conversation identifier
* resource - actor role of the conversation participant
* activity name - dialog (speech) act

Optional columns:

* start time, stop time - timestamps reflect ordering of messages along the time axis
* message count - counts the number of messages exchanged within a conversation
* message - transcript of the utterance
* query - information need describing the task (instruction) that participants are solving

[DSTC1&2](http://camdial.org/~mh521/dstc/downloads/handbook.pdf)

* turn count - counts the pairs of messages exchanged within a conversation
* slots - message attributes from the domain ontology

[SCS](https://github.com/JTrippas/Spoken-Conversational-Search):

* Query.complexity - one of three levels, referencing the task complexiy type (remember, understand, and analyze)
* Notes - comments such as the particular search is stopped by the user or researcher or extra notes which relate to the action of the participant regarding the search session.

[SWDA](http://compprag.christopherpotts.net/swda.html)

* length - duration of the conversation in seconds
* caller_dialect_area - geo identifier for the cluster of resources from the set of {MIXED, NEW ENGLAND, NORTH MIDLAND, NORTHERN, NYC, SOUTH MIDLAND, SOUTHERN, UNK, WESTERN}


## Annotations

Conducted by 2 annotators

Annotation schema: Krippendorff's alpha, 0.997

Dialogue success evaluation: Krippendorff's alpha 0.726


## References


* Stefan Sitter and Adelheit Stein. 1992. [Modeling the illocutionary aspects of information-seeking dialogues](https://ac.els-cdn.com/030645739290044Z/1-s2.0-030645739290044Z-main.pdf). Information Processing & Management, 393 28(2):165–180.

* Johanne R. Trippas, Damiano Spina, Lawrence Cavedon, and Mark Sanderson. [How Do People Interact in Conversational Speech-Only Search Tasks: A Preliminary Analysis](http://www.johannetrippas.com/papers/Trippas%20et%20al-CHIIR2017.pdf). The ACM SIGIR Conference on Human Information Interaction and Retrieval (CHIIR), Oslo, Norway, 2017.
