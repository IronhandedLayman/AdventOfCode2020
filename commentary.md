Commentary for AoC2020
----------------------


## Dec01 - Report Repair:

First off, I don't expect any points. I may start at midnight, but that is only because I am up. Really I do this as a way to flex my coding muscles, and show you one approach to solving these problems. I think I may go back and do the other years throughout: I may have a repo somewhere with some of that data on it.

I am also playing around with a brand new environment. Learning the setup is a bit wonky; I have forgotten a bit about the wonders of i3wm and my abandoned Ubuntu install, sitting quietly on my dual-boot machine gathering dust. The video drivers needed upgrading and the kernel needed rebuilding. No matter, I took care of that. The water is just fine over here lol. 

My fast python is a bit rusty. Part of me wanted to do the whole thing in golang or rust; python's infinite precision ints stayed my hand. I do my professional coding mostly in golang, sometimes in python. This December, I will flex those mental muscles. Also, the REPL approach is pretty useful for problems like this.

So the repo setup is that I will name all of the files dayNN_problem_title.py and the inevitable data for each problem in data/dayNN_data.txt. Any shared code should sit in a separate module I will import from the main. I am not there yet, but I will be; a quick refactor and I can add tests for what it is worth. 

Oh, so yeah, the problem! It was really easy, just try all combinations of 2/3 lines to see if they sum to 2020, then multiply. I think there were at most 200 lines? (haha just checked with wc -l, 200 on the nose) Anything that small can just be brute-forced (200 ^ 3 == 8 million possibilities thus no overthink), so I stated clearly in list comprehensions what I was looking for. Not the fastest code but that isn't what I am looking for here. I could have also just spouted a JH notebook; that would have worked just as well as my functions. 

OK, well I know they start easy and get progressively harder. Looking forward to the following days. Also, just checked the leaderboard: >4000 submissions in the first 30 minutes? Sheesh I would have to be far quicker on the trigger to get a spot on the top 100. I think those days are far behind me.

## Dec02 - Password Philosophy

Today was a refresher on the lowly regular expression imported by `import re`. A lot of stuff is coming back slowly. I am not as fast as I used to be surely, but I was able to work through the problem alright. Literally parse the file and see how many lines satisfy the parsing. Not too bad. Of course, I did misread the problem, where I was counting the number of times the letter appeared between the two points, as opposed to counting how many times the letter appears among the two letter positions. I wonder if that slowed anyone else down. 

I have a bit of reuse of functions, and a pretty solid structure to the problem setup. I will exploit that tomorrow when I have time to set things up to work a bit more smoothly. 

I decided for posterity sake to keep the current rankings in place. I had a meeting right before this, so I didn't track to see how long it actually took me to read and work through the problem. Nor do I expect to always be up at midnight to race to get a solution in place. I only want to be sure I do every problem this year and stick with it. I do know they get harder and it may not be possible to solve some of them as I go down the tree. I want to give it a good go this year. So far it has been quite smooth.

## Dec03 - Toboggan Trajectory

Today was just following the rules; literally you follow the path of the toboggan as it goes through the different angles. I feel like they could have made the problem a little more interesting by allowing you to steer and hit as few trees as possible, but it is still early in the competition and really this is all about being able to read the input in the given formats and just get a feel for the competition format. I had some good code structure that allowed me to exploit some of the code I wrote in part 1 for part 2. Knowing I didnt have to overoptimize was also a good thing, as it would have cost me time. Even so, I am not so fast with the fingers as I need to be. And I had a couple of unforced errors; I didn't save my file as quickly as I wanted, and I also misnamed it, which is awkward. I will get that better next time. It is now time to also allow the file pulling code to come out and be imported instead of copy-pasting it from run to run. But, I also need some sleep. I will do that tomorrow prior to the compeititon time.

## Dec04 - Passport Processing

Today was a disaster LOL.
The problem is a minefield of corner cases. If I had hair I'd be tearing it out. I was caught on one corner after another. And it didn't help that my code was inefficient. I cannibalized star1 to solve star 2 even. I missed that for regular expressions, I needed complete matches (submatches were getting through); I screwed up checking of intervals; I missed checking to see if there was an in or cm at the end of height (just that if it did, I checked the bounds). Oh man that was humbling.

At least I got to use a for-else clause. I will play during the day on Saturday. Not staying up again, that was insane.

Current rankings:
-----------------
```
    -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  4   00:32:16  6206      0   01:10:07  5107      0
  3   00:12:18  3077      0   00:16:01  2243      0
  2   00:18:05  4058      0   00:23:09  3541      0
  1   00:35:40  4612      0   00:42:25  4411      0
```
