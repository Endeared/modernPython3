# collection of the modern python 3 bootcamp assignments / simple python functions and / or project scripts

none of these functions have an individual / out-of-box purpose on their own. they are just simply for show to benchmark what i have learned / potential later use.

## assignments / functions / scripts included:

### simple scripts / assignments
+ repeat a string until for loop satisfied break condition (**breakPractice.py**)
+ randomly select int between 1-9, print out all nums not equal to 5 (**whileLoopPrac.py**)
    > __Note__ dependencies: **random**
+ print all nums and nums^2 up to random num x, take in word and print all letters (**forLoop1.py**)
+ takes in lower and higher num, inputs sum of all nums in range (**forLoopAdd.py**)
+ takes in password, reprompts for password until pw is correct (**passwordWhile.py**)
+ takes in number of times to repeat string, repeats string x times (**repeater.py**)
+ takes in string, repeats string until input = "stop copying me" (**stopCopyMe.py**)
+ takes in lower and upper numbers for range, prints if each number is even, odd, or unlucky (**unluckyNumbers.py**)
+ practice filling lists via while loop (**listsPractice1.py**)
+ practice editing data in list through while loop (**listsPractice2.py**)
+ takes list of strings, concatenates all strings together and capitalizes result (**listsPractice3.py**)
+ add elements from one list to another (**listsPractice4.py**)
+ practice adding, removing, inserting values from lists (**listsPractice5.py**)
+ practice iterating over lists and extracting data (**listComp1.py**)
+ practice iterating over lists and extracting more data / modifying lists (**listComp2.py**)
+ simple list comprehension to check for all numbers divisible by 12 between 1-10 (**listComp3.py**)
+ simple list comprehension to check for only non-vowels in a string (**listCompy4.py**)
+ use list comprehension to generate nested lists (**listComp5.py**)
+ use list comprehension to generate more nested lists (**listComp6.py**)
+ creation of a simple single object dictionary (**simpleDictionary.py**)
+ access values out of a single object dictionary (**dictPractice1.py**)
+ access values out of multiple items in dictionary, sum those values (**dictPractice2.py**)
+ check if a random food choice is in stock at a bakery dictionary (**dictionaryAccess.py**)
    > __Note__ dependencies: **random**
+ initialize a dictionary from a list of keys, set the value of all keys (**fromkeysPractice.py**)
+ practice dictionary methods to copy / update / remove items from dict (**dictionaryMethods.py**)
+ mock spotify playlist stored in python dictionary (**spotifyPlaylist.py**)
+ zip up two different lists into a dictionary (**stateAbbreviations.py**)
+ convert lists within list to dictionary key-value pairs (**listToDict.py**)
+ assign default value of 0 to list of vowels using fromkeys (**fromkeysVowels.py**)
+ create dict of ascii keys and their values (**ASCIIdict.py**)
+ practice making tuples and sets from lists (**tuplesAndSets.py**)
+ creating a function (**definingFunctions.py**)
+ practice using return (**understandingReturn.py**)
+ pig speak function (lol) (**speakPig.py**)
+ generate all even numbers between 1 and 50 (**generateEvens.py**)
+ return a yelled string (**practiceParams.py**)
+ practice setting a default parameter for a function (**defaultParams.py**)
+ a set of various functions for practice (**functionsPractice.py**)
+ check if a tuple of arguments contains the string "purple" (**argsExercise.py**)
+ check for kwargs in function params (**kwargsExercise.py**)
+ practice unpacking list for use in *args (**unpackingExercise.py**)
+ calculate exercise that uses kwargs (**calculateExercise.py**)
+ practice creating / defining a lambda function (**myFirstLamba.py**)
+ using the map + lambda to iterate over list (**mapTime.py**)
+ use filter + lambda to iterate over list (**filterExercise.py**)
+ use any/all functions to iterate over list (**anyAllExercise.py**)
+ identify min and max values in a list of ints (**extremeExercise.py**)
+ evaluate list for number of largest magnitude +/- (**max_magnitude.py**)
+ take sum of all even values in variable number of args (**sumEven.py**)
+ take sum of all floats in variable number of args (**sumFloats.py**)
+ take in strings, zip and return interleaved strings (**interleave.py**)
+ filter through list, then triple every int in filtered list (**tripleAndFilter**)
+ iterate through dictionary of person keys, return list of full names concatenated (**extractFullName.py**)
+ practice debugging with try / except statements (**debuggingPractice.py**)
+ practice importing modules (**importPractice1.py**)
    > __Note__ dependencies: **math**
+ check through *args for any python keywords (**modulesExercise.py**)
    > __Note__ dependencies: **keyword**
+ practice importing / calling custom modules (**exercise.py**)
    > __Note__ dependencies: **helpers**
+ practice making http get request for json data (**requestPractice.py**)
    > __Note__ dependencies: **requests**, **pprintpp**
+ create a simple class, practice creating instances (**simpleClass.py**)
+ create a class, practice instantiating attributes (**classPractice.py**)
+ create a mock bank account class, include several methods (**bankAccount.py**)
+ create a mock chicken coop class, include several methods / class variable (**chickenCoop.py**)
+ create mock rpg classes, include inheritance (**rpgClasses.py**)
+ create mock genetics classes, child inherits from mother / father using method resolution order (**mroGenetics.py**)
+ create mock train class, use magic / dunder methods (**specialMethods.py**)
+ weekday generator using yield (**weekGenerator.py**)
+ generator that alternates between yield (**yesOrNoGenerator.py**)
+ generator that writes a song, with different message for each yield (**makeSong.py**)
+ generator that yields count multiples of a number (**getMultiples.py**)
+ generator that yields an unlimited number of multiples of a number (**unlimitedMultiples.py**)
+ exercise that accepts a function and returns another function (**showArgs.py**)
    > __Note__ dependencies: **functools**
