# :loudspeaker: Spaced Repetition Manager

Doing spaced repetition is considered one of the most fruitful study technique. It consists on spacying out our studying schedule, in particular, by introducing time intervals between study sessions, you can remember more. That's because you try to "tackle" and to smooth the forgetting curve. 
There are plenty of resources online, these ones are just a few:
* How to Remember More of What You Learn with Spaced Repetition ([link](https://collegeinfogeek.com/spaced-repetition-memory-technique/))
* How to Study for Exams - Spaced Repetition | Evidence-based revision tips ([link](https://www.youtube.com/watch?v=Z-zNHHpXoMM))

In short, you should repeat over time the same argument. So, with this script you should be able to keep track of your progresses by maintaining a simple "session" file, that you can easily replace/update whenever you want. Notice that is is a quite "naive" active recall manager, because the questions will be randomly selected. So I am just considering the philosophy of the "spaced repetition", without taking into account the "dates" in which you repeated thats specific topic. 

In any case, it can be useful for doing periodic or last minute reviews  :D

## Structure

### Index file
It is a JSON file where you must report each chapter with the number of questions/paragraph (int). In the following example, chapter 5 has 44 questions (from 1 to 44), chapter 6 has 15 questions and so on: 
```
{
  "5" : 44,
  "6" : 15,
  "7" : 10
}
```

### Session file
Anytime you run the script, this file will be updated. It allows you to keep track of your progresses. In the following example, questions 19 and 44 from chapter 5 have been repeated once whereas question 8 from chapter 6 has been repeated twice.  
```
{
  "5": {
    "19": 1,
    "44": 1
  },
  "6": {
    "8": 2
  }
}
```

## How to run

The arguments that you can use are:
* --chapter \<CHAPTER-TO-REVIEW\> (default=None -> it will be randomly chosen)
* --num_extractions \<NUMBER-OF-QUESTIONS\> (default=1)
* --index \<PATH-TO-INDEX-FILE\> **
* --session \<PATH-TO-SESSION-FILE\> (default=None -> it will be created after the first run **)

\*\* I suggest you set as "default" the files that you are going to use 

### Example
```
python main.py --index indices/index.json --session progresses/session-index.json --chapter 5 --num_extractions 2
```

Output: 
```
Tell me from chapter 5 >> 15 14
```