+ exercise that accepts a function and returns another function, decorating the inner function (**doubleReturn.py**)
    > __Note__ dependencies: **functools**
+ exercise that accepts a function and invokes function if less than 3 args are provided (**fewerThanThreeArgs.py**)
    > __Note__ dependencies: **functools**
+ exercise that accepts a function and invokes function if all args are ints (**onlyInts.py**)
    > __Note__ dependencies: **functools**
+ exercise that accepts a function and invokes function if a keyword argument exists (**ensureAuthorized.py**)
    > __Note__ dependencies: **functools**
+ exercise that accepts a time, returning an inner function that accepts another function (**delay.py**)
    > __Note__ dependencies: **functools**, **time**
+ script that opens up one text file and copies all contents to second text file (**copyExercise.py**)
+ script that opens up one text file, copies all reversed contents to second text file (**copyReverse.py**)
+ script that opens up text file, returns dict of # of lines, # of words, # of chars (**fileStatistics.py**)
+ script that opens up a text file, replaces all instances of one value with another (**findAndReplace.py**)
+ script that opens up csv file, adds line to end of csv file (**addUser.py**)
    > __Note__ dependencies: **csv**
+ script that opens up csv file, prints data from each row (**printUsers.py**)
    > __Note__ dependencies: **csv**
+ script that opens up csv file, looks for matching values in file and prints index (**findUser.py**)
    > __Note__ dependencies: **csv**
+ script that opens up csv file, replaces old values with new values and returns count of replacements (**updateUsers.py**)
    > __Note__ dependencies: **csv**
+ script that opens up csv file, deleted matching users and keeps count of deletions (**updateUsers.py**)
    > __Note__ dependencies: **csv**
+ simple webscraping program (**firstScraper.py**)
+ simple regex script to check for valid time input (**regexTime.py**)
    > __Note__ dependencies: **re**
+ simple regex script to return list of binary strings in input string (**regexBytes.py**)
    > __Note__ dependencies: **re**
+ simple regex script to return dict of date groups from a string (**regexDate.py**)
    > __Note__ dependencies: **re**
+ simple regex script to to censor a substring within a string (**regexCensor.py**)
    > __Note__ dependencies: **re**
+ script to write list of tuples into sqlite3 db, checks for duplicates and deletes (**friends.py**)

### challenges (section 36)
+ reverse all letters of a string (**reverseString.py**)
+ takes in a list of items, checks if each item in list is a list (**listCheck.py**)
+ takes in a list of items, returns a list of every other item from original list (**removeEveryOther.py**)
+ takes in list of integers and target, and returns first two integers in list that add up to target (**sumPairs.py**)
+ takes in string, returns dict with vowel counts in string (**vowelCounter.py**)
+ takes in string, returns string where every first letter of each word is capitalized (**titleize.py**)
+ takes in number, returns list of all ints that the number is divisible by (**findFactors.py**)
+ takes in a collection, a value, and a starting index, and searches collection for matches after starting index (**includes.py**)
+ takes in a string and value, returns new string with original string repeated value times (**repeat.py**)
+ takes in string and amount to shorten, truncates the string if possible (**truncate.py**)
+ takes in two lists, creates a dict with first list as keys and second list as values (**twoListDict.py**)
+ takes in list, start index, end index, returns sum of all ints between incides (**rangeInList.py**)
+ takes in two numbers, checks of numbers contain the same digits + digit counts (**sameFrequency.py**)
+ takes in list and number, returns nth element in list. if negative, returns nth element from end (**nthElement.py**)
+ takes in list, returns the first duplicate value within list (**findTheDuplicate.py**)
+ takes in NxN list of lists, returns sum of two diagonals of the matrix / array (**sumDiagonals.py**)
+ takes in dictionary, returns lowest and highest keys in dict (**minMaxDict.py**)
+ takes in list, returns count of how many times a number is followed by a larger number in the list (**findGreaterNumbers.py**)
+ takes in list, returns two largest numbers in list (**twoOldest.py**)
+ takes in string, returns sum of positional values of characters in string, checks if odd / even (**isOddString.py**)
+ takes in string, returns string with all vowels reversed (**reverseVowels.py**)
+ takes in list of numbers, returns true / false depending on if sum of 3 consecutive nums is odd / even (**threeOddNums.py**)
+ takes in list of numbers, returns mode of the list (most frequent number) (**mode.py**)
+ function that returns a function that returns current avg of all previous function calls (**runningAvg.py**)
+ takes in string and search letter, returns count of search letter in string (slightly different from proposed solution / prompt) (**letterCounter.py**)
+ takes in function, returns new function (**once.py**)

### projects
+ guessing game for a number between 1 and 10 (**guessingGame.py**)
    > __Note__ dependencies: **random**
+ 2 player rps game (**rock_paper_scissor.py**)
+ 1 player rps game vs AI (**rpsAI.py**)
    > __Note__ dependencies: **random**
+ 1 player rps game vs AI, keeps score (**rpsAIv2.py**)
    > __Note__ dependencies: **random**
+ very simple coinflip function (**coinflip.py**)
    > __Note__ dependencies: **random**
+ very simple api project to retrieve dad jokes (lol) (**dad.py**)
    > __Note__ dependencies: **requests**, **random**
+ OOP deck of cards project, with deck and card classes (**deckOfCards.py**)
    > __Note__ dependencies: **pprintpp**, **random**
+ web scraping project for guessing quotes (**scrapingProject.py**)
    > __Note__ dependencies: **requests**, **bs4**, **random**